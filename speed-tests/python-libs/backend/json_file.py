import json


class JsonFile(object):
    def __init__(self, fn):
        self.data = json.load(open(fn, "r"))

    def __contains__(self, item):
        return item in self.data

    def get_all(self):
        return self.data

    def get(self, key):
        return self.data.get(key)
