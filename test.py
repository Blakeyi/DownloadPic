
from bs4 import BeautifulSoup
import requests
import urllib.request
import re, os
from PIL import Image



def searchDirFile(rootDir, fileList, fileType):
    print(id(fileList))
    for dir_or_file in os.listdir(rootDir):
        filePath = os.path.join(rootDir, dir_or_file)
        if os.path.isfile(filePath):
            if filePath[-len(fileType):] == fileType:
                fileList.append(filePath)
                #shutil.copyfile(filePath,os.path.join(saveDir,os.path.basename(filePath)))
            else:
                continue
        elif os.path.isdir(filePath):
            searchDirFile(filePath, fileList, fileType)
        else:
            print('not file and dir '+os.path.basename(filePath))


def deleteFile(fileList):
    countDele = 0
    count = 0
    print(id(fileList))
    for path in fileList:
        try:
            fp = open(path, 'rb')
            im = Image.open(fp)
            fp.close()
            x, y = im.size
            if x < 1920 or y < 1080:
                os.remove(path)
                countDele += 1
                count += 1
                if count == 100:
                    print('已删除 100 张图片')
                    count = 0
        except Exception:
            continue
    return countDele



if __name__ == "__main__":
    fileList = list()
    print(id(fileList))
    path = 'D:\\software_study\\PYTHON\\Project\\DownloadPic'
    # searchDirFile(path, fileList, '.jpg')   
    print('已删除 ' + str(deleteFile(fileList)) + ' 张图片')