#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gexf import Gexf
import config

class Gephi():

  def convert(self,nodes,ties):

    gexf = Gexf(config.CREATOR, config.DESCRIPTION)
    graph = gexf.addGraph(config.DEFAULTEDGETYPE, config.MODE, config.LABEL)

    # Percorre todos os nós
    for node in nodes.keys():
      for item in nodes[node]:
        graph.addNode(nodes[node][item]['id'], item)

    for i in xrange(len(ties)):
      graph.addEdge(i, ties[i][0], ties[i][1])

    output = open(config.OUTPUT_FILE,'w')
    gexf.write(output)

    output.close()