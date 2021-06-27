from encrypt import szyfrowanie, deszyfrowanie

operation = ''

while operation != 'wyjscie':
    operation = input(
        'Wybierz operacje (szyfrowanie, deszyfrowanie, wyjscie): ')

    if operation == 'szyfrowanie':
        # <--- tutaj program przechodzi do skryptu szyfrujacego
        szyfrowanie()
    elif operation == 'deszyfrowanie':
        # <--- tutaj program przechodzi do skryptu deszyfrujacego
        deszyfrowanie()
    elif operation != ('szyfrowanie' and 'deszyfrowanie' and 'wyjscie'):
        print('Bledna operacja!')
        print('Sprobuj ponownie')
