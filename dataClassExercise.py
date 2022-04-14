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
    effect: str
    sideEffects: str
    characteristics: str

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
class Ingredients:
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

#Populate ingredientList with Ingredient objects
responseIngre = requests.get("https://wizard-world-api.herokuapp.com/Ingredients")

ingres = responseIngre.json()
ingredientList = []
for i in ingres:
   ingredientList.append(Ingredients(i["id"], i["name"]))

#Populate elixirList with Elixir objects
responseElix = requests.get("https://wizard-world-api.herokuapp.com/Elixirs")

elixs = responseElix.json()
elixirList = []
for i in elixs:
   elixirList.append(Elixir(i["id"], i["name"], i["difficulty"], i["ingredients"], i["inventors"], i["manufacturer"],
                            i["effect"], i["sideEffects"], i["characteristics"]))

#Populate wizardList with Wizard objects
response = requests.get("https://wizard-world-api.herokuapp.com/Wizards")
wizardDict = response.json()
wizardList = []
for i in wizardDict:
    wizardList.append(Wizard(i['id'], i['firstName'], i['lastName']))