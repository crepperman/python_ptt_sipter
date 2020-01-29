from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import ssl


class PttParser:
    def __init__(self,url):
        self.url = url

        def OpenConnect(self):
            self.ssl._create_default_https_context = self.ssl._create_unverified_context
            req = self.Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
            ok = 1;
            try:
                self.webpage = self.urlopen(req).read()
            except:
                ok = 0;
            return ok

        def getWebTitle(self):
            return

        #
        def getContentTitle(self):
            return

        #
        def getContent(self):
            return

        def getList(self):

            return


ssl._create_default_https_context = ssl._create_unverified_context
req = Request('https://www.ptt.cc/bbs/Cross_Life/index.html', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
#print(webpage)

soup = BeautifulSoup(webpage,"html.parser")
print(soup.title.string)
#print(soup.find_all("div", {"class": "r-list-container action-bar-margin bbs-screen"}). )
#print(soup.find_all( "div", {"class": "r-list-container action-bar-margin bbs-screen"} ))
print('=============')
#print(soup.div)
value = soup.find_all( "div", {"class": "r-list-container action-bar-margin bbs-screen"} )

#for str1 in soup.find_all( "div", {"class": "r-list-container action-bar-margin bbs-screen"} ):
#    print(str1.attrs['class'])


soup2 = BeautifulSoup(str(value),"html.parser")
print( "取得討論版List ",len(soup2.find_all( "div", {"title"} )))
#print( soup2.find_all( "div", { "class": "title"} ) )

for content in soup2.find_all( "div", { "class": "title"} ):
    print(content.a['href'] + " " + content.a.string )

print( "---------------------------------------------------------")

#print( soup2.find_all( "div", {"class","title"} )[0].a['href'] ) # url
#print( soup2.find_all( "div", {"class","title"} )[0].a.string  )  # title

req = Request('https://www.ptt.cc/' + soup2.find_all( "div", {"class","title"} )[0].a['href'] , headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
#3print(webpage)

soup = BeautifulSoup(webpage,"html.parser")
print(soup.title.string)
#print( soup.find_all( "div", {"id": "main-container"} ) )
v  = soup.find_all( "div", {"id": "main-container"} )
soup2 = BeautifulSoup( str(v) , "html.parser" )
print( "-------------------- \r\n")
#print( soup2.find_all( "div" , { "class","bbs-screen bbs-content" }) )
#print( len(soup2.find_all( "div" )) )


content = soup2.find_all( "div")
print(len(content))
for st in content:
    for s in st:
        print( s.string )

print(content[0].find_all( "span", { "class" : "article-meta-value" } ))
content = soup2.find_all( "span", { "class" :  "f3 hl push-userid"})
print(content)
content = soup2.find_all( "span", { "class" :  "f3 push-content"})
print( content[0].string )