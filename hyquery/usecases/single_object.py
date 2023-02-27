from hyquery.query import hyquery, make_params


# params = {"name": "HD 23127",
#           "element": 'CH',
#           "solarnorm": 'lod09'}

params = make_params(name=['HD 23127', 'HIP 98355'],
                     element=['FeH', 'CH', 'OH', 'NaH', 'MgH', 'AlH', 'SiH', 'CaH', 'YH', 'BaIIH'],
                     solarnorm='lod09')
json, response = hyquery(params, verbose=True)
print(json)


