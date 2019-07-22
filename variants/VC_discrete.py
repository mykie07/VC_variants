if __name__ == "__main__":
    from constraint import *
    problem = Problem()
    #problem.addVariable("VC_CHR_GRAPHIC_CARD", ["N-Graphic", "A-Graphic", "Onboard"])
    problem.addVariable("VC_CHR_N_GRAPHIC_CARD", ["Yes", "No", ])
    problem.addVariable("VC_CHR_A_GRAPHIC_CARD", ["Yes", "No", ])
    problem.addVariable("VC_CHR_ONBOARD_GRAPHIC_CARD", ["Yes", "No", ])

   # problem.addVariable("VC_CHR_TYPE", ["Laptop", "Office", "Gaming", "Server"])
    problem.addVariable("VC_CHR_TYPE_LAPTOP", ["Yes", "No", ])
    problem.addVariable("VC_CHR_TYPE_OFFICE", ["Yes", "No", ])
    problem.addVariable("VC_CHR_TYPE_GAMING", ["Yes", "No", ])
    problem.addVariable("VC_CHR_TYPE_SERVER", ["Yes", "No", ])

    # problem.addVariable("VC_CHR_CPU", ["A-CPU", "I-CPU"])
    problem.addVariable("VC_CHR_A_CPU", ["Yes", "No", ])
    problem.addVariable("VC_CHR_I_CPU", ["Yes", "No", ])

    #problem.addVariable("VC_CHR_MAIN_MEMORY", ["2", "4", "8", "16"])
    problem.addVariable("VC_CHR_MAIN_MEM2", ["Yes", "No", ])
    problem.addVariable("VC_CHR_MAIN_MEM4", ["Yes", "No", ])
    problem.addVariable("VC_CHR_MAIN_MEM8", ["Yes", "No", ])
    problem.addVariable("VC_CHR_MAIN_MEM16", ["Yes", "No", ])

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


    # problem.addConstraint(
    #     lambda memory, cpu, typ:
    #     (memory == "8" or memory == "16" or cpu == "A-CPU") and
    #     typ == "Server",
    #     ("VC_CHR_MAIN_MEMORY", "VC_CHR_CPU", "VC_CHR_TYPE")

    #)

#VC_EX_CON1
    problem.addConstraint(
        lambda sound, tv, modem, server, laptop:
        (sound == "Yes" or tv == "Yes" or modem == "Yes") and
        (server != "Yes" and laptop != "Yes"),
        ("VC_MAT_EQU_SOUND", "VC_MAT_EQU_TV", "VC_MAT_EQU_MODEM", "VC_CHR_TYPE_SERVER", "VC_CHR_TYPE_LAPTOP")
    )

#VC_EX_CON2 20480
    problem.addConstraint(

        lambda mem8, mem16, acpu, server:
        ((mem8 == "Yes" and mem16 == "Yes") or acpu == "Yes") and
        server == "Yes",
        ("VC_CHR_MAIN_MEM2", "VC_CHR_MAIN_MEM16", "VC_CHR_A_CPU", "VC_CHR_TYPE_SERVER")
    )


# #VC_EX_CON3 24576
    problem.addConstraint(
        lambda ncard, acard, gaming, laptop:
        (ncard == "Yes" or acard == "Yes") and
        (gaming == "Yes" or laptop == "yes"),
        ("VC_CHR_N_GRAPHIC_CARD", "VC_CHR_A_GRAPHIC_CARD", "VC_CHR_TYPE_GAMING", "VC_CHR_TYPE_LAPTOP")
    )

#VC_EX_CON4 24576
    problem.addConstraint(
        lambda onboard, server, office :
        # (onboard == "Yes") and
        # (server == "Yes" or office == "Yes"),
        (onboard == "Yes" and server == "Yes") or
        (onboard == "Yes" and server == "Yes"),
        ("VC_CHR_ONBOARD_GRAPHIC_CARD", "VC_CHR_TYPE_SERVER", "VC_CHR_TYPE_OFFICE")
    )

    results = problem.getSolutions()


    # for x in results[:]:
    #     print(x)

    print(len(results))


    # # Wrte variants generated to a file
    # import pandas as pd
    #
    # my_results = pd.DataFrame(results)
    # my_results.to_csv('my_variants.csv', index=True, header=True)


