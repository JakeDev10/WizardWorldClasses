from dataclasses import dataclass, field
import requests

@dataclass
class Elixir:
    id: str
    name: str
    difficulty: str
    ingredient: str
    inventorFullName: str
    manufacturer: str

@dataclass
class House:
    id: str
    name: str
    houseColours: str
    founder: str
    animal: str
    element: str
    ghost: str
    commonRoom: str

@dataclass
class Ingredient:
    id: str
    name: str

@dataclass
class Spell:
    id: str
    name: str
    type: str
    incantation: str
    effect: str
    canBeVerbal: bool

@dataclass 
class Wizard:
    id: str
    firstName: str
    lastName: str

#fill spellList with Spell objects
response = requests.get("https://wizard-world-api.herokuapp.com/Spells")
spellDict = response.json()
spellList = []
for x in range(0, len(spellDict)):
    aSpell = Spell(spellDict[x]['id'], spellDict[x]['name'], spellDict[x]['type'],
    spellDict[x]['incantation'],spellDict[x]['effect'],spellDict[x]['canBeVerbal'])
    spellList.append(aSpell)

#fill houseList with House objects
response = requests.get("https://wizard-world-api.herokuapp.com/Houses")
houseDict = response.json()
houseList = []
for x in range(0, len(houseDict)):
    aHouse = House(houseDict[x]['id'],houseDict[x]['name'],houseDict[x]['houseColours'],
    houseDict[x]['founder'],houseDict[x]['animal'],houseDict[x]['element'],houseDict[x]['ghost'],houseDict[x]['commonRoom'])
    houseList.append(aHouse)

#fill elixirList with Elixir objects
response = requests.get("https://wizard-world-api.herokuapp.com/Elixirs")
elixirDict = response.json()
elixirList = []
print(elixirDict[0])
#for x in range(0, len(elixirDict)):
#    anElixir = Elixir(houseDict[x]['id'],houseDict[x]['name'],houseDict[x]['houseColours'],
#    houseDict[x]['founder'],houseDict[x]['animal'],houseDict[x]['element'],houseDict[x]['ghost'],houseDict[x]['commonRoom'])
#    houseList.append(aHouse)
#print(elixirList[0])