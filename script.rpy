# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define a = Character('Аня', color = '#de8545')
define m = Character('Артём', color = '#4f74ae', image = 'morgan', screen = 'say_side')
define s = Character('Никита', color = '#a1a882')
define mi = Character('Артём', color = '#4f74ae', image = 'morg', screen ='say_island_side')
define si = Character('Никита', color = '#a1a882', screen = 'say_island')
# Боковое изображение моргана до острова(дописать)
image side morgan surprised = "images/sprites/morgan surprised.png"

image side morgan csweat = "images/sprites/morgan csweat.png"
image side morgan lstress = "images/sprites/morgan lstress.png"
image side morgan sstress = "images/sprites/morgan sstress.png"
image side morgan awsmile = "images/sprites/morgan awsmile.png"
image side morgan confusion = "images/sprites/morgan confusion.png"
#image side morgan = "image/sprite/morgan "
#image side morgan = "image/sprite/morgan "
#боковое избражение моргана на острове
#image side morg = "image/sprite/morg "
#image side morg = "image/sprite/morg "
#image side morg = "image/sprite/morg "
#image side morg = "image/sprite/morg "
#объявление однотонных фонов
image bg black = "#000"
image bg white = "#fff"

#сплеш
label splashscreen:

    scene bg black with dissolve
    pause 2
    scene bg logo with dissolve
    pause 2
    #scene bg title with dissolve
    #pause 3
    scene bg white with dissolve
    pause 1
return

#игра
####пролог из предыдущей части
label start:
    scene bg black
    show text "пролог" with dissolve
    pause 2
    scene bg studio #with flashbulb #поработать над анимациями перехода красиво
    #кнопка скип, если Артём помнит, что тут

    screen skip_button():
        frame:
            xalign 0.9 ypos 50
            button:
                action Jump("morning") #я не помню, как правильно джамп из кнопки делать
                text "Пропустить"
    show screen skip_button

    show anna angry at center with vpunch
    a "{size=+40}Артёёёёёёёёёёём!{/size}"
    show anna rage
    a "{size=+40}Какого хуя тут происходит!{/size}"
    m surprised "А-Аня?"
    m surprised "Эт-это не то, о чём ты подумала."
    a "Артём, ты ахуел?"
    m lstress "Никита, скажи ей, что она всё неправильно поняла!"
    show anna rage at left with move
    show sausage confusion at right with moveoutright
    s "Аня, ты неправильно всё поняла."
    a "Что я неправильно поняла?"
    a "Вы тут значит сосались, пока меня не было, да?"
    m "Нет! Аня, нет!"
    show anna angry
    a "Артём, ты меня не обманешь! Я всё видела!"
    m awsmile "Ну да, мы поцеловались разок... {w = 1} Но это ничего не значит!"
    show sausage awsmile "Вот именно, всего разок, Аня!"
    show anna surprised
    a "А что делают презервативы на полу?"
    #play music "sadmusic.mp3" #грустная музыка
    show anna surpsad
    show anna shok
    a "{cps=*.5}Только не говорите, что вы...{/cps}"
    show sausage sstress with hpunch
    m sstress "..."
    "*неловкое молчание*"
    s "Я пожалуй пойду."
    hide sausage with moveinleft
    show anna surpsad at center with move
    a "Артём, скажи, пожалуйста, что это не то, о чём я подумала."
    m confusion "Аня... {w=1} Я пытался это всячески скрыть."
    m confusion "Аня, прости."
    show anna sad
    a "*молчит*"
    m confounded "Мы с Никитой очень давно...{nw}" #тут надо сделать резкий обрыв, чтобы после того, как пропечаталось, начала сразу говорить Аня.
    a "Артём, не продолжай."
    a "Можешь не возвращаться домой."
    a "Я привезу твои вещи завтра."
    a "{cps=*.5}Прощай.{/cps}"
    m csweat "Аня..."
    hide anna with moveinleft
    scene bg black with Dissolve(2.5)
    #stop music with fadeout 0.5

label morning:
    hide screen skip_button
    scene bg black
    show text "12 декабря 2019 года" with Dissolve(.5)
    #scene bg room with #я придумаю эффеккт позже
    return
