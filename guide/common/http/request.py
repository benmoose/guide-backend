import json


def parse_json_request(request_body):
    try:
        return json.loads(request_body)
    except json.JSONDecodeError:
        return None
