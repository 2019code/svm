from sklearn import svm
import matplotlib.colors
import matplotlib.pyplot as plt
from sklearn.metrics import accuacy_score, precision_score,recall_score,f1_score
from sklearn.exceptions import undefinedMetricWarning
import warnings 


if __name__ == "__main__:
    warnings.filterwarnings(action='ignore', category=UnderfinedMetricWarning)
    np.random.seed(0)
    
    c1 = 990
    c2 = 10
    N = c1 + c2
    x_c1 = 3*np.rendom.randn(c1,2)
    x_c2 = 0.5*np.random.randn(c2,2) + (4,4)
    x = np.vstack((x_c1,x_c2))
    y = np.ones(N)
    
