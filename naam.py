def printNameAndAge(name:str,age:str) -> str:
    print('Hallo '+ name + ', je leeftijd is '+age+' jaar')

while True:
    name = input("Wat is je naam? -> ")
    if name.lower() == "stop":
        break
    age = input("Hoe oud ben jij? -> ")
    if age.lower() == "stop":
        break

    printNameAndAge(name,age)
