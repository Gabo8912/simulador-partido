import random

def partido(turno_actual,marcador_chivas,marcador_atlas):
    action = random.randint(1,250)
    if 1 <= action <= 50:
        print("Shot from the wide area by the team: " + turno_actual)
    elif 51 <= action <= 100:
        print("Shoot from: " + turno_actual +" and the gooalkeeper of the rival team saves it.")
    elif 101 <= action <= 150:
        print("Goaaaal! from team " + turno_actual)
        if turno_actual=="Chivas":
            marcador_chivas=marcador_chivas+1
        else:
            marcador_atlas=marcador_atlas+1
    elif 151 <= action <= 200:
        print("Penalty Goaaal! form team " + turno_actual)
        if turno_actual=="Chivas":
            marcador_chivas=marcador_chivas+1
        else:
            marcador_atlas=marcador_atlas+1
    elif 201 <= action <= 250:
        print("Goaaaal! form team " + turno_actual +" by kick!")
        if turno_actual=="Chivas":
            marcador_chivas=marcador_chivas+1
        else:
            marcador_atlas=marcador_atlas+1
    
    return marcador_chivas,marcador_atlas


marcador_chivas=0
marcador_atlas=0
turno_actual=("Chivas")

for i in range(1,91):
     marcador_chivas, marcador_atlas = partido(turno_actual, marcador_chivas, marcador_atlas)

     if turno_actual=="Chivas":
         turno_actual ="Atlas"
     else:
        turno_actual="Chivas"

print("Resultado del partido es: \n Chivas: "+ str(marcador_chivas) + " Atlas: " + str(marcador_atlas))

