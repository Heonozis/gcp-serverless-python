import base64
import json


def get_topic_data(event):
    try:
        data = base64.b64decode(event["data"]).decode('utf-8')
        data = json.loads(data)
    except KeyError as e:
        raise ValueError('Invalid Pub/Sub message.')

    print(f'Received Pub/Sub message: {json.dumps(data)}')

    return data
