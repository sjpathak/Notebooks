from azure.storage.blob import BlobClient
import os

container_name = 'cnn'
blob_name = 'requirements.txt'

def upload_file_to_blob(sas_url, file_path):
    # Initialize the BlobClient using the SAS URL
    blob_client = BlobClient.from_blob_url(sas_url)

    # Open the file to upload
    with open(file_path, 'rb') as data:
        # Upload the file to Azure Blob Storage
        try:
            # Upload the file with the name of the file as the blob name
            blob_client.upload_blob(data, overwrite=True)
            print(f"File '{file_path}' uploaded successfully to blob storage.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # SAS URL pointing to your Blob (it includes container, blob name, and permissions)
    sas_url = f"https://spcnnblobstorage.blob.core.windows.net/{container_name}/{blob_name}?sv=2022-11-02&ss=b&srt=co&sp=rwdlaciytfx&se=2024-12-19T23:31:16Z&st=2024-12-16T15:31:16Z&spr=https&sig=T4EkpKvL%2FilCszTh9QwgqXhWdaZyO%2BxDik0VrR0whk0%3D"

    # Path to the file you want to upload
    file_path = "requirements.txt"

    # Upload the file
    upload_file_to_blob(sas_url, file_path)
