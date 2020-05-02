#success
from bs4 import BeautifulSoup
import requests
import urllib.request
import re

headers = {'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}


def geturlDeatil(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果状态不是200，引发异常
        r.encoding = 'utf-8'  # 无论原来用什么编码，都改成utf-8
        return r.text
    except Exception as e:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)''Chrome/51.0.2704.63 Safari/537.36'}
            r = requests.get(url, timeout=30, headers=headers, verify=False)
            r.raise_for_status()  # 如果状态不是200，引发异常
            r.encoding = 'utf-8'  # 无论原来用什么编码，都改成utf-8
            return r.text
        except Exception as e:
            return "访问网站异常"


def beautyText(htmlText):
    resultList = []
    soup = BeautifulSoup(htmlText, 'html.parser')
    for i in soup.find_all('img'):
        resultList.append(i.get('lazysrc'))
    return resultList


def childUrl(htmlText):  # 获取首页下的子网页地址
    resultUrlList = []
    pattern = r'^http.*'
    soup = BeautifulSoup(htmlText, 'html.parser')
    for i in soup.find_all('a'):
        str1 = i.get('href')
        if str1 is not None:
            state = re.match(pattern, str1)
            if state:
                resultUrlList.append(str1)

    return resultUrlList


def filterPic(listurl):
    result = []
    for i in listurl:
        if (i is not None and i[:5] == "https" and i[-4:] == '.jpg'):
            result.append(i)
        elif (i is not None and i[:5] == "https" and i[-4:] == '.png'):
            result.append(i)
    return result


def filter(listurl):
    result = []
    for i in listurl[2:]:
        if (i is not None and i[:5] == "https" and i[-5:] != '.html'):
            if i[-1:] == '/':
                i = i[0:-1]
            result.append(i)
    return result


def getPicture(listUrl, savePath):
    count = 0
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36')]
    urllib.request.install_opener(opener)
    for i in range(len(listUrl)):
        try:
            urllib.request.urlretrieve(listUrl[i], savePath + str(i) + ".jpg")
            count = count + 1
        except Exception:
            return "下载图片失败", count
    return "下载图片成功", count


if __name__ == "__main__":
    savePath = 'D://picture//'
    url = "https://tieba.baidu.com/p/4574440247?see_lz=1"
    url = "https://www.192td.com/gc/blfw/blfw411.html"
    url = "https://www.192td.com"
    htmlText = geturlDeatil(url)
    with open("D://picture//html.txt", 'w', encoding='utf-8') as file_object:
        file_object.write(htmlText)
    secondList = childUrl(htmlText)  # 先把首页下所有相关的网页全部记录下来
    result = filter(secondList)  # 过滤一下网址
    for i in result:
        savePath1 = savePath
        path = i.split('/')
        path_temp = ''.join(path[-1:])  # list转换为str
        isExists = os.path.exists(savePath1 + path_temp)
        if isExists is False:
            os.makedirs(savePath1 + path_temp)
            savePath1 = savePath1 + path_temp + "//"
        htmlText1 = geturlDeatil(i)
        listurl = beautyText(htmlText1)
        result = filterPic(listurl)
        getPrciture(result, savePath1)

