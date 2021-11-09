#Alexander den Otter   -   99067410
import sys
BakjeOfHoorntje = "bakje"
Aantal_Bolletjes = 0

def Welkom(Aantal_Bolletjes):
    print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')
    AantalBolletjes(Aantal_Bolletjes)

def AantalBolletjes(Aantal_Bolletjes):
    while True:
        try:  
            Aantal_Bolletjes = int(input('Hoeveel bolletjes wilt u?\n---> '))
            break
        except(ValueError):
            print('Sorry, dat snap ik niet...')
    Keuzes(Aantal_Bolletjes)
   
def Keuzes(Aantal_Bolletjes):
    if Aantal_Bolletjes <= 3:
        HoornOfBakje = input('Wilt u deze '+str(Aantal_Bolletjes)+' bolletje(s) in A) een hoorntje of B) een bakje?\n---> ')
        if HoornOfBakje == "A":
            BakjeOfHoorntje == "hoorntje"
        elif HoornOfBakje == "B":
            BakjeOfHoorntje == "bakje"
        else:
            print('Sorry, dat snap ik niet...')
            Keuzes(Aantal_Bolletjes)
        Uitslag(Aantal_Bolletjes)
    elif Aantal_Bolletjes <=8:
        print('Dan krijgt u van mij een bakje met '+ str(Aantal_Bolletjes)+' bolletjes')
        MeerOfNietBestellen(Aantal_Bolletjes)

    else:
        print('Sorry, zulke grote bakken hebben we niet')
        AantalBolletjes(Aantal_Bolletjes)

def Uitslag(Aantal_Bolletjes):
    print('Hier is uw '+str(BakjeOfHoorntje)+ ' met '+str(Aantal_Bolletjes)+' bolletje(s).')
    MeerOfNietBestellen(Aantal_Bolletjes)
    
def MeerOfNietBestellen(Aantal_Bolletjes):
    NogIets = input('Wilt u nog meer bestellen?\n---> ')
    if NogIets == "Ja":
        AantalBolletjes(Aantal_Bolletjes)
    elif NogIets =="Nee":
        print('Bedankt en tot ziens!')
    else:
        print('Sorry dat snap ik niet...')
        MeerOfNietBestellen(Aantal_Bolletjes)

Welkom(Aantal_Bolletjes)
