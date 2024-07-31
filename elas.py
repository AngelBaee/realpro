from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200/')

index_name = "my_index"

es.indices.create(index = index_name)

document ={
    "title": "Cleaning Company",
    "content": "service"
}

es.index(index=index_name, body=document)

search_query = ""

res = es.search(index = index_name, body = {
    "query": {
        "match":{
            "content": search_query
        }
    }
})

for hit in res ['hits']['hits']:
    print(hit['_source'])
