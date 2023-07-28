user_num1 = int(input("Enter first number to perform the magical division op: "))
user_num2 = int(input("Enter first number to perform the magical division op: "))

try:
  div = (user_num1 / user_num2)
except ZeroDivisionError:
    print("Ah Mate! Cannot divide by zero.") 
    non_zer = int(input("Enter any number greater than zero to perform the magical division:"))
    count = 0
    while (count == 0):
        if non_zer > 0:
            div = (user_num1 / non_zer)
            count = 3
        else:
            print("Mate! Told ya.. number greater than zero only.")
            non_zer = int(input("Enter any number greater than zero to perform the magical division: "))        
finally:
  print(f"Math Magic! Division Result: {div}")


  
  

    

