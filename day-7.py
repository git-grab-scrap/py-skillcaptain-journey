def even_odd(num):
  if num == 0:
    print("Ahoy Mate!! This is blasphemy!! You've entered neither an even nor an odd number but it is exactly zero.")
    return 5
  elif ( num == 1 ):
    print("Ahoy Mate!! This is irony!! You've entered neither an even nor an odd number but it is exactly One number which is number One.")
    return 5
  elif ( num % 2 == 0):
    return True
  else:
    return False
    

user_input = int(input("Enter a number to find if it is Even or Odd: "))
res = even_odd(user_input)
if ( res == True ):
  print("Gotcha!! You entered the sweet Even number.")
elif (res == False):
  print("There you go! You entered an OdD nUmBeR.")
else:
  pass
  
  
