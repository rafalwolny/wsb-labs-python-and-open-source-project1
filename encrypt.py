someText = ''

szyfrDict = {
    "a": "y",
    "e": "i",
    "i": "o",
    "o": "a",
    "y": "e"
}


def szyfrowanie():
    someText = input('Podaj tekst: ')
    zaszyfrowane = list(someText)
    for i in range(len(zaszyfrowane)):
        for x, y in szyfrDict.items():
            if zaszyfrowane[i] == x:
                zaszyfrowane[i] = y
                break
    print('Wynik:', ''.join(zaszyfrowane))


def deszyfrowanie():
    someText = input('Podaj tekst: ')
    rozszyfrowane = list(someText)
    for i in range(len(rozszyfrowane)):
        for x, y in szyfrDict.items():
            if rozszyfrowane[i] == y:
                # print('Znaleziono litere z klucza:', rozszyfrowane[i])
                # print('Ta sama litera ale printowana ze slownika:', y)
                # print('Trzeba zamienic na:', x)
                rozszyfrowane[i] = x
                break
    print('Wynik:', ''.join(rozszyfrowane))
