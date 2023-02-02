from classe.HttpReq import Fetch as fetch

class nutsPut(fetch.Fetch):

    def __init__(self, path, data):
        super()
        self.path = path
        self.data = data

    def initNutsPut(self):

        return fetch.Fetch.updateDataPut(self, self.path, self.path)
