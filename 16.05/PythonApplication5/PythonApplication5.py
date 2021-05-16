from flask import Flask, render_template, request
import re
import requests
from bs4 import BeautifulSoup
from flashtext import KeywordProcessor
from googlesearch import search




app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/', methods=['POST'])




def getvalue():
    name=request.form['name']
    
    #path="C:/Users/berk/Desktop/PROJE/metin.txt"
    #dosya = open(path, 'a')
    #dosya.write(name)
    #dosya.write("\n")
    #dosya.close()
    

    def main(name):
        keyword_processor = KeywordProcessor()


        def convert_list_to_string(org_list, seperator=' '):
   
            return seperator.join(org_list)


        metinler = ['ne', 'zaman']# bu şuan sadece "ne zaman" ile sorulan sorulara cevap verebiliyor
        #kaynak:https://python.yemreak.com/temel/string-islemleri

        g =requests.get("https://www.google.com/")
        gugıl = BeautifulSoup(g.content)
        print(gugıl.find_all("gLFyf gsfi"))


        soru = name# girilen string ifadeyi google da aratıyor
        # ne zaman sorusuna cevap
        #-------------------------------------------------------------------------------------------------------------------------------------------------------
        if(all(metin in soru for metin in metinler)):#sorulan soruda ne zaman yerine cevap olabilecek kelimeleri değiştiriyor

            tarihleriarasında ="tarihleri arasında"
            result1 = re.sub(r"ne zaman", tarihleriarasında, soru)#stringlerde replace metodu da olabilir
            #kaynak:https://stackabuse.com/using-regex-for-text-manipulation-in-python/

        if(all(metin in soru for metin in metinler)):

            tarihinde="tarihinde"
            result2 = re.sub(r"ne zaman", tarihinde, soru)
            #DÜZENLENECEK

        if(all(metin in soru for metin in metinler)):

            saatlerinde="saatlerinde"
            result2 = re.sub(r"ne zaman", saatlerinde, soru)
            #DÜZENLENECEK
        if(all(metin in soru for metin in metinler)):
    
            saatleriarasında="saatleri arasında"
            result2 = re.sub(r"ne zaman", saatleriarasında, soru)
        if(all(metin in soru for metin in metinler)):
    
            kadardevamedecek="kadar devam edecek"
            result2 = re.sub(r"ne zaman", kadardevamedecek, soru)
        if(all(metin in soru for metin in metinler)):
    
            tarih="tarih"
            result2 = re.sub(r"ne zaman", tarih, soru)
            #DÜZENLENECEK

        # bulunabiliecek ifademiz
        #print(result1)
        #print(result2)

        #-------------------------------------------------------------------------------------------------------------------------------------------------------
        #try:
        #    liste=result1.split(tarihleriarasında) #DÜZENLENECEK
        #    stringifade1 =convert_list_to_string(liste)# burada split ettiğimiz liste değişkenini stringe çevirdik
        #except:
        #    print("bu ifade bulunamıyor")
        ##şuan stringifade1 kullanılmıyor ama ilerde kullanılacak
        ##kaynak:https://thispointer.com/python-how-to-convert-a-list-to-string/#:~:text=Convert%20list%20to%20string%20in%20python%20using%20join()%20in,a%20function%20join()%20i.e.&text=join()%20function%20accepts%20an,it%20returns%20the%20concatenated%20string.


        #ilerde url kısmını otomatik olarak alacağız (RPA ile çözülebilir)
        for j in search(soru, tld="co.in", num=10, stop=1, pause=2):
            url=j#burada en başta sorulan soru sonucunda gelen ilk urlyi aldım
            #kaynak:https://www.geeksforgeeks.org/performing-google-search-using-python-code/

        r= requests.get(url)

        #r= requests.get("https://www.hurriyet.com.tr/galeri-hafta-sonu-sokaga-cikma-yasagi-ne-zaman-saat-kacta-bitiyor-23-25-nisan-sokaga-cikma-yasagi-saatleri-41795118/3")
        r.content
        # kaynak:https://docs.python-requests.org/en/master/
        soup=BeautifulSoup(r.content)
        soup.prettify()#burada web sitesinden aldığımız verileri düzenliyoruz ama çok gerek yok
        textamastringdegil=soup.find_all()#tüm siteyi taradı
        #kaynak:https://www.crummy.com/software/BeautifulSoup/bs4/doc/
        text=str(textamastringdegil)# ve text değişkenine koyduk

        #-------------------------------------------------------------------------------------------------------------------------------------------------------
        if re.search(tarihleriarasında, text):#kaynak:https://stackabuse.com/using-regex-for-text-manipulation-in-python/
            print("Match found")
        else:
            print("Match not found")

        if re.search(tarihinde, text):
            print("Match found")
        else:
            print("Match not found")

        if re.search(saatlerinde, text):
            print("Match found")
        else:
            print("Match not found")

        if re.search(saatleriarasında, text):
            print("Match found")
        else:
            print("Match not found")
        if re.search(kadardevamedecek, text):
            print("Match found")
        else:
            print("Match not found")
        if re.search(tarih, text):
            print("Match found")
        else:
            print("Match not found")

        #-------------------------------------------------------------------------------------------------------------------------------------------------------
        nezamanakarsilik=[tarihleriarasında,tarihinde,saatlerinde,saatleriarasında,kadardevamedecek,tarih]
        liste =[]
        for x in nezamanakarsilik:
            keyword_processor.add_keyword(x)#string 3 ü textin içinde arıyor ve bulduğu zaman belli bir aralığı veriyor
            keywords_found = keyword_processor.extract_keywords(text, span_info=True)
            #kaynak:https://flashtext.readthedocs.io/en/latest/

            try:
                aralık=keywords_found[0]# try ex k
                print(text[(aralık[1]-34):aralık[2]])# bu kısım soru  zarfına cevap olabilecek aralığı çıktı olarak veriyor
                print(str(aralık[1]))
                print(str(aralık[2]))
                son=text[(aralık[1]-40):(aralık[2]+50)]
                liste.append(son)
                # son olarak soruya cevap olabilecek sayırları verdi
            except IndexError:
                print(x+"-> bu kelime internet sitesinde yer almıyor")
                son ="-> bu kelime internet sitesinde yer almıyor"
        yazdır=""
        for x in liste:
            yazdır += x
            yazdır += "---------------------------------------------------------"
        print(yazdır)
        return yazdır

    print(main(name))
    txt=main(name)
    #path="C:/Users/berk/Desktop/PROJE/metin.txt"
    #dosya=open(path,"r")
    #for satir in dosya :
    #   text=satir
    #dosya.close()
    #print("bunu google aratıcaz:",text)
    #yaz=main(text)
    #print("google da aratıldı ve sonuc",yaz)


    #bunu başka bir text dosyasına yazıcaz ve onu passa veri yazan yer okuyacak
    #pathiki="C:/Users/berk/Desktop/PROJE/text.txt"
    #dosyaiki=open(pathiki,"a")
    #dosyaiki.write(yaz)
    #ddosyaiki.write("\n")
    #dosyaiki.close()
        
    


    #doyadan çıktıyı okuyucaz buraya yazıcaz
    #pathiki="C:/Users/berk/Desktop/PROJE/text.txt"
    #dosyaiki=open(pathiki,"r")
    #for satir in dosyaiki :
    #     text=satir
    return render_template('pass.html', n=txt)


if __name__ == '__main__':
    app.run(debug=True)

