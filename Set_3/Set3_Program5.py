"""
Create a class with functions to add, subtract, multiply and division. Also write unit test for each functions.
"""
class Operations:
    def add_fn(self,num1,num2):
        return num1+num2
    def sub_fn(self,num1,num2):
        return num1-num2
    def mul_fn(self,num1,num2):
        return num1*num2
    def div_fn(self,num1,num2):
        return num1//num2

obj = Operations()
choice=int(input("Input Your Choice :\n 1:Add\n2:Substract\n3:Multiply\n4:Division\n"))
if choice==1:
    print("Sum = ",obj.add_fn(int(input("Number 1 : ")),int(input("Number 2 :"))))
elif choice==2:
    print("Substraction = ",obj.sub_fn(int(input("Number 1 : ")),int(input("Number 2 :"))))
elif choice==3:
    print("Multiplication = ",obj.mul_fn(int(input("Number 1 : ")),int(input("Number 2 :"))))
elif choice==4:
    print("Division = ",obj.div_fn(int(input("Number 1 : ")),int(input("Number 2 :"))))
else:
    print("Correct Output")