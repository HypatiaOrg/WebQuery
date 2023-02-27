from hyquery.query import hyquery


params = {"name": "HD 23127",
          "element": 'CH',
          "solarnorm": 'lod09'}

json, response = hyquery(params, verbose=True)

print(json)


