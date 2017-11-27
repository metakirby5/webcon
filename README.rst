========
 webcon
========

|Preview|

Control your computer through shell commands from a barebones web interface.

Example configuration: `config.yaml`_

::

  __variables__:
      mpvfifo: ~/.local/share/mpv/fifo
  mpv:
      rewind: echo seek -5 > {mpvfifo}
      play/pause: echo cycle pause > {mpvfifo}
      fast forward: echo seek 5 > {mpvfifo}
  announcer:
      greet: say hello
      part: say farewell

Installation
------------

::

  pip3 install webcon

Tab completion
--------------

::

  sudo activate-global-python-argcomplete

If you installed via pip, you may need to run the following before autocompletion works:

::

  grep 'PYTHON_ARGCOMPLETE_OK' "$(which webcon)" &>/dev/null || sudo sed -i "1a # PYTHON_ARGCOMPLETE_OK" "$(which webcon)"

Usage
-----

::

  usage: webcon [-h] [--host HOST] [-p PORT] [config_file]

  Control your computer through shell commands from a barebones web interface.

  Configuration goes in ~/.config/webcon/config.yaml, or an alternate location
  may be provided by command line argument.

  Configuration format:

  - Throughout the configuration, order of each mapping is taken into account to
    ensure the layout does not deviate from expectations.
  - The top level of the configuration is a mapping.
  - Variables in the top-level key `__variables__` will be substituted once via
    `str.format` throughout the entire file. This may be used to extract long
    constants, etc.
  - Every other top-level key will define a service, and its value shall be a
    mapping of the actions it supports.
  - Each action shall define a label/command pair, in the the form of
    `label: command`.

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

  Explanation:

  - Define `mpvfifo` as a variable holding the location of a mpv fifo.
  - Define a service `mpv`.
      - This service exports the actions `rewind`, `play/pause`, and
        `fast forward`. The actions are different echoes to `mpvffo`.
  - Define a service `announcer`.
      - This service exports the actions `greet` and `part`. The actions are
      different phrases which will be synthesized through `say`.

  positional arguments:
    config_file           The config file to use. Default:
                          /Users/echan/.config/webcon/config.yaml

  optional arguments:
    -h, --help            show this help message and exit
    --host HOST           The server host. Default: 0.0.0.0
    -p PORT, --port PORT  The server port. Default: 8080

.. |Preview| image:: https://i.imgur.com/YWVbGoc.png
   :target: https://i.imgur.com/YWVbGoc.png
   :alt: Preview of webcon.
.. _config.yaml: config.yaml
