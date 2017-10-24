import elasticsearch
from pten.ElasticSearch import config

class ESOperations():
    index = ''
    doc_type = config.doc_type
    esClient = None
    es = None

    def __init__(self,myindex=None,mytype=None):
        self.es = elasticsearch.Elasticsearch()
        self.esClient = elasticsearch.client.IndicesClient(self.es)
        if myindex:
            self.index = myindex
        else:
            self.index = config.index
        if mytype:
            self.doc_type = mytype
        else:
            self.doc_type = config.doc_type

    def insertDocumentES(self,data):
        self.es.index(index=self.index, doc_type=self.doc_type, id=data[0],
                 body={"Purpose": data[1],"Inclusion Criteria":data[2],"Exclusion Criteria":data[3],
                       "description": data[4],"gender":data[5],"minimumAge":data[6],"maximumAge":data[7],"brief_title":data[8],"official_title":data[9],"Conditions":data[10],
                       "stages":data[11], "grades" : data[12],"locations" : data[13],"update_date":data[14]})


    def putMappingES(self):
        self.esClient.put_mapping(
            doc_type=self.doc_type,
            body={
                self.doc_type : {
                "properties" : {
                    "Exclusion Criteria": {
                        "type": "multi_field",
                        "fields":{
                            "Exclusion Criteria" : {"type" : "string","analyzer":"gene_synonyms","search_analyzer" :"gene_synonyms"},
                            "whitespace":{"type" : "string" ,"analyzer":"gene_synonyms_whitespace","search_analyzer" :"gene_synonyms_whitespace"},
                            "normal" : {"type" : "string","analyzer" : "normal"},
                            "disease" : {"type" : "string","analyzer":"gene_synonyms","search_analyzer" :"gene_synonyms"},
                            "disease_whitespace": {"type" : "string" ,"analyzer":"disease_synonyms_whitespace","search_analyzer" :"disease_synonyms_whitespace"}
                        }
                       },
                       "Inclusion Criteria": {
                          "type": "multi_field",
                        "fields":{
                            "Inclusion Criteria" : {"type" : "string","analyzer":"gene_synonyms","search_analyzer" :"gene_synonyms"},
                            "whitespace":{"type" : "string" ,"analyzer":"gene_synonyms_whitespace","search_analyzer" :"gene_synonyms_whitespace"},
                            "normal" : {"type" : "string","analyzer" : "normal"},
                            "disease" : {"type" : "string","analyzer":"gene_synonyms","search_analyzer" :"gene_synonyms"},
                            "disease_whitespace": {"type" : "string" ,"analyzer":"disease_synonyms_whitespace","search_analyzer" :"disease_synonyms_whitespace"}
                        }
                       },
                       "Purpose": {
                          "type": "multi_field",
                        "fields":{
                            "Purpose" : {"type" : "string","analyzer":"gene_synonyms","search_analyzer" :"gene_synonyms"},
                            "whitespace":{"type" : "string" ,"analyzer":"gene_synonyms_whitespace","search_analyzer" :"gene_synonyms_whitespace"},
                            "normal" : {"type" : "string","analyzer" : "normal"},
                            "disease" : {"type" : "string","analyzer":"gene_synonyms","search_analyzer" :"gene_synonyms"},
                            "disease_whitespace": {"type" : "string" ,"analyzer":"disease_synonyms_whitespace","search_analyzer" :"disease_synonyms_whitespace"}
                        }
                       },
                       "description": {
                          "type": "multi_field",
                        "fields":{
                            "description" : {"type" : "string","analyzer":"gene_synonyms","search_analyzer" :"gene_synonyms"},
                            "whitespace":{"type" : "string" ,"analyzer":"gene_synonyms_whitespace","search_analyzer" :"gene_synonyms_whitespace"},
                            "normal" : {"type" : "string","analyzer" : "normal"},
                            "disease" : {"type" : "string","analyzer":"gene_synonyms","search_analyzer" :"gene_synonyms"},
                            "disease_whitespace": {"type" : "string" ,"analyzer":"disease_synonyms_whitespace","search_analyzer" :"disease_synonyms_whitespace"}
                        }
                       },
                       "gender": {
                          "type": "string"
                       },
                       "maximumAge": {
                          "type": "long"
                       },
                       "minimumAge": {
                          "type": "long"
                       },
                       "brief_title": {
                         "type": "multi_field",
                        "fields":{
                            "brief_title" : {"type" : "string","analyzer":"gene_synonyms","search_analyzer" :"gene_synonyms"},
                            "whitespace":{"type" : "string" ,"analyzer":"gene_synonyms_whitespace","search_analyzer" :"gene_synonyms_whitespace"},
                            "normal" : {"type" : "string","analyzer" : "normal"},
                            "disease" : {"type" : "string","analyzer":"gene_synonyms","search_analyzer" :"gene_synonyms"},
                            "disease_whitespace": {"type" : "string" ,"analyzer":"disease_synonyms_whitespace","search_analyzer" :"disease_synonyms_whitespace"}
                        }
                       },
                       "official_title": {
                          "type": "multi_field",
                        "fields":{
                            "official_title" : {"type" : "string","analyzer":"gene_synonyms","search_analyzer" :"gene_synonyms"},
                            "whitespace":{"type" : "string" ,"analyzer":"gene_synonyms_whitespace","search_analyzer" :"gene_synonyms_whitespace"},
                            "normal" : {"type" : "string","analyzer" : "normal"},
                            "disease" : {"type" : "string","analyzer":"gene_synonyms","search_analyzer" :"gene_synonyms"},
                            "disease_whitespace": {"type" : "string" ,"analyzer":"disease_synonyms_whitespace","search_analyzer" :"disease_synonyms_whitespace"}
                        }
                       },
                       "conditions": {
                          "type": "multi_field",
                        "fields":{
                            "conditions" : {"type" : "string","analyzer":"gene_synonyms","search_analyzer" :"gene_synonyms"},
                            "whitespace":{"type" : "string" ,"analyzer":"gene_synonyms_whitespace","search_analyzer" :"gene_synonyms_whitespace"},
                            "normal" : {"type" : "string","analyzer" : "normal"},
                            "disease" : {"type" : "string","analyzer":"gene_synonyms","search_analyzer" :"gene_synonyms"},
                            "disease_whitespace": {"type" : "string" ,"analyzer":"disease_synonyms_whitespace","search_analyzer" :"disease_synonyms_whitespace"}
                        }
                       },
                       "stages":{
                            "type":"string",
                       },
                       "grades":{
                           "type":"string"
                       },
                       "locations":{
                           "type":"string"
                       },
                       "update_date":{
                           "type":"date",
                           "format": "yyyy-MM-dd"
                       }
                       
                }
                }
            },
            index=self.index
        )



    def putSettingES(self):
        self.esClient.close(self.index,ignore_unavailable=True)
        #The settings tokenizer is set to standard which might break the names based on '-' and '.' which might not be desirable in using some of the gene mutations.
        #For those cases we will need to use the whitespace tokenizer.

        self.esClient.put_settings(
            body={

                "analysis": {
                   "filter": {
                      "gene_synonym_filter": {
                         "type": "synonym",
                         "synonyms_path": config.synonyms_file
                      },
                      "disease_synonym_filter": {
                         "type": "synonym",
                         "synonyms_path": config.disease_synonym_file
                      }
                   },
                   "analyzer": {
                      "normal": {
                         "filter": [
                            "lowercase"
                         ],
                         "tokenizer": "standard"
                      },
                      "normal_whitespace": {
                         "filter": [
                            "lowercase"
                         ],
                         "tokenizer": "whitespace"
                      },
                      "gene_synonyms": {
                         "filter": [
                            "lowercase",
                            "gene_synonym_filter"
                         ],
                         "tokenizer": "standard"
                      },
                      "gene_synonyms_whitespace": {
                         "filter": [
                            "lowercase",
                            "gene_synonym_filter"
                         ],
                         "tokenizer": "whitespace"
                      },
                      "disease_synonyms": {
                         "filter": [
                            "lowercase",
                            "disease_synonym_filter"
                         ],
                         "tokenizer": "standard"
                      },
                      "disease_synonyms_whitespace": {
                         "filter": [
                            "lowercase",
                            "disease_synonym_filter"
                         ],
                         "tokenizer": "whitespace"
                      }

                   }
                }

            },
            index = self.index
        )

        self.esClient.open(self.index)

    def queryES(self,body,results):
        return 	self.es.search(
                    index = self.index,
                    doc_type=self.doc_type,
                    body = body,
                    size = results
                )

    def explain(self, id, body):
        return self.es.explain(
            index = self.index,
            doc_type=self.doc_type,
            body = body,
            id = id
        )
