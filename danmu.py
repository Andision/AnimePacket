import bilili.api.danmaku
import bilili.api.bangumi
import re,os
from danmaku2ass import Danmaku2ASS

url = input()
# url = 'https://www.bilibili.com/bangumi/play/ss1172/?from=search&seid=11632503908693000797'

ss_id = re.findall(r"/ss(.*)/",url)[0]
print(ss_id)

title = bilili.api.bangumi.get_bangumi_title(season_id=ss_id)
print(title)

bangumi_list = bilili.api.bangumi.get_bangumi_list(season_id=ss_id)
os.mkdir(title)
for i in bangumi_list:
    print(i)

    danmaku = bilili.api.danmaku.get_danmaku(cid=i['cid'])
    # print(a)
    f=open(title+'/'+i['name']+'.xml','w+',encoding="UTF-8")
    f.write(danmaku)
    f.close()
    Danmaku2ASS([title+'/'+i['name']+'.xml'], 'autodetect', title+'/'+i['name']+'.ass', 1920, 1080, 0, 'sans-serif', 50.0, 0.9, 10.0, 5.0, None, None, False)

# python .\danmaku2ass.py .\danmu.xml -s 1920x1080 -o ./danmu.ass -fs 50 -dm 10
# Namespace(alpha=1.0
# duration_marquee=10.0
# duration_still=5.0
# file=['.\\danmu.xml']
# filter=None
# filter_file=None
# font='sans-serif'
# fontsize=50.0
# format='autodetect'
# output='./danmu.ass'
# protect=0
# reduce=False
# size='1920x1080')