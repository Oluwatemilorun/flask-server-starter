import json
from json import JSONEncoder

class ObjEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

def object_to_json(obj):
    obj_str = ObjEncoder().encode(obj)
    return json.loads(obj_str)
