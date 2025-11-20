class employee:
    company_name="TCS"
    def __init__(self,name,city):
        self.name=name
        self.city=city
    def show_details(self):
        print(f"Name:{self.name} city:{self.city}")
    def change_city(self,city):
        self.city=city
e1=employee("ruchitha","hyd")
e1.show_details()
print(e1.city)
