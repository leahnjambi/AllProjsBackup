# WHILE LOOP
x = 0
while x <= 5:
    print(x)
    x += 1


    y = 90
    while y <= 100:
        print(y)
        y += 1


    m = 0
    while m <= 50:
        print(m)
        m += 1


counter_two =1
while counter_two <= 100:
    if(counter_two%2) == 0:
        print(counter_two)
        counter_two += 1
    else:
        counter_two += 1

# FOR IN LOOP
cars =["BMW", "Range","Tesla","Toyota","Noah"]
print(cars[1])
print(cars[3])
cars.append("mercedes")
cars.append("landrover")
for gari in cars:
    print(gari)
    #How many names do you have?
    #5
    #Enter the five names
    #--
    #--
    #--
    #--
    #--
    #Logic prints all the entered names
num = input("Enter your number\n")
jina = input("enter your name\n")
print("Hello",jina,"you entered number",num)
