from urllib.request import urlopen, Request
import urllib
import bs4

def Get_NaverChart(embed):
        url = "https://www.naver.com/"
        html = urllib.request.urlopen(url)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        realTimeSerach1 = bsObj.find('div', {'class': 'ah_roll_area PM_CL_realtimeKeyword_rolling'})
        realTimeSerach2 = realTimeSerach1.find('ul', {'class': 'ah_l'})
        realTimeSerach3 = realTimeSerach2.find_all('li')
        for i in range(0, 10):
            realTimeSerach4 = realTimeSerach3[i]
            realTimeSerach5 = realTimeSerach4.find('span', {'class': 'ah_k'})
            realTimeSerach = realTimeSerach5.text.replace(' ', '')
            realURL = 'https://search.naver.com/search.naver?ie=utf8&query=' + realTimeSerach
            print(realTimeSerach)
            embed.add_field(name=str(i + 1) + '위', value='\n' + '[%s](<%s>)' % (realTimeSerach, realURL),
                            inline=False)  # [텍스트](<링크>) 형식으로 적으면 텍스트 하이퍼링크 만들어집니다
        return embed

def Get_Record(location, embed):
        enc_location = urllib.parse.quote(location)
        url = "http://www.op.gg/summoner/userName=" + enc_location
        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")
        rank1 = bsObj.find("div", {"class": "TierRankInfo"})
        ##rank2 = rank1.find("div", {"class": "TierType"})
        if rank1 == None:
            embed.add_field(name='-정보 없음-', value="닉네임을 다시 확인해주세요.", inline=False)
            return embed
        else:
            rank2 = rank1.find("div", {"class": "TierRank"})
            rank3 = rank2.text.strip()  # 티어표시 (브론즈1,2,3,4,5 등등

            ##print(rank3)
            ##if rank3 != 'Unranked':
            if rank3 == 'Unranked':
                embed.add_field(name='당신의 티어', value=rank3, inline=False)
                embed.add_field(name='-당신은 언랭-', value="언랭은 정보를 제공하지 않습니다.", inline=False)
                return embed

            else:
                jumsu1 = rank1.find("div", {"class": "TierInfo"})
                jumsu2 = jumsu1.find("span", {"class": "LeaguePoints"})
                jumsu3 = jumsu2.text
                jumsu4 = jumsu3.strip()  # 점수표시 (11LP등등)
                print(jumsu4)

                winlose1 = jumsu1.find("span", {"class": "WinLose"})
                winlose2 = winlose1.find("span", {"class": "wins"})
                winlose2_1 = winlose1.find("span", {"class": "losses"})
                winlose2_2 = winlose1.find("span", {"class": "winratio"})

                winlose2txt = winlose2.text
                winlose2_1txt = winlose2_1.text
                winlose2_2txt = winlose2_2.text  # 승,패,승률 나타냄  200W 150L Win Ratio 55% 등등

                print(winlose2txt + " " + winlose2_1txt + " " + winlose2_2txt)

                embed.add_field(name='당신의 티어', value = rank3, inline=False)
                embed.add_field(name='당신의 LP(점수)', value=jumsu4, inline=False)
                embed.add_field(name='당신의 승,패 정보', value=winlose2txt + " " + winlose2_1txt, inline=False)
                embed.add_field(name='당신의 승률', value=winlose2_2txt, inline=False)
                return embed


def Get_Most(location, embed):
    enc_location = urllib.parse.quote(location)
    url = "http://www.op.gg/summoner/userName=" + enc_location
    html = urllib.request.urlopen(url)

    bsObj = bs4.BeautifulSoup(html, "html.parser")

    most = "";
    most = bsObj.find_all('div', {'class': 'ChampionBox Ranked'})

    if len(most) < 1:
        embed.add_field(name='-전적없음-', value="모스트 정보가 없습니다.", inline=False)
        return embed
    else :
        for i in range(0, len(most)):

            i_ = i + 1
            _i = str(i_)

            if int(i_) > 3:
                break

            most1Name1 = most[i].find_all('div')
            most1Name2 = most1Name1[1]
            most1Name3 = most1Name2.find_all('div')
            most1Name4 = most1Name3[0]
            most1Name = most1Name4.find('a').text.strip() ##챔프이름

            csAverage1 = most1Name3[1]
            csAverage2 = str(csAverage1)[str(csAverage1).find('m)"') + 4:str(csAverage1).find('</di')]
            csAverage3 = csAverage2.split(" ")
            csAverage = csAverage3[2]
            csHigh = csAverage3[1]  # cs평균

            WinRate1 = most1Name1[8]
            WinRate = str(WinRate1)[str(WinRate1).find('o">') + 4:str(WinRate1).find('</di')]


            GamePlay1 = most1Name1[9]
            GamePlay2 = str(GamePlay1)[str(GamePlay1).find('e">') + 3:str(GamePlay1).find('</di')]
            GamePlay3 = GamePlay2.split(" ")
            GamePlay = GamePlay3[0]

            print("KDA = ?")

            kda1 = most1Name1[4]
            kda2 = kda1.find_all('div')
            kda3 = kda2[0]

            print(kda3.find('span', {'class': 'Perfect'}))

            if kda3.find('span', {'class': 'Perfect'}) == None:##perfect
                Kda = kda3.find('span', {'class': 'KDA'}).text.strip() ##KDA
            else :
                Kda = kda3.find('span', {'class': 'Perfect'}).text.strip()

            embed.add_field(name='-------------------모스트 ' + _i + '위-------------------',
                            value='\n챔프명 : ' + most1Name + '\n' + '\n판수 : ' + GamePlay
                                  + '\n승률 : ' + WinRate + 'KDA : ' + Kda + '\nCS(분당) : ' + csHigh + csAverage,
                            inline=False)

        return embed

def Get_MRanking(embed):
    # http://ticket2.movie.daum.net/movie/movieranklist.aspx
    i1 = 0  # 랭킹 string값
    hdr = {'User-Agent': 'Mozilla/5.0'}
    url = 'http://ticket2.movie.daum.net/movie/movieranklist.aspx'
    print(url)
    req = Request(url, headers=hdr)
    html = urllib.request.urlopen(req)
    bsObj = bs4.BeautifulSoup(html, "html.parser")
    moviechartBase = bsObj.find('div', {'class': 'main_detail'})
    moviechart1 = moviechartBase.find('ul', {'class': 'list_boxthumb'})
    moviechart2 = moviechart1.find_all('li')

    for i in range(0, 3):
        i1 = i1 + 1
        stri1 = str(i1)  # i1은 영화랭킹을 나타내는데 사용됩니다
        print()
        print(i)
        print()
        moviechartLi1 = moviechart2[i]  # ------------------------- 1등랭킹 영화---------------------------
        moviechartLi1Div = moviechartLi1.find('div', {'class': 'desc_boxthumb'})  # 영화박스 나타내는 Div
        moviechartLi1MovieName1 = moviechartLi1Div.find('strong', {'class': 'tit_join'})
        moviechartLi1MovieName = moviechartLi1MovieName1.text.strip()  # 영화 제목
        print(moviechartLi1MovieName)

        moviechartLi1Ratting1 = moviechartLi1Div.find('div', {'class': 'raking_grade'})
        moviechartLi1Ratting2 = moviechartLi1Ratting1.find('em', {'class': 'emph_grade'})
        moviechartLi1Ratting = moviechartLi1Ratting2.text.strip()  # 영화 평점
        print(moviechartLi1Ratting)

        moviechartLi1openDay1 = moviechartLi1Div.find('dl', {'class': 'list_state'})
        moviechartLi1openDay2 = moviechartLi1openDay1.find_all('dd')  # 개봉날짜, 예매율 두개포함한 dd임
        moviechartLi1openDay3 = moviechartLi1openDay2[0]
        moviechartLi1Yerating1 = moviechartLi1openDay2[1]
        moviechartLi1openDay = moviechartLi1openDay3.text.strip()  # 개봉날짜
        print(moviechartLi1openDay)

        moviechartLi1Yerating = moviechartLi1Yerating1.text.strip()  # 예매율 ,랭킹변동
        print(moviechartLi1Yerating)  # ------------------------- 1등랭킹 영화---------------------------
        print()
        embed.add_field(name='---------------랭킹' + stri1 + '위---------------',
                        value='\n영화제목 : ' + moviechartLi1MovieName + '\n영화평점 : ' + moviechartLi1Ratting + '점'
                              + '\n개봉날짜 : ' + moviechartLi1openDay + '\n예매율,랭킹변동 : ' + moviechartLi1Yerating,
                        inline=False)  # 영화랭킹

    return embed


def Get_topTier(embed):
    url = "http://www.op.gg/champion/statistics"
    html = urllib.request.urlopen(url)

    bsObj = bs4.BeautifulSoup(html, "html.parser")
    TI = bsObj.find("tbody", {"class": "tabItem champion-trend-tier-TOP"})
    tierInfo = TI.find_all("tr")

    for item in range(0, 5):
        champTier = tierInfo[item].find("td", {"class": "champion-index-table__cell champion-index-table__cell--rank"}).text ##<td class="champion-index-table__cell champion-index-table__cell--rank">1</td>
        print(champTier)

        champName1 = tierInfo[item].find("td", {"class": "champion-index-table__cell champion-index-table__cell--champion"})
        print(champName1)
        champName2 = champName1.find_all("a")
        print(champName2)
        champName3 = champName2[0].find("div", { "class": "champion-index-table__name"}).text
        print(champName3)

        Rate = tierInfo[item].find_all("td", {"class": "champion-index-table__cell champion-index-table__cell--value"})
        WinRate = (Rate[0]).text
        PickRate = (Rate[1]).text
        print(WinRate)
        print(PickRate)

        embed.add_field(name='-------------------탑 ' + champTier + '위-------------------',
                        value = '\n챔프명 : ' + champName3 + '\n승률 : ' + WinRate
                        + '\n픽률 : ' + PickRate,
                        inline = False)

    return embed

def Get_jgTier(embed):
    url = "http://www.op.gg/champion/statistics"
    html = urllib.request.urlopen(url)

    bsObj = bs4.BeautifulSoup(html, "html.parser")
    TI = bsObj.find("tbody", {"class": "tabItem champion-trend-tier-JUNGLE"})
    tierInfo = TI.find_all("tr")

    for item in range(0, 5):
        champTier = tierInfo[item].find("td", {"class": "champion-index-table__cell champion-index-table__cell--rank"}).text ##<td class="champion-index-table__cell champion-index-table__cell--rank">1</td>
        print(champTier)

        champName1 = tierInfo[item].find("td", {"class": "champion-index-table__cell champion-index-table__cell--champion"})
        print(champName1)
        champName2 = champName1.find_all("a")
        print(champName2)
        champName3 = champName2[0].find("div", { "class": "champion-index-table__name"}).text
        print(champName3)

        Rate = tierInfo[item].find_all("td", {"class": "champion-index-table__cell champion-index-table__cell--value"})
        WinRate = (Rate[0]).text
        PickRate = (Rate[1]).text
        print(WinRate)
        print(PickRate)

        embed.add_field(name='-------------------정글 ' + champTier + '위-------------------',
                        value = '\n챔프명 : ' + champName3 + '\n승률 : ' + WinRate
                        + '\n픽률 : ' + PickRate,
                        inline = False)

    return embed

def Get_midTier(embed):
    url = "http://www.op.gg/champion/statistics"
    html = urllib.request.urlopen(url)

    bsObj = bs4.BeautifulSoup(html, "html.parser")
    TI = bsObj.find("tbody", {"class": "tabItem champion-trend-tier-MID"})
    tierInfo = TI.find_all("tr")

    for item in range(0, 5):
        champTier = tierInfo[item].find("td", {"class": "champion-index-table__cell champion-index-table__cell--rank"}).text ##<td class="champion-index-table__cell champion-index-table__cell--rank">1</td>
        print(champTier)

        champName1 = tierInfo[item].find("td", {"class": "champion-index-table__cell champion-index-table__cell--champion"})
        print(champName1)
        champName2 = champName1.find_all("a")
        print(champName2)
        champName3 = champName2[0].find("div", { "class": "champion-index-table__name"}).text
        print(champName3)

        Rate = tierInfo[item].find_all("td", {"class": "champion-index-table__cell champion-index-table__cell--value"})
        WinRate = (Rate[0]).text
        PickRate = (Rate[1]).text
        print(WinRate)
        print(PickRate)

        embed.add_field(name='-------------------미드 ' + champTier + '위-------------------',
                        value = '\n챔프명 : ' + champName3 + '\n승률 : ' + WinRate
                        + '\n픽률 : ' + PickRate,
                        inline = False)

    return embed

def Get_adcTier(embed):
    url = "http://www.op.gg/champion/statistics"
    html = urllib.request.urlopen(url)

    bsObj = bs4.BeautifulSoup(html, "html.parser")
    TI = bsObj.find("tbody", {"class": "tabItem champion-trend-tier-ADC"})
    tierInfo = TI.find_all("tr")

    for item in range(0, 5):
        champTier = tierInfo[item].find("td", {"class": "champion-index-table__cell champion-index-table__cell--rank"}).text ##<td class="champion-index-table__cell champion-index-table__cell--rank">1</td>
        print(champTier)

        champName1 = tierInfo[item].find("td", {"class": "champion-index-table__cell champion-index-table__cell--champion"})
        print(champName1)
        champName2 = champName1.find_all("a")
        print(champName2)
        champName3 = champName2[0].find("div", { "class": "champion-index-table__name"}).text
        print(champName3)

        Rate = tierInfo[item].find_all("td", {"class": "champion-index-table__cell champion-index-table__cell--value"})
        WinRate = (Rate[0]).text
        PickRate = (Rate[1]).text
        print(WinRate)
        print(PickRate)

        embed.add_field(name='-------------------원딜 ' + champTier + '위-------------------',
                        value = '\n챔프명 : ' + champName3 + '\n승률 : ' + WinRate
                        + '\n픽률 : ' + PickRate,
                        inline = False)

    return embed

def Get_supTier(embed):
    url = "http://www.op.gg/champion/statistics"
    html = urllib.request.urlopen(url)

    bsObj = bs4.BeautifulSoup(html, "html.parser")
    TI = bsObj.find("tbody", {"class": "tabItem champion-trend-tier-SUPPORT"})
    tierInfo = TI.find_all("tr")

    for item in range(0, 5):
        champTier = tierInfo[item].find("td", {"class": "champion-index-table__cell champion-index-table__cell--rank"}).text ##<td class="champion-index-table__cell champion-index-table__cell--rank">1</td>
        print(champTier)

        champName1 = tierInfo[item].find("td", {"class": "champion-index-table__cell champion-index-table__cell--champion"})
        print(champName1)
        champName2 = champName1.find_all("a")
        print(champName2)
        champName3 = champName2[0].find("div", { "class": "champion-index-table__name"}).text
        print(champName3)

        Rate = tierInfo[item].find_all("td", {"class": "champion-index-table__cell champion-index-table__cell--value"})
        WinRate = (Rate[0]).text
        PickRate = (Rate[1]).text
        print(WinRate)
        print(PickRate)

        embed.add_field(name='-------------------서폿 ' + champTier + '위-------------------',
                        value = '\n챔프명 : ' + champName3 + '\n승률 : ' + WinRate
                        + '\n픽률 : ' + PickRate,
                        inline = False)

    return embed

def Get_Rumble(embed):
    url = "http://www.op.gg/champion/statistics"
    html = urllib.request.urlopen(url)

    bsObj = bs4.BeautifulSoup(html, "html.parser")
    TI = bsObj.find("tbody", {"class": "tabItem champion-trend-tier-MID"})
    tierInfo = TI.find_all("tr")

    for item in range(0, len(tierInfo)):
        champTier = tierInfo[item].find("td", {"class": "champion-index-table__cell champion-index-table__cell--rank"}).text ##<td class="champion-index-table__cell champion-index-table__cell--rank">1</td>

        champName1 = tierInfo[item].find("td", {"class": "champion-index-table__cell champion-index-table__cell--champion"})
        champName2 = champName1.find_all("a")
        champName3 = champName2[0].find("div", { "class": "champion-index-table__name"}).text

        Rate = tierInfo[item].find_all("td", {"class": "champion-index-table__cell champion-index-table__cell--value"})
        WinRate = (Rate[0]).text
        PickRate = (Rate[1]).text

        if champName3 == "Rumble":
            embed.add_field(name='-------------------미드 ' + champTier + '위-------------------',
                            value = '\n챔프명 : ' + champName3 + '\n승률 : ' + WinRate
                            + '\n픽률 : ' + PickRate,
                            inline = False)
            break

    url2 = "http://www.op.gg/champion/statistics"
    html2 = urllib.request.urlopen(url2)

    bsObj2 = bs4.BeautifulSoup(html2, "html.parser")
    TI2 = bsObj2.find("tbody", {"class": "tabItem champion-trend-tier-JUNGLE"})
    tierInfo2 = TI2.find_all("tr")

    for item in range(0, len(tierInfo2)):
        champTier = tierInfo2[item].find("td", {"class": "champion-index-table__cell champion-index-table__cell--rank"}).text ##<td class="champion-index-table__cell champion-index-table__cell--rank">1</td>

        champName1 = tierInfo2[item].find("td", {"class": "champion-index-table__cell champion-index-table__cell--champion"})
        champName2 = champName1.find_all("a")
        champName3 = champName2[0].find("div", { "class": "champion-index-table__name"}).text


        Rate = tierInfo2[item].find_all("td", {"class": "champion-index-table__cell champion-index-table__cell--value"})
        WinRate = (Rate[0]).text
        PickRate = (Rate[1]).text

        if champName3 == "Rumble":
            embed.add_field(name='-------------------정글 ' + champTier + '위-------------------',
                            value = '\n챔프명 : ' + champName3 + '\n승률 : ' + WinRate
                            + '\n픽률 : ' + PickRate,
                            inline = False)
            break

    url3 = "http://www.op.gg/champion/statistics"
    html3 = urllib.request.urlopen(url3)

    bsObj3 = bs4.BeautifulSoup(html3, "html.parser")
    TI3 = bsObj3.find("tbody", {"class": "tabItem champion-trend-tier-TOP"})
    tierInfo3 = TI3.find_all("tr")

    for item in range(0, len(tierInfo3)):
        champTier = tierInfo3[item].find("td", {"class": "champion-index-table__cell champion-index-table__cell--rank"}).text ##<td class="champion-index-table__cell champion-index-table__cell--rank">1</td>

        champName1 = tierInfo3[item].find("td", {"class": "champion-index-table__cell champion-index-table__cell--champion"})
        champName2 = champName1.find_all("a")
        champName3 = champName2[0].find("div", { "class": "champion-index-table__name"}).text

        Rate = tierInfo3[item].find_all("td",
                                        {"class": "champion-index-table__cell champion-index-table__cell--value"})
        WinRate = (Rate[0]).text
        PickRate = (Rate[1]).text

        if champName3 == "Rumble":

            embed.add_field(name='-------------------탑 ' + champTier + '위-------------------',
                            value = '\n챔프명 : ' + champName3 + '\n승률 : ' + WinRate
                            + '\n픽률 : ' + PickRate,
                            inline = False)
            break

    return embed

def Get_Champion(SearchName, num, embed):

    if num >= 10000:
        num -= 10000
        url3 = "http://www.op.gg/champion/statistics"
        html3 = urllib.request.urlopen(url3)

        bsObj3 = bs4.BeautifulSoup(html3, "html.parser")
        TI3 = bsObj3.find("tbody", {"class": "tabItem champion-trend-tier-TOP"})
        tierInfo3 = TI3.find_all("tr")

        for item in range(0, len(tierInfo3)):
            champTier = tierInfo3[item].find("td", {
                "class": "champion-index-table__cell champion-index-table__cell--rank"}).text  ##<td class="champion-index-table__cell champion-index-table__cell--rank">1</td>

            champName1 = tierInfo3[item].find("td", {
                "class": "champion-index-table__cell champion-index-table__cell--champion"})
            champName2 = champName1.find_all("a")
            champName3 = champName2[0].find("div", {"class": "champion-index-table__name"}).text

            if champName3 == SearchName:
                Rate = tierInfo3[item].find_all("td", {
                    "class": "champion-index-table__cell champion-index-table__cell--value"})
                WinRate = (Rate[0]).text
                PickRate = (Rate[1]).text

                embed.add_field(name='-------------------탑 ' + champTier + '위-------------------',
                                value='\n챔프명 : ' + champName3 + '\n승률 : ' + WinRate
                                      + '\n픽률 : ' + PickRate,
                                inline=False)
                break


    if num >= 1000:
        num -= 1000
        url2 = "http://www.op.gg/champion/statistics"
        html2 = urllib.request.urlopen(url2)

        bsObj2 = bs4.BeautifulSoup(html2, "html.parser")
        TI2 = bsObj2.find("tbody", {"class": "tabItem champion-trend-tier-JUNGLE"})
        tierInfo2 = TI2.find_all("tr")

        for item in range(0, len(tierInfo2)):
            champTier = tierInfo2[item].find("td", {
                "class": "champion-index-table__cell champion-index-table__cell--rank"}).text  ##<td class="champion-index-table__cell champion-index-table__cell--rank">1</td>

            champName1 = tierInfo2[item].find("td", {
                "class": "champion-index-table__cell champion-index-table__cell--champion"})
            champName2 = champName1.find_all("a")
            champName3 = champName2[0].find("div", {"class": "champion-index-table__name"}).text

            if champName3 == SearchName:
                Rate = tierInfo2[item].find_all("td", {
                    "class": "champion-index-table__cell champion-index-table__cell--value"})
                WinRate = (Rate[0]).text
                PickRate = (Rate[1]).text

                embed.add_field(name='-------------------정글 ' + champTier + '위-------------------',
                                value='\n챔프명 : ' + champName3 + '\n승률 : ' + WinRate
                                      + '\n픽률 : ' + PickRate,
                                inline=False)
                break

    if num >= 100:
        num -= 100
        url = "http://www.op.gg/champion/statistics"
        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")
        TI = bsObj.find("tbody", {"class": "tabItem champion-trend-tier-MID"})
        tierInfo = TI.find_all("tr")

        for item in range(0, len(tierInfo)):
            champTier = tierInfo[item].find("td", {"class": "champion-index-table__cell champion-index-table__cell--rank"}).text ##<td class="champion-index-table__cell champion-index-table__cell--rank">1</td>

            champName1 = tierInfo[item].find("td", {"class": "champion-index-table__cell champion-index-table__cell--champion"})
            champName2 = champName1.find_all("a")
            champName3 = champName2[0].find("div", { "class": "champion-index-table__name"}).text

            if champName3 == SearchName:
                Rate = tierInfo[item].find_all("td", {"class": "champion-index-table__cell champion-index-table__cell--value"})
                WinRate = (Rate[0]).text
                PickRate = (Rate[1]).text

                embed.add_field(name='-------------------미드 ' + champTier + '위-------------------',
                                value = '\n챔프명 : ' + champName3 + '\n승률 : ' + WinRate
                                + '\n픽률 : ' + PickRate,
                                inline = False)
                break

    if num >= 10:
        num -= 10
        url4 = "http://www.op.gg/champion/statistics"
        html4 = urllib.request.urlopen(url4)

        bsObj4 = bs4.BeautifulSoup(html4, "html.parser")
        TI4 = bsObj4.find("tbody", {"class": "tabItem champion-trend-tier-ADC"})
        tierInfo4 = TI4.find_all("tr")

        for item in range(0, len(tierInfo4)):
            champTier = tierInfo4[item].find("td", {
                "class": "champion-index-table__cell champion-index-table__cell--rank"}).text  ##<td class="champion-index-table__cell champion-index-table__cell--rank">1</td>

            champName1 = tierInfo4[item].find("td", {
                "class": "champion-index-table__cell champion-index-table__cell--champion"})
            champName2 = champName1.find_all("a")
            champName3 = champName2[0].find("div", {"class": "champion-index-table__name"}).text

            if champName3 == SearchName:
                Rate = tierInfo4[item].find_all("td", {
                    "class": "champion-index-table__cell champion-index-table__cell--value"})
                WinRate = (Rate[0]).text
                PickRate = (Rate[1]).text

                embed.add_field(name='-------------------원딜 ' + champTier + '위-------------------',
                                value='\n챔프명 : ' + champName3 + '\n승률 : ' + WinRate
                                      + '\n픽률 : ' + PickRate,
                                inline=False)
                break

    if num == 1:
        url5 = "http://www.op.gg/champion/statistics"
        html5 = urllib.request.urlopen(url5)

        bsObj5 = bs4.BeautifulSoup(html5, "html.parser")
        TI5 = bsObj5.find("tbody", {"class": "tabItem champion-trend-tier-SUPPORT"})
        tierInfo5 = TI5.find_all("tr")

        for item in range(0, len(tierInfo5)):
            champTier = tierInfo5[item].find("td", {
                "class": "champion-index-table__cell champion-index-table__cell--rank"}).text  ##<td class="champion-index-table__cell champion-index-table__cell--rank">1</td>

            champName1 = tierInfo5[item].find("td", {
                "class": "champion-index-table__cell champion-index-table__cell--champion"})
            champName2 = champName1.find_all("a")
            champName3 = champName2[0].find("div", {"class": "champion-index-table__name"}).text

            if champName3 == SearchName:
                Rate = tierInfo5[item].find_all("td", {
                    "class": "champion-index-table__cell champion-index-table__cell--value"})
                WinRate = (Rate[0]).text
                PickRate = (Rate[1]).text

                embed.add_field(name='-------------------서폿 ' + champTier + '위-------------------',
                                value='\n챔프명 : ' + champName3 + '\n승률 : ' + WinRate
                                      + '\n픽률 : ' + PickRate,
                                inline=False)
                break

    return embed


