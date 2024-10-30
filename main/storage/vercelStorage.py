# main/storage_backends/vercel_storage.py

import requests
from django.core.files.storage import Storage
from django.conf import settings

class VercelBlobStorage(Storage):
    def __init__(self):
        self.base_url = getattr(settings, 'VERCEL_BLOB_BASE_URL', None)
        self.token = settings.VERCEL_BLOB_TOKEN

    def _save(self, name, content):
        url = f"{self.base_url}/upload"
        files = {'file': (name, content)}
        headers = {'Authorization': f"Bearer {self.token}"}
        
        response = requests.post(url, files=files, headers=headers)
        
        if response.status_code == 200:
            return response.json().get('url')
        else:
            raise Exception("Failed to upload file to Vercel Blob Storage")

    def url(self, name):
        return f"{self.base_url}/{name}"
    
    def exists(self, name):
        # Implemente se precisar verificar se o arquivo já existe (opcional)
        return False
