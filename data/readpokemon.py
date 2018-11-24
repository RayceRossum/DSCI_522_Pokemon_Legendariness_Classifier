import sys
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.feature_extraction.text import CountVectorizer

pokemon = pd.read_csv("./data/Pokemon.csv")
pokemon.head()
