import configparser


class ToxIniParser:

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = configparser.ConfigParser()
        self.config.read(ini_file)


    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        return len(self.config.sections())

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        envlist = self.config.get("tox", "envlist")
        if "," not in envlist:
            return envlist.strip().splitlines()
        stripped = "".join([c for c in envlist if not c.isspace()])
        if stripped.endswith(","):
            return stripped.split(",")[0:-1]
        return stripped.split(",")

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        s = set()
        for section in self.config.sections():
            for item in self.config.items(section):
                if item[0] == "basepython":
                    s.add(item[1])
        return list(s)
