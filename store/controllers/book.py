from store.engine.utils import APIResource


class Book(APIResource):
    def get(self):
        return "OK"