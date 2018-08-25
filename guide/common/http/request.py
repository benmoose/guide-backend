import json


def parse_body_to_dict(request_body):
    try:
        return json.loads(request_body)
    except json.JSONDecodeError:
        return None
