from django.core.files.storage import Storage
from django.conf import settings
from vercel_storage import blob

class VercelBlobStorage():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = getattr(settings, 'VERCEL_BLOB_TOKEN', None)
        if not self.token:
            raise ValueError("VERCEL_BLOB_TOKEN must be set in settings or passed to methods")

    def save(self, name, content, **kwargs):
        # Upload do arquivo para o blob storage
        response = blob.put(
            pathname=name,
            body=content.read(),
            options={'token': self.token}
        )
        if response.get('url'):
            return name  # Retorna o nome do arquivo salvo
        else:
            raise Exception(f"Failed to upload file to Vercel Blob Storage: {response}")

    def url(self, name):
        return f"{self.base_url}/{name}"

    def exists(self, name):
        # Método para verificar se o arquivo existe
        response = blob.head(name, options={'token': self.token})
        return response.status_code == 200


    def delete(self, name):
        response = blob.delete(name, options={'token': self.token})
        if not response.get('success', False):
            raise Exception(f"Failed to delete file: {name}")

    def list_files(self, prefix=None):
        options = {'token': self.token}
        if prefix:
            options['prefix'] = prefix
        response = blob.list(options=options)
        return response.get('items', [])

    def copy_file(self, source_url, destination_path):
        response = blob.copy(source_url, destination_path, options={'token': self.token})
        if not response.get('success', False):
            raise Exception(f"Failed to copy file from {source_url} to {destination_path}")

    def file_info(self, name):
        response = blob.head(name, options={'token': self.token})
        return response
    
    def exists(self, name):
        return False
    
    def generate_filename(self, filename):
        # Retorna o nome do arquivo gerado; pode ser customizado para um diretório específico
        return filename