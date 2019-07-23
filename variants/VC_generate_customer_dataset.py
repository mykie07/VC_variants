from constraint import *

from variants import VC_feature_model

import random
import numpy
import pandas as pd

 #   list = [20.5, 40.5, 30.5, 50.5, 70.5]

def generate_samples( *params, k):
    random.seed(4)
    # sample_list = random.sample(list, 3)
    # print("random List", sample_list)


    sample_list = random.choices(*params,k)
    #print("random List", sample_list)
    return sample_list







if __name__ == "__main__":
    list = [20.5, 40.5, 30.5, 50.5, 70.5]
    x=numpy.random.randn(4,5)
    df=pd.DataFrame(x)
    print(df)

    random_with_replacement=df.sample(4,replace=True)
    print(random_with_replacement)