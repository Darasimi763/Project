print("select an operation to perform:")
print("1.ADD")
print("2.SUBSTRACT")
print("3.Mutilply")
print("4.DIVIDE")
operation=input()
if operation=="1":
    num1=input ("Enter first number:")
    num2=input ("Enter first number:")
    print("answer is "+ str(int(num1) + (num2)) )
    
 elif operation=="2":
      num1=input ("Enter first number:")
    num2=input ("Enter first number:")
    print("answer is "+  str(int(num1) - (num2)))
 elif operation=="3":
     num1=input ("Enter first number:")
    num2=input ("Enter first number:")
    print("answer is "+ str(int(num1) * (num2)))
   elif operation == "4":  
        num1=input ("Enter first number:")
    num2=input ("Enter first number:")
    print("answer is "+  str(int(num1) / (num2)))
  else:
      print ("INVAILD ENTRY")   
