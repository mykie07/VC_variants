if __name__ == "__main__":
    res=(lambda x, y: x + y)(5, 3)
    print(res)

    from constraint import *
    problem = Problem()
    problem.addVariable("a", [1, 2, 3])
    problem.addVariable("b", [4, 5, 6])
    res1=problem.getSolutions()
    print(res1)


    problem.addConstraint((lambda a, b: a != 3),
                               ("a", "b"))
    res2=problem.getSolutions()
    print(res2)
