import os

import boto3
from dotenv import load_dotenv

load_dotenv()

FILE_NAME = "Sviatoslav_Isaienko.html"  # має лежати поруч зі скриптом

client = boto3.client(
    "s3",
    region_name=os.getenv("AWS_REGION_NAME"),
    endpoint_url=os.getenv("AWS_ENDPOINT_URL"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
)

bucket_name = os.getenv("AWS_BUCKET_NAME")
public_url_base = os.getenv("AWS_PUBLIC_URL")

client.upload_file(
    Filename=FILE_NAME,
    Bucket=bucket_name,
    Key=FILE_NAME,
    ExtraArgs={"ContentType": "text/html; charset=utf-8"},
)

public_url = f"{public_url_base}/{FILE_NAME}"
print("Файл завантажено!")
print("Публічне посилання:", public_url)