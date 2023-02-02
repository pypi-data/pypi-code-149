from Fetch import Fetch

class nutsFetchGet(Fetch):

    def __init__(self, path):
        super()
        self.path = path

    def initGetNuts(self):
        return fetch.Fetch.fetchDataGet(self, self.path)
