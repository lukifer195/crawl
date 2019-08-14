import sys
from bs4 import BeautifulSoup
import urllib.request
import re
# key = 'có'
# key =  urllib.parse.quote('có')
# # print(key)


url = r'https://hamtruyen.com/doc-truyen/tensei-shitara-slime-datta-ken-chapter-60.html'
# print(url)
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
ul = soup.find('ul',class_ = 'listtruyen')
danhsach = ul.select(r'div > div > a')
ten_list = list(a.img.get('alt') for a in danhsach[0::2])
ten_list = list(re.findall('^.*-',a) for a in ten_list)
# print((ten_list))
Chapter_list = list(a.text for a in danhsach[1::2])
# print(Chapter_list)
# link_list = list(a.get('href') for a in danhsach[0::2])
# print(link_list)

# a = zip((a[0] for a in ten_list), Chapter_list ,(url + b for b in link_list))     #zip 3 list
a = zip((a[0] for a in ten_list), Chapter_list)

# chuyển thành list thuần 1 phần tử
b = []
for x in a:
    c = ''.join(x)
    b.append(c)
# print(b)

# <ul class="listtruyen">
#     <li>
#         <div class="item_truyennendoc">
#             <div class="wrapper_imgage">
#                 <a href="/chung-cuc-dau-la-0.html">
#                     <img alt="Chung Cực Đấu La - Thực Hiện Bởi hamtruyen.vn" src="https://media.hamtruyen.vn/Pictures/Truyen/Small/chung-cuc-dau-la.jpg" u="image"/>
#                 </a>
#                 <a href="/doc-truyen/chung-cuc-dau-la-chapter-49.html">
#                     <h5 class="tenchap_slide">
#                         Chapter 49 vide...
#                     </h5>
#                 </a>
#             </div>
#             <a href="/chung-cuc-dau-la-0.html">
#                 <h5 class="tentruyen_slide">
#                     Chung Cực Đấu La
#                 </h5>
#             </a>
#         </div>
#     </li>

def option_load():
    with open('input.txt', 'r',encoding= ' utf-8-sig') as file :
        return file.readlines()

def save(data):
    print('Success')
    with open (r'output.txt' , 'w+' , encoding = 'utf8') as file:
        file.writelines(["%s\n" % item  for item in data])

##################################################################################
if __name__ == '__main__':
    truyentranh = []
    list_truyen_follow = option_load()
    for truyen_fl in list_truyen_follow:
        for truyen in b:
            if re.search( str(truyen_fl.strip('\n')).lower() , str(truyen).lower() ):
                truyentranh.append(truyen)
                break
            # else:
                # print(truyen_fl)
                # print(truyen)
    print(truyentranh)
    save(truyentranh)
    import os
    os.startfile('output.txt')
    
    # import subprocess as sp
    # programName = "notepad.exe"
    # fileName = "output.txt"
    # sp.Popen([programName, fileName])

