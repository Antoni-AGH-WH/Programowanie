# Civilisation

# klasy - miasto, cywilizacja, budynki, jednostki
import random
class Civilisation:
    def __init__(self, name, leader, money, great_people_points, tech_points):
        print("A great civilisation has risen")
        self.name = name
        self.leader = leader
        self.money = money
        self.great_people_points = great_people_points
        self.tech_points = tech_points

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
        self.upgrade = []

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

class City:
    def __init__(self, name):
        print("The city has been created")
        self.name = name
        self.citizens = 1
        self.citizen_income = 10
        self.defence = 1
        self.growth_required = 10
        self.growth_points_income = 0
        self.growth = 0
        self.city_income = 0
    def populationAction(self):
        self.growth = self.growth + self.growth_points_income
        a = self.growth_required
        if self.growth >= self.growth_required:
            self.growth = 0
            self.citizens += 1
            self.city_income = self.citizen_income * self.citizens
            self.growth_required = self.growth_required + int(a * 0.1)
            print("The city has gained a new citizen!")

class Unit:
    def __init__(self, name, movement, ability):
        self.name = name
        self.movement = movement
        self.mov_remaining = movement
        self.ability = ability
        print("{} reporting for duty".format(self.name))
class Technology:
    def __init__(self, cost, effect):
        self.cost = cost
        if type(effect) == list:
            self.effect = effect
        else:
            print("You must provide description for you technology")

class Teren:
    def __init__(self, kierunek):
        self.road = "No Road"
        self.resources = []
        self.direction = kierunek
        self.distance = random.randint(2,6)

        if self.direction == "West":
            self.name = "Lands to the West"
        elif self.direction == "South":
            self.name = "Lands to the South"
        elif self.direction == "East":
            self.name = "Lands to the East"
        else:
            self.name = "Lands to the North"

        if random.randint(1,9) == 7 or random.randint(1,9) == 8:
            self.water = "Small River"
        elif random.randint(1,9) == 9:
            self.water = "Big River"
        else:
            self.water = "None"

    def losowanie_zasobów(self, resource_list):
        if len(resource_list) <= 3:
            a = random.randint(1,len(resource_list))
        else:
            a = random.randint(1,3)
        for i in range(a):
            self.resources = self.resources + [resource_list[i]]
        for element in self.resources:
            resource_list.remove(element)
        return resource_list

    def zakładanie_kolonii(self, kolonista):
        Kolonia = Colony[self]
        del kolonista
        return Kolonia

class Morze(Teren):
    def __init__(self, kierunek):
        super(Morze, self).__init__(kierunek)
        if self.direction == "West":
            self.name = "Islands to the West"
        elif self.direction == "South":
            self.name = "Islands to the South"
        elif self.direction == "East":
            self.name = "Islands to the East"
        else:
            self.name = "Islands to the North"
        self.water = "None"

    def losowanie_zasobów(self, marine_resource_list):
        self.resources = marine_resource_list

class Colony:
    def __init__(self, Teren):
        self.colony_resources = Teren.resources
        self.level = 1
        if self.colony_resources >= 1:
            self.resource_1_level = 1
        else:
            self.resource_2_level = 0
        if self.colony_resources >= 2:
            self.resource_2_level = 1
        else:
            self.extraction_level_2 = 0
        if self.colony_resources >= 3:
            self.resource_3_level = 1
        else:
            self.resource_3_level = 0
        self.water = Teren.water


# lista jednostek (do zrobienia)



## START HANDLING FILE - Budynki są wczytywane z osobobnego pliku

text_file = open("Budynki.txt", "r")
lines = text_file.readlines()

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

    a = str(lista[0]) #name
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

text_file.close()

## KONIEC HANDLING FILE

#Tworzenie świata gry (regiony i ich zasoby)

lista_regionów = ["West", "South", "East", "North"]
resource_list = ["Wheat", "Grapes", "Iron", "Copper", "Tin", "Potatoes", "Cattle"]
marine_resource_list = ["Fish", "Whales"]

for i in range(3):
    a = random.randint(0,3-i)
    kierunek = lista_regionów[a]
    region = Teren(kierunek)
    resource_list = region.losowanie_zasobów(resource_list)
    del lista_regionów[a]
    lista_regionów = lista_regionów + [region]

region = Morze(lista_regionów[0])
region.losowanie_zasobów(marine_resource_list)
del lista_regionów[0]
lista_regionów = lista_regionów + [region]

# listy i inne dane potrzebne do działania gry i komend

list_build_orders = ["build", "construct", "zbuduj",
                     "zbudujmy", "let's build", "lets build", "construction"]
list_build_buildings_orders = ["building", "buildings", "budynki"]
list_build_units_orders = ["jednostki", "units","unit", "jednostka"]
list_build_great_people_orders = ["great people","gp","wielcy ludzie", "great"]
list_help = ["help", "help!", "pomoc", "hilfe", "pomocy", "assistance"]
list_of_commands_main = {"data" : "Shows data related to your city or civilisation",
                         "build" : "you can order construction of units or buildings",
                         "skip turn" : "skips x turns, chosen by you",
                         "end turn" : "ends current turn"}

list_of_commands_data = {"City Data, or just city": "Data about your city and buildings build inside it",
                         "Civilsation Data, or just civ":"Data about your civilisation",
                         "Buildings Avalible":"Shows what buildings avalible to you ",
                         "Lands":"Shows your intel about neighbouring lands "}

lista_anulacji = ["cancel", "stop", "no"]

is_building = False


#obsługa konstrukcji w mieście
construction_que = {}
built_buildings = []

# definiowanie funckcji, czyli co gracz może zrobić w grze

def show_me_data(civ_gracz_1):
    dn = civ_gracz_1.name
    dl = civ_gracz_1.leader
    dm = civ_gracz_1.money
    dgpp = civ_gracz_1.great_people_points
    dtp = civ_gracz_1.tech_points
    return dn, dl, dm, dgpp, dtp
def show_me_buildings_avalible(all_buildings, built_buildings):  # funkcja do wyświetlania listy nazw dostępnych budynków, czyli zostaną wyświetlone tylko budynki do których gracz ma dostęp
    avalible_buildings = []
    for i in range(len(all_buildings)):
        building_chosen = all_buildings[i]
        b = len(building_chosen.access)
        a = len(list(set(building_chosen.access) and set(built_buildings)))
        if a == b and building_chosen.access != ["Zbudowany"] and building_chosen.cost <= civ_gracz_1.money:
            avalible_buildings = avalible_buildings + [building_chosen.name]
        else:
            continue
    return avalible_buildings
def show_me_lands(lista_regionów):
    print(" ")
    for element in lista_regionów:
        # print(element.name)
        print(f"{element.name}.\nThey are {element.distance} tiles away\nThey have", end=" ")
        a = len(element.resources)
        if a == 1:
            print(f"{element.resources[0]}")
        else:
            for i in range(0, len(element.resources) - 1):
                print(element.resources[i], end=", ")
            print(f"and {element.resources[i + 1]}")
        if element.water != "None":
            print(f"A {element.water.lower()} flows through these lands")
        print(" ")
def building_operation_1(a):  # tu jest wybierana kategoria: Mamy do wyboru budowanie wielkich ludzi, jednostek albo budynków

    request = input("What do you want to build? [Category]\nInput:").lower()
    if request == "buildings" or request == "building":
        chosen = "buildings"
        return chosen

    elif request == "help" or request == "help!":
        print("You have 3 cathegories that you can build stuff from: Unites, Buildings and Great People")
        chosen = "again"
        return chosen
    elif request == "return" or request == "nothing" or request in lista_anulacji:
        chosen = "we're leaving"
        return chosen
    else:
        print("You can't build anything from your {} category".format(request))
        chosen = "again"
        return chosen
def building_operation_2():
    a = all_buildings
    avalible_buildings = show_me_buildings_avalible(a, built_buildings)
    if len(avalible_buildings) > 0:
        print("These are the buildings avalible to you:")
        print(avalible_buildings, sep=", ")

        option = input("Pick a building you want to build\nInput:").lower()
        if option == "exit" or option == "nothing" or option == "go back to start" or option == "go back":
            option = "we're leaving"

        if option != "we're leaving":
            chosen_building = "Can't build shit"
            for i in range(len(a)):
                if option == a[i].name.lower():
                    chosen_building = a[i]
                else:
                    continue
            return chosen_building
        else:
            return option
    else:
        print("You have no buildings avalible to be build")
        chosen_building = "Can't build shit"
        return chosen_building
def handle_orders_buildings(chosen):
    if chosen == "buildings":
        building_chosen = building_operation_2()
        if building_chosen != "Can't build shit" and building_chosen != "we're leaving":
            print("We will be building {}".format(building_chosen.name))
            building_chosen.access = ["Zbudowany"]
            civ_gracz_1.money = civ_gracz_1.money - building_chosen.cost
            building_a_building(building_chosen, construction_que)
            x = 0
            turn_skip = 0
        elif building_chosen == "we're leaving" or building_chosen == "Can't build shit":
            x = 0
            turn_skip = -1
        else:
            print("Ow, I can't build that")
            x = 1
            turn_skip = 0
    elif chosen == "we're leaving":
        x = 0
        turn_skip = -1

    return x, turn_skip
def building_a_building(building_chosen, construction_que):  # kolejka budowania - przyda się póżniej
    turns_needed = building_chosen.time_to_build
    newdict = {building_chosen: turns_needed}
    construction_que = construction_que.update(newdict)
    return construction_que
def provide_data_type(order_follow):
    if order_follow == "civilisation data" or order_follow == "civilisation" or order_follow == "civ" or order_follow == "civ data":
        dn, dl, dm, dgpp, dtp = show_me_data(civ_gracz_1)
        print("You have {} gold, {} great people points and {} tech points\n".format(dm, dgpp, dtp))
    elif order_follow == "city data" or order_follow == "city":
        print("Your city has {} citizens, and has {} growth points out of {} required for population growth".format(
            miasto_Gracza.citizens, miasto_Gracza.growth, miasto_Gracza.growth_required))
        if len(built_buildings) == 0:
            print(f"Currently there are no buildings in the city")
        else:
            print(f"Currently build buildings are: {built_buildings} ")
    elif order_follow == "avalible buildings" or order_follow == "buildings avalible":
        print(show_me_buildings_avalible(all_buildings))
    elif order_follow == "buildings":
        if len(built_buildings) == 0:
            print(f"Currently there are no buildings in the city")
        else:
            print(f"Currently build buildings are: {built_buildings} ")
    elif order_follow == "lands" or order_follow == "possible colonies" or order_follow == "tereny" or order_follow == "ziemie":
        show_me_lands(lista_regionów)
    else:
        print("This is not a correct type of data")

def handle_orders(order, timer, all_buildings, built_buildings):
    turn_skip = 0
    a = order.lower()
    x = 0
    b = len(a.split("_"))
    if b == 1:
        if a in list_build_orders:  # sprawdzamy, czy gracz chce coś zbudować - jest na to więcej niż 1 komenda
            while x != 1:
                chosen = building_operation_1(a)  # wybieramy jaki budynek chcemy zbudować
                if chosen != "again" and chosen != "Can't build shit":
                    x = 1
                elif chosen == "we're leaving":
                    x = 1
                elif chosen == "Can't build shit":
                    x = 1
                else:
                    continue
            while x != 0:
                x, turn_skip = handle_orders_buildings(chosen)
        elif a in list_build_buildings_orders:
            x = 1
            while x != 0:
                chosen = "buildings"
                x, turn_skip = handle_orders_buildings(chosen)

        elif a in list_help:
            c = list_of_commands_main.keys()
            for element in c:
                a = element
                b = list_of_commands_main[a]
                print("{} - {}".format(a,b))
            print('And remember, you can always write "help"')
            turn_skip = -1
        elif a == "data" or a == "info":
            request = input("What data do you require?\nInput:").lower()
            provide_data_type(request)
            turn_skip = -1
        elif a == "skip turn" or a == "turn skip" or a == "skip":
            turn_skip = int(input("How many turns would you like to skip?\nInput:"))
            if turn_skip + timer > turn_limit:
                print("You can't skip that many turns!")
                turn_skip = -1
            elif turn_skip <0:
                print("You can't skip negative number of turns!")
                turn_skip = -1
        elif a == "end turn":
            pass
        else:
            print("This is not a valid command")
            turn_skip = -1
        return turn_skip, all_buildings
    elif b == 2:
        order_1 = a.split("_")[0]
        order_follow = a.split("_")[1]
        if order_1 == "data" or a == "info":
            provide_data_type(order_follow)
        else:
            print("You haven't gave a lawful command")
            turn_skip = -1
    else:
        print("This is not a valid command")
        turn_skip = -1
    return turn_skip, all_buildings

def produkcja_miasta(construction_que):
    finished_list = []
    a = list(construction_que.keys())
    list_d = a.copy()
    for element in list_d:
        t_remaining = construction_que[element]
        t_remaining = t_remaining - 1
        if t_remaining == 0:
            finished_list = finished_list + [element]
            construction_que.pop(element)
        else:
            construction_que[element] = t_remaining
    return construction_que, finished_list
def finalizacja_kontrukcji_budynków(finished_list, built_buildings):
    constructed_buildings = built_buildings
    for element in finished_list:
        constructed_buildings += [element]
        finished_list.remove(element)
    return constructed_buildings, finished_list
def income(built_buildings, civ_gracz_1, miasto_Gracza):
    f_incum = 0
    incum = 0
    for building in built_buildings:
        f_incum += building.growth
        incum += building.income

    przychód_z_obywateli = miasto_Gracza.city_income
    incum += przychód_z_obywateli

    miasto_Gracza.growth += f_incum
    miasto_Gracza.growth_points_income = f_incum

    miasto_Gracza.income = incum
    civ_gracz_1.money += incum

    print(f"You gained {incum} cash")
    print(f"You gain {f_incum} growth points")
    return civ_gracz_1, miasto_Gracza
def kolejka_budowania(construction_que):
    if len(construction_que) > 0:
        print("Current construction que:")
        new = list(construction_que.keys())
        for i in range(len(new)):
            klucz = new[i]
            value = construction_que[klucz]
            print("{}, turns remaing: {} ".format(klucz.name, value))
    else:
        print("Currently there's nothing in production")


# rozpoczęcie gry

civ_gracz_1 = Civilisation("Polanie", "Jadwiga", 1500, 0, 0)
miasto_Gracza = City("Kraków")

# gra właściwa

turn_limit = 10
timer = -20
skip_turns = False


#testing area - start

#testing area - end

while timer <= turn_limit:
    if skip_turns == False:
        print(" \n ")
        turns_remaining = turn_limit - timer

        kolejka_budowania(construction_que)

        print("[{} turns remaining]".format(turns_remaining))
        print(" ")
        order = input("Awaiting your instructions:")

        skip, all_buildings = handle_orders(order, timer, all_buildings, built_buildings)

        if skip == -1:
            end_turn = 0
        else:
            end_turn = 1
            construction_que, finished_list = produkcja_miasta(construction_que)  # tutaj wykorzystamy kolejkę budowania

            built_buildings, finished_list = finalizacja_kontrukcji_budynków(finished_list, built_buildings)
            civ_gracz_1, miasto_Gracza  = income(built_buildings, civ_gracz_1, miasto_Gracza)
            miasto_Gracza.populationAction()

        timer = timer + end_turn

        if skip > 1:
            skip_turns = True
        else:
            continue
    elif skip_turns == True :

        construction_que, finished_list = produkcja_miasta(construction_que)

        built_buildings, finished_list = finalizacja_kontrukcji_budynków(finished_list, built_buildings)
        civ_gracz_1, miasto_Gracza = income(built_buildings, civ_gracz_1, miasto_Gracza)
        miasto_Gracza.populationAction()

        end_turn = 1
        timer = timer + end_turn

        skip = skip - 1
        if skip == 1:
            skip_turns = False
        else:
            continue



if timer >= turn_limit:
    print("This is the end of the game! Barbarians are approaching!")

# zakończenie gry: czy wygraliśmy czy nie

power = 5
invaders = 6
if power > invaders:
    print("You win")
else:
    print("You loose")