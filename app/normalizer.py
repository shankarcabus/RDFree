#!/usr/bin/env python
# -*- coding: utf-8 -*-

def normalizer(results):

  nodes = {}
  ties = []

  # Creates dict with variables (columns):
  # nodes = { 'foo' : {}, 'bar' : {} }
  for var in results['head']['vars']:
    nodes[var] = {}

  count = 1
  # Runs the rows
  for item in results['results']['bindings']:
    tie = []
    # Runs the columns of row
    for node in nodes.keys():
      label = item[node]['value']

      _id = None
      # Check if node exists and add
      if not nodes[node].has_key(label):
        _id = count
        nodes[node][label] = {'id' : _id}
        count += 1
      else:
        _id = nodes[node][label]['id']

      tie.append(_id)

    ties.append(tie)

  print nodes
  print '*'*50
  print ties

  return nodes, ties
