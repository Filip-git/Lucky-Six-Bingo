import random
import time

list = []
brojevi = []

print('Dobrodošao na Lucky Six Bingo!')
print('')
    
def izbor():
    print ('Želiš li sam birati brojeve [Y/DA], ili želiš automatski listić [N/NE]?')
    izbor1 = input()
    if izbor1 == 'Y' or izbor1 =='y' or izbor1 =='da' or izbor1 =='DA' or izbor1 =='Da' or izbor1 =='D' or izbor1 =='d':
        brojevi_igraca_rucno()
    elif izbor1 == 'N' or izbor1 =='n' or izbor1 =='ne' or izbor1 =='NE' or izbor1 =='Ne':
        brojevi_igraca_automatski()
    else:
        print('Molim ponovite unos i birajte [Y/DA] ili [N/NE]!')
        izbor()

def brojevi_igraca_rucno():
    while len(brojevi) < 6:
        unos = int(input('Unesi brojeve za igranje od 1 do 49 i nakon svakog unesenog broja pritisni enter: '))
        if unos in brojevi:
            unos = print('Broj je već odabran, unesi drugi od 1 do 49: ')
        elif unos <= 0:
            unos = print('Uneseni broj je manji od 0, unesi novi: ')
        elif unos > 49:
            unos = print('Uneseni broj je veći od 49, unesi novi: ')
        else:
            brojevi.append(unos)

    print('Odabrani brojevi su: ' , brojevi)
    print('')
    bingo()
    


def brojevi_igraca_automatski():
    while len(brojevi) <= 6:
        broj = random.randint(1,49)
        if broj in brojevi:
            broj = random.randint(1,49)
        else:
            brojevi.append(broj)
    print ('Igračevi brojevi su: ' , brojevi)
    print('')
    bingo()

def bingo():
    pogodeno = 0
    print('Izvlačenje: ')
    time.sleep(1)
    while len(list) <= 35:
        broj = random.randint(1,49)
        while broj in list:
            broj = random.randint(1,49)
        print('Broj:', broj)
        list.append(broj)
        time.sleep(0.5)
        if broj in brojevi:
            print ('POGODAK!')
            pogodeno += 1
    print ('Izvučeni brojevi su: ' , list)
    if pogodeno < 6:
        print('Pogođeno je: ' , pogodeno , ' brojeva!')
    else:
        print('Pogođeno je 6/6 brojeva, BINGO!')
    brojevi.clear()
    end()
        
def end():
    
    list.clear()
    print('Hvala za igranje, ukoliko želite nastaviti igru, upišite [Y/DA]!')
    end1 = input()
    if end1 == 'Y' or end1 =='y' or end1 =='da' or end1 =='DA' or end1 =='Da' or end1 =='D' or end1 =='d':
        izbor()
        bingo()
    else:
        print('Hvala na igranju!')
            
izbor()