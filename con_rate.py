number_list = []
while True:
  '''asking users for random numbers 
  and save them in a list'''
  print('Hi, welcome user, enter any number')
  user = input()
  
  if user=='q':
    break
  elif user in number_list:
    print('number is already taken, enter different number')
  else:
    number_list.append(user)


print('Thanks for passing through user!. Here is your list')
print(number_list)