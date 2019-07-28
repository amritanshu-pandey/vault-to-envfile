import json
import os

import requests

from urllib.parse import urljoin

VAULT_ADDR = os.environ['PLUGIN_VAULT_ADDR']
VAULT_TOKEN = os.environ['PLUGIN_VAULT_TOKEN']
VAULT_SECRET_PATH = os.environ['PLUGIN_VAULT_SECRET_PATH']
OUTPUT_ENV_FILE = os.environ.get('PLUGIN_VAULT_ENV_FILE', '/drone/src/vault.env')

VAULT_API_VERSION_STRING = 'v1'

def get_vault_secrets():
    vault_url = urljoin(
        VAULT_ADDR, f'{VAULT_API_VERSION_STRING}/{VAULT_SECRET_PATH}'
    )

    print(f'INFO: Vault path = {vault_url}')

    request_output = requests.get(
        url=vault_url,
        headers={
            'X-Vault-Token': VAULT_TOKEN
        }
    ).json()

    secrets_found = request_output['data']['data']

    return secrets_found

def write_env_file(secrets_dict):
    with open(OUTPUT_ENV_FILE, 'w') as envfile:
        for k,v in secrets_dict.items():
            envfile.write(f'{k}={v}\n')
    print(f'INFO: Wrote {len(secrets_dict)} entries to {OUTPUT_ENV_FILE}')

if __name__ == '__main__':
    secrets_dict = get_vault_secrets()
    write_env_file(secrets_dict)
