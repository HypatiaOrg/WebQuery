"""For getting plot-like data returns from the hypatiacatalog.com"""
from hyquery.query import hyquery


verbose = True
local_test = False

if __name__ == '__main__':
    # data query for default return example
    data_default_json, data_default_response = hyquery(params=None, mode='data',
                                                       verbose=verbose, local_test_mode=local_test)

    # data query for histogram example
    data_hist_json, data_hist_response = hyquery(params={'mode': 'hist'}, mode='data',
                                                 verbose=verbose, local_test_mode=local_test)
    print(f'histogram data-query example {data_hist_json}')
