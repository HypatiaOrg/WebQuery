hypatia_url = "https://hypatiacatalog.com"
testing_url = 'http://127.0.0.1:8000'

api_uri = "/hypatia/api/v2/composition"


def get_api_url(local_test_mode=False):
    if local_test_mode:
        return testing_url + api_uri
    else:
        return hypatia_url + api_uri
