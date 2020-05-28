# elasticsearch configurations
host = 'localhost'
host_addr = 'localhost:9200'
elastic_username = 'elastic'
elastic_password = 'elastic123'
index_name = 'pak_pop_100m_gt_5'


buffer_distance = 0.008
# elasticsearch mapping for the rollout index
mapping = {
    "settings": {
        "number_of_shards": 2,
        "number_of_replicas": 0
    },
    "mappings": {
        "properties": {
            "x":{
                "type":"long"
            },
            "y":{
                "type":"long"
            },
            "location" : {
              "type" : "geo_point"
            },
            "pop":{
                "type":"long"
            }
        }
    }
}

query_body = {
  "query": {
    "bool": {
      "filter": [
        {
          "term": {
            "District": "BAHAWALNAGAR"
          }
        }
      ]
    }
  }
}