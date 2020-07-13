# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define a = Character('Аня', color = '#000000')
define m = Character('Артём', color = '#000000', image = 'morgan')
define s = Character('Никита', color = '#000000')

# Боковое изображение моргана(дописать)
image side morgan surpised = "image/sprite/morgan surpised"
image side morgan confounded = "image/sprite/morgan confounded"
image side morgan csweat = "image/sprite/morgan csweat"
image side morgan lstress = "image/sprite/morgan lstress"
image side morgan sstress = "image/sprite/morgan sstress"
image side morgan awsmile = "image/sprite/morgan awsmile"
image side morgan confusion = "image/sprite/morgan confusion"
image side morgan = "image/sprite/morgan "
image side morgan = "image/sprite/morgan "
#объявление однотонных фонов
image bg black = "#000"
image bg white = "#fff"

#сплеш
label splashscreen:

    scene bg black with dissolve
    pause 2
    scene bg logo with dissolve
    pause 2
    scene bg title with dissolve
    pause 3
    scene bg white with dissolve
    pause 1
return

#игра
####пролог из предыдущей части
label prologue:
    scene bg black
    show text "пролог"
    scene bg room with flashbulb #поработать над анимациями перехода красиво
    #кнопка скип, если Артём помнит, что тут
    screen skip_button():
        frame:
            xalign 0.9 xpos 50
            button:
                action Jump("home") #я не помню, как правильно джамп из кнопки делать
                text "Пропустить"
    show anna angry at center with vpunch
    a "{size = +40}Артёёёёёёёёёёём!{/size}"
    show anna rage at right
    a "{size = +40}Какого хуя тут происходит!{/size}"
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
    play music "sadmusic.mp3" #грустная музыка
    show anna surpsad
    show anna shok
    a "{csp = *.5}Только не говорите, что вы...{/csp}"
    show sausage sstress with hpunch
    m sstress "..."
    "*неловкое молчание*"
    s "Я пожалуй пойду."
    hide sausage with moveinleft
    show anna surpsad at center with move
    a "Артём, скажи, пожалуйста, что это не то, о чём я подумала."
    m confusion "Аня... {w = 1} Я пытался это всячески скрыть."
    m confounded "Аня, прости."
    show anna sad
    a "*молчит*"
    #config.default_text_cps = 2 возможно - это вообще не нужно
    m confounded "Мы с Никитой очень давно... {nw}" #обрыв
    a "Артём, не продолжай."
    a "Можешь не возвращаться домой."
    a "Я привезу твои вещи завтра."
    a "{csp = *.5}Прощай.{/csp}"
    m csweat "Аня..."
    hide anna with moveinleft
    scene bg black with dissolve(2.5)
    stop music fadeout 0.5 #вот тут наверное надо остановить грустную песню

label home:
    scene bg black
    show text "12 декабря 2019 года"
    return
