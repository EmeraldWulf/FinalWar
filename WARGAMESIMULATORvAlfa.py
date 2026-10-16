import random

# Dictionary to store usernames and passwords
users = {
    "Felix": "1019002",
    "Zev": "0000001",
    "Jenkins": "Halo"
}

countriesInfo = {
    "USA": {
        "states": [
            {"Alabama": "Montgomery"}, {"Alaska": "Juneau"}, {"Arizona": "Phoenix"}, {"Arkansas": "Little Rock"}, {"California": "Sacramento"}, {"Colorado": "Denver"}, {"Connecticut": "Hartford"},
            {"Delaware": "Dover"}, {"Florida": "Tallahassee"}, {"Georgia": "Atlanta"}, {"Hawaii": "Honolulu"}, {"Idaho": "Boise"}, {"Illinois": "Springfield"}, {"Indiana": "Indianapolis"},
            {"Iowa": "Des Moines"}, {"Kansas": "Topeka"}, {"Kentucky": "Frankfort"}, {"Louisiana": "Baton Rouge"}, {"Maine": "Augusta"}, {"Maryland": "Annapolis"},
            {"Massachusetts": "Boston"}, {"Michigan": "Lansing"}, {"Minnesota": "Saint Paul"}, {"Mississippi": "Jackson"}, {"Missouri": "Jefferson City"}, {"Montana": "Helena"}, {"Nebraska": "Lincoln"},
            {"Nevada": "Carson City"}, {"New Hampshire": "Concord"}, {"New Jersey": "Trenton"}, {"New Mexico": "Santa Fe"}, {"New York": "Albany"}, {"North Carolina": "Raleigh"}, {"North Dakota": "Bismarck"},
            {"Ohio": "Columbus"}, {"Oklahoma": "Oklahoma City"}, {"Oregon": "Salem"}, {"Pennsylvania": "Harrisburg"}, {"Rhode Island": "Providence"}, {"South Carolina": "Columbia"}, {"South Dakota": "Pierre"},
            {"Tennessee": "Nashville"}, {"Texas": "Austin"}, {"Utah": "Salt Lake City"}, {"Vermont": "Montpelier"}, {"Virginia": "Richmond"}, {"Washington": "Olympia"},
            {"West Virginia": "Charleston"}, {"Wisconsin": "Madison"}, {"Wyoming": "Cheyenne"}
        ],
        "capital": "Washington D.C.",
        "major_cities": ["New York City", "Los Angeles", "Chicago", "Houston", "Phoenix"]
    },
    "United Kingdom": {
        "countries": [
            {"England": "London"}, {"Scotland": "Edinburgh"}, {"Wales": "Cardiff"}, {"Northern Ireland": "Belfast"}
        ],
        "capital": "London",
        "major_cities": ["London", "Birmingham", "Manchester", "Liverpool", "Leeds"]
    },
    "Japan": {
        "prefectures": [
            {"Aichi": "Nagoya"}, {"Akita": "Akita"}, {"Aomori": "Aomori"}, {"Chiba": "Chiba"}, {"Ehime": "Matsuyama"}, {"Fukui": "Fukui"}, {"Fukuoka": "Fukuoka"}, {"Fukushima": "Fukushima"},
            {"Gifu": "Gifu"}, {"Gunma": "Maebashi"}, {"Hiroshima": "Hiroshima"}, {"Hokkaido": "Sapporo"}, {"Hyogo": "Kobe"}, {"Ibaraki": "Mito"}, {"Ishikawa": "Kanazawa"}, {"Iwate": "Morioka"},
            {"Kagawa": "Takamatsu"}, {"Kagoshima": "Kagoshima"}, {"Kanagawa": "Yokohama"}, {"Kochi": "Kochi"}, {"Kumamoto": "Kumamoto"}, {"Kyoto": "Kyoto"}, {"Mie": "Tsu"}, {"Miyagi": "Sendai"},
            {"Miyazaki": "Miyazaki"}, {"Nagano": "Nagano"}, {"Nagasaki": "Nagasaki"}, {"Nara": "Nara"}, {"Niigata": "Niigata"}, {"Oita": "Oita"}, {"Okayama": "Okayama"}, {"Okinawa": "Naha"},
            {"Osaka": "Osaka"}, {"Saga": "Saga"}, {"Saitama": "Saitama"}, {"Shiga": "Otsu"}, {"Shimane": "Matsue"}, {"Shizuoka": "Shizuoka"}, {"Tochigi": "Utsunomiya"}, {"Tokushima": "Tokushima"},
            {"Tokyo": "Tokyo"}, {"Tottori": "Tottori"}, {"Toyama": "Toyama"}, {"Wakayama": "Wakayama"}, {"Yamagata": "Yamagata"}, {"Yamaguchi": "Yamaguchi"}, {"Yamanashi": "Kofu"}
        ],
        "capital": "Tokyo",
        "major_cities": ["Tokyo", "Yokohama", "Osaka", "Nagoya", "Sapporo"]
    },
    "Germany": {
        "states": [
            {"Baden-Württemberg": "Stuttgart"}, {"Bavaria": "Munich"}, {"Berlin": "Berlin"}, {"Brandenburg": "Potsdam"}, {"Bremen": "Bremen"}, {"Hamburg": "Hamburg"}, {"Hesse": "Wiesbaden"},
            {"Lower Saxony": "Hanover"}, {"Mecklenburg-Vorpommern": "Schwerin"}, {"North Rhine-Westphalia": "Düsseldorf"}, {"Rhineland-Palatinate": "Mainz"}, {"Saarland": "Saarbrücken"},
            {"Saxony": "Dresden"}, {"Saxony-Anhalt": "Magdeburg"}, {"Schleswig-Holstein": "Kiel"}, {"Thuringia": "Erfurt"}
        ],
        "capital": "Berlin",
        "major_cities": ["Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt"]
    },
    "Canada": {
        "provinces": [
            {"Alberta": "Edmonton"}, {"British Columbia": "Victoria"}, {"Manitoba": "Winnipeg"}, {"New Brunswick": "Fredericton"}, {"Newfoundland and Labrador": "St. John's"},
            {"Nova Scotia": "Halifax"}, {"Ontario": "Toronto"}, {"Prince Edward Island": "Charlottetown"}, {"Quebec": "Quebec City"}, {"Saskatchewan": "Regina"}
        ],
        "capital": "Ottawa",
        "major_cities": ["Toronto", "Montreal", "Vancouver", "Calgary", "Edmonton"]
    }
}

def login():
     username = entry_username.get()
     password = entry_password.get()

def check_login(username, password): 
    if username in users and users[username] == password: 
        return True
    return False

def country_selector():
    print("Available Countries:")
    for c in countriesInfo.keys():
        print(f'{c} and the capital is {countriesInfo[c]["capital"]}')
        print(f'The major cities are: {", ".join(countriesInfo[c]["major_cities"])}')
        # Get the key that references the districts like states, countries, prefectures, provinces
#Got this to work, but I'm also still trying to breakdown what it's...doing. SEE Ln138
        districts = list(countriesInfo[c].keys())[0] 
        print(f'The {districts} are: {", ".join([list(district.keys())[0] for district in countriesInfo[c][districts]])}\n')
    
    while True:
        user_country = input("\nSelect a country: ")
        
        if user_country in countriesInfo:
            capital = countriesInfo[user_country]["capital"]
            print(f"Country selected: {user_country}, the capital is: {capital}")
            countriesInfo.pop(user_country)  # Remove the user's selected country
            break
        else:
            print("Invalid country selected. Please try again.")
            country_selector()

def allocate_units():
    #Idk but somehow setting these to global worked. feel like there is more streamline way
    global user_units
    global userSoldiers
    global userVehicles
    global userSupport
    global userTotal
    global computerSoldiers
    global computerVehicles

    user_units = random.randint(500, 1500)
    computer_units = random.randint(500, 1500)

    while True:
        print(f"\nYou have {user_units} units to use.")
        
        userSoldiers = int(input(f"How many soldiers: (Maximum: {user_units}) "))
        userTotal = user_units - userSoldiers
        print(f"Remaining units: {userTotal}")
        
        userVehicles = int(input(f"How many vehicles: (Maximum: {int(userTotal/5)}) "))
        userTotal -= userVehicles * 5
        print(f"Remaining units: {userTotal}")
        
        userSupport = int(input(f"How much support: (Maximum: {int(userTotal/3)}) "))
        userTotal -= userSupport * 3
        print(f"Remaining units: {userTotal}")

        # Check if the allocation exceeds the total units available
        if userTotal < 0:
            print("Error: The total allocated units exceed the available units.")
        else:
            print(f"Allocated units - Soldiers: {userSoldiers}, Vehicles: {userVehicles}, Support: {userSupport}")
            print(f"Remaining units: {userTotal}")
            reallocate = input("Would you like to choose again? (Yes or No): \n")
            if reallocate.lower() != "yes":
                userSoldiers += userTotal  # Add remaining units to soldiers
                print(f"Final allocation - Soldiers: {userSoldiers}, Vehicles: {userVehicles}, Support: {userSupport}")
                break

    print(f"\nComputer has {computer_units} units to use.")
    computerSoldiers = random.randint(0, computer_units)
    remaining_units = computer_units - computerSoldiers
    computerVehicles = random.randint(0, remaining_units)
    remaining_units -= computerVehicles
    computerSupport = remaining_units
    print(f"Computer allocated units - Soldiers: {computerSoldiers}, Vehicles: {computerVehicles}, Support: {computerSupport}")
    war()

# def allocateUnits():
#     commanderUnits = random.randint;

def war():
    userfinalpower = (userSoldiers * userVehicles ** userSupport)/random.randint(1,20)
    computerfinalpower = (computerSoldiers * computerVehicles ** userSupport)/random.randint(1,20)

    if userfinalpower > computerfinalpower:
        print("\nYOU WON") 
        print(f"User score: {userfinalpower}, Computer score: {computerfinalpower}")
    elif computerfinalpower > userfinalpower:
        print("\nYou lost")
        print(f"User score: {userfinalpower}, Computer score: {computerfinalpower}")
    else:
        print("Nope")