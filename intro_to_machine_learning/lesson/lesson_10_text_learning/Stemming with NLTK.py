# -*- coding: utf-8 -*-
"""
Created on Sat Dec 06 17:40:14 2014

@author: tvu
"""

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
stemmer.stem("responsiveness")
stemmer.stem("responsivity")
stemmer.stem("unresponsive")