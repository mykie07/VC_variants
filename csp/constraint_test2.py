#This version of the configuration of laptop has no constraints
#It generates all possible valid configurations
#It writes these cnfigurations to a CSV a configuration per row

if __name__ == "__main__":
    from constraint import *
    problem = Problem()
    problem.addVariable("VC_CHR_GRAPHIC_CARD", ["N-Graphic", "A-Graphic", "Onboard"])
    problem.addVariable("VC_CHR_TYPE", ["Laptop", "Office", "Gaming", "Server"])
    problem.addVariable("VC_CHR_CPU", ["A-CPU", "I-CPU"])
    problem.addVariable("VC_CHR_MAIN_MEMORY", ["2", "4", "8", "16"])
    problem.addVariable("VC_MAT_EQU_SOUND",["Yes", "No", ])
    problem.addVariable("VC_MAT_EQU_TV", ["Yes", "No", ])
    problem.addVariable("VC_MAT_EQU_MODEM", ["Yes", "No", ])

    # results =problem.getSolutions()
    #
    # print(type(results))
    # for x in results[:]:
    #     print(x)

   # problem.addConstraint((lambda v, z: (v != z) and z == "Laptop"), ("VC_CHR_GRAPHIC_CARD", "VC_CHR_TYPE"))

    results = problem.getSolutions()

    print(len(results))
    for x in results[:]:
        print(x)

    import csv
    import pandas as pd

    my_results = pd.DataFrame(results)
    my_results.to_csv('my_variants.csv', index=True, header=True)


    # with open("output.csv", "wb") as f:
    #     writer = csv.writer(f)
    #     writer.writerows(results)