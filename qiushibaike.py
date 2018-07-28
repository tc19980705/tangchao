import requests
import re
import threading

# 得到HTML
def get_html(page):
    ori_url = 'https://www.qiushibaike.com/imgrank/page/%d/' % page
    req = requests.get(ori_url)
    url_text = req.text
    return url_text

# 获取HTML中的图片地址
def get_pics(html):
    pattern = r'//pic.*jpeg'
    pics_urllist = re.findall(pattern, html)
    return pics_urllist

# 下载图片
def download_pics(lst):
    for i in lst:
        full_url = "http:" + i
        pic_name = i.split('/')[-1]
        r = requests.get(full_url)
        with open(r'H:\Pythonproject\Final_project\pictures\%s' % pic_name, 'wb') as f:
            f.write(r.content)
            print("下载完成：%s" % pic_name)

if __name__ == '__main__':
    while True:
        start_page = int(input("请输入起始页："))
        end_page = int(input("请输入终止页："))
        print("开始下载")
        for page in range(start_page, end_page + 1):
            html = get_html(page)
            pic_url = get_pics(html)
            thread = []
            t = threading.Thread(target = download_pics, args = (pic_url,))
            thread.append(t)
            t.start()
            for x in thread:
                x.join()
        print("下载结束")
        break
