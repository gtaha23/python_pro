meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "SHEESH": "onaylamamak",
            "CREEPY": "korkunç",
            }
            
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print(word,"kelimesinin anlamı",meme_dict[word])
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print(word,"kelimesinin anlamı bulunamadı.")
