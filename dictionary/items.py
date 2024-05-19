
inventory ={
    'name': "Підор"
}

armor = input('Яка броня буде в Вашого Персонажа?  ')
weapon = input ('Яка зброя буде в вашого персонажа? ')

inventory['armor'] = armor
inventory['weapon'] = weapon

del inventory['weapon']

print(inventory)
