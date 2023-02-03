import name_a_toon

namelist = name_a_toon.NameList.from_file("names.txt")
print(name_a_toon.Name.random(namelist).to_string())