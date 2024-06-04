"""For getting stellar data from the hypatia catalog"""

from hyquery.query import hyquery


verbose = True
local_test = True

if __name__ == '__main__':
    # star query example,
    star_json, star_response = hyquery(mode='solarnorm', verbose=verbose, local_test_mode=local_test)
    for rec in star_json:
        print(rec['identifier'], rec['author'])
