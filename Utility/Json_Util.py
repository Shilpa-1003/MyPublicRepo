import json


class ReadFromJson:
    def fetch_json_value(self, key, path):
        myfiles = open(path, "r")
        data = myfiles.read()
        obj = json.loads(data)
        return str(obj[key])






























