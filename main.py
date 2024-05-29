import random
print ("Vítej ve hře Chicago! Pokud chcete začít hrát, napište do konzole zacit. Budete-li chtít hru ukončit, napište do konzole konec")
zacit = input()
def hod_kostkou():
    return random.randint(1, 6)
def hraj_hru(jmeno_hrace):
    celkem_body = 0
    for _ in range(3):  # Každý hráč hází třikrát třemi kostkami
        body_kola = 0
        for _ in range(3):  # Třikrát se hází kostkami
            hod_kostky = hod_kostkou()
            if hod_kostky == 1:
                print(f"{jmeno_hrace} hodil 1, získává 100 bodů")
                body_kola += 100
            elif hod_kostky == 6:
                print(f"{jmeno_hrace} hodil 6, získává 60 bodů")
                body_kola += 60
            else:
                print(f"{jmeno_hrace} hodil {hod_kostky}, získává {hod_kostky} bodů")
                body_kola += hod_kostky

        print(f"{jmeno_hrace} získal {body_kola} bodů v tomto kole")
        celkem_body += body_kola
    return celkem_body
def main():
    body_hrace1 = hraj_hru("Hráč 1")
    body_hrace2 = hraj_hru("Hráč 2")
    if body_hrace1 > body_hrace2:
        print("Hráč 1 vyhrál s", body_hrace1, "body!")
    elif body_hrace2 > body_hrace1:
        print("Hráč 2 vyhrál s", body_hrace2, "body!")
    else:
        print("Remíza!")
main()
print("Děkuji za hru!")


      