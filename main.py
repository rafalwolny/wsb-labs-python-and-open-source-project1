from encrypt import szyfrowanie, deszyfrowanie

operation = ''

while operation != 'wyjscie':
  operation = input('Wybierz operacje (szyfrowanie, deszyfrowanie, wyjscie): ')

  if operation == 'szyfrowanie':
    szyfrowanie()                                  # <--- tutaj program przechodzi do skryptu szyfrujacego
  elif operation == 'deszyfrowanie':
    deszyfrowanie()                                # <--- tutaj program przechodzi do skryptu deszyfrujacego
  elif operation != ('szyfrowanie' and 'deszyfrowanie' and 'wyjscie'):
    print('Bledna operacja! Niepoprawne dane')
    print('Sprobuj ponownie')
    
