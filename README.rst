========
 webcon
========

Control your computer from a web interface.

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

  Configuration goes in ~/.config/webcon/config.yaml, or may be provided by
  command line argument. Variables in `__variables__` will be substituted once via
  `str.format`.

  Example configuration:

  __variables__:
      mpvfifo: ~/.local/share/mpv/fifo
  mpv:
      rewind: echo seek -5 > {mpvfifo}
      play/pause: echo pause > {mpvfifo}
      fast forward: echo seek 5 > {mpvfifo}
  announcer:
      greet: say hello
      part: say farewell

  positional arguments:
    config_file           The config file to use. Default:
                          /Users/echan/.config/webcon/config.yaml

  optional arguments:
    -h, --help            show this help message and exit
    --host HOST           The server host. Default: 0.0.0.0
    -p PORT, --port PORT  The server port. Default: 8080
