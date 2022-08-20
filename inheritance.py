#Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
#SINGLE LEVEL INHERITANCE
class School:
    pass
class Headmaster(School):
    pass
#MULTILEVEL INHERITANCE
class School:
    pass
class Headmaster(School):
    pass
class Teachers(Headmaster):
    pass
#MUTIPLE INHERITANCE
class Headmaster:
    pass
class Teachers:
    pass
class Student(Headmaster,Teachers):
    pass
#HEIRARCHICAL INHERITANCE
class Teachers:
    pass
class Stu1(Teachers):
    pass
class Stu2(Teachers):
    pass
#EXAMPLE PROGRAM FOR INHERITANCE
class Clothe:
    def __init__(self,colour,size,cost):
        self.colour=colour
        self.size=size
        self.cost=cost
    def material_cost(self):
        if self.cost >= 500:
            return"within the budget"
        else:
            return "out of the budget"

class Womens_wear:
    def __init__(self,saree,chudithar):
        self.saree=saree
        self.chudithar=chudithar

    def chudithar_material(self):
        if self.chudithar :
            return"not Available"
      
        else:
            return"available"
class Cotton(Clothe):
    def __init__(self,colour,size,cost,types_of_saree):
        super().__init__(colour,size,cost)
        self.types_of_saree=types_of_saree

class Silk(Clothe):
    def __init__(self,colour,size,cost,types_of_chudithar):
        super().__init__(colour,size,cost)
        self.types_of_chudithar=types_of_chudithar

class Lehanga(Clothe,Womens_wear):
    def __init__(self,colour,size,cost,saree,chudithar):
        Clothe. __init__(self,colour,size,cost)
        Womens_wear. __init__(self,saree,chudithar)

lehanga1=Lehanga('black',34,7000,'silk saree','cotton chudithar')
lehanga2=Lehanga('green',54,10000,'synthetic saree','cotton and silk mixed chudithar')
print(lehanga2.material_cost())
print(lehanga1.chudithar_material())
print(lehanga2.colour)
print(lehanga1.cost)
print(lehanga1.saree)
print(lehanga2.chudithar)
