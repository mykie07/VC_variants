def testemptyvar(**kwargs):
    xx=kwargs.get('xx', None)
    yy=kwargs.get('yy', None)

    for arguments in kwargs:
        return arguments

    print(kwargs)

def nonstyle(xx=None, yy=None):

    if xx:
        print("xx=%s" % str(xx))

    if yy==2:
        print(yy)



if __name__ == "__main__":

    nonstyle(xx="my thing",yy=2)













    # from constraint import *
    # problem = Problem()
    # #
    # # problem = Problem()
    # # problem.addVariables(["a", "b"], [1, 2])
    # #
    # #
    # # def func(a, b):
    # #
    # #     return b>a
    #
    # #problem = Problem()
    # problem.addVariables(["a", "b"], [1, 2])
    # problem.addConstraint(SomeNotInSetConstraint([1]))
    # ss=sorted(sorted(x.items()) for x in problem.getSolutions())
    #
    #
    # # problem.addConstraint(FunctionConstraint(func), ["a", "b"])
    # # sol=problem.getSolution()
    #
    # print(ss)