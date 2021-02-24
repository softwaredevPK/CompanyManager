class SingleInstanceClass:
    """https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html"""
    __instance = None

    def __new__(cls):
        if SingleInstanceClass.__instance is None:
            SingleInstanceClass.__instance = object.__new__(cls)
        return SingleInstanceClass.__instance









