print("Bu programda Metropoll Araştırma Şirketi'nin 2019 yılının başından itibaren "
      "yapmış olduğu siyasi araştırmaların verileri kullanılmıştır. 24 Haziran 2018 "
      "seçimlerinde yarışan partiler isimleri ile diğer partiler ise 'diğer' ismi altında "
      "kendisine yer bulmuştur. Kararsızların aritmatik dağılımı yanlış çıkarımlara sebep "
      "olacağından'kararsızlar' olarak ayrı bir isimle tasnif edilmiştir. Bu program ile 5 "
      "partinin, diğerlerinin ve kararsızların bir önceki aya göre düşüş yaşadığı zaman dilimleri "
      "ile 24 ankette kaç defa düşüş yaşadığını tespit etme imkanınız olacaktır.")
#Sorumlu olduğumuz konular arasında fonksiyonlar bulunmuyordu. Ancak bir sonraki konu buydu.
# Araştırdım ve kullanmaya çalıştım. Temel seviyede öğrendim diyebiliirim.

def calculate_akp_votes():
#Videolardan tüm her şeyi yazmak yerine kaynak dosyadan alıp kullanmayı öğrendim.
#Anket verilerini .txt uzantılı dosyalara yazdım ve bu kaynak dosyaları size de gönderdim.
    akp = open("akp.txt", "r").read()
#Veriler 'ay - yıl,oran' şeklinde olduğundan ve ölçüm oy oranı üzerinden yapılacağından bunları ayırdım.
    akplist = akp.splitlines()
    counter = 0
#For döngüsünü kullanmaya çalıştım.
    for i in range(len(akplist) - 1):
        if akplist[i].split(",")[1] < akplist[i + 1].split(",")[1]:
            print(akplist[i + 1].split(",")[0] + " anketi: " + akplist[i + 1].split(",")[1])
            counter += 1
    print("Toplam Anket Sayısı:", len(akplist))
    print("Bir Önceki Aya Göre Düşüş Yaşadığı Anket Sayısı:", counter)
#Yukarıda yapmış olduğum tüm açıklamalar tüm girdiler için geçerli. AKP için bunu yaptıktan sonra kopyalayıp yazdım.
def calculate_chp_votes():
    chp = open("chp.txt", "r").read()
    chplist = chp.splitlines()
    counter = 0
    for i in range(len(chplist) - 1):
        if chplist[i].split(",")[1] < chplist[i + 1].split(",")[1]:
            print(chplist[i + 1].split(",")[0] + " anketi: " + chplist[i + 1].split(",")[1])
            counter += 1
    print("Toplam Anket Sayısı:", len(chplist))
    print("Bir Önceki Aya Göre Düşüş Yaşadığı Anket Sayısı:", counter)


def calculate_iyi_votes():
    iyi = open("iyi.txt", "r").read()
    iyilist = iyi.splitlines()
    counter = 0
    for i in range(len(iyilist) - 1):
        if iyilist[i].split(",")[1] < iyilist[i + 1].split(",")[1]:
            print(iyilist[i + 1].split(",")[0] + " anketi: " + iyilist[i + 1].split(",")[1])
            counter += 1
    print("Toplam Anket Sayısı:", len(iyilist))
    print("Bir Önceki Aya Göre Düşüş Yaşadığı Anket Sayısı:", counter)


def calculate_hdp_votes():
    hdp = open("hdp.txt", "r").read()
    hdplist = hdp.splitlines()
    counter = 0
    for i in range(len(hdplist) - 1):
        if hdplist[i].split(",")[1] < hdplist[i + 1].split(",")[1]:
            print(hdplist[i + 1].split(",")[0] + " anketi: " + hdplist[i + 1].split(",")[1])
            counter += 1
    print("Toplam Anket Sayısı:", len(hdplist))
    print("Bir Önceki Aya Göre Düşüş Yaşadığı Anket Sayısı:", counter)


def calculate_mhp_votes():
    mhp = open("mhp.txt", "r").read()
    mhplist = mhp.splitlines()
    counter = 0
    for i in range(len(mhplist) - 1):

        if mhplist[i].split(",")[1] < mhplist[i + 1].split(",")[1]:
            print(mhplist[i + 1].split(",")[0] + " anketi: " + mhplist[i + 1].split(",")[1])
            counter += 1
    print("Toplam Anket Sayısı:", len(mhplist))
    print("Bir Önceki Aya Göre Düşüş Yaşadığı Anket Sayısı:", counter)


def calculate_diger_votes():
    diger = open("diger.txt", "r").read()
    digerlist = diger.splitlines()
    counter = 0
    for i in range(len(digerlist) - 1):
        if digerlist[i].split(",")[1] < digerlist[i + 1].split(",")[1]:
            print(digerlist[i + 1].split(",")[0] + " anketi: " + digerlist[i + 1].split(",")[1])
            counter += 1
    print("Toplam Anket Sayısı:", len(digerlist))
    print("Bir Önceki Aya Göre Düşüş Yaşadığı Anket Sayısı:", counter)


def calculate_kararsizlar_votes():
    kararsizlar = open("kararsizlar.txt", "r").read()
    kararsizlarlist = kararsizlar.splitlines()
    counter = 0
    for i in range(len(kararsizlarlist) - 1):
        if kararsizlarlist[i].split(",")[1] < kararsizlarlist[i + 1].split(",")[1]:
            print(kararsizlarlist[i+1].split(",")[0] + " anketi: " + kararsizlarlist[i+1].split(",")[1])
            counter += 1
    print("Toplam Anket Sayısı:", len(kararsizlarlist))
    print("Bir Önceki Aya Göre Düşüş Yaşadığı Anket Sayısı:", counter)

#while döngüsünü kullanarak işlemi tekrarlama imkanı oluşturdum.
#lowercase sayesinde isimlerin hatalı girilmesini minimuma indirmek istedim.
# Çünkü ben bile isimleri her zaman doğru giremedim. Büyük-küçük harf sorunu nedeni ile.
# Bir de halk farklı isimler kullanıyor her parti için imkanı genişletmek istedim.
while True:
    value = input("Parti İsmi Giriniz (Desteklenen AKP, CHP, IYI, HDP, MHP, DIGER ve KARARSIZLAR): ")
    if value.lower() == "akp" or value.lower() == "ak parti":
        calculate_akp_votes()
    elif value.lower() == "chp":
        calculate_chp_votes()
    elif value.lower() == "IYI" or value.lower() == "iyi" or value.lower() == "iyi parti":
        calculate_iyi_votes()
    elif value.lower() == "hdp":
        calculate_hdp_votes()
    elif value.lower() == "mhp":
        calculate_mhp_votes()
    elif value.lower() == "diger":
        calculate_diger_votes()
    elif value.lower() == "kararsızlar":
        calculate_kararsizlar_votes()
    else:
        print("Yanlis giris yaptiniz. Lutfen tekrar deneyiniz")
#Projenin fikri https://adventofcode.com/2021/day/1 linkinde bulunan Day 1'in ilk bölümünü yapmaya çalışırken geldi.
# Ordaki sorunun çözümünü araştırırken nasıl bunu yapacağımı da öğrendim.