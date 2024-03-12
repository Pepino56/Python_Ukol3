import os
from colorama import Fore

def otevriSouborTXT():
    """Načtení slovníku českých slov a jeho vrácení v proměnné"""
    with open("slovnik_cs_CZ_utf8.txt", "r", encoding="utf-8") as slovnikTXT:
        slovnik = slovnikTXT.readlines()
    return slovnik

def zadejSlovo():
    """"""

def porovnejSlovo(slovo):
    """Určí zda se slovo nachází ve slovníku"""
    if slovo in slovnikBezEnter:
        return True
    else:
        return False
       
            

def urciKrajniPismena():
    """"""

#Volání metody pro načtení je ošetřeno try-except
try:
    #nactenySlovnik = otevriSouborTXT()
    print("Seznam je načtený.")
    slovnikBezEnter = [s.replace('\n', '').lower() for s in otevriSouborTXT()] #odstraní znak \n ze seznamu, poté je možné porovnat zadané slovo
except Exception as ex:
    print(f"Došlo k chybě při práci se souborem: {ex}")


vstupniSlovo = "OHAŘ".lower()
trefa = porovnejSlovo(vstupniSlovo)
print(trefa)
bodyHrac1 = 0
bodyHrac2 = 0
maxScore = 10
# while bodyHrac1 < maxScore or bodyHrac2 < maxScore:
#     input("Hraje hráč 1.")




#print(nactenySlovnik)