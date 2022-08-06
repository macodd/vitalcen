from abc import ABC

from storages.backends.s3boto3 import S3Boto3Storage


# Storage classes for AWS
class StaticRootS3BotoStorage(S3Boto3Storage, ABC):
    location = 'static'
    default_acl = 'public-read'


class MediaRootS3BotoStorage(S3Boto3Storage, ABC):
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False
