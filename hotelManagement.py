from unicodedata import name
import sqlite3



class hotelmanage:

    try:
        musteriler =  sqlite3.connect("C:/Users/rozer/OneDrive/Masaüstü/musteriler.db")
        cursor = musteriler.cursor()
        print("Successfully Connected to SQLite")
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)

    

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1000,name='',yas='',cindate='',coutdate='',rno=1):

        print ("\n\n*****HOTEL LUNA HOŞGELDİNİZ*****\n")

        self.rt=rt
        self.r=r
        self.t=t
        self.p=p
        self.s=s
        self.a=a
        self.name=name
        self.yas=yas
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
    
    def inputdata(self):
        musteriler_dict = {}
        musteri_oda_dict = {}
        
        #self.name=input("\nTam adınızı giriniz:")
        try:
            name = input("\nTam adınızı giriniz:")
        except:
            print("\nGeçersiz değer girdiniz!")
        else:
            if name.isnumeric():
                print("İsim harflerden oluşmalıdır.")
            else:
                self.name = name
                
        
        #self.yas=input("\nYaşınızı giriniz:")
        try:
            yas = int(input("\nYaşınızı giriniz:"))
        except:
            print("\nGeçersiz değer girdiniz!")
        else:
            if yas < 1:
                print("Bir yaşından küçük olamazsınız.")
            else:
                musteriler_dict[name]= yas
                self.yas= yas


        
        self.cindate=input("\nGiriş tarihini giriniz:")
        self.coutdate=input("\nÇıkış tarihini giriniz:")
        print("Oda numaranız:",self.rno,"\n")
        musteri_oda_dict[name]= self.rno

        
    def odaKirala(self):

        print ("Sizin için şu odalarımız var:-")

        print ("1.  Class A----4000")

        print ("2.  Class B----3000")

        print ("3.  Class C----2000")

        print ("4.  Class D----1000")

        x=int(input("Lütfen seçeneğinizi giriniz:"))

        #n=int(input("Kaç gece kalacaksınız:"))

        try:
            gece=int(input("Kaç gece kalacaksınız:"))
        except:
            print("\nGeçersiz değer girdiniz!")
        else:
            if gece<1:
                print("Bir geceden az kalamazsınız!")
            else:
                n = gece

        if(x==1):

            print ("Class A'yı seçtiniz...")

            self.s=4000*n

        elif (x==2):

            print ("Class B'yi seçtiniz...")

            self.s=3000*n

        elif (x==3):

            print ("Class C'yi seçtiniz...")

            self.s=2000*n

        elif (x==4):
            print ("Class D'yi seçtiniz...")

            self.s=1000*n

        else:

            print ("Lütfen bir Class seçiniz...")

        print ("Seçtiğiniz oda ücreti =",self.s,"TL\n")
        self.s = self.s

       # devam = input("Devam etmek istiyor musunuz? e/h\n")
       # if(devam == 'e'):
       #     main()
      #  else:
       #     quit()
       
    def yiyecekHesapla(self):

        print("*****RESTAURANT MENU*****")

        yemekList = ["1.Tatlı---100TL", "2.İçecek---50TL","3.Kahvaltı---90TL", "4.Öğle Yemeği---110TL", "5.Akşam Yemeği---150TL", "6. Çıkış"]
        for i in yemekList:
            print(i)


        while (1):

            c=int(input("Seçeneğinizi giriniz:"))


            if (c==1):
                d=int(input("Miktarı girin:"))
                self.r=self.r+100*d

            elif (c==2):
                 d=int(input("Miktarı girin:"))
                 self.r=self.r+50*d

            elif (c==3):
                 d=int(input("Miktarı girin:"))
                 self.r=self.r+90*d

            elif (c==4):
                 d=int(input("Miktarı girin:"))
                 self.r=self.r+110*d

            elif (c==5):
                 d=int(input("Miktarı girin:"))
                 self.r=self.r+150*d

            elif (c==6):
                break;
            else:
                print("You've Enter an Invalid Key")

        print ("Total food Cost=Rs",self.r,"\n")

        


    def display(self):
        print ()
        print ("******OTEL FATURASI******")
        print ()
        print ("Müşteri adı:",self.name)
        print ("Müşteri yaşı:",self.yas)
        print ("Giriş tarihi:",self.cindate)
        print ("Çıkış tarihi",self.coutdate)
        print ("Oda numarası",self.rno)
        print ("Oda ücretiniz:",self.s,"TL")
        print ("Yemek ücretiniz:",self.r,"TL")

        self.rt=self.s+self.t+self.p+self.r

        print ("Ham fiyat(yemek+oda):",self.rt,"TL")
        print ("Ek servis ücreti:",self.a,"TL")
        print ("Ödemeniz gereken toplam ücret:",self.rt+self.a,"TL\n")
        self.rno+=1

        

        add_to_Tasks_table = "INSERT INTO musteriler (musteri_isim, musteri_yas, musteri_oda, musteri_totalPrice) values (?, ?, ?, ?)"
        self.cursor.execute(add_to_Tasks_table, (self.name, self.yas, self.rno, self.rt))
        self.musteriler.commit()
    
        
    def gunSonuRaporu(self):
        
        print ("\n\n*****HOTEL LUNA GÜN SONU RAPORU*****\n")

        musteriler =  sqlite3.connect("C:/Users/rozer/OneDrive/Masaüstü/musteriler.db")
        cursor = musteriler.cursor()
        cursor.execute("Select * from musteriler")
        
       
        rows = cursor.fetchall()
        total = sum([row[3] for row in rows])

        cursor.execute('SELECT COUNT(*) from musteriler')
        cur_result = cursor.fetchone()

        kisi_sayisi = len(rows)

        print("Toplam kişi sayısı: ",kisi_sayisi)
        print("Gün sonu toplam kazanç: ",total)
        print()

def main():

    a=hotelmanage()
    

    while (1):
        print("1.Müşteri Bilgisini Girin")
        
        print("2.Oda Kirasını Hesapla")

        print("3.Satın Alınan Yemekleri Hesapla")

        print("4.Toplam Ücreti Hesapla")

        print("5.Gün Sonu Raporu")

        print("6. ÇIKIŞ")

        b=int(input("\nSEÇENEĞİNİZİ GİRİNİZ:"))
        
        if (b==1):
            a.inputdata()

        if (b==2):

            a.odaKirala()

        if (b==3):

            a.yiyecekHesapla()

        if (b==4):

            a.display()
        
        if (b==5):

            a.gunSonuRaporu()

        if (b==6):
            
           
            quit()




main()