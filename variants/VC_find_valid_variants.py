import os
import pandas as pd

from constraint import *

problem = Problem()

def create_chars():
    problem.addVariable("VC_CHR_GRAPHIC_CARD", ["N-Graphic", "A-Graphic", "Onboard"])
    problem.addVariable("VC_CHR_TYPE", ["Laptop", "Office", "Gaming", "Server"])
    problem.addVariable("VC_CHR_CPU", ["A-CPU", "I-CPU"])
    problem.addVariable("VC_CHR_MAIN_MEMORY", ["2", "4", "8", "16"])
    problem.addVariable("VC_MAT_EQU_SOUND", ["Yes", "No"])
    problem.addVariable("VC_MAT_EQU_TV", ["Yes", "No"])
    problem.addVariable("VC_MAT_EQU_MODEM", ["Yes", "No"])

def create_constraints(
        VC_CHR_GRAPHIC_CARD=None,
                       VC_CHR_TYPE=None,
                       VC_CHR_CPU=None,
                       VC_CHR_MAIN_MEMORY=None,
                       VC_MAT_EQU_SOUND=None,
                       VC_MAT_EQU_TV=None,
                       VC_MAT_EQU_MODEM=None):
#VC_EX_CON1
    # if VC_MAT_EQU_SOUND == "Yes" or VC_MAT_EQU_TV == "Yes" or VC_MAT_EQU_MODEM == "Yes":
    #     problem.addConstraint(lambda sound, tv, modem, typ:
    #                           (sound == "Yes" or tv == "Yes" or modem == "Yes") and
    #                           (typ != "Server" and typ != "Laptop"),
    #                           ("VC_MAT_EQU_SOUND", "VC_MAT_EQU_TV", "VC_MAT_EQU_MODEM", "VC_CHR_TYPE"))
    #

    #VERSION 2

    if VC_MAT_EQU_SOUND == "Yes" or VC_MAT_EQU_TV == "Yes" or VC_MAT_EQU_MODEM == "Yes":
        problem.addConstraint(lambda xx, typ:

                              (typ != "Server" and typ != "Laptop"),
                              ("VC_MAT_EQU_SOUND","VC_CHR_TYPE")
                              )



#VC_EX_CON2
    # if VC_CHR_MAIN_MEMORY == "8" or VC_CHR_MAIN_MEMORY == "16" or VC_CHR_CPU == "A-CPU":
    #     problem.addConstraint(
    #         lambda memory, cpu, typ:
    #         (memory == "8" or memory == "16" or cpu == "A-CPU") and
    #         typ == "Server",
    #         ("VC_CHR_MAIN_MEMORY", "VC_CHR_CPU", "VC_CHR_TYPE")
    #
    #     )

    #VERSION 2

    if (VC_CHR_MAIN_MEMORY == "8" or VC_CHR_MAIN_MEMORY == "16") and VC_CHR_CPU == "A-CPU":
        problem.addConstraint(
            lambda xx, typ:

            typ == "Server",
            ("VC_CHR_CPU", "VC_CHR_TYPE")


            )

#VC_EX_CON3


    #VERSION 2
    if VC_CHR_GRAPHIC_CARD == "N-Graphic" or VC_CHR_GRAPHIC_CARD == "A-Graphic":
        problem.addConstraint(
            lambda xx, typ:

            typ== "Gaming" or typ == "Laptop",
            ("VC_CHR_CPU", "VC_CHR_TYPE")

        )



#VC_EX_CON4
    if VC_CHR_GRAPHIC_CARD == "Onboard":
        problem.addConstraint(
            lambda xx, typ :

            typ == "Server" or typ == "Office",
            ("VC_CHR_CPU", "VC_CHR_TYPE")

        )






if __name__ == "__main__":
    trainFile = "C:\\Users\\mike\\PycharmProjects\\csp1\\csp\\my_variants.csv"
    pwd = os.getcwd()
    os.chdir(os.path.dirname(trainFile))
    my_selections = pd.read_csv(os.path.basename(trainFile))
    # df = pd.read_csv(os.path.basename(trainFile))

    create_chars()

    # # results = problem.getSolutions()
    # # rs = pd.DataFrame(results)
    # print(my_selections)
    #
    # # for x in results[:]:
    # #     print(x)
    #
    # print(len(my_selections))
    # print(type(my_selections))
    # # results = pd.DataFrame(results)
    # print(my_selections.head())
    #
    # # results = problem.getSolutions()
    # valid_count = 0
    # for i in range(len(my_selections)):
    #     #
    #     VC_CHR_GRAPHIC_CARD = str(my_selections.iloc[i]["VC_CHR_GRAPHIC_CARD"])#"N-Graphic"
    #     VC_CHR_TYPE = str(my_selections.iloc[i]["VC_CHR_TYPE"])    #"Gaming"  # None #"Gaming"
    #     VC_CHR_CPU = str(my_selections.iloc[i]["VC_CHR_CPU"]) #"I-CPU"
    #     VC_CHR_MAIN_MEMORY = str(my_selections.iloc[i]["VC_CHR_MAIN_MEMORY"])  # None  # "4"
    #     VC_MAT_EQU_SOUND = str(my_selections.iloc[i]["VC_MAT_EQU_SOUND"])  #"No"
    #     VC_MAT_EQU_TV = str(my_selections.iloc[i]["VC_MAT_EQU_TV"])    #"No"
    #     VC_MAT_EQU_MODEM = str(my_selections.iloc[i]["VC_MAT_EQU_MODEM"])    #"No"
    #
    #     create_constraints(
    #         VC_CHR_GRAPHIC_CARD,
    #         VC_CHR_TYPE,
    #         VC_CHR_CPU,
    #         VC_CHR_MAIN_MEMORY,
    #         VC_MAT_EQU_SOUND,
    #         VC_MAT_EQU_TV,
    #         VC_MAT_EQU_MODEM
    #     )
    # #
    #     solution_space = problem.getSolutions()
    # #
    #     # print("combination no: " + str(i) + " has " + str(len(solution_space)) + " solutions")
    # #     # print(VC_CHR_TYPE)
    # #     # print(VC_CHR_GRAPHIC_CARD)
    #     if len(solution_space) > 0:
    #
    #         df = pd.DataFrame(solution_space)
    #         # print(len(df))
    #         valid_variant = df[(df['VC_CHR_GRAPHIC_CARD'] == VC_CHR_GRAPHIC_CARD) & (df['VC_CHR_TYPE'] == VC_CHR_TYPE) &
    #                 (df['VC_CHR_CPU'] == VC_CHR_CPU) & (df['VC_CHR_MAIN_MEMORY'] == VC_CHR_MAIN_MEMORY) & (df['VC_MAT_EQU_SOUND'] == VC_MAT_EQU_SOUND) &
    #                 (df['VC_MAT_EQU_TV'] == VC_MAT_EQU_TV) & (df['VC_MAT_EQU_MODEM'] == VC_MAT_EQU_MODEM)
    #                 ]
    #         if len(valid_variant) > 0:
    #             valid_count=valid_count+1
    #             print(my_selections.loc[i])
    #             print(valid_variant.to_string())
    # print("valid count is : ", valid_count)
    #     # print(type(VC_MAT_EQU_MODEM))
    #     # print(VC_MAT_EQU_MODEM)
    #     # # x=VC_MAT_EQU_MODEM
    #     # # if x=='No':
    #     # #     print(x)
    #     # print(df.head())

    # create_chars()
    # VC_CHR_GRAPHIC_CARD = "N-Graphic"
    # VC_CHR_TYPE = "Gaming"  # None #"Gaming"              ######find a way to search with empty assignments
    # VC_CHR_CPU = "I-CPU"
    # VC_CHR_MAIN_MEMORY = "4"  # "4"
    # VC_MAT_EQU_SOUND = "No"
    # VC_MAT_EQU_TV = "No"
    # VC_MAT_EQU_MODEM = "No"

    VC_CHR_GRAPHIC_CARD = 'A-Graphic'
    VC_CHR_TYPE = "Server"              ######find a way to search with empty assignments
    VC_CHR_CPU = "A-CPU"
    VC_CHR_MAIN_MEMORY = "4"
    VC_MAT_EQU_SOUND = None
    VC_MAT_EQU_TV = None
    VC_MAT_EQU_MODEM = None

    create_constraints(
        VC_CHR_GRAPHIC_CARD,
        VC_CHR_TYPE,
        VC_CHR_CPU,
        VC_CHR_MAIN_MEMORY,
        VC_MAT_EQU_SOUND,
        VC_MAT_EQU_TV,
        VC_MAT_EQU_MODEM
    )

    results = problem.getSolutions()
    for x in results:
        print(x)
    df=pd.DataFrame(results)
    print(len(df))
    print(my_selections.head())

    valid_variant = df[ (df['VC_CHR_TYPE'] == "Gaming") & (df['VC_CHR_CPU'] == "I-CPU") & (df['VC_CHR_MAIN_MEMORY'] == "4")
    & (df['VC_CHR_GRAPHIC_CARD'] == "N-Graphic") & (df['VC_MAT_EQU_SOUND'] == "No") & (df['VC_MAT_EQU_MODEM'] == "No")
    & (df['VC_MAT_EQU_TV'] == 'No')]


    print(valid_variant.to_string())