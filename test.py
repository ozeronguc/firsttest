#print("Baaşarı ile giriş yaptınız! Hoş geldiniz", "Özer " + "Öngüç!")


#test satırı ekledim. 


#myName = "  Sertaç      "
#print(myName.strip())


username = input("İsminizi girin ")
surname = input("Soy isminizi girin ")
password = input("Şifrenizi oluşturun ")
year = int(input("Yaşınızı girin "))

if year >= 18:
    print("Hesabınız başarı ile oluşturuldu! ")

else:
    print("Yaşınız hesap oluşturmak için yetmiyor.")

kalan_hak = 3

while kalan_hak > 0 and year >= 18:
    name = input("İsminizi girin ")
    pw = input("Şifrenizi girin ")
    

    if username == name and password == pw:
        print("Baaşarı ile giriş yaptınız! Hoş geldiniz", username, surname+"!")
        #print("Baaşarı ile giriş yaptınız! Hoş geldiniz", username, surname.strip(),"!")
        break
    
    else:
        kalan_hak = kalan_hak -1
        print("Giriş başarısız. Kalan hakkınız: ", kalan_hak)

    if kalan_hak == 0:
        print("Giriş başarısız bloke edildiniz, kalan hakkınız:", kalan_hak)