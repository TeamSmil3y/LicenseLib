# LicenseLib
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
print(pkg) # prints all pkg data

dependencies = pkg.dependencies
print(dependencies) # prints all pkg dependencies as list including version
```

