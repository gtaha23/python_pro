import random

sifre = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

son_sifre = ""

sayi = int(input("kaç defa tekrar etsin :"))

for i in range(sayi):
    son_sifre += random.choice(sifre)

print(son_sifre)
