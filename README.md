# LicenseLib
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Library for fetching licenses and dependencies.

# Install
```bash
python3 -m pip install --user licenselib
```

# Usage
Retrieve package info from PyPI:
```python
from licenselib import pypi

pkg = pypi.get_package('licenselib')
print(pkg) # all pkg data

dependencies = pkg.dependencies
print(dependencies) # pkg dependencies as list including version
```

