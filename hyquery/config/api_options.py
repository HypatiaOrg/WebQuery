hypatia_url = "https://hypatiacatalog.com"
testing_url = 'http://127.0.0.1'

api_uri = "/hypatia/api/v2/"


def get_url(local_test_mode=False):
    if local_test_mode:
        return testing_url
    else:
        return hypatia_url


def get_api_url(local_test_mode=False):
    return get_url(local_test_mode) + api_uri


modes_without_params = {
    'solarnorm',
    'element',
    'catalog',
    'data',
    'nea',
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
    if mode in modes_without_params and params is not None and mode not in modes_with_params:
        raise ValueError(f'Mode {mode} does not take parameters')
    if mode in modes_with_params and params is None and mode not in modes_without_params:
        raise ValueError(f'Mode {mode} requires parameters')
