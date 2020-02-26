from google.cloud import firestore
from app.config import project_id


def create_document(table, key, data):
    db = firestore.Client(project=project_id)
    try:
        doc_ref = db.collection(table).document(key)
        doc_ref.set(data)
    except Exception as e:
        print(f'Error occurred while creating {table} document with key {key} and data {data}: {e}')

