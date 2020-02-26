from google.cloud import firestore
from app.config import project_id


def delete_document(table, key):
    db = firestore.Client(project=project_id)
    try:
        doc_ref = db.collection(table).document(key)
        doc_ref.delete()
    except Exception as e:
        print(f'Error occurred while deleting {table} document with key {key}: {e}')
