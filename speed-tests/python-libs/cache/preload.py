class Preload(object):
    def __init__(self, backend):
        self.data = backend.get_all()

    def __contains__(self, item):
        return item in self.data

    def get(self, key):
        return self.data.get(key)
