"""Return the installation location of cacert.pem or its contents.

This is a minimal, self-contained replacement for the ``certifi`` package
bundled with python-telegram-bot so the CA bundle shipped with this plugin
can be located without an external dependency.
"""

import os

__version__ = "2021.05.30"

__all__ = ["where", "contents"]

_CACERT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cacert.pem")


def where():
    """Return the absolute path to the bundled CA certificate bundle."""
    return _CACERT_PATH


def contents():
    """Return the contents of the bundled CA certificate bundle as text."""
    with open(_CACERT_PATH, "rb") as f:
        return f.read().decode("ascii", errors="replace")
