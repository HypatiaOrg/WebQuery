"""For getting selected elemental abundance data from hypatiacatalog.com
for all hypatiacatalog.com objects know to have an exoplanet."""
from hyquery.query import hyquery


verbose = True
local_test = False

if __name__ == '__main__':
    # nea query example
    nea_json, nea_response = hyquery(mode='nea', verbose=verbose, local_test_mode=local_test)
    # this is a large set of data, so we'll just print the first 100 entries
    print(nea_json[:100])

    wanted = []
    for rec in nea_json:
        is_wanted = False
        for name in rec['all_names']:
            if name.lower().replace(' ', '') == 'kepler-11':
                is_wanted = True
                break
        if is_wanted:
            wanted.append(rec)

