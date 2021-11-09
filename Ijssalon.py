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
ToppingKosten = 0
DoorgaanOfNiet = "Ja"
Liters = 0
Liter = 1

def ParticulierOfZakelijk():
    PartOfZak = input('Bent u 1) particulier of 2) zakelijk?\n---> ')
    if PartOfZak == "1":
        Welkom(Aantal_Bolletjes)
    elif PartOfZak == "2":
        WelkomZakelijk(Liters)

def WelkomZakelijk(Liters):
    Liters = int(input('Hoeveel liter wilt u hebben?'))
    LiterSmaak(Liter,Aardbei,Chocolade,Munt,Vanille,Liters)

def LiterSmaak(Liter,Aardbei,Chocolade,Munt,Vanille,Liters):
    AantalLiters = Liters
    while AantalLiters >=1:
        SmaakBol = input('Welke smaak wilt u voor de '+str(Liter)+'e liter? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?\n---> ')
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
        AantalLiters = AantalLiters - 1
    print('Oke, u heeft dus de smaken:\n--------------\n'+str(Aardbei)+'x Aardbei\n'+str(Chocolade)+'x Chocolade\n'+str(Munt)+'x Munt\n'+str(Vanille)+'x Vanille\n--------------')
    Doorgaan = input('Wilt u een bonnetje? (Ja/Nee)\n---> ')
    if Doorgaan == "Ja":
        BonnetjeZakelijk(Liters)

def BonnetjeZakelijk(Liters):
    btw = 9
    PrijsLiters = Liters * 9.80
    Totaal = PrijsLiters + btw
    btw = PrijsLiters / 100 * 9
    print('------------[ Papi Gelato ]------------')
    print(' ')
    print("Liter('s)       "+str(Liters)+' x 9.80         = '+"{:.2f}".format(PrijsLiters))
    print('                                 ----- +')
    print("BTW 9%                           = "+"{:.2f}".format(btw))
    print('Totaal                           = '+"{:.2f}".format(Totaal))
    print('---------------------------------------')

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
        Toppings(Aantal_Bolletjes,ToppingKosten,DoorgaanOfNiet,Hoorntje,Bakje)

    elif Aantal_Bolletjes <=8:
        print('Dan krijgt u van mij een bakje met '+ str(Aantal_Bolletjes)+' bolletjes')
        Bakje = Bakje + 1
        Toppings(Aantal_Bolletjes,ToppingKosten,DoorgaanOfNiet,Hoorntje,Bakje)
        
    else:
        print('Sorry, zulke grote bakken hebben we niet')
        AantalBolletjes(Aantal_Bolletjes)


def Toppings(Aantal_Bolletjes,ToppingKosten,DoorgaanOfNiet,Hoorntje,Bakje):
    WelOfGeenTopping = input('Wilt u een topping?(Ja/Nee)\n---> ')
    if WelOfGeenTopping == "Ja":
        while DoorgaanOfNiet == "Ja":
            Topping = input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?\n---> ')
            if Topping == "A":
                ToppingKosten = ToppingKosten + 0
                Uitslag(Aantal_Bolletjes,Hoorntje,Bakje)
            elif Topping == "B":
                ToppingKosten = ToppingKosten + 0.50
            elif Topping == "C":
                AantalSprinkelBollen = int(input('Op hoeveel bolletjes van de '+str(Aantal_Bolletjes)+' bollen wilt u de sprinkel topping?\n---> '))
                ToppingKosten = ToppingKosten + AantalSprinkelBollen * 0.30
            elif Topping == "D":
                if Hoorntje == 1:
                    ToppingKosten = ToppingKosten + 0.60
                else:
                    ToppingKosten = ToppingKosten + 0.90
            else:
                print("Sorry dat snap ik niet...")
                Toppings(Aantal_Bolletjes,ToppingKosten,DoorgaanOfNiet,Hoorntje,Bakje)
            DoorgaanOfNiet = input('Wilt u nog een topping? (Ja/Nee)\n---> ')
    

    Uitslag(Aantal_Bolletjes,Hoorntje,Bakje,ToppingKosten)

def Uitslag(Aantal_Bolletjes,Hoorntje,Bakje,ToppingKosten):
    print('Hier is uw '+str(BakjeOfHoorntje)+ ' met '+str(Aantal_Bolletjes)+' bolletje(s).')
    Bonnetje(Aantal_Bolletjes,Hoorntje,Bakje,ToppingKosten)
    
def MeerOfNietBestellen(Aantal_Bolletjes):
    NogIets = input('Wilt u nog meer bestellen?\n---> ')
    if NogIets == "Ja":
        AantalBolletjes(Aantal_Bolletjes)
    elif NogIets =="Nee":
        print('Bedankt en tot ziens!')
    else:
        print('Sorry dat snap ik niet...')
        MeerOfNietBestellen(Aantal_Bolletjes)

def Bonnetje(Aantal_Bolletjes,Hoorntje,Bakje,ToppingKosten):
    PrijsBolletjes = Aantal_Bolletjes*1.10
    PrijsHorrentje = Hoorntje*1.25
    PrijsBakje = Bakje*0.75
    Totaal = PrijsBolletjes + PrijsHorrentje + PrijsBakje + ToppingKosten
    print('------------[ Papi Gelato ]------------')
    print(' ')
    print("Bolletje('s)       "+str(Aantal_Bolletjes)+' x 1,10       = '+"{:.2f}".format(PrijsBolletjes))
    if Hoorntje == 1:
        print("Horrentje('s)   "+str(PrijsHorrentje)+' x 1,25       = '+"{:.2f}".format(PrijsHorrentje))
    if Bakje == 1:
        print("Bakje('s)       "+str(PrijsBakje)+' x 0,75       =  '+"{:.2f}".format(PrijsBakje))
    if ToppingKosten !=0:
        print("Topping('s)"'                        = ' +"{:.2f}".format(ToppingKosten))
    print('                                 ----- +')
    print('Totaal                           = '+"{:.2f}".format(Totaal))
    print('---------------------------------------')
    MeerOfNietBestellen(Aantal_Bolletjes)

ParticulierOfZakelijk()
