import re
from flashtext import KeywordProcessor
keyword_processor = KeywordProcessor()


def convert_list_to_string(org_list, seperator=' '):
   
    return seperator.join(org_list)


metinler = ['ne', 'zaman']# bu şuan sadece "ne zaman" ile sorulan sorulara cevap verebiliyor
#kaynak:https://python.yemreak.com/temel/string-islemleri



soru = input("sorunu sor:")
# ne zaman sorusuna cevap

if(all(metin in soru for metin in metinler)):#sorulan soruda ne zaman yerine cevap olabilecek kelimeleri değiştiriyor

    string1 ="tarihleri arasında"
    result1 = re.sub(r"ne zaman", string1, soru)#stringlerde replace metodu da olabilir
    #kaynak:https://stackabuse.com/using-regex-for-text-manipulation-in-python/

        
if(all(metin in soru for metin in metinler)):

    string2="tarihinde"
    result2 = re.sub(r"ne zaman", string2, soru)


if(all(metin in soru for metin in metinler)):

    string3="saatlerinde"
    result2 = re.sub(r"ne zaman", string3, soru)


# bulunabiliecek ifademiz
#print(result1)
#print(result2)


liste=result1.split(string1)
stringifade1 =convert_list_to_string(liste)# burada split ettiğimiz liste değişkenini stringe çevirdik
#şuan stringifade1 kullanılmıyor ama ilerde kullanılacak
#kaynak:https://thispointer.com/python-how-to-convert-a-list-to-string/#:~:text=Convert%20list%20to%20string%20in%20python%20using%20join()%20in,a%20function%20join()%20i.e.&text=join()%20function%20accepts%20an,it%20returns%20the%20concatenated%20string.



#text değişkenini girilen internet sitesinin metinleri olacak
text = "Hafta sonu 10.00-17.00 saatlerinde 1998 açık olan bakkal, market, kasap, manav ve kuru yemişçi ile şehirler arası seyaına dair usul r 23 Nisan Cuma günü de birebir uygulanacak."

if re.search(string1, text):#kaynak:https://stackabuse.com/using-regex-for-text-manipulation-in-python/
    print("Match found")
else:
    print("Match not found")

if re.search(string2, text):
    print("Match found")
else:
    print("Match not found")

if re.search(string3, text):
    print("Match found")
else:
    print("Match not found")


keyword_processor.add_keyword(string3)
keywords_found = keyword_processor.extract_keywords(text, span_info=True)
#kaynak:https://flashtext.readthedocs.io/en/latest/

aralık=keywords_found[0]
olasıaralık=aralık[1]-20

print(text[olasıaralık:aralık[2]])# bu kısım soru  zarfına cevap olabilecek aralığı çıktı olarak veriyor
