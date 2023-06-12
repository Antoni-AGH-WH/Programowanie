class Building:
    def __init__(self, name, access, time_to_build, cost):
        self.name = name
        self.access = access
        self.time_to_build = time_to_build
        self.cost = cost
        self.growth = 0
        self.income = 0
        self.science = 0
        self.defence = 0
        self.fortification = 0
        self.great_people = 0

    def add_value(self, number, type):
        if type  == "G":
            self.growth += number
        elif type  == "I":
            self.income += number
        elif type == "S":
            self.science += number
        elif type  == "D":
            self.defence += number
        elif type  == "F":
            self.fortification += number
        elif type  == "GP":
            self.great_people += number

## START HANDLING FILE - Budynki są wczytywane z osobobnego pliku

text_file = open("Budynki.txt", "r")
lines = text_file.readlines()
#for line in lines:
    #print(line)

#print(" \n  \n")


def tworzenie_stringu(b):
    new_string = ""
    otwarcie_nawiasu = "no"
    for character in b:
        if character == '"' or character == '[' or character == ']' or character == "\n":
            continue
        elif character == " " and otwarcie_nawiasu == "yes":
            new_string = new_string + "_"
        elif character == "{":
            otwarcie_nawiasu = "yes"
        elif character == "}":
            otwarcie_nawiasu = "no"
        else:
            new_string = new_string + character

    new_list = new_string.split(", ")
    if len(new_list) >= 2:
        if new_list[1] != "None":
            new_list[1] = new_list[1].split(",_")
        else:
            new_list[1] = []
    return new_list

def tworzenie_objektów_budynki(lista):

    a = str(lista[0]).lower() #name
    b = list(lista[1]) #rquirement
    c = int(lista[2]) #cost_time
    d = int(lista[3]) #cost_money
    nowy_budynek = Building(a, b, c, d)
    for i in range(4, len(lista), 2):
        a = int(lista[i])
        b = str(lista[i+1])
        nowy_budynek.add_value(a,b)
    return nowy_budynek

def tworzenie_budynków (lines):
    all_buildings = []
    for element in lines:
        if element[0] != "#":
            #print(element)
            new_list = tworzenie_stringu(element)
            if len(new_list) >=2:
                nowy_budynek = tworzenie_objektów_budynki(new_list)
                all_buildings = all_buildings + [nowy_budynek]
        else:
            continue
    return all_buildings


all_buildings = tworzenie_budynków(lines)

for element in all_buildings:
    print(element.name)
    print(element.access)

text_file.close()

## KONIEC HANDLING FILE

