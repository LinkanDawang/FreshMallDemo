from abc import ABC

from django.conf import settings
from django.core.files.storage import Storage
from qiniu import Auth, BucketManager, put_data


class QiNiuStorage(Storage, ABC):
    def __init__(self):
        self.base_url = settings.OSS_BASE_URL
        self.q = Auth(settings.OSS_ACCESS_KEY, settings.OSS_SECRET_KEY)

    def exists(self, name):
        bucket = BucketManager(self.q)
        ret, info = bucket.stat(settings.OSS_BUCKET_NAME, name)
        return False

    def _open(self, name, mode="rb"):
        pass

    def _save(self, file_name, file_content):
        key = file_name
        token = self.q.upload_token(settings.OSS_BUCKET_NAME, key, 3600)
        ret, info = put_data(token, key, file_content)
        return file_name

    def url(self, name):
        return self.base_url + name
