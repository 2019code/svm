import numpy as np
import pandas as pd
import matplotlib as mpl
import matplot.pyplot as plt
from sklearn import svm
from  sklearn.metrics import accuracy_score

if __name__ == "__main__":
    path = '..\\phone.data'
    data = pd.read_csv(path,header=None)
    x, y = data[range(4)], data[4]
    
