from abc import ABC
from storages.backends.s3boto3 import S3Boto3Storage

__all__ = (
    "MinioMediaStorage",
    "MinioStaticStorage"
)


class MinioMediaStorage(ABC, S3Boto3Storage):
    location = "media"


class MinioStaticStorage(ABC, S3Boto3Storage):
    location = "static"
