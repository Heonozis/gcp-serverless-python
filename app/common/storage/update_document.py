from google.cloud import firestore
from app.config import project_id


def update_document(table, key, data):
    db = firestore.Client(project=project_id)
    try:
        doc_ref = db.collection(table).document(key)
        doc_ref.update(data)
    except Exception as e:
        print(f'Error occurred while updating {table} document with key {key} and data {data}: {e}')
