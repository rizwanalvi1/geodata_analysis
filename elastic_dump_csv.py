from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from elasticsearch import ElasticsearchException
import csv
import uuid
import configurations as conf
import geojson

# es=Elasticsearch(['localhost:9200'],http_auth=('elastic', 'sshclient'))
es = Elasticsearch([conf.host_addr])

print(es.indices.delete(index=conf.index_name, ignore=[400, 404]))

response = es.indices.create(
    index=conf.index_name,
    body=conf.mapping,
    ignore=400 # ignore 400 already exists code
)
print('response:', response)

url = 'C:\\Users\\Dell\\Documents\\GIS DataBase\\processed\\popmap15adj_vector_points_gt_5_geojson.geojson'

with open(url) as f:
    data = geojson.load(f)

actions = []

for d in data['features']:
    doc = {
        'x' : d['geometry']['coordinates'][0],
        'y' : d['geometry']['coordinates'][1],
        'pop' : d['properties']['VALUE'],
        'location':
            {
                "lat": str(d['geometry']['coordinates'][1]),
                "lon": str(d['geometry']['coordinates'][0])
            }
    }
    action = [{"_source": doc}]
    actions.append(action[0])

try:
    response = helpers.bulk(es, actions, index=conf.index_name)
    print("\nRESPONSE:", response)
except ElasticsearchException as e:
    print("\nERROR:", e)
# for action in actions:
#     print(action[0])
