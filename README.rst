###############
README
###############
:Author:   chinot7
:Date:   2016-08-16
:Version: 0.1
:Tags:  streema, python

Get info from ``streema.com`` client.

.. ATTENTION::
   This script can be used to display info in ``tmux`` bar status

.
Install
#########

::

   python setup.py develop --user

Configuration
#############

In ``~/.bashrc`` or ``~/.zshrc`` include:

::

   export PATH=~/.local/bin:$PATH


Usage
#####

By default ``streema.py`` prints the **Artist-Title** if ``ROCK`` env variable is defined, just type:

::

    streema.py



Version 0.1
###########

1. Get `Artist-Title` info from ``streema.com``

