import random

def Get_Dice():

        randomNum = random.randrange(1, 7)  # 1~6까지 랜덤수
        print(randomNum)
        if randomNum == 1:
            DiceNumber = ':one: '
        if randomNum == 2:
            DiceNumber = ':two: '
        if randomNum == 3:
            DiceNumber = ':three: '
        if randomNum == 4:
            DiceNumber = ':four: '
        if randomNum == 5:
            DiceNumber = ':five: '
        if randomNum == 6:
            DiceNumber = ':six: '

        return DiceNumber


def Get_emoji():
    emoji = [" ꒰⑅ᵕ༚ᵕ꒱ ", " ꒰◍ˊ◡ˋ꒱ ", " ⁽⁽◝꒰ ˙ ꒳ ˙ ꒱◜⁾⁾ ", " ༼ つ ◕_◕ ༽つ ", " ⋌༼ •̀ ⌂ •́ ༽⋋ ",
             " ( ･ิᴥ･ิ) ", " •ө• ", " ค^•ﻌ•^ค ", " つ╹㉦╹)つ ", " ◕ܫ◕ ", " ᶘ ͡°ᴥ͡°ᶅ ", " ( ؕؔʘ̥̥̥̥ ه ؔؕʘ̥̥̥̥ ) ",
             " ( •́ ̯•̀ ) ",
             " •̀.̫•́✧ ", " '͡•_'͡• ", " (΄◞ิ౪◟ิ‵) ", " ˵¯͒ བ¯͒˵ ", " ͡°͜ʖ ͡° ", " ͡~ ͜ʖ ͡° "," (づ｡◕‿‿◕｡)づ ",
             " ´_ゝ` ", " ٩(͡◕_͡◕ ", " ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄ ", " ٩(͡ï_͡ï☂ ", " ௐ ", " (´･ʖ̫･`) ", " ε⌯(ง ˙ω˙)ว ",
             " (っ˘ڡ˘ς) ", "●▅▇█▇▆▅▄▇", "╋╋◀", "︻╦̵̵̿╤──", "ー═┻┳︻▄", "︻╦̵̵͇̿̿̿̿══╤─",
             " ጿ ኈ ቼ ዽ ጿ ኈ ቼ ዽ ጿ ", "∑◙█▇▆▅▄▃▂", " ♋♉♋ ", " (๑╹ω╹๑) ", " (╯°□°）╯︵ ┻━┻ ",
             " (///▽///) ", " σ(oдolll) ", " 【o´ﾟ□ﾟ`o】 ", " ＼(^o^)／ ", " (◕‿‿◕｡) ", " ･ᴥ･ ", " ꈍ﹃ꈍ "
                                                                                                  " ˃̣̣̣̣̣̣︿˂̣̣̣̣̣̣ ",
             " ( ◍•㉦•◍ ) ", " (｡ì_í｡) ", " (╭•̀ﮧ •́╮) ", " ଘ(੭*ˊᵕˋ)੭ ", " ´_ゝ` ", " (~˘▾˘)~ "]  # 이모티콘 배열입니다.

    randomNum = random.randrange(0, len(emoji))  # 0 ~ 이모티콘 배열 크기 중 랜덤숫자를 지정합니다.
    print("랜덤수 값 :" + str(randomNum))
    print(emoji[randomNum])

    return emoji[randomNum]


def Get_Shuffle(x):

    random.shuffle(x)

    return x