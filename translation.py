def Trans_ChampN(ChampN):

    EngName = ""

    Kr = ["가렌", "갈리오", "갱플", "그라가스", "그브", "나르", "나미", "나서스", "노틸", "녹턴", "누누", "니달리",
          "니코", "다리", "다이애나", "드븐", "라이즈", "라칸", "람머", "럭스", "럼블", "레넥", "레오나", "렉사이",
          "렝가", "루시안", "룰루", "르블랑", "리신", "리븐", "리산", "마이", "마오", "말자", "말파", "모데", "몰가",
          "문도", "미포", "바드", "바루스", "바이", "베이가", "베인", "벨코즈", "볼베", "브랜드","브라움", "블라디",
          "블츠", "빅토르", "뽀삐", "사이온", "사일러스", "샤코", "세주", "소나", "소라카", "쉔", "쉬바나", "스웨인",
          "스카너", "시비르", "짜오", "신드라", "신지드", "쓰레쉬", "아리", "아무무", "아우솔", "아이번", "아지르",
          "아칼리", "아트", "알리", "애니", "애니비아", "애쉬", "야스오", "에코", "엘리스", "오공", "오른", "오리",
          "올라프", "요릭", "우디르", "우르곳", "워윅", "이렐리아", "이블린", "이즈", "일라", "자르반", "자야",
          "자이라", "자크", "잔나", "잭스", "제드", "제라스", "제이스", "조이", "직스", "진", "질리언", "징크스",
          "초가스", "카르마", "카밀", "카사딘", "카서스", "카시", "카이사", "카직스", "칼리", "카타", "케넨", "케틀",
          "케인", "케일", "코그모", "코르키", "퀸", "클레드", "킨드", "타릭", "탈론", "탈리야", "켄치", "트런들", "트타",
          "트린", "트페", "트위치", "티모", "파이크", "판테", "피들", "피오라", "피즈", "딩거", "헤카림"]
    Eng = ["Garen", "Galio", "Gangplank", "Gragas", "Graves", "Gnar", "Nami", "Nasus", "Nautilus", "Nocturne",
           "Nunu & Willump", "Nidalee", "Neeko", "Darius", "Diana", "Draven", "Ryze", "Rakan", "Rammus", "Lux", "Rumble",
           "Renekton", "Leona", "Rek'Sai", "Rengar", "Lucian", "Lulu", "LeBlanc", "Lee Sin", "Riven", "Lissandra", "Master Yi",
           "Maokai", "Malzahar", "Malphite", "Mordekaiser", "Morgana", "Dr. Mundo", "Miss Fortune", "Bard", "Varus",
           "Vi", "Veigar", "Vayne", "Vel'Koz", "Volibear", "Brand", "Braum", "Vladimir", "Blitzcrank", "Viktor", "Poppy",
           "Sion", "Sylas", "Shaco", "Sejuani", "Sona", "Soraka", "Shen", "Shyvana", "Swain", "Skarner", "Sivir",
           "Xin Zhao", "Syndra", "Singed", "Thresh", "Ahri", "Amumu", "Aurelion Sol", "Ivern", "Azir", "Akali", "Aatrox",
           "Alistar", "Annie", "Anivia", "Ashe", "Yasuo", "Ekko", "Elise", "Wukong", "Ornn", "Orianna", "Olaf", "Yorick",
           "Udyr", "Urgot", "Warwick", "Irelia", "Evelynn", "Ezreal", "Illaoi", "Jarvan IV", "Xayah", "Zyra", "Zac",
           "Janna", "Jax", "Zed", "Xerath", "Jayce", "Zoe", "Ziggs", "Jine", "Zilean", "Jinx", "Cho'Gath", "Karma",
           "Camille", "Kassadin", "Karthus", "Cassiopeia", "Kai'Sa", "Khazix", "Kalistar", "Katarina", "Kennen", "Caitlyn",
           "Kayn", "Kayle", "Kog'Maw", "Corki", "Quinn", "Kled", "Kindred", "Taric", "Talon", "Taliyah", "Tahm Kench",
           "Trundle", "Tristana", "Tryndamere", "Twisted Fate", "Twitch", "Teemo", "Pyke", "Pantheon", "Fiddlesticks",
           "Fiora", "Fizz", "Heimerdinger", "Hecarim"]

    for i in range(0, len(Kr)):
          if Kr[i] == ChampN:
                EngName = Eng[i]
                break

    return EngName

def Line_ChampN(LineX):

    Num = 0;

    Top = ["Garen", "Gangplank", "Gnar", "Nami", "Nasus",
           "Darius","Ryze", "Rumble",
           "Renekton", "Rengar", "Riven", "Lissandra",
           "Maokai", "Malzahar", "Malphite", "Mordekaiser", "Dr. Mundo",
           "Vayne", "Volibear", "Vladimir", "Viktor", "Poppy",
           "Sion", "Sylas", "Shen",
           "Singed", "Akali", "Aatrox",
           "Yasuo", "Wukong", "Ornn", "Olaf", "Yorick",
           "Urgot", "Irelia", "Illaoi",
           "Jax", "Jayce", "Cho'Gath", "Karma",
           "Camille", "Karthus", "Cassiopeia", "Kennen",
           "Kayle", "Quinn", "Kled", "Tahm Kench",
           "Tryndamere", "Teemo", "Pantheon",
           "Fiora", "Heimerdinger", "Hecarim"]
    Jg =  ["Gragas", "Graves", "Nocturne",
           "Nunu & Willump", "Nidalee", "Rammus", "Lux",
           "Rek'Sai", "Rengar", "Lee Sin", "Riven",
           "Master Yi", "Vi", "Poppy",
           "Sylas", "Shaco", "Sejuani", "Shyvana",
           "Xin Zhao", "Amumu", "Ivern", "Aatrox",
           "Elise", "Wukong", "Olaf",
           "Udyr", "Warwick", "Evelynn", "Jarvan IV", "Zac",
           "Jax", "Camille", "Karthus", "Khazix",
           "Kayn", "Kindred", "Taliyah",
           "Pantheon", "Fiddlesticks",
           "Hecarim"]
    Mid = ["Galio", "Nocturne",
           "Neeko", "Diana", "Ryze", "Lux", "Rumble",
           "Renekton", "Lulu", "LeBlanc", "Riven", "Lissandra",
           "Malzahar",
           "Veigar", "Vel'Koz", "Vladimir", "Viktor",
           "Sion", "Sylas", "Swain",
           "Syndra", "Ahri", "Aurelion Sol", "Azir", "Akali",
           "Aatrox",
           "Annie", "Anivia", "Yasuo", "Ekko", "Orianna",
           "Irelia",
           "Zed", "Xerath", "Jayce", "Zoe", "Ziggs", "Zilean", "Jinx", "Karma",
           "Kassadin", "Karthus", "Cassiopeia", "Katarina",
           "Corki", "Kled", "Talon", "Taliyah",
           "Twisted Fate", "Pantheon",
           "Fiora", "Fizz"]
    Adc = ["Draven", "Lucian", "Miss Fortune", "Varus",
           "Vayne", "Vladimir", "Viktor",
           "Sivir",
           "Ashe", "Yasuo", "Ezreal", "Xayah", "Jine", "Jinx",
           "Cassiopeia", "Kai'Sa", "Kalistar", "Caitlyn",
           "Kog'Maw", "Tristana", "Twitch"]
    Sup = ["Gragas", "Nami", "Nautilus",
           "Neeko", "Rakan", "Lux",
           "Leona", "Lulu",
           "Morgana", "Bard",
           "Veigar", "Vel'Koz", "Brand", "Braum", "Blitzcrank",
           "Poppy",
           "Sona", "Soraka", "Shen",
           "Thresh", "Alistar", "Ornn",
           "Zyra", "Janna", "Xerath", "Zilean", "Karma",
           "Taric", "Tahm Kench",
           "Pyke", "Fiddlesticks"]

    for i in range(0, len(Top)):
          if Top[i] == LineX:
                Num += 10000
                break

    for i in range(0, len(Jg)):
          if Jg[i] == LineX:
                Num += 1000
                break

    for i in range(0, len(Mid)):
          if Mid[i] == LineX:
                Num += 100
                break

    for i in range(0, len(Adc)):
          if Adc[i] == LineX:
                Num += 10
                break

    for i in range(0, len(Sup)):
          if Sup[i] == LineX:
                Num += 1
                break

    return Num
