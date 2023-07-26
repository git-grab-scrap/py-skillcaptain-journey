user_age=int(input("Enter your age honestly for a message: "))
if user_age < 18:
  print("Huh! You are a minor")
elif user_age >= 18 and user <= 65:
  print("D'oh! You are an adult now")
else:
  print("Argh!! You are a Senior Citizen mate")
