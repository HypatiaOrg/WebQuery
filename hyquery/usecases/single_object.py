"""For getting elemental abundance data from hypatiacatalog.com for a single star"""
from hyquery.query import hyquery, make_params


verbose = True
local_test = False
params = make_params(name='HD 23127',
                     element=['FeH', 'CH', 'OH', 'NaH', 'MgH', 'AlH', 'SiH', 'CaH', 'YH', 'BaIIH'],
                     solarnorm='lod09')

if __name__ == "__main__":
    # single object query example, for multiple objects in the same query see composition.py query example
    single_json, single_response = hyquery(params=params, mode='composition',
                                           verbose=verbose, local_test_mode=local_test)
    print(f'single query json {single_json}')

