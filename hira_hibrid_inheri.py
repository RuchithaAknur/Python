class parent:
    def  parent_info(self):
        print("parent :works as ateacher")
class child1(parent):
    def child1_info(self):
        print("child1: works a engineer")
class child2(parent):
    def child2_info(self):
        print("child:student")

a1=child2()
b1=child1()
b1.child1_info()
a1.parent_info()
a1.child2_info()


class A:
    def showA(self):
        print("class A")
class B(A):
    def showB(self):
        print("class B")
class C(A):
    def showC(self):
        print("class C")
class D(B,C):
    def showD(self):
        print("class D")
a1=D()
a1.showD()
a1.showC()
a1.showB()
a1.showA()
