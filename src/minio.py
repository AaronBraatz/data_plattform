"""MinIO helper."""
import io
from pathlib import Path

import requests
from minio import Minio
from minio.error import S3Error
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


BUCKET_SENSOR_COMMUNITY = 'sensor-community'

def load_file_to_bucket(file_url: str, file_path: Path, bucket_name: str) -> None:
    # Download the file
    response = requests.get(file_url)
    response.raise_for_status()  # Check if the request was successful

    # Create an in-memory buffer
    file_buffer = io.BytesIO(response.content)

    # MinIO client configuration
    minio_client = Minio(
        os.getenv('MINIO_ENDPOINT'),
        access_key=os.getenv('MINIO_ACCESS_KEY'),
        secret_key=os.getenv('MINIO_SECRET_KEY'),
        secure=False  # Set to False if not using HTTPS
    )

    # Upload the file to MinIO
    try:
        minio_client.put_object(
            bucket_name=bucket_name,
            object_name=file_path.as_posix(),
            data=file_buffer,
            length=len(response.content),
            content_type='application/csv'
        )
        # print(f"'{file_path}' is successfully uploaded to bucket 'your-bucket-name'.")
    except S3Error as e:
        print(f"Error occurred: {e}")

