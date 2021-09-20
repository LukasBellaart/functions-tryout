print("De bedoeling van dit is dat je vanaf Maastricht naar Groningen reist.\nDoor middel van vragen te beantwoorden gaat u proberen in Groningen te komen\nHoe meer vragen u goed heeft hoe dichterbij u bij groningen komt.")
def checkAntwoord(antwoord):
        antwoord = antwoord
        if antwoord in provincies:
            if not antwoord in alGegevenAntwoorden:
                alGegevenAntwoorden.append(antwoord)
                print("Dat is een goed antwoord!")
            else:
                print("Jij hebt dat antwoord al gegeven.")

        else:
            print("Dat is niet een van de nederlandse provincies")

Groningen = input("welke bekende nederlander is geen groninger?\nArjen Robben\nBert Visser\nAndré van Duin\n")
Rotterdam = input("In welk jaar werd De Kuip geopend?\n1937\n1957\n")
Amsterdam = input("Wat zijn de artiestennamen van Jorik Scholten?\nLil Kleine\nSevn Alias\nBokoesam\n")
Utrecht = input("Wat is de oudste studentenverenging van utrecht?\nC.S.Unitas\nUnitas.S.R\nUSC\n")
Breda = input("Door wie werd de Bredase Yordi(Djordie!) bekend?\nMo Bicep\nBram Krikke\nRapper Sjors\n")
groningenInwonersVraag = int(input("Hoeveel inwoners heeft groningen? (10% margin)\n"))
punten = 0

if Groningen == "André van Duin":
    punten += 1

if Rotterdam == "1937":
    punten += 1
if Amsterdam == "Lil Kleine":
    punten += 1
if Utrecht == "USC":
    punten += 1
if Breda == "Bram Krikke":
    punten += 1


inwonersGroningen = 232652
onderDoel = 209386
bovenDoel = 255917

if groningenInwonersVraag <= bovenDoel and groningenInwonersVraag >= onderDoel or groningenInwonersVraag == inwonersGroningen:
    punten += 1
    if groningenInwonersVraag == inwonersGroningen:
        punten += 3

provincies = [
    "groningen",
    "friesland",
    "drenthe",
    "overijssel",
    "flevoland",
    "gelderland",
    "utrecht",
    "noord-holland",
    "zuid-holland",
    "zeeland",
    "noord-brabant",
    "limburg"
]

alGegevenAntwoorden = []

for x in provincies:
    antwoord = input("Noem een van de 12 nederlandse provincies. -> ").lower()   
    checkAntwoord(antwoord)

vragenGoed = 0
for x in alGegevenAntwoorden:
    vragenGoed = vragenGoed + 1

gescoordePunten = vragenGoed/4
punten = punten + gescoordePunten

print("Je hebt "+str(punten)+" punten behaald")
if punten > 0 and punten <= 2.5:
    print("U bent geëindigt in Engeland. Jammer u heeft Groningen niet gehaald.")
elif punten > 2.5 and punten <= 5:
    print("U bent geëindigt in Rotterdam. Jammer u heeft Groningen niet gehaald.")
elif punten > 5 and punten <= 7.5:
    print("U bent geëindigt in Leeuwarden. Jammer u heeft Groningen niet gehaald.")
elif punten > 7.5:
    print("U bent geëindigt in Groningen! Gefeliciteerd!")
