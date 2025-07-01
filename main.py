internet_sozluk={
    "LOL" : "Gülmek",
    "AFK" : "Bilgisayardan uzak",
    "TDK" : "Türk dil kurumu"
}
while True:
    word = input("Bilemediğiniz kelimeleri yazınız:")
    if word in internet_sozluk.keys():
        print(internet_sozluk[word])
    else:
        print("Bu bu kelime sözlükte bulunamadı")

