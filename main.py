import requests
from bs4 import BeautifulSoup
from time import sleep
import random

my_url = requests.get('https://escapefromtarkov.gamepedia.com/Weapons')
# https://escapefromtarkov.gamepedia.com/Weapons
# https://escapefromtarkov.gamepedia.com/Armor_vests
# https://escapefromtarkov.gamepedia.com/Chest_rigs
# https://escapefromtarkov.gamepedia.com/Eyewear
# https://escapefromtarkov.gamepedia.com/Face_cover
# https://escapefromtarkov.gamepedia.com/Headsets
# https://escapefromtarkov.gamepedia.com/Headwear
# https://escapefromtarkov.gamepedia.com/Backpacks
# https://escapefromtarkov.gamepedia.com/Armbands


# Check if scraper will access website
# Generate individual JSON lists for all items
# Create logic for the random selection, including chances for nothing in each category.
# Announce the game to the community

# Save url content
src = my_url.content

# Parsing the url
soup = BeautifulSoup(src, 'html.parser')

# Empty weapons list to append to.
weapons = []

# Get all of the weapon names from the tag elements
for target in soup.findAll('tr'):
    i = 0
    for string in target.stripped_strings:
        i += 1
        if i == 1:
            weapons.append(string)

# Printing final list, testing to make sure we end when we've gathere all current weapons.
print('Final List:')   
final_list = []    
sleep(1)
i = 0
for weapon in weapons:
    if weapon.lower() == 'name':
        pass
    elif '9A-91/VSK-94' in weapon:
        break
    elif 'Gear' in weapon:
        break
    else:
        final_list.append(weapon)
        print(weapon)
        sleep(.05)
print(f'There are {len(final_list)} weapons so far.')
print(f'Random weapon is {random.choice(final_list)}')