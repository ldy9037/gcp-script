from google.cloud import storage

def list_blobs_with_prefix(bucket_name, prefix, delimiter=None):
    storage_client = storage.Client()

    return storage_client.list_blobs(bucket_name, prefix=prefix, delimiter=delimiter)

def copy_blob(
    bucket_name, blob_name, destination_bucket_name, destination_blob_name,
):
    storage_client = storage.Client()

    source_bucket = storage_client.bucket(bucket_name)
    source_blob = source_bucket.blob(blob_name)
    destination_bucket = storage_client.bucket(destination_bucket_name)

    destination_generation_match_precondition = 0

    blob_copy = source_bucket.copy_blob(
        source_blob, destination_bucket, destination_blob_name, if_generation_match=destination_generation_match_precondition,
    )

    print(
        "Blob {} in bucket {} copied to blob {} in bucket {}.".format(
            source_blob.name,
            source_bucket.name,
            blob_copy.name,
            destination_bucket.name,
        )
    )

bucket_name = ""
prefix = ""

blobs = list_blobs_with_prefix(bucket_name, prefix)
destination_folder = ""

for blob in blobs:
    destination_blob_name=destination_folder+blob.name
    copy_blob(bucket_name, blob.name, bucket_name, destination_blob_name)