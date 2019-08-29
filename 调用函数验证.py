import numpy as np
from scipy import stats
from scipy.stats import  levene
import matplotlib.pyplot as plt

def demo1():
    mu ,sigma = 0, 1
    sampleNo = 100000
    data_1 = np.random.normal(mu, sigma, sampleNo)
    plt.hist(data_1, bins=100, normed=True)
    plt.title("data distribution")
    plt.xlabel("value")
    plt.show()
    norm_test = stats.kstest(data_1, 'norm', (0, 1)) # p值大于0.05，说明数据是服从正太分布的
    print(norm_test)
def var_test():
    data_1 = np.random.normal(0, 1, 10000)
    data_2 = np.random.normal(0, 999, 10000)
    data_3 = np.random.normal(0, 1, 100)
    print(levene(data_1, data_2)) # p值小于0.05， 说明方差不齐
    print(levene(data_1, data_3)) # p值大于0.05，说明方差是齐的
demo1()
var_test()
