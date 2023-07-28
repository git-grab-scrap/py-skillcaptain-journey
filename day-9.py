dict1 = {
    'key1': "value1",
    'key2': "value2",
    'key3': "value3"
}


print(f" Contents of dictionary are: {dict1}")

dict1['key4'] = "value4"
dict1['key5'] = "value5"

print(f"After adding a few key,val pairs contents are: {dict1}")

try:
  dict1_key, new_key_val = input("Mate! Now from the contents displayed above, input a key to modify its value here: ").split(", ")
except (KeyError or ValueError):
  print("Mate You've missed something! enter key,value pairs for ops. Don't slack and skimp.")
finally:
  dict1[dict1_key] = new_key_val
  print(f" Contents of dictionary after modifications are: {dict1}")

user_key = input("Now that you've seen the dictionary a few times, Enter a key to check it exists in the dictionary: ")
if user_key in dict1.keys():
    print(f"Woah! Entered key exists and it's value is {dict1[user_key]}")
else:
    print(f"You need to Observe more. Entered key does not exist in this realm.Hard luck!")

try:
  dict1_key_del = input("Mate! Enter a key to cease its existence: ")
except (KeyError or ValueError):
  print("Mate You've missed something! enter a key whihc exists in the realm. Don't slack and skimp.")
finally:
  del dict1[dict1_key_del]
  print(f" Contents of dictionary after modifications are: {dict1}")


print("One more time now. All keys in the dictionary so far after all ops are: ")
for key,val in dict1.items():
    print(key)
    
