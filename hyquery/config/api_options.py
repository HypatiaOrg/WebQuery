hypatia_url = "https://hypatiacatalog.com"
testing_url = 'http://127.0.0.1:8000'

api_uri = "/hypatia/api/v2/"


def get_api_url(local_test_mode=False):
    if local_test_mode:
        return testing_url + api_uri
    else:
        return hypatia_url + api_uri


modes_without_params = {
    'solarnorm',
    'element',
    'catalog',
}

modes_with_params = {
    'star',
    'composition',
    'data',
}

modes_all = modes_without_params | modes_with_params


def check_mode(mode, params):
    if mode not in modes_all:
        raise ValueError(f'Mode {mode} not in {modes_all}')
    if mode in modes_without_params and params is not None:
        raise ValueError(f'Mode {mode} does not take parameters')
    if mode in modes_with_params and params is None:
        raise ValueError(f'Mode {mode} requires parameters')
