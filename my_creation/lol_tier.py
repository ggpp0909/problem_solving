import requests
from bs4 import BeautifulSoup
nickname=input('닉네임 입력 : ')
url =f'https://www.op.gg/summoner/userName={nickname}'

response = requests.get(url).text
data = BeautifulSoup(response,"html.parser")
tier = BeautifulSoup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierRank")
#왜 못불러와 ..
print(tier.text)
