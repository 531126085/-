import urllib.request
import re

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    return html

def get_img(html):
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'
    imglist = re.findall(p,html)          #findall函数，如果正则表达式里有带（）的，则查找到之后会将括号的里面的信息返回给imglist
    
    for each in imglist:
        print(each)
    
    for each in imglist:
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each,filename,None)
        

if __name__=='__main__':
    url = "http://tieba.baidu.com/p/6093575289?pid=125013245611&cid=0#125013245611"
    get_img(open_url(url))