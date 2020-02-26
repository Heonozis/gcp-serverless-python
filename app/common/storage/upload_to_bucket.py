from mimetypes import guess_type
from google.cloud import storage


def upload_to_bucket(bucket, path, data, metadata=None):
    client = storage.Client()
    bucket_ref = client.bucket(bucket)
    content_type = guess_type(path)[0]

    blob = bucket_ref.blob(path)
    blob.upload_from_string(data, content_type=content_type)

    if metadata is not None:
        blob.metadata = metadata
        blob.patch()

    print(f'File {path} saved to GCS {bucket_ref}...')

    return path
