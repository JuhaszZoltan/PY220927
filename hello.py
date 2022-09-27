nev = input('írd be a neved: ')
print(f'Hello {nev}!')
print(f'Milyen szép név az, hogy {nev}!')
print(f'Szerintem már most Beléd vagyok zúgva, {nev}! <3')

valasz = input(f'szeretsz programozni {nev}? ')
if valasz.lower() in {'igen', 'aha', 'ja', 'persze', 'hogyne'}:
    print('Akkor még itt sokra viheted!')
else:
    print('Akkor remélem, majd megszereted!')

szam = int(input('hányszor írjam ki a neved? '))
for x in range(szam):
    print(f'{nev}', end=' ')