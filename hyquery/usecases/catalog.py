"""For getting stellar data from the hypatia catalog"""

from hyquery.query import hyquery


verbose = True
local_test = True

if __name__ == '__main__':
    # star query example,
    star_json, star_response = hyquery(mode='catalog', verbose=verbose, local_test_mode=local_test)
    for rec in star_json:
        if rec['override_name'] is not None:
            print(rec['override_name'])
