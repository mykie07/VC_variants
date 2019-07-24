from constraint import *

problem = Problem()
def create_chars():
    problem.addVariable("VC_CHR_GRAPHIC_CARD", ["N-Graphic", "A-Graphic", "Onboard"])
    problem.addVariable("VC_CHR_TYPE", ["Laptop", "Office", "Gaming", "Server"])
    problem.addVariable("VC_CHR_CPU", ["A-CPU", "I-CPU"])
    problem.addVariable("VC_CHR_MAIN_MEMORY", ["2", "4", "8", "16"])
    problem.addVariable("VC_MAT_EQU_SOUND", ["Yes", "No" ])
    problem.addVariable("VC_MAT_EQU_TV", ["Yes", "No" ])
    problem.addVariable("VC_MAT_EQU_MODEM", ["Yes", "No" ])

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
    create_chars()
    VC_CHR_GRAPHIC_CARD = "N-Graphic"
    VC_CHR_TYPE = "Gaming" #None #"Gaming"              ######find a way to search with empty assignments
    VC_CHR_CPU = "I-CPU"
    VC_CHR_MAIN_MEMORY = "4" #"4"
    VC_MAT_EQU_SOUND = "No"
    VC_MAT_EQU_TV = "No"
    VC_MAT_EQU_MODEM = "No"

    create_constraints(
                    VC_CHR_GRAPHIC_CARD,
                    VC_CHR_TYPE,
                    VC_CHR_CPU,
                    VC_CHR_MAIN_MEMORY,
                    VC_MAT_EQU_SOUND,
                    VC_MAT_EQU_TV,
                    VC_MAT_EQU_MODEM
    )

    results = problem.getSolutions() \
              # in ({'VC_CHR_MAIN_MEMORY': 4}, {'VC_CHR_MAIN_MEMORY': 8})

    for x in results[:]:
        print(x)
    print(type(results))
    print(len(results))

    import pandas as pd

    df=pd.DataFrame(results)
    print(df.head())
    #MY_VAR = "N-Graphic"
    dd=df[(df['VC_CHR_GRAPHIC_CARD'] ==VC_CHR_GRAPHIC_CARD) & (df['VC_CHR_TYPE'] == VC_CHR_TYPE) &
          (df['VC_CHR_CPU'] == VC_CHR_CPU) & (df['VC_CHR_MAIN_MEMORY'] == VC_CHR_MAIN_MEMORY) & (df['VC_MAT_EQU_SOUND'] == VC_MAT_EQU_SOUND) &
          (df['VC_MAT_EQU_TV'] == VC_MAT_EQU_TV) & (df['VC_MAT_EQU_MODEM'] == VC_MAT_EQU_MODEM)
          ]
#dd dataframe filtering does not produce any row is a characteristic is assigned a None value
#This actually means that the user has not submited a value, however the system should till give a limited list of variants.
#SEARCH THE DATAFRAME WITH PLACE HOLDER WILD CARD LIKE FEATURE

    print(dd.to_string())

    # print(results(({'VC_CHR_MAIN_MEMORY': 4}, {'VC_CHR_MAIN_MEMORY': 8})))
    # print(results["VC_CHR_MAIN_MEMORY"])

    # rr=list(filter(lambda x: x if x['VC_CHR_MAIN_MEMORY'] == 8 else None, results.  values()))
    # print(rr)
    #
    # print(results)
