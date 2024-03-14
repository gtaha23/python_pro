isim = input("İsminizi lütfen giriniz :")

sifre = int(input("Lütfen şifreyi giriniz :"))

isim_dogrula = input("Doğrulamak için isminizi tekrar giriniz :")

sifre_dogrula = int(input("Doğrulamak için şifrenizi tekrar giriniz :"))

hata = "sanırım bir hata var :( tekrar denemek için baştan başlat"

if isim_dogrula == isim:
    print("Doğrulandı!")

else:
    print(hata)    

if sifre_dogrula == sifre:
    print("Doğrulandı!")

else:
    print(hata)

if isim_dogrula == isim and sifre_dogrula == sifre:
    print("Hesabınız başarıyla oluşturuldu!")

else:
    print(hata)
