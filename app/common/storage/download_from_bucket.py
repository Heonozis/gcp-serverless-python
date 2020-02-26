from google.cloud import storage


def download_from_bucket(bucket, path, destination):
    storage_client = storage.Client()

    bucket_reference = storage_client.bucket(bucket)
    blob = bucket_reference.blob(path)
    blob.download_to_filename(destination)

    print(f'File {bucket}/{path} downloaded to {destination}...')
