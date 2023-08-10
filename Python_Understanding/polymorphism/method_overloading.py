''' 
1. same name but different argument types, python wont provide supoport of constructor overloading, we give different argument types, Type concept 
explicity is not available
2. python wont provide support method/constructor overlaoding
3. Overloading concept doesnt require in python
'''

#Overloading is not required in python
#default arguments
#variable length arguments

# class Test:
#     def m1(self,i):
#         print(i)

# t = Test()
# t.m1(10)
# t.m1("Durga")
# t.m1(10.5)

#if a method can work then we dont require method overloading
class Test:
    def sum(self,a=None,b=None,c=None):
        if a!= None and b!= None and c!= None:
            print("Sum of Three Number",a+b+c)
        elif a!=None and b!=None:
            print("Sum of 2 Number",a+b)
        else:
            print("Please provide 2 or 3 arguments")
        
t = Test()
t.sum(10,20,30)
t.sum(10,20)
t.sum(10)