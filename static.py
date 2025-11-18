class marks:
    @staticmethod
    def grade_conversion(marks):
        if marks>35:
            return True
        return False
print(marks.grade_conversion(90))
print(marks.grade_conversion(23))


class subject:
    def __init__(self,t,h,e):
        self.t=t
        self.h=h
        self.e=e
    def add(self):
        total=self.t+self.h+self.e
        print(f"Total:{total}")
a1=subject(20,20,60)
a1.add()
