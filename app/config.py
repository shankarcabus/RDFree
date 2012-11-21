#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
DESCRIPTION = u'Aplicando a solucao em um dominio'
DEFAULTEDGETYPE = 'undirected'
MODE = 'static'
LABEL = 'Relacionamento entre bandas e genero'