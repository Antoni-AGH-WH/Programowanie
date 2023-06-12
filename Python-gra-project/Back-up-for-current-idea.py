# Civilisation

# klasy - miasto, cywilizacja, budynki, jednostki

class Civilisation:
    def __init__(self, name, leader, money, great_people_points, tech_points):
        print("A great civilisation has risen")
        self.name = name
        self.leader = leader
        self.money = money
        self.great_people_points = great_people_points
        self.tech_points = tech_points


class Building:
    def __init__(self, name, access, time_to_build, cost, effect1, effect_type_1, effect2, effect_type_2):
        self.name = name
        self.access = access
        self.time_to_build = time_to_build
        self.cost = cost
        self.effect1 = effect1
        self.effect_type_1 = effect_type_1
        self.effect2 = effect2  # niektóre budynki będą miały więcej niż 1 efekt, choć dla większości będziemy widzieć "None" w tym miejscu
        self.effect_type_2 = effect_type_2

class City:
    def __init__(self, name):
        print("The city has been created")
        self.name = name
        self.citizens = 1
        self.defence = 1
        self.growth_required = 10
        self.growth_points_income = 0
        self.growth = 0
        self.income = 0
    def populationAction(self):
        self.growth = self.growth + self.growth_points_income
        a = self.growth_required
        if self.growth >= self.growth_required:
            self.growth = self.growth - a
            self.citizens = self.citizens + 1
            self.income = self.income + 10
            self.growth_required = self.growth_required + int(a * 0.1)
            print("The city has gained a new citizen!")

class Unit:
    def __init__(self, name, HP, attack, movement, ability):
        self.name = name
        self.HP = HP
        self.damage = 0
        self.attack = attack
        self.movement = movement
        self.mov_remaining = movement
        self.ability = ability
        print("{} reporting for duty".format(self.name))

class Technology:
    def __init__(self, cost):
        self.cost = cost



# lista jednostek (do zrobienia)

# great_people_and_tech_building

## START HANDLING FILE

text_file = open("Budynki[old].txt", "r")

lines = text_file.readlines()
def tworzenie_nazwy_budynku(list):
    a = list[0]
    a = a.lower()
    return a
def tworzenie_listy(b):
    new_string = ""
    for character in b:
        if character == '"' or character == '[' or character == ']':
            continue
        else:
            new_string = new_string + character

    new_list = new_string.split(", ")
    return new_list

lista_budynków_f = []
lista_budynków_d = []

for line in lines:
    if "#" not in line:
        if "[" in line:
            b = list(line.removesuffix("\n"))
            b = tworzenie_listy(b)
            name_for_building = tworzenie_nazwy_budynku(b)
            lista_budynków_f = lista_budynków_f + [name_for_building]
            lista_budynków_d = lista_budynków_d + [b]
        else:
            continue
    else:
        continue

lista_par = zip(lista_budynków_f, lista_budynków_d)
dictionary_for_buildings = dict(lista_par)
#print(dictionary_for_buildings)
all_buildings = []
text_file.close()


for key in dictionary_for_buildings.keys():
    lista_cech = dictionary_for_buildings[key]
    name = key
    a = lista_cech[0]
    b = lista_cech[1]
    c = lista_cech[2]
    d = lista_cech[3]
    e = lista_cech[4]
    f = lista_cech[5]
    g = lista_cech[6]
    h = lista_cech[7]
    name = Building(a,b,c,d,e,f,g,h)
    all_buildings = all_buildings + [name]

## KONIEC HANDLING FILE

# listy i inne dane potrzebne do działania gry i komend

list_build_orders = ["build", "construct", "zbuduj", "zbudujmy", "let's build", "lets build", "construction",
                     "building"]
list_help = ["help", "pomoc", "hilfe", "pomocy"]

is_building = False
construction_que = {}


#obsługa konstrukcji w mieście

build_buildings = {}
build_buildings_growth = {}
build_buildings_tech = {}
build_buildings_defence = {}
build_buildings_income = {}





# definiowanie funckcji, czyli co gracz może zrobić w grze

def show_me_data(civ_gracz_1):
    dn = civ_gracz_1.name
    dl = civ_gracz_1.leader
    dm = civ_gracz_1.money
    dgpp = civ_gracz_1.great_people_points
    dtp = civ_gracz_1.tech_points
    return dn, dl, dm, dgpp, dtp


def show_me_buildings_avalible(
        all_buildings):  # funkcja do wyświetlania listy nazw dostępnych budynków, czyli zostaną wyświetlone tylko budynki do których gracz ma dostęp
    avalible_buildings = []
    for i in range(len(all_buildings)):
        building_chosen = all_buildings[i]
        if building_chosen.access == True and building_chosen.cost <= civ_gracz_1.money:
            avalible_buildings = avalible_buildings + [building_chosen.name]
        else:
            continue
    return avalible_buildings


def building_operation_1(
        a):  # tu jest wybierana kategoria: Mamy do wyboru budowanie wielkich ludzi, jednostek albo budynków

    request = input("What do you want to build? [Category]\nInput:").lower()
    if request == "buildings" or request == "building":
        chosen = "buildings"
        return chosen

    elif request == "help" or request == "help!":
        print("You have 3 cathegories that you can build stuff from: Unites, Buildings and Great People")
        chosen = "again"
        return chosen
    elif request == "return" or request == "nothing":
        chosen = "we're leaving"
        return chosen
    else:
        print("You can't build anything from your {} category".format(request))
        chosen = "again"
        return chosen


def building_operation_2():
    a = all_buildings
    avalible_buildings = show_me_buildings_avalible(a)
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


def building_a_building(building_chosen, construction_que):  # kolejka budowania - przyda się póżniej
    turns_needed = building_chosen.time_to_build
    newdict = {building_chosen.name: turns_needed}
    construction_que = construction_que.update(newdict)
    return construction_que


def handle_orders(order, timer, all_buildings):
    turn_skip = 0
    a = order.lower()
    x = 0

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
            if chosen == "buildings":
                building_chosen = building_operation_2()
                if building_chosen != "Can't build shit" and building_chosen != "we're leaving":
                    print("We will be building {}".format(building_chosen.name))
                    building_chosen.access = False
                    civ_gracz_1.money = civ_gracz_1.money - building_chosen.cost
                    building_a_building(building_chosen, construction_que)
                    x = 0
                elif building_chosen == "we're leaving" or building_chosen == "Can't build shit":
                    x = 0
                    turn_skip = -1
                else:
                    print("Ow, I can't build that")
            elif chosen == "we're leaving":
                x = 0
                turn_skip = -1

    elif a in list_help:
        print("amogus")
        turn_skip = -1
    elif a == "data":
        request = input("What data do you require?\nInput:").lower()
        if request == "civilisation data" or request == "civilisation" or request == "civ" or request == "civ data":
            dn, dl, dm, dgpp, dtp = show_me_data(civ_gracz_1)
            print("You have {} gold, {} great people points and {} tech_points\n".format(dm, dgpp, dtp))
            turn_skip = -1
        elif request == "city data" or request == "city":
            print("Your city has {} citizens, and has {} growth points out of {} required for population growth".format(
                miasto_Gracza.citizens, miasto_Gracza.growth, miasto_Gracza.growth_required))
            turn_skip = -1
        elif request == "avalible buildings" or request == "buildings avalible":
            print(show_me_buildings_avalible(all_buildings))
            turn_skip = -1

    elif a == "skip turn" or a == "turn skip" or a == "skip":
        turn_skip = int(input("How many turns would you like to skip?\nInput:"))
        if turn_skip + timer > turn_limit:
            print("You can't skip that many turns!")
            turn_skip = -1
    elif a == "end turn":
        turn_skip = 0
    else:
        print("This is not a valid command")
        turn_skip = -1
    return turn_skip, all_buildings


def produkcja_miasta(construction_que):
    for key in construction_que:
        t_remaining = construction_que[key]
        t_remaining = t_remaining - 1

        if t_remaining == 0:
            print(key)
        else:
            construction_que[key] = t_remaining
    return construction_que


# rozpoczęcie gry

civ_gracz_1 = Civilisation("Polanie", "Jadwiga", 1500, 0, 0)
miasto_Gracza = City("Kraków")

# gra właściwa

turn_limit = 10
timer = -5
skip_turns = False


#testing area - start

for element in all_buildings:
    print(element.name)
    print(element.access)
    print(element.time_to_build)
    print(element.cost)
    print(element.effect1)
    print(element.effect_type_1)

#testing area - end

while timer <= turn_limit:
    if skip_turns == False:
        print(" \n ")
        turns_remaining = turn_limit - timer

        if len(construction_que) > 0:
            is_building = True
        else:
            is_building = False

        if is_building == True:
            print("Current construction:")
            new = list(construction_que.keys())
            for i in range(len(new)):
                klucz = new[i]
                value = construction_que[klucz]
                print("{}, turns remaing: {} ".format(klucz, value))
        else:
            print("Currently there's nothing in production")

        print("There are {} turns remaining".format(turns_remaining))
        print(" ")
        order = input("Awaiting your instructions:")



        skip, all_buildings = handle_orders(order, timer, all_buildings)
        if skip == -1:
            end_turn = 0
        else:
            end_turn = 1
            miasto_Gracza.populationAction()
            construction_que = produkcja_miasta(construction_que)  # tutaj wykorzystamy kolejkę budowania

        timer = timer + end_turn

        if skip > 1:
            skip_turns = True
        else:
            continue
    elif skip_turns == True :

        construction_que = produkcja_miasta(construction_que)
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