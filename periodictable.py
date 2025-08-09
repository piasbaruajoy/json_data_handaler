#এখন আমি একটা periodic table বানাবো জেটাকে পর্জায় সারনী বলে 
import time
from colorama import Style,Fore
periodic_table = [
    {"atomic_number": 1, "name": "Hydrogen", "symbol": "H", "atomic_mass": 1.008, "melting_point": -259.14, "boiling_point": -252.87},
    {"atomic_number": 2, "name": "Helium", "symbol": "He", "atomic_mass": 4.0026, "melting_point": -272.2, "boiling_point": -268.93},
    {"atomic_number": 3, "name": "Lithium", "symbol": "Li", "atomic_mass": 6.94, "melting_point": 180.54, "boiling_point": 1342},
    {"atomic_number": 4, "name": "Beryllium", "symbol": "Be", "atomic_mass": 9.0122, "melting_point": 1287, "boiling_point": 2470},
    {"atomic_number": 5, "name": "Boron", "symbol": "B", "atomic_mass": 10.81, "melting_point": 2076, "boiling_point": 3927},
    {"atomic_number": 6, "name": "Carbon", "symbol": "C", "atomic_mass": 12.011, "melting_point": 3550, "boiling_point": 4827},
    {"atomic_number": 7, "name": "Nitrogen", "symbol": "N", "atomic_mass": 14.007, "melting_point": -210, "boiling_point": -196},
    {"atomic_number": 8, "name": "Oxygen", "symbol": "O", "atomic_mass": 15.999, "melting_point": -218.79, "boiling_point": -182.95},
    {"atomic_number": 9, "name": "Fluorine", "symbol": "F", "atomic_mass": 18.998, "melting_point": -219.67, "boiling_point": -188.11},
    {"atomic_number": 10, "name": "Neon", "symbol": "Ne", "atomic_mass": 20.18, "melting_point": -248.59, "boiling_point": -246.08},
    {"atomic_number": 11, "name": "Sodium", "symbol": "Na", "atomic_mass": 22.99, "melting_point": 97.79, "boiling_point": 883},
    {"atomic_number": 12, "name": "Magnesium", "symbol": "Mg", "atomic_mass": 24.305, "melting_point": 650, "boiling_point": 1090},
    {"atomic_number": 13, "name": "Aluminium", "symbol": "Al", "atomic_mass": 26.982, "melting_point": 660.32, "boiling_point": 2470},
    {"atomic_number": 14, "name": "Silicon", "symbol": "Si", "atomic_mass": 28.085, "melting_point": 1414, "boiling_point": 3265},
    {"atomic_number": 15, "name": "Phosphorus", "symbol": "P", "atomic_mass": 30.974, "melting_point": 44.15, "boiling_point": 280.5},
    {"atomic_number": 16, "name": "Sulfur", "symbol": "S", "atomic_mass": 32.06, "melting_point": 115.21, "boiling_point": 444.6},
    {"atomic_number": 17, "name": "Chlorine", "symbol": "Cl", "atomic_mass": 35.45, "melting_point": -101.5, "boiling_point": -34.04},
    {"atomic_number": 18, "name": "Argon", "symbol": "Ar", "atomic_mass": 39.948, "melting_point": -189.34, "boiling_point": -185.85},
    {"atomic_number": 19, "name": "Potassium", "symbol": "K", "atomic_mass": 39.098, "melting_point": 63.5, "boiling_point": 759},
    {"atomic_number": 20, "name": "Calcium", "symbol": "Ca", "atomic_mass": 40.078, "melting_point": 842, "boiling_point": 1484},
    {"atomic_number": 21, "name": "Scandium",    "symbol": "Sc", "atomic_mass": 44.9559,
     "melting_point": round(1814 - 273.15, 4), "boiling_point": round(3103 - 273.15, 4)},
    {"atomic_number": 22, "name": "Titanium",    "symbol": "Ti", "atomic_mass": 47.88,
     "melting_point": round(1941 - 273.15, 4), "boiling_point": round(3560 - 273.15, 4)},
    {"atomic_number": 23, "name": "Vanadium",    "symbol": "V",  "atomic_mass": 50.9415,
     "melting_point": round(2183 - 273.15, 4), "boiling_point": round(3680 - 273.15, 4)},
    {"atomic_number": 24, "name": "Chromium",    "symbol": "Cr", "atomic_mass": 51.996,
     "melting_point": round(2180 - 273.15, 4), "boiling_point": round(2944 - 273.15, 4)},
    {"atomic_number": 25, "name": "Manganese",   "symbol": "Mn", "atomic_mass": 54.938,
     "melting_point": round(1519 - 273.15, 4), "boiling_point": round(2334 - 273.15, 4)},
    {"atomic_number": 26, "name": "Iron",        "symbol": "Fe", "atomic_mass": 55.847,
     "melting_point": round(1811 - 273.15, 4), "boiling_point": round(3134 - 273.15, 4)},
    {"atomic_number": 27, "name": "Cobalt",      "symbol": "Co", "atomic_mass": 58.9332,
     "melting_point": round(1768 - 273.15, 4), "boiling_point": round(3200 - 273.15, 4)},
    {"atomic_number": 28, "name": "Nickel",      "symbol": "Ni", "atomic_mass": 58.6934,
     "melting_point": round(1728 - 273.15, 4), "boiling_point": round(3186 - 273.15, 4)},
    {"atomic_number": 29, "name": "Copper",      "symbol": "Cu", "atomic_mass": 63.546,
     "melting_point": round(1357.77 - 273.15, 4), "boiling_point": round(2835 - 273.15, 4)},
    {"atomic_number": 30, "name": "Zinc",        "symbol": "Zn", "atomic_mass": 65.39,
     "melting_point": round(692.68 - 273.15, 4), "boiling_point": round(1180 - 273.15, 4)},
    {"atomic_number": 31, "name": "Gallium",     "symbol": "Ga", "atomic_mass": 69.723,
     "melting_point": round(302.91 - 273.15, 4), "boiling_point": round(2477 - 273.15, 4)},
    {"atomic_number": 32, "name": "Germanium",   "symbol": "Ge", "atomic_mass": 72.61,
     "melting_point": round(1211.4 - 273.15, 4), "boiling_point": round(3093 - 273.15, 4)},
    {"atomic_number": 33, "name": "Arsenic",     "symbol": "As", "atomic_mass": 74.9216,
     "melting_point": round(1090 - 273.15, 4), "boiling_point": round(887 - 273.15, 4)},
    {"atomic_number": 34, "name": "Selenium",    "symbol": "Se", "atomic_mass": 78.96,
     "melting_point": round(494 - 273.15, 4), "boiling_point": round(958 - 273.15, 4)},
    {"atomic_number": 35, "name": "Bromine",     "symbol": "Br", "atomic_mass": 79.904,
     "melting_point": round(265.8 - 273.15, 4), "boiling_point": round(332 - 273.15, 4)},
    {"atomic_number": 36, "name": "Krypton",     "symbol": "Kr", "atomic_mass": 83.8,
     "melting_point": round(115.79 - 273.15, 4), "boiling_point": round(119.93 - 273.15, 4)},
    {"atomic_number": 37, "name": "Rubidium",    "symbol": "Rb", "atomic_mass": 85.4678,
     "melting_point": round(312.46 - 273.15, 4), "boiling_point": round(961 - 273.15, 4)},
    {"atomic_number": 38, "name": "Strontium",   "symbol": "Sr", "atomic_mass": 87.62,
     "melting_point": round(1050 - 273.15, 4), "boiling_point": round(1655 - 273.15, 4)},
    {"atomic_number": 39, "name": "Yttrium",     "symbol": "Y",  "atomic_mass": 88.9059,
     "melting_point": round(1799 - 273.15, 4), "boiling_point": round(3618 - 273.15, 4)},
    {"atomic_number": 40, "name": "Zirconium",   "symbol": "Zr", "atomic_mass": 91.224,
     "melting_point": round(2128 - 273.15, 4), "boiling_point": round(4682 - 273.15, 4)},
    {"atomic_number": 41, "name": "Niobium",     "symbol": "Nb", "atomic_mass": 92.9064,
     "melting_point": round(2750 - 273.15, 4), "boiling_point": round(5017 - 273.15, 4)},
    {"atomic_number": 42, "name": "Molybdenum",  "symbol": "Mo", "atomic_mass": 95.94,
     "melting_point": round(2896 - 273.15, 4), "boiling_point": round(4912 - 273.15, 4)},
    {"atomic_number": 43, "name": "Technetium",  "symbol": "Tc", "atomic_mass": 98,
     "melting_point": round(2430 - 273.15, 4), "boiling_point": round(4538 - 273.15, 4)},
    {"atomic_number": 44, "name": "Ruthenium",   "symbol": "Ru", "atomic_mass": 101.07,
     "melting_point": round(2607 - 273.15, 4), "boiling_point": round(4423 - 273.15, 4)},
    {"atomic_number": 45, "name": "Rhodium",     "symbol": "Rh", "atomic_mass": 102.9055,
     "melting_point": round(2237 - 273.15, 4), "boiling_point": round(3968 - 273.15, 4)},
    {"atomic_number": 46, "name": "Palladium",   "symbol": "Pd", "atomic_mass": 106.42,
     "melting_point": round(1828.05 - 273.15, 4), "boiling_point": round(3236 - 273.15, 4)},
    {"atomic_number": 47, "name": "Silver",      "symbol": "Ag", "atomic_mass": 107.868,
     "melting_point": round(1234.93 - 273.15, 4), "boiling_point": round(2435 - 273.15, 4)},
    {"atomic_number": 48, "name": "Cadmium",     "symbol": "Cd", "atomic_mass": 112.241,
     "melting_point": round(594.22 - 273.15, 4), "boiling_point": round(1040 - 273.15, 4)},
    {"atomic_number": 49, "name": "Indium",      "symbol": "In", "atomic_mass": 114.82,
     "melting_point": round(429.75 - 273.15, 4), "boiling_point": round(2345 - 273.15, 4)},
    {"atomic_number": 50, "name": "Tin",         "symbol": "Sn", "atomic_mass": 118.71,
     "melting_point": round(505.08 - 273.15, 4), "boiling_point": round(2875 - 273.15, 4)},

]
#
# এখন এই ডাটা গুলি আমি একটা টেক্সট ফাইলে রাখব
#
#
file_path=r"p:python\file\test.txt"
with open(f"{file_path}",'w') as periodic:
    periodic.write("=================================================================================================\n")
    periodic.write("| Atomic Number | Element Name | Symbol | Atomic Mass (u)| Melting Point (°C) |Boiling Point(°C)|")
    periodic.write("\n================================================================================================\n")

    print(Fore.CYAN+"===========================================================================================")
    print("|Atomic Number|Element Name|Symbol|  Atomic Mass (u)|Melting Point (°C) |Boiling Point(°C)|")
    print("===========================================================================================")
    for x in periodic_table:
        print(f"{x['atomic_number']:^12} {x["name"]:^15} {x["symbol"]:^6} {x["atomic_mass"]:^18} {x["melting_point"]:^15} {x["boiling_point"]:^15}") 
        periodic.write(f"{x['atomic_number']:^12} {x["name"]:^15} {x["symbol"]:^6} {x["atomic_mass"]:^18} {x["melting_point"]:^15}, {x["boiling_point"]:^15}\n")
        time.sleep(.5)