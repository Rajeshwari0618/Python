class Num:
    def __init__(self,inte):
        self.inte=inte

    def __add__(self,other):
        return self. inte+other.inte

    def __eq__(self,other):
        return self.inte==other.inte
    
    def __getitem__(self,key):
        return self.inte[key]
    def __contains__(self,other):
        if other in self.inte:
            return True
        return False
    def __len__(self):
        return len(self.inte)
    def __str__(self):
        return self.inte
    def __repr__(self):
        return self.inte

num1=Num(70)
num2=Num(70)
str1=Num('Rajeshwari')
print(num1+num2)
print(num1==num2)
print(str1[1:-1])
print('r' in str1)
print(len(str1))
print(str1)
print([str1])
