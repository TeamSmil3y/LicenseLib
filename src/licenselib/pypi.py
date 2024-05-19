import requests
import json

def api_call(pkg_name: str) -> dict | None:
    """
    Performs an api call to the PyPI API for the given package

    :param pkg_name: Name of the package
    :return: dict of json data or None on failure
    """
