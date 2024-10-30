import requests
from django.core.files.storage import Storage
from django.conf import settings

class VercelBlobStorage(Storage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_url = getattr(settings, 'VERCEL_BLOB_BASE_URL', None)
        self.token = getattr(settings, 'VERCEL_BLOB_TOKEN', None)
        
        if not self.base_url or not self.token:
            raise ValueError("VERCEL_BLOB_BASE_URL and VERCEL_BLOB_TOKEN must be set in settings")

    def _save(self, name, content):
        url = f"{self.base_url}/upload"
        files = {'file': (name, content)}
        headers = {'Authorization': f"Bearer {self.token}"}
        
        response = requests.post(url, files=files, headers=headers)
        
        if response.status_code == 200:
            return response.json().get('url')
        else:
            # Adicione detalhes do erro na exceção
            raise Exception(f"Failed to upload file to Vercel Blob Storage: {response.status_code} - {response.text}")

    def url(self, name):
        return f"{self.base_url}/{name}"
    
    def exists(self, name):
        return False
