#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SPARQLWrapper import SPARQLWrapper, JSON
import json, config

def extractor():
  results = ''

  print u'Iniciando conversão a partir do endpoint %s'%config.ENDPOINT

  sparql = SPARQLWrapper(config.ENDPOINT)
  sparql.setQuery(config.QUERY)
  sparql.setReturnFormat(JSON)

  print u'Executando query SPARQL...'
  try:
    results = sparql.query().convert()
    print u'Pronto, foram retornados %s resultados.'%len(results['results']['bindings'])
  except Exception as error:
    print 'Ocorreu um erro ao executar a query: \n %s'%error
    return False

    print u'Foram carregados %s resultados'%len(results['results']['bindings'])
  #print results
  return results