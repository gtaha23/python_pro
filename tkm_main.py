import time
import random

seninPuanin = 0
bilgisayarPuani = 0
while True:
    secenek = input("Birisini seç: taş, kağıt, makas:")
    if secenek == "taş" or secenek =="kağıt" or secenek=="makas":
        bilgisayar = random.randint(1,3)
        if bilgisayar == 1:
            bilgisayar = "taş"
            print("bilgisayar taşı seçti")
        elif bilgisayar == 2:
            bilgisayar = "kağıt"
            print("bilgisayar kağıdı seçti")
        elif bilgisayar == 3:
            bilgisayar = "makas"
            print("bilgisayar makası seçti")
        if bilgisayar == secenek:
            print("Berabere kaldınız")
        elif (bilgisayar == "taş" and secenek =="kağıt") or (bilgisayar =="kağıt" and secenek=="makas") or (bilgisayar=="makas" and secenek=="taş"): 
            print("Siz kazandınız")
            seninPuanin += 1
        else:
            print("Bilgisayar kazandı")
            bilgisayarPuani += 1
        print("Bilgisayar puanı:", bilgisayarPuani, "Senin puanın:", seninPuanin)
        time.sleep(1)
    else:
        print("Seçimde hata var")
