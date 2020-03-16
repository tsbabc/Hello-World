import requests
import os
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}
basis_url="https://www.znlzd.com/ar.php?KeyWord="
KeyWorld=str(input("欢迎使用本小说下载器，请输入正确的小说名:"))
res=requests.get(url=basis_url+KeyWorld,headers=headers)
soup1=BeautifulSoup(res.content.decode("utf-8","ignore"),"lxml")

ur=soup1.find_all("div", class_="layout layout2 layout-co18")


soup2=BeautifulSoup(str(ur[0].ul),"lxml")


li_list=soup2.find_all("li")
m=len(li_list)
for i in range(1,m):
    soup3=BeautifulSoup(str(li_list[i]),"lxml")
    url=soup3.find_all("a")[0]["href"]
    url="https://www.znlzd.com"+url
    #print(url)
    res=requests.get(url,headers=headers)
    soup4=BeautifulSoup(res.content.decode("utf-8","ignore"),"lxml")
    des=soup4.find_all("div",class_="m-desc xs-show")[0].get_text()
    print(des)
    div=soup4.find_all("div",class_="section-box")[1]
    soup5=BeautifulSoup(str(div.ul),"lxml")
    url_list=soup5.find_all("a")
    try:
        if KeyWorld in os.listdir():
            os.remove(KeyWorld)
    except:
        print("Error!")
    os.makedirs(KeyWorld)
    os.chdir(KeyWorld)
    for item in url_list:

        
        url1=url+item['href']
        #print(url1)
        title=item.string
        if title[-1]=='?':
            title=title[:-1]
        res2=requests.get(url1,headers=headers)
        soup6=BeautifulSoup(res2.content.decode("utf-8","ignore"),"lxml")
        con=soup6.find(id="content").get_text()
        with open ("{}.txt".format(title),"w",encoding="utf-8") as f:
    	    f.write(con)
    try:
        KeyWorld.sort(Key=lambda x:os.path.getctime(x))
    except:
        print("Error!!!")




