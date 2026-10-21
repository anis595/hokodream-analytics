"""Test minimal d'installation — PAS un test de pipeline métier."""
from hokodream_analytics import __version__


def test_package_imports():
    assert __version__ == "0.1.0"
