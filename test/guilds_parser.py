#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a testing script to parse an OTU table for its taxonomic information.

What we want is an output file with OTU name and taxa. Ideally, for an known format,
such as UNITE, SINTAX, RDP, we can have multiple taxa column from phylum to species.

By doing this, we can feed accurate key word to FUNGuild, and search much much faster.

Please feel free to contact me for any question.
Fri Apr 28 08:47:36 2017
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
www.songzewei.org
"""
##%
from __future__ import print_function
from __future__ import division

#%% Input parameters

#%% Read in OTU Tabe
# Txt format

# Biom format                                                        