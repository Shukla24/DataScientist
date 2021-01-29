#for link
from bs4 import BeautifulSoup
import requests
num=42309
for i in range(1,31):
    url="https://timesofindia.indiatimes.com/2015/11/{0}/archivelist/year-2015,month-11,starttime-{1}.cms".format(i,num)
    print(url)
    #a=a+int(i)
    r = requests.get(url)
    #time.sleep()
    #print(r)
    soup = BeautifulSoup(r.text, 'lxml')
    a=soup.select(".cnt table tr td a")
    for j,k in enumerate(a):
        try:
                
        #print(j,k["href"],sep="========")
            with open("data50link.csv","a",encoding="utf-8") as f:
                f.write(k["href"]+"\n")
        except Exception as e: #base class
            print(e)
            

    #time.sleep(10)
    num+=1
   
  
