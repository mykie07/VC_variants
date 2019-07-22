if __name__ == "__main__":
    from constraint import *
    problem = Problem()
    problem.addVariable("VC_CHR_GRAPHIC_CARD", ["x1", "x2"])
    problem.addVariable("VC_CHR_TYPE", ["x1","y2"])
    # results =problem.getSolutions()
    #
    # print(type(results))
    # for x in results[:]:
    #     print(x)

    problem.addConstraint((lambda v, z: v != z and v=="x2"), ("VC_CHR_GRAPHIC_CARD", "VC_CHR_TYPE"))

    results = problem.getSolutions()

    print(type(results))
    for x in results[:]:
        print(x)