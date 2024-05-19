from licenselib.license import License
from licenselib.utils import DataContainer
import requests
import json


class Package(DataContainer):
    @property
    def dependencies(self) -> list | None:
        """
        Grab dependencies

        :return: List of dependencies or None if not found
        """
        if hasattr(self, 'info') and hasattr(self.info, 'requires_dist') and isinstance(self.info.requires_dist, list):
            return self.info.requires_dist
        else:
            return None


def api_call(pkg_name: str) -> dict | None:
    """
    Performs an api call to the PyPI API for the given package

    :param pkg_name: Name of the package
    :return: dict of json data or None on failure
    """
    url = f'https://pypi.org/pypi/{pkg_name}/json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    return None


def api_call_version(pkg_name: str, pkg_release: str) -> dict | None:
    """
    Performs an api call to the PyPI API for the given package and release

    :param pkg_name: Name of the package
    :param pkg_release: Release of the package
    :return: dict of json data or None on failure
    """

    pkg_data = api_call(pkg_name)
    if not pkg_data:
        return None

    return pkg_data['releases'].get(pkg_release)


def get_license(pkg_name: str) -> License | None:
    """
    Retrieves the license for the given package

    :param pkg_name: Name of the package
    :return: License or None on failure
    """
    raise NotImplementedError


def get_package(pkg_name: str) -> Package | None:
    """
    Retrieves the package info from the PyPI API

    :param pkg_name: Name of the package
    :return: Package or None on failure
    """
    pkg_data = api_call(pkg_name)
    if not pkg_data:
        return None

    pkg = Package(name=pkg_name, **pkg_data)
    return pkg


if __name__ == '__main__':
    from rich import print
    print('\n[bold green]TESTCASE #1:[/]')
    pkg = get_package('PyDooray')
    print(pkg.dependencies)

    print('\n[bold green]TESTCASE #2:[/]')
    print(get_package('non_existent_package'))
