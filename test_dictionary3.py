mijn_dictionary = {
    "Voornaam" : "Harry",
    "Geboortedatum" : "31-maart-1939",
    "Registratienummer" : "AA18891"
}

mijn_dictionary["Achternaam"] = "de Vries"

print()

for k, v in mijn_dictionary.items():
    print (k, v)

print()
print(len(mijn_dictionary))