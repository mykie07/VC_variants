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

    #problem.addConstraint((lambda v, z: (v != z) and z == "Laptop"), ("VC_CHR_GRAPHIC_CARD", "VC_CHR_TYPE"))

    #problem.addConstraint(lambda v, z: (z == "Laptop"),  ("VC_CHR_GRAPHIC_CARD", "VC_CHR_TYPE"))/

    # problem.addConstraint(lambda sound, tv, modem, typ:
    #                       (sound == "Yes" or tv == "Yes" or modem == "Yes") and
    #                       (typ != "Server" and typ != "Laptop"),
    #                       ("VC_MAT_EQU_SOUND", "VC_MAT_EQU_TV", "VC_MAT_EQU_MODEM", "VC_CHR_TYPE"))


    problem.addConstraint(
        lambda memory, cpu, typ:
        (memory == "8" or memory == "16" or cpu == "A-CPU") and
        typ == "Server",
        ("VC_CHR_MAIN_MEMORY", "VC_CHR_CPU", "VC_CHR_TYPE")

    )

    # problem.addConstraint(
    #     lambda memory, cpu, typ:
    #     ((memory == "8" or memory == "16") and typ == "Server")
    #     or ( cpu == "A-CPU" and typ == "Server"),
    #     ("VC_CHR_MAIN_MEMORY", "VC_CHR_CPU", "VC_CHR_TYPE")
    #
    # )

    results = problem.getSolutions()

    print(len(results))
    for x in results[:]:
        print(x)

    # # Wrte variants generated to a file
    # import pandas as pd
    #
    # my_results = pd.DataFrame(results)
    # my_results.to_csv('my_variants.csv', index=True, header=True)


