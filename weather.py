# coding:utf-8
import chardet
import requests
import re
from time import sleep

CountryDic = {
               '宗谷地方':301,
               '上川・留萌地方':302,
               '網走・北見・紋別地方':303,
               '釧路・根室・十勝地方':304,
               '胆振・日高地方':305,
               '石狩・空知・後志地方':306,
               '渡島・檜山地方':307,
               '青森県':308,
               '秋田県':309,
               '岩手県':310,
               '山形県':311,
               '宮城県':312,
               '福島県':313,
               '茨城県':314,
               '群馬県':315,
               '栃木県':316,
               '埼玉県':317,
               '千葉県':318,
               '東京都':319,
               '神奈川県':320,
               '山梨県':321,
               '長野県':322,
               '新潟県':323,
               '富山県':324,
               '石川県':325,
               '福井県':326,
               '静岡県':327,
               '岐阜県':328,
               '愛知県':329,
               '三重県':330,
               '大阪府':331,
               '兵庫県':332,
               '京都府':333,
               '滋賀県':334,
               '奈良県':335,
               '和歌山県':336,
               '島根県':337,
               '広島県':338,
               '鳥取県':339,
               '岡山県':340,
               '香川県':341,
               '愛媛県':342,
               '徳島県':343,
               '高知県':344,
               '山口県':345,
               '福岡県':346,
               '佐賀県':347,
               '長崎県':348,
               '熊本県':349,
               '大分県':350,
               '宮崎県':351,
               '鹿児島県':352,
               '沖縄本島地方':353,
               '大東島地方':354,
               '宮古島地方':355,
               '八重山地方':356               
}

CountryDic_x = {
               '千葉県':318,
               '東京都':319,
               '神奈川県':320,
               '静岡県':327,
               '愛知県':329
}


print('気象庁:http://www.jma.go.jp/jma/index.html')
for i in CountryDic.keys():
    CountryCode = CountryDic[ i ]
    print ('---[ {} ]---'.format(i))
    src = requests.get('http://www.jma.go.jp/jp/yoho/{0}.html'.format(CountryCode)).text
    weather_info = re.findall('<th colspan="." class="th-area">.*?<div style="float: left">(.*?)</div>.*?<th class="weather">.*?今日(\d+)日.+? title="(.+?)"', src,  flags=(re.MULTILINE | re.DOTALL))   
    for j in weather_info:
        print(' {} : {}'.format(j[0],j[2]))
    sleep(0.5)

