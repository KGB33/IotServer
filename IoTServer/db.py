from tinydb import TinyDB, Query

db = TinyDB("db.json")

SensorQ = Query()


def append(key, value):
    def transform(doc):
        doc[key].append(value)

    return transform
