# app/utils/debug.py
from pprint import pprint
import json


def pp(data):
    try:
        if hasattr(data, 'dict'):
            print(json.dumps(data.dict(), indent=2, default=str))
        elif isinstance(data, list):
            print(json.dumps([
                i.dict() if hasattr(i, 'dict') else i
                for i in data
            ], indent=2, default=str))
        else:
            pprint(data)
    except Exception:
        pprint(data)
