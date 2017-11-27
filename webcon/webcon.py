#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK

"""
Control your computer through shell commands from a barebones web interface.

Configuration goes in ~/.config/webcon/config.yaml, or may be provided by
command line argument. Variables in `__variables__` will be substituted once via
`str.format`.

Example configuration:

__variables__:
    mpvfifo: ~/.local/share/mpv/fifo
mpv:
    rewind: echo seek -5 > {mpvfifo}
    play/pause: echo cycle pause > {mpvfifo}
    fast forward: echo seek 5 > {mpvfifo}
announcer:
    greet: say hello
    part: say farewell
"""

import argcomplete
import argparse
import collections
import bottle
import os
import subprocess
import sys
import termcolor
import yaml


# Constants.
DEFAULT_HOST = '0.0.0.0'
DEFAULT_PORT = '8080'
HOME = os.getenv('HOME')
CONFIG_DIR = os.getenv(
    'XDG_CONFIG_HOME',
    os.path.join(HOME, '.config'))
DEFAULT_CONFIG_FILE = os.path.join(
    CONFIG_DIR, 'webcon', 'config.yaml')

VARIABLES_KEY = '__variables__'
HERE = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(HERE, 'static')
STATIC_PATH = '/static'
SERVICE_BASE_PATH = '/service'


# Use package views only.
bottle.TEMPLATE_PATH = [os.path.join(HERE, 'views')]


def fail_with(msg):
    print(termcolor.colored(msg, 'red'))
    sys.exit(1)


# https://stackoverflow.com/a/21912744/6693050
def ordered_load(stream,
                 Loader=yaml.Loader,
                 object_pairs_hook=collections.OrderedDict):
    class OrderedLoader(Loader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))

    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)

    return yaml.load(stream, OrderedLoader)


def parse_args():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
        '--host',
        help=f"""
        The server host.
        Default: {DEFAULT_HOST}
        """,
        type=str,
        default=DEFAULT_HOST)

    parser.add_argument(
        '-p', '--port',
        help=f"""
        The server port.
        Default: {DEFAULT_PORT}
        """,
        type=str,
        default=DEFAULT_PORT)

    parser.add_argument(
        'config_file',
        help=f"""
        The config file to use.
        Default: {DEFAULT_CONFIG_FILE}
        """,
        nargs='?',
        type=str,
        default=DEFAULT_CONFIG_FILE)

    argcomplete.autocomplete(parser, always_complete_options=False)
    return parser.parse_args()


def main():
    args = parse_args()

    # Attempt to open the config file.
    try:
        with open(args.config_file) as f:
            config_contents = f.read()
    except FileNotFoundError:
        fail_with(f'Config file "{config_file}" not found.')

    # Try to substitute in variables.
    try:
        vars = yaml.load(config_contents)[VARIABLES_KEY]
    except yaml.YAMLError as e:
        fail_with(f'Config error:\n\n{e}')
    except KeyError:
        pass
    else:
        try:
            config_contents = config_contents.format(**vars)
        except Exception as e:
            fail_with(f'Variable substitution failed:\n\n{e}')

    config = ordered_load(config_contents)
    config.pop(VARIABLES_KEY, None)

    # Serve satic files.
    @bottle.get(f'{STATIC_PATH}/<filepath:path>')
    def static_route(filepath):
        return bottle.static_file(filepath, root=STATIC_ROOT)

    # Construct the service routes.
    service_data = []
    for service, actions in config.items():
        service_path = f'{SERVICE_BASE_PATH}/{service}'

        # Construct the action routes.
        action_data = []
        for action, do in actions.items():
            action_path = f'{service_path}/{action}'
            @bottle.post(action_path)
            def action_route(action=action,
                             do=do):
                try:
                    return subprocess.check_output(
                        do, stderr=subprocess.STDOUT,
                        shell=True)
                except subprocess.CalledProcessError as e:
                    return (
                        f'=== FAILED WITH RETURN CODE {e.returncode} ===',
                        e.output)

            action_data.append((action, action_path))

        @bottle.get(service_path)
        @bottle.view('service')
        def service_route(service=service,
                          action_data=action_data):
            return {'title': service,
                    'actions': action_data}

        service_data.append((service, service_path))

    # Construct the index route.
    @bottle.get('/')
    @bottle.view('index')
    def index_route():
        return {'services': service_data}

    # Start the server.
    bottle.run(host=args.host, port=args.port)


if __name__ == '__main__':
    main()
