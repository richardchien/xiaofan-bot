import json
import sys

import config

data_file = sys.argv[1]

with open(data_file, 'r', encoding='utf-8') as f:
    data = json.loads(f.read())

value1 = data['value1']  # event from CoolQ
value2 = data['value2']  # API call from IFTTT
value3 = data['value3']  # unused

config.super_id = data['super_id']
config.token = data['token']
config.maker_webhook = data['maker_webhook']

if value1:
    try:
        e = json.loads(value1)
        import event
        event.handle(e)
        exit(0)
    except Exception:
        pass

if value2:
    try:
        a = json.loads(value2)
        import api_call
        api_call.handle(a)
        exit(0)
    except Exception:
        pass
