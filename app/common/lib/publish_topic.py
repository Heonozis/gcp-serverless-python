from app.config import project_id
import json


def publish_topic(topic, message):
    from google.cloud import pubsub_v1

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic)
    message_data = json.dumps(message).encode('utf-8')
    future = publisher.publish(topic_path, data=message_data)
    future.result()
    print(f'Published Pub/Sub topic {topic} with message: {json.dumps(message)}')
