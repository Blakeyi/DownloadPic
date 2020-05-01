import threading
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
import search_main_window
import url_download as urlDL
import os


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
    t = MulThreadDownload(url)
    t.start()


def start_download(ui, url):
    savePath = 'D://picture//'
    # url = "https://tieba.baidu.com/p/4574440247?see_lz=1"
    # url = "https://www.192td.com/gc/blfw/blfw411.html"
    # url = "https://www.192td.com"
    htmlText = urlDL.geturlDeatil(url)
    if htmlText == "访问网站异常":
        ui.textShow.append("访问网站异常,请检查重试")
    # with open("D://picture//html.txt", 'w', encoding='utf-8') as file_object:
    # file_object.write(htmlText)
    secondList = urlDL.childUrl(htmlText)  # 先把首页下所有相关的网页全部记录下来
    result = urlDL.filter(secondList)  # 过滤一下网址
    ui.textShow.append("开始下载")
    for i in result:
        savePath1 = savePath
        path = i.split('/')
        path_temp = ''.join(path[-1:])  # list转换为str
        isExists = os.path.exists(savePath1 + path_temp)
        if isExists is False:
            os.makedirs(savePath1 + path_temp)
            savePath1 = savePath1 + path_temp + "//"
        htmlText1 = urlDL.geturlDeatil(i)
        listurl = urlDL.beautyText(htmlText1)
        result = urlDL.filterPic(listurl)
        ui.textShow.append("图片保存在："+savePath1)
        ui.textShow.append("正在下载，请稍后...")
        state_list = urlDL.getPicture(result, savePath1)
        str = state_list[0] + "已下载" + state_list[1] + "张图片"
        ui.textShow.append(str)
        QApplication.processEvents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = search_main_window.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.start.clicked.connect(partial(click_button_start, ui))
    sys.exit(app.exec_())
