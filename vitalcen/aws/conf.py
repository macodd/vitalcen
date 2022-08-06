import os

# Digital Ocean keys
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_KEY")

# Digital Ocean Bucket
AWS_STORAGE_BUCKET_NAME = 'zitio-bucket'
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_CUSTOM_DOMAIN = "%s.sfo3.digitaloceanspaces.com" % AWS_STORAGE_BUCKET_NAME
AWS_S3_ENDPOINT_URL = "https://sfo3.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
# static files
AWS_LOCATION = 'static'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'vitalcen.aws.utils.StaticRootS3BotoStorage'
# media files
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, PUBLIC_MEDIA_LOCATION)
DEFAULT_FILE_STORAGE = 'vitalcen.aws.utils.MediaRootS3BotoStorage'
