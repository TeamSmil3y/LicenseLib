class License:
    def __init__(self, license: str, licensetext: str):
        # short description of license (e.g. GNU/GPL3, CC ZERO, MIT, ...)
        self.license = license
        # full license text
        self.licensetext = licensetext
