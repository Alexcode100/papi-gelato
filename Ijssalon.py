#Alexander den Otter   -   99067410
import sys

BakjeOfHoorntje = "bakje"
Aantal_Bolletjes = 0
Bolletje = 1
Aardbei = 0
Chocolade = 0
Munt = 0
Vanille = 0
Hoorntje = 0
Bakje = 0

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
    SmaakBolletjes(Aantal_Bolletjes,Bolletje,Aardbei,Chocolade,Munt,Vanille)

def SmaakBolletjes(Aantal_Bolletjes,Bolletje,Aardbei,Chocolade,Munt,Vanille):
    Aantalx = Aantal_Bolletjes
    while Aantalx >= 1:
        SmaakBol = input('Welke smaak wilt u voor bolletje nummer '+str(Bolletje)+'? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?\n---> ')
        Bolletje = Bolletje + 1
        Aantalx = Aantalx - 1
        if SmaakBol == "A":
            Aardbei = Aardbei + 1
        elif SmaakBol == "C":
            Chocolade = Chocolade + 1
        elif SmaakBol == "M":
            Munt = Munt + 1
        elif SmaakBol == "V":
            Vanille = Vanille + 1
        else:
            Aantalx = Aantalx + 1
            print('Sorry dat snap ik niet...')

    print('Oke, u heeft dus de smaken:\n--------------\n'+str(Aardbei)+'x Aardbei\n'+str(Chocolade)+'x Chocolade\n'+str(Munt)+'x Munt\n'+str(Vanille)+'x Vanille\n--------------')
    Keuzes(Aantal_Bolletjes,Hoorntje,Bakje)

def Keuzes(Aantal_Bolletjes,Hoorntje,Bakje):
    if Aantal_Bolletjes <= 3:
        HoornOfBakje = input('Wilt u deze '+str(Aantal_Bolletjes)+' bolletje(s) in A) een hoorntje of B) een bakje?\n---> ')
        if HoornOfBakje == "A":
            BakjeOfHoorntje == "hoorntje"
            Hoorntje = Hoorntje + 1
        elif HoornOfBakje == "B":
            BakjeOfHoorntje == "bakje"
            Bakje = Bakje + 1
        else:
            print('Sorry, dat snap ik niet...')
            Keuzes(Aantal_Bolletjes,Hoorntje,Bakje)
        Uitslag(Aantal_Bolletjes,Hoorntje,Bakje)
    elif Aantal_Bolletjes <=8:
        print('Dan krijgt u van mij een bakje met '+ str(Aantal_Bolletjes)+' bolletjes')
        Bakje = Bakje + 1
        print(Bakje)
        Bonnetje(Aantal_Bolletjes,Hoorntje,Bakje)

    else:
        print('Sorry, zulke grote bakken hebben we niet')
        AantalBolletjes(Aantal_Bolletjes)

def Uitslag(Aantal_Bolletjes,Hoorntje,Bakje):
    print('Hier is uw '+str(BakjeOfHoorntje)+ ' met '+str(Aantal_Bolletjes)+' bolletje(s).')
    Bonnetje(Aantal_Bolletjes,Hoorntje,Bakje)
    
def MeerOfNietBestellen(Aantal_Bolletjes):
    NogIets = input('Wilt u nog meer bestellen?\n---> ')
    if NogIets == "Ja":
        AantalBolletjes(Aantal_Bolletjes)
    elif NogIets =="Nee":
        print('Bedankt en tot ziens!')
    else:
        print('Sorry dat snap ik niet...')
        MeerOfNietBestellen(Aantal_Bolletjes)

def Bonnetje(Aantal_Bolletjes,Hoorntje,Bakje):
    PrijsBolletjes = Aantal_Bolletjes*1.10
    PrijsHorrentje = Hoorntje*1.25
    PrijsBakje = Bakje*0.75
    Totaal = PrijsBolletjes + PrijsHorrentje + PrijsBakje
    print(Bakje)
    print(Hoorntje)
    print('------------[ Papi Gelato ]------------')
    print(' ')
    print("Bolletje('s)       "+str(Aantal_Bolletjes)+' x 1,10       = '+"{:.2f}".format(PrijsBolletjes))
    if Hoorntje == 1:
        print("Horrentje('s)   "+str(PrijsHorrentje)+' x 1,25       = '+"{:.2f}".format(PrijsHorrentje))
    if Bakje == 1:
        print("Bakje('s)       "+str(PrijsBakje)+' x 0,75       = '+"{:.2f}".format(PrijsBakje))
    print('                                 ----- +')
    print('Totaal                           = '+"{:.2f}".format(Totaal))
    print(' ')
    print('---------------------------------------')
    MeerOfNietBestellen(Aantal_Bolletjes)

Welkom(Aantal_Bolletjes)
