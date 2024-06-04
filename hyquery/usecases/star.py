"""For getting stellar data from the hypatia catalog"""

from hyquery.query import hyquery


verbose = True
local_test = True
star_names = ['kepler-11', 'HD 23127']
params = {"name": star_names}

if __name__ == '__main__':
    # star query example,
    star_json, star_response = hyquery(params=params, mode='star', verbose=verbose, local_test_mode=local_test)
