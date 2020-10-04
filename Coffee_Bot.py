#########Main coffee bott function###########################
def coffee_bot():
  print('Welcome to the cafe!')
  name = input("What is your name?\n")
  size = get_size()
  drink_type = get_drink_type()
  #print(size)### For debugging
  #print(drink_type)### For debugging
  print("Alright, that's a " + size + " " + drink_type + " !")
  print("Thanks, " + name + " Your drink will be ready shortly.")
#############################################################

#######Get the size of the drink#############################
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return 'Small'

  elif res == 'b':
    return 'Medium'

  elif res == 'c':
    return 'Large'

  else:
    print_message()
    return get_size()
###########################################################

########Get the drink type#################################
def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>')
  if res == 'a':
    return 'Brewed coffee'

  elif res == 'b':
    return 'Mocha'

  elif res == 'c':
    return order_latte()

  else:
    print_message()
    return get_drink_type()
###########################################################

#############if latte is ordered and milk is added#########
def order_latte():
  res = input('And what kind of milk for your latte?\n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk\n')
  if res == 'a':
    return 'latte'

  elif res == 'b':
    return 'non-fat latte'

  elif res == 'c':
    return 'Soy latte'

  else:
    print_message()
    return order_latte()
###########################################################

##Print error message if user does not choose A, B, or C###
def print_message():
      print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.\n")
###########################################################

####Call coffee_bot########################################
coffee_bot()
###########################################################
