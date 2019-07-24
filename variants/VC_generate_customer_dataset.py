from constraint import *

from variants import VC_find_valid_variants

import random
import numpy
import pandas as pd
import os
 #   list = [20.5, 40.5, 30.5, 50.5, 70.5]

def generate_samples( *params, k):
    random.seed(4)
    # sample_list = random.sample(list, 3)
    # print("random List", sample_list)


    sample_list = random.choices(*params,k)
    #print("random List", sample_list)
    return sample_list




def initialize_seed():
    random.seed(4)

    return


if __name__ == "__main__":
    initialize_seed()
    # list = [20.5, 40.5, 30.5, 50.5, 70.5]
    # x=numpy.random.randn(4,5)
    # df=pd.DataFrame(x)
    # print(df)
    #
    # random_with_replacement=df.sample(10,replace=True)
    # print(random_with_replacement)
    #
    # print(random_with_replacement[9:])
    #
    # random_with_replacement=random_with_replacement.reset_index(drop=True)
    #
    # print(random_with_replacement)

    trainFile = "C:\\Users\\mike\\PycharmProjects\\csp1\\csp\\my_variants.csv"
    pwd = os.getcwd()
    os.chdir(os.path.dirname(trainFile))
    my_variants = pd.read_csv(os.path.basename(trainFile))

    print(len(my_variants))

    print(my_variants.head())
    random_with_replacement=my_variants.sample(100000,replace=True)

    print(random_with_replacement.head())


    #
    # random_with_replacement=random_with_replacement.drop(columns='ID')
    # random_with_replacement=random_with_replacement.reset_index(drop=True)


    plus1= random_with_replacement['ID']+1
    random_with_replacement['ID']=plus1
    print(random_with_replacement.head())

    random_with_replacement["new"]=1
    print(random_with_replacement.head())

    print(len(random_with_replacement))

    random_with_replacement=random_with_replacement.reset_index(drop=True)

    print(random_with_replacement.head())

    variant=random_with_replacement.iloc[[2]]['ID']
    print(variant)

    print(random_with_replacement[2:3])