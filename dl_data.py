from google.cloud import storage
import os

def download_blob(bucket_name, source_blob_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client.from_service_account_json('storage.json')
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    destination_file_name = os.path.join("./data", blob.name)
    os.makedirs(os.path.dirname(destination_file_name), exist_ok=True)
    blob.download_to_filename(destination_file_name)

    print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")

def list_blobs_with_prefix(bucket_name, prefix='', delimiter=None):
    """Lists all the blobs in the bucket that begin with the prefix."""
    storage_client = storage.Client.from_service_account_json('storage.json')
    blobs = storage_client.list_blobs(bucket_name, prefix=prefix, delimiter=delimiter)
    return blobs

def download_directory(bucket_name, prefix):
    """Download all files in a directory from GCS bucket."""
    blobs = list_blobs_with_prefix(bucket_name, prefix)
    for blob in blobs:
        download_blob(bucket_name, blob.name)

# Example usage
bucket_name = 'stgat_data'
directory_prefix = ""  # This is the GCS folder path you want to download

download_directory(bucket_name, directory_prefix)
