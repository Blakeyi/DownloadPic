import threading
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from functools import partial
import search_main_window
import url_download as urlDL
import os
from builtins import str
import preferences


class MulThreadDownload(threading.Thread):
    def __init__(self, url):
        super(MulThreadDownload, self).__init__()
        self.url = url

    def download(self):
        start_download(ui, self.url)
        # f.close()

    def run(self):
        self.download()


def click_button_start(ui):  # 按钮点击响应函数
    url = ui.urlEdit.text()
    if url == '':
        ui.textShow.append("请输入网址！")
        return
    if ui.start.text() == "开始下载":
        ui.start.setText("暂停下载")
        t = MulThreadDownload(url)
        t.start()
    else:
        ui.start.setText("开始下载")
        threading.stop_thread(t)
    return


def openDialog(ui):  # 打开preference对话框
    ui.di = QDialog()
    d = preferences.Ui_Dialog()
    d.setupUi(ui.di)
    ui.di.show()


def start_download(ui, url):
    # 常用网址
    # url = "https://www.192td.com"
    # url = "https://www.meitulu.com"
    # url = "https://www.mzitu.com/all/" 妹子图从每日更新这里爬

    # 匹配常用网址
    if ui.defaultPath != '':
        savePath = ui.defaultPath + "//"
    else:
        savePath = ui.cwd + "//"
    savePath = 'D:\\pic\\'
    htmlText = urlDL.geturlDeatil(url)
    if htmlText == "访问网站异常":
        ui.textShow.append("访问网站异常,请检查重试")
    # with open("D://picture//html.txt", 'w', encoding='utf-8') as file_object:
    # file_object.write(htmlText)
    firstList = urlDL.childUrl(htmlText)  # 先把首页下所有相关的网页全部记录下来
    firstList = urlDL.filter(firstList)  # 过滤一下网址
    firstList = set(firstList)
    ui.textShow.append("开始下载")
    for i in firstList:
        savePath1 = savePath
        path = i.split('/')
        path_temp = ''.join(path[-1:])  # list转换为str
        isExists = os.path.exists(savePath1 + path_temp) # 判断文件夹存不存在
        if isExists is False:
            os.makedirs(savePath1 + path_temp)
        else:
            continue  # 存在文件夹就跳过
        savePath1 = savePath1 + path_temp + "//"
        htmlText1 = urlDL.geturlDeatil(i)  # 获取子网页的图片地址
        if htmlText1 == "访问网站异常":
            ui.textShow.append("访问网站异常,请检查重试")
        secondList = urlDL.get_html(htmlText1)  # 先把子分类的所有相关的网页全部记录下来
        if not secondList:
            pic_url = urlDL.get_picture(htmlText1)  # 获取子网页的图片地址
            if len(pic_url) == 0:  # 没有图片就跳到下一个网址
                continue
            pic_url = pic_url[0:1]
            pic_url1 = pic_url[0][0:-6]
            for num in range(100):
                pic_url2 = pic_url1 + str(num).zfill(2) + ".jpg"
                pic_url.append(pic_url2)
            pic_url = list(set(pic_url))
            ui.textShow.append("图片保存在："+savePath1)
            ui.textShow.append("正在下载，请稍后...")
            state_list = urlDL.getPicture(pic_url, savePath1)
            num = state_list[1]
            num1 = state_list[2]
            str1 = state_list[0] + ", 已下载" + str(num) + "张图片" + ", 已删除" + str(num1) + "张小图片"
            ui.textShow.append(str1)
        else:  # 需要中间查找HTML   
            secondList = set(secondList)
            for j in secondList:
                path = j.split('/')
                path_temp = ''.join(path[-1:])  # list转换为str
                isExists = os.path.exists(savePath1 + path_temp) # 判断文件夹存不存在
                if isExists is False:
                    os.makedirs(savePath1 + path_temp)
                savePath2 = savePath1 + path_temp + "//"
                htmlText2 = urlDL.geturlDeatil(j)  # 获取子网页的图片地址
                if htmlText2 == "访问网站异常":
                    ui.textShow.append("访问网站异常,请检查重试")
                pic_url = urlDL.get_picture(htmlText2)
                result = urlDL.filterPic(pic_url)
                if len(result) < 3:  # 没有图片就跳到下一个网址
                    continue
                pic_url1 = pic_url[2][0:-5]
                for num in range(100):
                    pic_url2 = pic_url1 + str(num) + ".jpg"
                    pic_url.append(pic_url2)
                pic_url = list(set(pic_url))  
                ui.textShow.append("图片保存在："+savePath2)
                ui.textShow.append("正在下载，请稍后...")
                state_list = urlDL.getPicture(pic_url, savePath2)
                num = state_list[1]
                num1 = state_list[2]
                str1 = state_list[0] + ", 已下载" + str(num) + "张图片" + ", 已删除" + str(num1) + "张小图片"
                ui.textShow.append(str1)
        QApplication.processEvents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = search_main_window.Ui_MainWindow()
    ui.setupUi(main_window)  # 将新产生的窗口绑定到虚拟窗口
    main_window.show()
    ui.start.clicked.connect(partial(click_button_start, ui))
    ui.action_Preferences.triggered.connect(partial(openDialog, ui))
    sys.exit(app.exec_())
