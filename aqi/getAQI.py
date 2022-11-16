from importlib.machinery import SourceFileLoader
import ozon3 as ooo
import pandas as pd
import numpy as np
import json

# Done
# "Shanghai", "Beijing", "Tianjin", "Guangzhou", "Shenzhen", "Wuhan", "Dongguan", "Chongqing", "Chengdu", "Nanjing", "Taipei", "Kaohsiung", "Taichung",
# "tainan", "banqiao", "hsinchu", "taoyuan-city", "Keelung", "Hong Kong", "Macao", "Hanyang", "Busan", "Incheon", "Daejeon", "Ulsan", "Daegu", "Gwangju",
#"Suwon", "Goyang", "Seongnam", "Edo", "Yokohama", "Osaka", "Nagoya", "Sapporo", "Kobe", "Kyoto", "Fukuoka", "Kawasaki", "saitama", "Moscow", "Krasnoyarsk",
#"Kaliningrad", "Leningrad", "Novo-Nikolaevsk", "Nizhniy Novgorod", "Chelyabinsk",
#"Ufa", "Dhaka", "Kathmandu", "Pokhara", "Patan", "biratnagar", "Birgunj", "dharan-bazar"
#"Bharatpur", "Bombay", "Delhi", "Bangalore", "Calcutta", "Chennai", "Ahmedabad", "Hyderabad", "Pune", "Kanpur", "Bangkok", "mueang-samut-prakan", "Nonthaburi", "chon-buri"
#"Nakhon Ratchasima", "Chiangmai", "Hat Yai", "Pak Kret", "si-racha", "Amphoe Phra Pradaeng", "Lampang", "surin", "Vientiane",
# "Rangoon", "Kota Bharu", "Kuala Lumpur", "klang",
# "kampung-baru-subang", "Johor Bahru", "Subang Jaya", "Ipoh", "Kuching", "Ho Chi Minh City", "Hanoi", "Da Nang", "Haiphong", "bien-hoa", "Huế", "Nha Trang", "Bandar Seri Begawan",
# "City of Manila", "Jakarta", "Medan", "Bekasi", "Palembang", "Tangerang", "south-tangerang", "Colombo", "galkissa", "moratuwa", "Negombo", "pita-kotte", "Kotte", "Astana",
# "Almaty", "Dushanbe", "vahdat", "tursunzoda", "Bishkek", "Tashkent", "Phnom Penh", "Montreal", "Toronto", "Vancouver", "Calgary", "Ottawa", "Edmonton", "Mississauga",
# "north-york", "Winnipeg", "scarborough", "Auckland", "Wellington", "Christchurch", "Manukau", "waitakere", "North Shore", "Hamilton", "Dunedin", "Lower Hutt", "Syd",
# "Melbourne", "Brisbane", 'Perth', 'Adelaide', 'Gold', 'Canberra',
# 'Newcastle', 'Wollongong', 'Logan', 'New York', 'LA', 'Chicago', 'Borough of Brooklyn', 'borough-of-queens',
# 'houston', 'Philadelphia', 'manhattan', 'Phoenix', 'Borough of Bronx', 'Lima', 'Callao', 'laventille', 'Santiago', 'puente-alto', 'Antofagasta', 'Viña del Mar', 'Valparaíso',
# 'Talcahuano', 'san-bernardo', 'temuco', 'Iquique', 'Concepción', 'São Paulo', 'Mexico City', 'iztapalapa', 'Ecatepec de Morelos', 'Guadalajara', 'Puebla',
# 'Ciudad Juárez', 'Tijuana', 'Ciudad Neza', 'Bogotá', 'Santiago de Cali', 'Medellín', 'Willemstad', 'sint-michiel-liber', 'barber', 'dorp-soto', 'newport', 'sabana-westpunt',
# 'dorp-sint-willebrordus', 'lagun', 'Quito', 'Cuenca', 'Buenos Aires', 'San Salvador', 'San Juan', 'Guatemala City', 'San José', 'Paris', 'Marseille', 'Lyon', 'Toulouse',
# 'Nice', 'Nantes', 'Strasbourg', 'Montpellier', 'Bordeaux', 'Lille', 'Tallinn', 'Tartu', 'Narva', 'Kohtla-Järve', 'rakvere', 'Sillamäe', 'Maardu', 'Kuressaare', 'Madrid',
# 'Barcelona', 'Valencia', 'Seville', 'Saragossa', 'Málaga', 'Murcia', 'Palma de Mallorca', 'Las Palmas de Gran Canaria', 'bilbao', 'City of London', 'Zurich', 'Geneva',
# 'Basel', 'Bern', 'Lausanne', 'Winterthur', 'St. Gallen', 'Lucerne', 'Prague', 'Brno', 'Ostrava',
# 'Pilsen', 'Olomouc', 'Liberec', 'Budweis', 'Hradec Králové', 'Rome', 'Milan',
# 'Naples', 'Turin', 'Genoa', 'Bologna', 'Florence', 'Bratislava', 'Košice', 'Prešov', 'Nitra', 'Žilina', 'Banská Bystrica', 'Trnava', 'martin', 'Oslo', 'Bergen', 'Trondheim',
# 'Stavanger', 'Drammen', 'Fredrikstad', 'Kristiansand', 'Sandnes', 'Vienna', 'Graz', 'Linz', 'Salzburg', 'Innsbruck', 'Klagenfurt', 'Villach', 'Wels',
# 'Nicosia', 'Limassol',
# 'Larnaca', 'Famagusta', 'Paphos', 'Keryneia', 'Protaras', 'pergamos', 'Warsaw', 'Łódź', 'Krakow', 'Wrocław', 'poznan', 'Gdańsk', 'Szczecin', 'Bydgoszcz', 'Lublin', 'Katowice',
# 'Brussels', 'Antwerp', 'Ghent', 'Charleroi', 'Liège', 'Bruges', 'Namur', 'Leuven', 'Amsterdam', 'Rotterdam', 'Hague', 'Utrecht', 'Eindhoven', 'Tilburg', 'Groningen',
# 'Almere', 'Breda', 'Nijmegen', 'Copenhagen', 'frederiksberg', 'Vilnius', 'Kaunas', 'Klaipėda', 'Šiauliai', 'dainava-kaunas', 'eiguliai', 'Budapest', 'Debrecen', 'Miskolc',
# 'szeged','Pécs', 'nyiregyhaza', 'Bucharest', 'Iași', 'Cluj-Napoca', 'Timişoara', 'Craiova', 'Braşov', 'Ploieşti', 'Brăila', 'Dublin', 'Zagreb', 'Split', 'Rijeka', 'Osijek',
# 'Zadar', 'Slavonski Brod', 'Pula', 'Ljubljana', 'Maribor', 'Celje', 'Kranj', 'Velenje', 'Koper', 'Novo Mesto', 'Ptuj', 'Birkirkara', 'qormi', 'Mosta', 'zabbar',
# 'Saint John', 'fgura', 'zejtun', 'Berlin', 'Hamburg', 'Munich', 'Cologne', 'Frankfurt', 'Essen', 'Stuttgart', 'Dortmund', 'Duesseldorf', 'Bremen', 'Helsinki', 'Espoo',
# 'Tampere', 'Vantaa', 'Turku', 'Oulu', 'Lahti',
cities = [
    'Kuopio', 'Jyvaskyla', 'Pori', 'Noumea', 'Stockholm', 'Goteborg', 'Malmo', 'Uppsala', 'Västerås', 'Linköping', 'Helsingborg',
    'Sofia', 'Plovdiv', 'Varna', 'Burgas', 'Rousse', 'Stara Zagora', 'Pleven', 'Sliven', 'Belgrade', 'Niš', 'Novi Sad', 'zemun', 'Kragujevac', 'Čačak', 'Subotica', 'Leskovac',
    'Sarajevo', 'Banja Luka', 'Zenica', 'Tuzla', 'Mostar', 'Bugojno', 'brcko', 'Prishtina', 'Prizren', 'Kosovska Mitrovica', 'gjakove', 'Peć', 'Suva Reka', 'ferizaj',
    'glogovac', 'Skopje', 'Bitola', 'Kumanovo', 'Prilep', 'Tetovo', 'cair', 'kisela-voda', 'Veles', 'Podgorica', 'niksic', 'Herceg Novi', 'Pljevlja', 'Budva', 'Bar',
    'Bijelo Polje', 'Cetinje', 'Reykjavik', 'Kopavogur', 'Hafnarfirdi', 'Akureyri', 'Garðabaer', 'Mosfellsbaer', 'Akranes', 'selfoss', 'Lisbon', 'Porto', 'Amadora',
    'Braga', 'Setúbal', 'Queluz', 'Funchal', 'Athens', 'Kiev', 'Dnipro', 'Odesa', 'Alexandrovsk', 'Lviv', 'Kryvyi Rih', 'Mariupol', 'ivano-frankivsk', 'Tbilisi', 'Kutaisi', 'Batumi',
    'Rustavi', 'Haifa', 'Tel Aviv', 'Ariel', 'West Jerusalem', 'Ashdod', 'Rishon LeZion', 'Petach Tikva', 'Beersheba', 'Ankara', 'Istanbul', 'Izmir', 'Bursa', 'Adana', 'Gaziantep',
    'Konya', 'cankaya', 'Antalya', 'Tehran', 'Mashhad', 'Isfahan', 'Karaj', 'Tabriz', 'Shiraz', 'Qom', 'Ahvaz', 'Dubai', 'al-sohar', 'Saham', 'Manama', 'Al Muharraq',
    'dar-kulayb', 'sitrah', 'Al Ahmadi', 'Kuwait', 'Amman', 'Zarqa', 'Irbid', 'russeifa', ' Wadi Al Seer', 'Adjlun', 'Aqaba', 'Madaba', 'Baghdad', 'Basra', 'Abu Ghraib',
    'Jeddah', 'Medina', 'Riyadh', 'Mecca', 'sultanah', 'Dammam', 'Taif', 'tabuk', 'Karachi', 'Lahore', 'Rawalpindi', 'Peshawar', 'Kabul', 'Ashgabat', 'Cape Town', 'Durban',
    'Soweto', 'Pretoria', 'Port Elizabeth', 'Pietermaritzburg', 'benoni', 'Addis Ababa', 'Nairobi', 'Kampala', 'Algiers', 'Bamako'
]

geocode = SourceFileLoader('geocode', 'geocode.py').load_module()

targetFolder = 'aqi'

stationLoc = []

o3 = ooo.Ozon3('c9978475a94b889bdfa222c395fbcdf4ea019959')
for city in cities:
    try:
        stations = o3.get_city_station_options(city)
    except:
        print(f'❌  No stations in {city}')
    else:
        stations = stations.to_numpy()

        for station in stations:
            stationData = o3.get_historical_data(city_id=station[0]).dropna(
                axis=0, thresh=6).fillna(0).to_numpy()

            finalStationData = np.column_stack(
                (np.full(len(stationData), station[2][0]), stationData[:, 0], np.amax(stationData[:, 1:], axis=1)))

            # try:
            #    data = np.row_stack((data, finalStationData))
            #    print(f'{station[2][0]} written to data')
            # except:
            #    data = finalStationData
            #    print('using finalStationData')

            pd.DataFrame(finalStationData).to_csv(
                f'aqi/output-data/{station[0]}.csv', index=False, header=["location", "date", "aqi"])
            print(f'{station[2][0]} written to data')

# if input('Check geocode data?') == 'y':
#    with open(f'{targetFolder}/geocode/inputData.json', "w") as outfile:
#        json.dump(np.unique(data[:, 0]).tolist(), outfile)
#
#    geocode.geocode(targetFolder, warnSkip=True)
#
#geocodeData = json.load(open(f'{targetFolder}/geocode/outputData.json'))
#
# for year in range(1750, 2021):
#    yearData = data[np.where(data[:, 1] == year)]
#    for i, info in enumerate(yearData):
#        yearData[i, 1] = geocodeData[info[0]]['lon']
#        yearData[i, 0] = geocodeData[info[0]]['lat']
#    pd.DataFrame(yearData).to_csv(
#        f'{targetFolder}/output-data/{year}.csv', index=False, header=["lat", "lon", "co2"])
#
print('✔  All Data Saved')
#
##pd.DataFrame(data).to_csv(f'aqi/output-data/data.csv', index=False, header=["date", "aqi"])
