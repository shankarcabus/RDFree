# RDFree

A computational solution for integrating Semantic Web and Complex Networks.

RDFree is a converter of the semantic web data to formats readable by software of network analysis ([Pajek](http://vlado.fmf.uni-lj.si/pub/networks/pajek/), [Gephi](https://gephi.org/), etc.).

## Get Started

Edits the `config.py`
```python
OUTPUT_FILE = 'output.gexf'
ENDPOINT = "http://dbpedia.org/sparql"
QUERY = '''
  SELECT ?band_uri, ?genre_uri
  WHERE {
    ?band_uri a <http://dbpedia.org/ontology/Band> ;
    dbpedia-owl:genre ?genre_uri .
  }
  LIMIT 1000
'''

# GEXF
CREATOR = 'Shankar Cabus de Teive e Argollo'
DESCRIPTION = u'Get Start'
DEFAULTEDGETYPE = 'undirected'
MODE = 'static'
LABEL = 'Relacionamento entre bandas e genero'
```
