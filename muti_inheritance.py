class father:
    def  father_info(self):
        print("father :works as ateacher")
class mother:
    def mother_info(self):
        print("mother: works a homemaker")
class child(father,mother):
    def child_info(self):
        print("child:student")

a1=child()
a1.mother_info()
a1.father_info()
a1.child_info()


class grandfather:
    def  grand_info(self):
        print("this is a grandparent class")
class father(grandfather):
    def father_info(self):
        print("This is a father class")
class child(father):
    def child_info(self):
        print("This is a child class")
a1=child()
a1.child_info()
a1.grand_info()
a1.father_info()
