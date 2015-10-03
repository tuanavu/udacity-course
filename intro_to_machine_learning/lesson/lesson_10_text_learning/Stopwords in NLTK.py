# -*- coding: utf-8 -*-
"""
Created on Sat Dec 06 17:06:49 2014

@author: tvu
"""


# Download nltk
# import nltk
# nltk.download()


from nltk.corpus import stopwords
sw = stopwords.words("english")

sw[0]
sw[10]

# Count how many stop words
len(sw)