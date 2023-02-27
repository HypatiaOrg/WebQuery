import requests
from typing import Dict

from hyquery.config.get_key import api_key
from hyquery.config.api_options import get_api_url


def hyquery(params: Dict[str, str], verbose: bool = False):
    response = requests.get(get_api_url(local_test_mode=True),
                            auth=(api_key, "api_token"),
                            params=params)
    if verbose:
        print(f'Remaining queries {response.headers["X-Rate-Limit-Remaining"]} before reset in ' +
              f'{response.headers["X-Rate-Limit-Reset"]} seconds.')
    if response.status_code != 200:
        print(f'Error code: {response.status_code}')
        print(f'Error text: {response.text}')
        return None, response
    else:
        json = response.json()
    return json, response

