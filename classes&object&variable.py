Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name='rajeshwari'
print(type(name))
<class 'str'>
print(dir(name))
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
list=[]
print(type(list))
<class 'list'>
print(dir(list))
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
class Teacher:
    pass

tea1=Teacher()
tea2=Teacher()
print(tea1)
<__main__.Teacher object at 0x000001746FC15510>
print(tea2)
<__main__.Teacher object at 0x000001746FC15C90>
class Staff:
    pass

stf1=Staff()
stf2=Staff()
stf1.name='kanimozhi'
stf1.dob=1920
stf1.idn0=23
stf1.name='kanimozhi'
stf1.name='kanimozhi'
stf2.name='pavi'
stf2.dob=1930
stf2.idno=20
print(stf1.name)
kanimozhi
print(stf2.name)
pavi
class Staff:
    def __init__(self,name,dob,idno,city):
        self.name=name
        self.dob=dob
        self.idno=idno
        self.city=city

        
stf1=Staff('pavithra',1998,23,'chennai')
stf2=Staff('nandhini',1980,12,'sivagangai')
print(stf1.name)
pavithra
print(stf2.name)
nandhini
class Staff:
    def __init__(self,name,dob,idno,city):
        self.name=name
        self.dob=dob
        self.idno=idno
        self.city=city

        
class Staff:
    def __init__(self,name,dob,idno,city):
        self.name=name
        self.dob=dob
        self.idno=idno
        self.city=city
    def address(self):
        addr=f'Name : {self.name}\ndob:{self.dob}\nidno:{self.idno}\ncity:{self.city}'

        
stf1=Staff('pavithra',1998,23,'chennai')
stf2=Staff('nandhini',1980,12,'sivagangai')
print(stf1.address())
None
print(stf2.address())
None
class Staff:
    def __init__(self,name,dob,idno,city):
        self.name=name
        self.dob=dob
        self.idno=idno
        self.city=city
    def address(self):
        addr=f'Name : {self.name}\ndob:{self.dob}\nidno:{self.idno}\ncity:{self.city}'
        return addr

    
stf1=Staff('pavithra',1998,23,'chennai')
stf2=Staff('nandhini',1980,12,'sivagangai')
print(stf1.address())
Name : pavithra
dob:1998
idno:23
city:chennai
print(stf2.address())
Name : nandhini
dob:1980
idno:12
city:sivagangai
class Staff:
    def __init__(self,name,dob,idno,city):
        self.name=name
        self.dob=dob
        self.idno=idno
        self.city=city
    def address(self):
        addr=f'Name : {self.name}\ndob:{self.dob}\nidno:{self.idno}\ncity:{self.city}'
        return addr

    
from datetime import date
class Student:
    def __init__(self,name,rollno,dob,city):
        self.name=name
        self.dob=dob
        self.rollno=rollnoi
        self.city=city

        
class Student:
    def __init__(self,name,rollno,dob,city):
        self.name=name
        self.dob=dob
        self.rollno=rollnoi
        self.city=city

        
from datetime import date
class Student:
    def __init__(self,name,rollno,dob,city):
        self.name=name
        self.dob=dob
        self.rollno=rollnoi
        self.city=city
    def address(self):
        addr=f'name:{self.name}\ndob:{self.dob}\nrollno:{slef.rollno}\ncity:{self.city}'
        return addr
    def age(self):
        current_year=date.today().year
        return current_year-self.dob

    
stu1=Student('pavithra',100,1998,'chennai')
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    stu1=Student('pavithra',100,1998,'chennai')
  File "<pyshell#76>", line 5, in __init__
    self.rollno=rollnoi
NameError: name 'rollnoi' is not defined. Did you mean: 'rollno'?
stu1=Student('pavithra',1998,43,'chennai')
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    stu1=Student('pavithra',1998,43,'chennai')
  File "<pyshell#76>", line 5, in __init__
    self.rollno=rollnoi
NameError: name 'rollnoi' is not defined. Did you mean: 'rollno'?
from datetime import dateclass Student:
    def __init__(self,name,rollno,dob,city):
        self.name=name
        self.dob=dob
        self.rollno=rollno
        self.city=city
    def address(self):
        addr=f'name:{self.name}\ndob:{self.dob}\nrollno:{slef.rollno}\ncity:{self.city}'
        return addr
    def age(self):
        current_year=date.today().year
        return current_year-self.dob
    
SyntaxError: invalid syntax
class Student:
    def __init__(self,name,rollno,dob,city):
        self.name=name
        self.dob=dob
        self.rollno=rollnoi
        self.city=city
    def address(self):
        addr=f'name:{self.name}\ndob:{self.dob}\nrollno:{slef.rollno}\ncity:{self.city}'
        return addr
    def age(self):
        current_year=date.today().year
        return current_year-self.dob

    
from datetime import date
class Student:
    def __init__(self,name,rollno,dob,city):
        self.name=name
        self.dob=dob
        self.rollno=rollno
        self.city=city
    def address(self):
        addr=f'name:{self.name}\ndob:{self.dob}\nrollno:{slef.rollno}\ncity:{self.city}'
        return addr
    def age(self):
        current_year=date.today().year
        return current_year-self.dob

    
stu1=Student('pavithra',1998,100,'chennai')
stu2=Student('nandhini',1995,40,'sivagangai')
stu3=Student('mouni',1991,78,'trichy')
print(stu1.age())
1922
print(stu2.age())
1982
Student.age(stu1)Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from datetime import date
class Employee:
    def __init__(self,name,idno,dob,city):
        self.name=name
        self.idno=idno
        self.dob=dob
        self.city=city

        
from datetime import date
class Employee:
    def __init__(self,name,idno,dob,city):
        self.name=name
        self.idno=idno
        self.dob=dob
        self.city=city
    def address(self):
        addr=f'name:{self.name}\nidno:{self.idno}\ndob:{self.dob}\ncity:{self.city}'
        return addr
    def age(self):
        current_year=date.today().year
        return current_year - self.dob

    
emp1=Employee('pavithra',100,1998,'chennai')
emp2=Employee('nano',200,1999,'sivagangai')

emp1.fees=10000
print(emp1.fees)
10000
Employee.fees=2000
print(emp1.fees)
10000
print(emp2.fees)
2000
from datatime import date
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    from datatime import date
ModuleNotFoundError: No module named 'datatime'
from datetime import date
class Employee:
    def __init__(self,name,idno,dob,city):
        self.name=name
        self.idno=idno
        self.dob=dob
        self.city=city
    def address(self):
        addr=f'name:{self.name}\nidno:{self.idno}\ndob:{self.dob}\ncity:{self.city}'
        return addr
    def age(self):
        current_year=date.today().year
        return current_year - self.dob

    
emp1=Employee('pavithra',100,1998,'chennai')
emp2=Employee('nano',200,1999,'sivagangai')
Employee.fees=20000
print(emp1.fees)
20000
print(emp2.fees)
20000
emp1.fees=30000

print(emp1.__dict__)
{'name': 'pavithra', 'idno': 100, 'dob': 1998, 'city': 'chennai', 'fees': 30000}
Employee.fees=9000
print(emp1.fees)
30000
print(emp1.__dict__)
{'name': 'pavithra', 'idno': 100, 'dob': 1998, 'city': 'chennai', 'fees': 30000}
print(Employee.__dict__)
{'__module__': '__main__', '__init__': <function Employee.__init__ at 0x0000023764B92B90>, 'address': <function Employee.address at 0x0000023764B92CB0>, 'age': <function Employee.age at 0x0000023764B92D40>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None, 'fees': 9000}
from datetime import date
class Employee:
    def __init__(self,name,idno,dob,city):
        self.name=name
        self.idno=idno
        self.dob=dob
        self.city=city
    def address(self):
        addr=f'name:{self.name}\nidno:{self.idno}\ndob:{self.dob}\ncity:{self.city}'
        return addr
    def age(self):
        current_year=date.today().year
        return current_year - self.dob
    def pay_fees(self,amount):
        self.fees = self.fees.amount

        
emp1=Employee('pavithra',100,1998,'chennai')
emp2=Employee('nano',200,1999,'sivagangai')
emp1.pay_fees(40000)
1922
print(stu1.age())
1922
stu1.fees=1000
print(stu1.fees)Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from datetime import date
class Employee:
    def __init__(self,name,idno,dob,city):
        self.name=name
        self.idno=idno
        self.dob=dob
        self.city=city

        
from datetime import date
class Employee:
    def __init__(self,name,idno,dob,city):
        self.name=name
        self.idno=idno
        self.dob=dob
        self.city=city
    def address(self):
        addr=f'name:{self.name}\nidno:{self.idno}\ndob:{self.dob}\ncity:{self.city}'
        return addr
    def age(self):
        current_year=date.today().year
        return current_year - self.dob

    
emp1=Employee('pavithra',100,1998,'chennai')
emp2=Employee('nano',200,1999,'sivagangai')

emp1.fees=10000
print(emp1.fees)
10000
Employee.fees=2000
print(emp1.fees)
10000
print(emp2.fees)
2000
from datatime import date
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    from datatime import date
ModuleNotFoundError: No module named 'datatime'
from datetime import date
class Employee:
    def __init__(self,name,idno,dob,city):
        self.name=name
        self.idno=idno
        self.dob=dob
        self.city=city
    def address(self):
        addr=f'name:{self.name}\nidno:{self.idno}\ndob:{self.dob}\ncity:{self.city}'
        return addr
    def age(self):
        current_year=date.today().year
        return current_year - self.dob

    
emp1=Employee('pavithra',100,1998,'chennai')
emp2=Employee('nano',200,1999,'sivagangai')
Employee.fees=20000
print(emp1.fees)
20000
print(emp2.fees)
20000
emp1.fees=30000

print(emp1.__dict__)
{'name': 'pavithra', 'idno': 100, 'dob': 1998, 'city': 'chennai', 'fees': 30000}
Employee.fees=9000
print(emp1.fees)
30000
print(emp1.__dict__)
{'name': 'pavithra', 'idno': 100, 'dob': 1998, 'city': 'chennai', 'fees': 30000}
print(Employee.__dict__)
{'__module__': '__main__', '__init__': <function Employee.__init__ at 0x0000023764B92B90>, 'address': <function Employee.address at 0x0000023764B92CB0>, 'age': <function Employee.age at 0x0000023764B92D40>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None, 'fees': 9000}
from datetime import date
class Employee:
    def __init__(self,name,idno,dob,city):
        self.name=name
        self.idno=idno
        self.dob=dob
        self.city=city
    def address(self):
        addr=f'name:{self.name}\nidno:{self.idno}\ndob:{self.dob}\ncity:{self.city}'
        return addr
    def age(self):
        current_year=date.today().year
        return current_year - self.dob
    def pay_fees(self,amount):
        self.fees = self.fees.amount

        
emp1=Employee('pavithra',100,1998,'chennai')
emp2=Employee('nano',200,1999,'sivagangai')
emp1.pay_fees(40000)
print(emp1.fees)
20000
print(emp2.fees)
20000
emp1.fees=30000

print(emp1.__dict__)
{'name': 'pavithra', 'idno': 100, 'dob': 1998, 'city': 'chennai', 'fees': 30000}
Employee.fees=9000
print(emp1.fees)
30000
print(emp1.__dict__)
{'name': 'pavithra', 'idno': 100, 'dob': 1998, 'city': 'chennai', 'fees': 30000}
print(Employee.__dict__)
{'__module__': '__main__', '__init__': <function Employee.__init__ at 0x0000023764B92B90>, 'address': <function Employee.address at 0x0000023764B92CB0>,'age': <function Employee.age at 0x0000023764B92D40>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None, 'fees': 9000}

from datetime import date
class Employee:
    def __init__(self,name,idno,dob,city):
        self.name=name
        self.idno=idno
        self.dob=dob
        self.city=city
    def address(self):
        addr=f'name:{self.name}\nidno:{self.idno}\ndob:{self.dob}\ncity:{self.city}'
        return addr
    def age(self):
        current_year=date.today().year
        return current_year - self.dob
    def pay_fees(self,amount):
        self.fees = self.fees.amount

        
emp1=Employee('pavithra',100,1998,'chennai')
emp2=Employee('nano',200,1999,'sivagangai')
emp1.pay_fees(40000)


