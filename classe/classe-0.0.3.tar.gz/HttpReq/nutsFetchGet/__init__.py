from classe.HttpReq import Fetch as fetch

class nutsFetchGet(fetch.Fetch):

    def __init__(self, path):
        super()
        self.path = path

    def initGetNuts(self):
        return fetch.Fetch.fetchDataGet(self, self.path)
