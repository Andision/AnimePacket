from threading import Thread
import requests
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-mode', required=False, default='list',  help='')
parser.add_argument('-d', required=False, default='./',  help='')
args = parser.parse_args()

url_prefix = "http://www.yhdm.io"

if args.mode == "list":
    url = input()
    conn = requests.get(url)
    conn.encoding='UTF-8'

    if conn.status_code == 200:
        soup = BeautifulSoup(conn.text,"html.parser")
        a = soup.find(name='div',id = 'main0')
        
        t = soup.find('div',{"class": "rate r"})
        t=t.h1.text
        print(t)

        pagelist_text = BeautifulSoup(str(a),"html.parser")
        b = pagelist_text.find_all("a", {"target": "_blank"})

        f=open(args.d+t+'.dpl',"w+",encoding='utf-8')
        f.write("DAUMPLAYLIST\nplayname="+t+"\nplaytime=0\ntopindex=0\nsaveplaypos=0\n")
        j=0
        for i in b:
            j+=1
            print(i.text,i['href'])

            url2 = url_prefix + i['href']
            conn2 = requests.get(url2)
            conn2.encoding='UTF-8'
            if conn2.status_code == 200:
                soup2 = BeautifulSoup(conn2.text,"html.parser")
                a2 = soup2.find(name='div',id = 'playbox')
                dow_url = a2['data-vid'].split('$')[0]
                print(dow_url,j)
                f.write(str(j)+"*file*"+dow_url+'\n'+str(j)+"*title*"+str(i.text)+'\n'+str(j)+"*played*0\n")
            else:
                print(url2 + "ERROR!")
        f.close()




    else:
        print('ERROR')