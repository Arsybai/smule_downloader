import requests

def smule_download(link):
    smule = requests.get(link).text
    print('Title : ' + smule[smule.find('<title>') + 7 : smule.find('</title>')-9])
    print('\n')
    print('Url : '+smule.split('twitter:player:stream" content="')[1].split('">')[0].replace('amp;', ''))

  
url = "https://www.smule.com/recording/jamalu-ya-jamalu-%D9%8A%D8%A7-%D8%AC%D9%85%D8%A7%D9%84-jamalu/570753960_2355454569/ensembles"
smule_download(url)

#c 2018 Arsybai All right reserved
