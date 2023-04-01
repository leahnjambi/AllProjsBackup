# TUPLES
cars = ("Marcedes","Toyota","Bmw","Audi","Range")
print(cars[1])
print(cars[4])
print(cars[0:3])
for gari in cars:
    print(gari)
# LISTS
students =["Dennis","Leah","Glory","Walter","Jared"]
students.append("Michelle")
students.append("Quinton")
students.append("Donald")
students[3] = "Wairimu"
print(students[1])
print(students[3])
print(students[2:4])
for std in students:
    print(std)
# DICTIONARIES
vehicles = {"v1":"Bmw","v2":"Ford","v3":"Mitsubishi", "v4":"probox"}
print(vehicles["v4"])
#printing all the keys of dictionary
for key in vehicles.keys():
    print(key)

#printing all the values of the dictionary
for value in vehicles.values():
    print(value)