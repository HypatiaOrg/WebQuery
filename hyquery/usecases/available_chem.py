from hyquery.query import hyquery


verbose = True
if __name__ == '__main__':
    # data query for default return example
    local_json, local_data_default_response = hyquery(params=None, mode='element',
                                                      verbose=verbose, local_test_mode=True)

    live_json, live_data_default_response = hyquery(params=None, mode='element',
                                                    verbose=verbose, local_test_mode=False)

    diff = sorted(set(live_json) - set(local_json))
    local_list = sorted(local_json)
    local_set = set(local_list)
    live_list = sorted(live_json)
    live_set = set(live_list)
    for el_index, element_name in list(enumerate(live_json)):
        el_str = f'{el_index:3}: {element_name:8}'
        if element_name in diff:
            print(f'{el_str} <--- Missing from Local')
        elif local_set:
            print(f'{el_str}')
        else:
            print(f'{el_str} <--- Missing from Live!!!!!!')
