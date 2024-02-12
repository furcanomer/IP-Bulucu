import ping3
import os
import socket

global ozet
ozet = []
def ekle(z):
    ozet.append(z)

def genel_hata():
    print("""****************************************************************************
Bir hata ile karşılaştım.
Bu yüzden kendimi yeniden başlattım.
****************************************************************************\n""")
    print("Hata ile karşılaşmadan önce\nağda bulduğum IP'lerin listesi:\n")
    for x in ozet:
            print(x)
    ozet.clear()
    print("\n****************************************************************************\n")

    
GenelHata = 0
while(True):
    os.system("clear") # eğer Windows için derleyecekseniz "cls" olarak değiştirin.
    print("""****************************************************************************
IP Bulucu 1.0
        
https://github.com/furcanomer/IP-Bulucu

****************************************************************************

Ben IP Bulucu programıyım. 192.168 ile başlayan local (yerel) IP'leri tararım.
Tarama işlemi bittikten sonra, bulduğum tüm cihazların
IP'lerini ve -bulabildiysem- isimlerini sana listelerim.
Sadece taramak istediğin Gurup ID'yi girmelisin.
Ben ise belirttiğin gurup ID'deki tüm local (yerel) IP'leri tararım.

****************************************************************************
""")
    if (GenelHata == 1):
        genel_hata()
        GenelHata = 0


    try:
        
        while(True):
            try:
                gurup = int(input("Gurup ID: "))
                if (gurup > 254):
                    print("\nGurup ID, 254'ten büyük olamaz.\nTekrar dene.\n")
                    continue
                elif (gurup < 0):
                    print("\nGurup ID, 0'dan küçük olamaz.\nTekrar dene.\n")
                    continue
                else:
                    break
            except:
                print("\n****************************\nHatalı tuşlama yaptın.\nTekrar dene.\n****************************\n\n")
                continue
        print("\n****************************************************************************\n")

        for i in range(255):
            ip_address = f"192.168.{gurup}.{str(i)}"

            ping_result = ping3.ping(ip_address, timeout=0.5)

            if type((ping_result)) == float:
                try:
                    isim = socket.gethostbyaddr(ip_address)[0]
                    durum = f" - Cihazın ismi: {isim}"
                except socket.herror:
                    durum = ""
                print(ip_address,f"    - Başarılı :) {durum}")
                ekle(ip_address + durum)

            else:
                print(ip_address,"    - YOK")
        
        print("\n***************************\n\nİşlem Tamamlandı.\n\n***************************\n")
        print("Ağdaki IP'lerin listesi:\n")
        for x in ozet:
            print(x)
        ozet.clear()
        bitti = input("\n****************************************************************************\n\nYeniden başlamak istiyorsan (Y)'ye bas ve 'enter' tuşuna bas.\n--> ")
        if bitti == "Y" or bitti == "y":
            continue
        else:
            break
    except:
        GenelHata = 1
        continue
