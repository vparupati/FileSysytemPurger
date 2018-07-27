class A:
    def __init__(self, file_name):
        self.file_name = file_name.lower()

    def mk(self, keys):
        for key in keys:
            matched = self.file_name.find(key.lower())
            if matched > -1:
                return key
        return None
