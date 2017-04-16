import os
from app import app

class UploadImage(object):
    def __init__(self):
        self.APP_ROOT = app.root_path

    def process(self, domain):
        target = os.path.join(self.APP_ROOT, 'static/images/')

        if not os.path.isdir(target):
            os.mkdir(target)

        filename = domain['image'].filename
        destination = '/'.join([target, filename])
        domain['image'].save(destination)
