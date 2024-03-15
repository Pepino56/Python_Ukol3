import os
from colorama import Fore

def otevriSouborTXT():
    """Funkce, která provede načtení souboru a jeho vrácení v proměnné"""

    with open("slovnik_cs_CZ_utf8.txt", "r", encoding="utf-8") as slovnikTXT:
        slovnik = slovnikTXT.readlines()
    return slovnik

def zadejSlovo():
    """"""

def porovnejSlovo(slovo, slovnik):
    """Funkce, která určí zda se slovo nachází ve slovníku"""

    if slovo in slovnik:
        return True
    else:
        return False
       
def urciKrajniPismena(slovo):
    """Funkce, která určí první a poslední písmeno vloženého slova"""
    prvni = slovo[0]
    posledni = slovo[-1]
    return [prvni, posledni]

def main():
    bodyHrac1 = 0
    bodyHrac2 = 0
    hrac = 1
    maxScore = 10
    krajniPismena = ['a', 'a']

    #Volání metody pro načtení je ošetřeno try-except
    try:
        #odstraní znak \n ze seznamu, poté je možné porovnat zadané slovo
        slovnikBezEnter = [s.replace('\n', '').lower() for s in otevriSouborTXT()]
        print("Soubor je načtený.")
    except Exception as ex:
        print(f"Došlo k chybě při práci se souborem: {ex}")


    while bodyHrac1 < maxScore and bodyHrac2 < maxScore:
        print()
        if hrac == 1:
            print(f"Hraje hráč 1. Stav bodů: {bodyHrac1}")
            slovoH1 = input(f"Napis slovo které začíná na písmeno {krajniPismena[1]}: ")
            if porovnejSlovo(slovoH1, slovnikBezEnter) == True:
                if slovoH1[0] == krajniPismena[1]:
                    krajniPismena = urciKrajniPismena(slovoH1)
                    print(f"Slovo {Fore.LIGHTGREEN_EX + slovoH1 + Fore.RESET} nalezeno v českém slovníku. Poslední písmeno je: {Fore.CYAN + krajniPismena[1] + Fore.RESET}.")
                    bodyHrac1 += 1
                else:
                       print(f"Slovo {slovoH1} nezačíná na {krajniPismena[1]}.")
                hrac = 2            
            else:
                print(f"Slovo {Fore.LIGHTRED_EX + slovoH1 + Fore.RESET} se nenachází v českém slovníku")
                hrac = 2

        elif hrac == 2:
            print(f"Hraje hráč 2. Stav bodů: {bodyHrac2}")
            slovoH2 = input(f"Napis slovo které začíná na písmeno {krajniPismena[1]}: ")
            if porovnejSlovo(slovoH2, slovnikBezEnter) == True:
                    if slovoH2[0] == krajniPismena[1]:
                        krajniPismena = urciKrajniPismena(slovoH2)
                        print(f"Slovo {Fore.LIGHTGREEN_EX + slovoH2 + Fore.RESET} nalezeno v českém slovníku. Poslední písmeno je: {Fore.CYAN + krajniPismena[1] + Fore.RESET}.")
                        bodyHrac2 += 1
                    else:
                        print(f"Slovo {slovoH2} nezačíná na {krajniPismena[1]}.")
                    hrac = 1                    
            else:
                print(f"Slovo {Fore.LIGHTRED_EX + slovoH2 + Fore.RESET} se nenachází v českém slovníku")
                hrac = 1
    print(f"Konec hry. Hráč č.{hrac} prohrál.")
       
main()