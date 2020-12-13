print('Welcome to the riddle adventure game! Choose your own path. Try to make it past the three challenges alive!\n')

username = input('Enter your name: ')
inventory = []

def print_inventory(inventory):
  output = 'Inventory:'
  if inventory == []:
    return output + ' none'
  else:
    for item in inventory:
      output += '\n' + item
  return output

print('Okay', username + ', let the game begin!')
print(print_inventory(inventory))
print('Points (moves alive): 0')

print('\nFIRST CHALLENGE')
print('You are trapped in a room with three doors. Behind Door 1 is a room full of raging fires. Behind Door 2 is a room full of assassins with loaded guns. Behind Door 3 is a room full of lions that haven’t eaten in 3 months.')

move = ''
while move not in ['1', '2', '3']:
  move = input('Which number room do you choose? ')

if move in ['1', '2']:
  print('\nYou died. Better luck next time, ' + username + '!')
  print(print_inventory(inventory))
  print('Points (moves alive): 1')

else:
  bone = input('\nNice choice, ' + username + '. All the lions have starved to death. Would you like to take a large bone to use as self defense? ').lower()
  if bone == 'yes':
    inventory.append('bone')
  print(print_inventory(inventory))
  print('Points (moves alive): 1')

  input('\nPress Enter to move onto the second challenge.')
  print('\nSECOND CHALLENGE')
  print('You escape the room to freedom! You exit into a city; however, as soon as you make it, an earthquake hits and the city blacks out. Some criminals immediately take advantage and kidnap you for ransom.')
  print('\nYou once again you find yourself in a room, this time with four doors. Behind Door 1 is a death trap that will kill you. Behind Door 2 is a room full of chainsaws that will cut you to pieces. Behind Door 3 is a professional killer waiting to kill you. Behind Door 4 is acid that will burn you at once.')
  
  move = ''
  while move not in ['1', '2', '3', '4']:
    move = input('Which number room do you choose? ')
  
  if move in ['1', '3', '4']:
    print('\nYou died. Better luck next time, ' + username + '!')
    print(print_inventory(inventory))
    print('Points (moves alive): 2')
  
  else:
    chainsaw = input('\nGood job. There\'s no power in the city, so the chainsaws wouldn\'t have functioned. Would you like to take a chainsaw to use as self defense? ').lower()
    if chainsaw == 'yes':
      print('Too bad. You have arthritis of the spine, so the weight of the chainsaw weighs you down. It becomes too much for you, and you die.')
      inventory.append('chainsaw')
      print(print_inventory(inventory))
      print('Points (moves alive): 2')
    
    else:
      print(print_inventory(inventory))
      print('Points (moves alive): 2')

      input('\nPress Enter to move onto the last challenge. You\'re almost at the end!')
      print('\nLAST CHALLENGE')
      print('You exit the chainsaw room to another room. What you didn\'t know was that there was a hungry dog in it.')
      
      if inventory != []:
        useInventory = input('\nChoose an item from your inventory to use, or press Enter to wait it out: ').lower()

        if useInventory == 'bone':
          print('Too bad, ' + username + '. The dog kills you anyway because he needs to make sure there\'s no other competition for his precious bone.')
          inventory.remove('bone')
          print(print_inventory(inventory))
          print('Points (moves alive): 3')
        
        else:
          print('What are you doing, ' + username + '? You had a bone the whole time, but didn\'t put it to good use?! The dog kills you. The end!')
          print(print_inventory(inventory))
          print('Points (moves alive): 3')
        
      else:
        input('What do you do? ')
        print('Looks like you should\'ve taken the bone when you had the chance. The dog kills you. Better luck next time, ' + username + '!')
        print('Points (moves alive): 3')
