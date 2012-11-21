#!/usr/bin/env python
# -*- coding: utf-8 -*-

from templates.gephi import Gephi
from extractor import extractor
from normalizer import normalizer

if __name__ == "__main__":

  results = extractor()
  nodes, ties = normalizer(results)

  # Convertendo para gexf
  gephi = Gephi()
  gephi.convert(nodes, ties)



