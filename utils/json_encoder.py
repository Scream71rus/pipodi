
import datetime
import json


class ObjectEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, datetime.datetime):
            return datetime.datetime.strftime(o, "%Y-%m-%d %H:%M")

        if isinstance(o, datetime.date):
            return datetime.datetime.strftime(o, "%Y-%m-%d")

        return json.JSONEncoder.default(self, o)
