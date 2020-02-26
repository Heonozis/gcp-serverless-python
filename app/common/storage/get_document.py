from google.cloud import firestore
from app.config import project_id


def get_document(table, key):
    db = firestore.Client(project=project_id)
    try:
        doc_ref = db.collection(table).document(key)
        data = doc_ref.get()
        return data
    except Exception as e:
        print(f'Error occurred while updating {table} document with key {key} and data {data}: {e}')
