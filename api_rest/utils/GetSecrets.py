import json
import os
from django.core.exceptions import ImproperlyConfigured
from pathlib import Path

B_D = Path(__file__).resolve().parent.parent.parent

with open(os.path.join(B_D, 'secrets.json')) as secrets_file:
    secrets = json.load(secrets_file)

def get_secret(setting, secrets=secrets):
    """Get secret setting or fail with ImproperlyConfigured"""
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))