import requests
from typing import Dict, List, Union

from hyquery.config.get_key import api_key
from hyquery.config.api_options import get_api_url, check_mode


def hyquery(params: Dict[str, str] = None,
            mode: str = 'composition',
            verbose: bool = False,
            local_test_mode: bool = False):
    check_mode(mode=mode, params=params)
    url = get_api_url(local_test_mode=local_test_mode) + mode
    if params is None:
        response = requests.get(url, auth=(api_key, "api_token"))
    else:
        response = requests.get(url, auth=(api_key, "api_token"), params=params)
    if response.status_code != 200:
        print(f'Error code: {response.status_code}')
        print(f'Error text: {response.text}')
        return None, response
    else:
        if verbose:
            print(f'Remaining queries {response.headers["X-Rate-Limit-Remaining"]} before reset in ' +
                  f'{response.headers["X-Rate-Limit-Reset"]} seconds.')
        json = response.json()
    return json, response


def make_params(name: Union[str, List[str]],
                element: Union[str, List[str]] = 'SiH',
                solarnorm: Union[str, List[str]] = 'lod09'):
    if isinstance(name, str):
        name = [name]
    if isinstance(element, str):
        element = [element]
    if isinstance(solarnorm, str):
        solarnorm = [solarnorm]
    names = name * len(element) * len(solarnorm)
    elements = element * len(solarnorm) * len(name)
    solarnorms = solarnorm * len(name) * len(element)
    params = {"name": names, "element": elements, "solarnorm": solarnorms}
    return params
