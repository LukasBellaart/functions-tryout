
def rekenReeks(nummer:int):
    nummer1, nummer2 = 0, 1
    count = 0           
    if nummer <= 0:
        print("geef een positief nummber ")
    elif nummer == 1:
        print("Fibonacci reekts tot ",nummer,":")
        print(nummer1)
    else:
        print("Fibonacci reeks:")
        while count < nummer:
            print(nummer1)
            nth = nummer1 + nummer2
            nummer1 = nummer2
            nummer2 = nth
            count += 1


nterms = int(input("hoeveel reeksen? "))
rekenReeks(nterms)