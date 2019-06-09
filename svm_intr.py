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
    y = pd.Categorical(y).codes
    x = x[[0,1]]
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1,train_size=0.6)
    
    # fen lei 
    clf = svm.SVC(C=0.1, kernel='linear', decision_function_shape='ovr')
    clf.fit(x_train,y_train.ravel())
    
    print clf.score(x_train, y_train)
    print 'xunlianji:'
    print clf.score(x_test, y_test)
    print 'ceshiji:'
    
    
    
