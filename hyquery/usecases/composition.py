"""
For getting elemental abundance data from hypatiacatalog.com
Request multiple stars, elements, and even solar normalizations.
"""
from hyquery.query import hyquery, make_params


verbose = True
local_test = False
star_names = ['Kepler-11']
params = make_params(name=star_names,
                     element=['FeH', 'CH', 'OH', 'NaH', 'MgH', 'AlH', 'SiH', 'CaH', 'YH', 'BaIIH'],
                     solarnorm='lod09')

if __name__ == "__main__":
    # composition query example
    comp_json, comp_response = hyquery(params=params, mode='composition', verbose=verbose, local_test_mode=local_test)
    print(f'composition query json: {comp_json}')
