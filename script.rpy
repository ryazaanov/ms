﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define a = Character('Аня', color = '#de8545')
define m = Character('Артём', color = '#4f74ae', image = 'morgan', screen = 'say_side')
define s = Character('Никита', color = '#67835b')
define st1 = Character('Сотрудник таможни', color = '#000')
define st2 = Character('Сотруднца таможни', color = '#000')
define d = Character('Собака', color = '#000')
define p = Character('Пилот', color = '#000')
define mi = Character('Артём', color = '#4f74ae', image = 'morg', screen ='say_island_side')
define si = Character('Никита', color = '#67835b', screen = 'say_island')
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

#видеокартинка в главном меню
init -2:
    image beach = Movie(play="gui/main_menu.webm",size=(1920,1080))

label main_menu:
    scene beach
    jump main_menu_screen
#заставка
label splashscreen:

    scene bg black with dissolve
    pause 2
    scene bg logo with dissolve
    pause 2
    scene bg white with dissolve
    pause 1
    scene bg title with dissolve
    pause 2
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


label morning:
    hide screen skip_button
    scene bg black
    show text "12 декабря 2019 года" with Dissolve(.5)
    #scene bg room with #я придумаю эффеккт позже
    "Артём просыпается после пятого по счёту за этот месяц бухлострима и видит пустую комнату."
    m tired "Как же сильно болит голова..."
    m tired "А ещё эта ёбанная изжога..."
    m tired "Нужно выпить таблетку от головы и Омепразол."
    "Артём пытается встать, но его попытка безуспешна."
    m tired "Слишком сильная боль, невозможно даже думать, не то, что встать."
    m tired "Плохая идея была устраивать целый марафон бухлостримов."
    m tired "За 2 месяца мы столько их провели, я даже сосчитать сейчас не смогу."
    m tired "Чувствую, что ещё один и моя печень повесится."
    m tired "Надо завязать с ними на время, это уже невозможно продолжать."
    m tired "Так же невозможно, как и терпеть эту боль."
    "В комнату заходит Никита."
    show sausage normal with Dissolve(.5)
    s "О, ты уже проснулся, я посмотрю. Доброе утро."
    m lstress  "Если сейчас доброе утро, то тогда я не хочу знать, что такое плохое."
    s "Держи свой набор первой помощи, тут Омепразол, Ибупрофен и стакан воды."
    "Никита поставил стакан с водой и положил таблетки на тумбочку."
    m tired "А я смотрю ты подготовился к моему пробуждению."
    s "Ну не в первый раз такое."
    m tired "А ты сам бодрячком... Везет. И спасибо за подгон."
    show sausage smile
    s "Артём, у меня есть идея."
    s "Давай короче возьмём и махнём на отдых. Что думаешь, об этом?"
    m lstress "Ничего сейчас не хочу, а ещё до лета долго ждать."
    s "А кто сказал, что мы полетим летом? Как насчёт на Новый год!"
    m lstress "А как же видосы, стримы?  Новогодний стрим - это почти традиция."
    show sausage sad
    s "Его никто и не отменял, будет новогодний спешл, а не скучный стрим из квартирки."
    s "Да и оставь ты эти дела на потом. Разве ты не устал от всего этого?"
    s "Разве не пора отдохнуть?"
    m think "Нууу."
    m tired "Всё равно, надо видео сделать, да и обычные стримы не отменялись."
    s "Так те же стримы можно проводить и там, можно сделать серию видосов про путешествие."
    s "Неплохо, неправда ли?"
    m "Звучит неплохо, но ещё не убедил."
    s "Чего тебе больше хочется?"
    show sausage happy
    s "Подумай, как это зайдёт аудитории, может даже новая появится!"
    m "Допустим уговорил."
    m "И куда ты хочешь полететь?"
    s "Как насчёт Карибских островов? Можно будет снять видос про пиратов карибского моря."
    m smile "А что, хорошая идея, Никита."
    s "Капитан Никита, прошу заметить!"
    m smile "Мы ещё не на островах, пират."
    s "Хорошо, Капитан Морган, тогда я пойду куплю билеты и посмотрю нам отель!"
    m "Ок."
    hide sausage with dissolve
    "Никита покинул комнату и Артём остался один на один со своими недугами и мыслями о предстоящем отпуске."
    m "Новый год на островах, значит."
    m "Это влетит нам в копеечку."
    m "Надеюсь, после такого отпуска у нас останутся хотя бы деньги на еду."
    m tired "И вообще я хотел купить новый микрофон и камеру."
    m tired "Видимо придётся отложить эту покупку на потом."
    m tired "Ээээ..."
    m tired "Пора пить лекарства, пока хуже не стало."
    scene bg black with Dissolve(2.5)
    #scene - сцена заканчивается и дейтвие переносится к Никите
    "Артём выпивает лекарства и ему почти сразу становится лучше."
    m "Какое облегчение."
    "Артём лежит в ожидании пока боль окончательно пройдёт, чтобы без проблем встать с кровати и пойти вместе с Никитой посмотреть отели."
    "Боль окончательно прошла и Артём с лёгкостью встаёт с кровати."
    "Он выходит из комнаты, и подходит к Никите, сидящему за компом."
    m "Чё делаем?"
    show sausage normal
    s "О, тебе уже лучше стало?"
    m "Да, намного, спасибо."
    show sausage smile
    s "Всегда пожалуйста."
    m "Чё делаем?"
    show sausage normal
    s "Смотрю отели."
    m "А билеты ещё не брал?"
    s "Нет, но уже взял путёвку на месяц."
    m surprised "Ты хочешь там провести месяц?"
    s "Да, норм же."
    s "И отдохнуть успеем и ролики снять."
    m lstress "Это можно успеть и за недели 2."
    s "Да ладно, зато как проведём этот месяц."
    show sausage happy
    s "Посмотри лучше, какой отель классный нашёл!"
    m awsmile "Тебе он понравился из-за того парня на шезлонге?"
    show sausage blush
    s "Что?! Нет!"
    show sausage smile
    s "Из-за того парня у стойки!"
    m awsmile "Весомый аргумент, чтобы заселиться в этот отель."
    show sausage happy
    s "Я вот также думаю, но есть ещё такой, тут немного дешевле, чем в том, да и условия жизни соответствуют цене."
    m "Да хз, если честно, не шарю за такое. Ты знаешь, мне главное чтобы тараканов не было и спать не на полу."
    m "И по цене, чтобы норм было. По возвращении думаю взять новый микрофон и камеру."
    show sausage surprised
    s "А со старыми что?"
    m "Неудовлетворяют мои стримерские потребности."
    show sausage normal
    s "Ну если ты не против, тогда я делаю бронь в том, где парень у стойки."
    s "Он по всем парметрам хорош."
    m awsmile "Парень или отель?"
    show sausage confusion
    s "Отель!"
    m "Хорошо, как знаешь."
    m "Начнём собираться потихоньку?"
    show sausage normal
    s "Да, надо будет ещё подписчиков об этом оповестить."
    m "Сделаю видос в тикток."
    s "Наконец-то наш первый совместный отдых."
    hide sausage with dissolve
    scene bg black with Dissolve(2.5)
#тут аэропорт, зачем нам эта фигня лабел
    scene bg black
    show text "20 декабря 2019" with dissolve
    pause 2
    scene airport with dissolve
    "Артём с Никитой прибыли в аэропорт и продвигаются к стойкам регистрации."
    m lstress "Я же говорил, что будет очередь!"
    show sausage normal with dissolve
    s "Не ссы, рассосется в два счета!"
    m lstress "Странные у тебя понятия времени, если ебаный час у тебя - два счета."
    show sausage at left with move

    d "гав гав"
    m surprised "Что за хуйня?"

    show st1 at center with dissolve
    st1 "Добрый день, собака что-то унюхала в вашем чемодане."
    m surprised "Что?! В моем чемодане почти пусто!"
    s "Черт, Артем, ты что кокс не вытащил перед вылетом?"
    m lstress "Никита, это несмешно!"
    show sausage smile
    s  "Хотите анекдот расскажу."
    m "Ну вот опять."
    s "Заходит как-то в бар ахаххаххаха..."
    s "...сотрудник таможни с собакой аххахаххахаха и чёрный аххахахахах..."
    s "...и и собака начинает лаять аххахахаххах на чёрного ахаххаха..."
    st1 "Прекратите, пожалуйста."
    s "Но я же ещё не дорассказал ахахахахах."
    st1 "Мне всё равно."
    st1 "Прошу вас пройти со мной к стойке охраны, там мы вас досмотрим."
    hide sausage with dissolve
    hide staff with dissolve
    "Артём с Никитой подошли к стойке охраны и отдали свои сумки на проверку."
    show staff think at right
    st1 "Странно, все чисто. А у вас случаем нет собаки?"
    m "Есть. В смысле... была."
    show staff normal at right
    st1 "Тогда понятно, Рекс у нас новенький, он иногда реагирует на чужих собак."
    st1 "Простите за беспокойство, можете вернуться к стойке регистрации, я проведу вас без очереди."
    show sausage happy at left
    s "Видишь, что не делается - все к лучшему! Но кокс в следующий раз, конечно перепрячь."
    m lstress "Дурак."
    hide staff with dissolve
    hide sausage with dissolve
    "Охраник провёл их к стойке регистрации."
    show staffessa normal
    st2 "Паспорта, пожалуйста"
    st2 "Чемоданы ставьте на ленту"
    st2 "Вы бронировали места заранее?"
    menu:
        "Да":
            $ registration = True
            m "Да *показывает места*"
            show sausage smile
            s "Решили сесть у окошка, как влюбленные голубки"
            m confusion "Да, именно так."
            st2 "Хорошо, можете проходить дальше."
            st2 "Приятного полёта, спасибо, что пользуетесь нашими авиалиниями."
        "Нет":
            $ registration = False
            m "Нет, не успели"
            st2 "Хорошо, к сожалению, соседних мест не осталось, есть одно у окна и одно в проходе."
            show sausage sad
            s "Эх, не попускать мне слюни тебе на плечо, пока сплю."
            m "Нам подходит."
            st2 "Хорошо, тогда держите ваши билеты."
            "Сотрудница передала 2 билета Артёму."
            st2 "Приятного полёта, спасибо, что пользуетесь нашими авиалиниями."
    hide staffessa
    "Пройдя регистрацию, они отправились в зону ожидания."
    m "С этими регистрациями и внеплановыми проверками мы совсем потеряли время."
    m "До вылета осталось совсем немного, пошли к посадочному трапу."
    show sausage normal
    s "Да подожди ты, времени ещё достаточно."
    m "Я так не думаю."
    s "Давай вот перед посадкой зайдём в дюти-фри?"
    menu:
        "Давай":
            $ alcohol = True
            m "Ну пошли, если мы опоздаем - это будет твоя вина."
            show sausage normal
            s "Хэхэ"
            "В дюти-фри на удивление не было очереди и вообще самих людей, что было довольно странно."
            s "Не хочешь взять спиртное?"
            m "Только, если хорошее."
            s "Балтика 9 пойдёт?"
            m "Лучше уж Cтрайк."
            s "Ну давай тогда ни тебе, ни мне. Может коньяк?"
            m "Я только за, но давай быстрее, время!"
            s "Хорошо."
            "Никита берёт пятизвёздночный коньяк с полки и неспеша идёт к кассе и, спустя мгновение, возвращается к Артёму."
            m "А не слишком ли?"
            s "Да ладно, один раз живём, нечего так трястись над деньгами."
            m "Ладно, пошли уже, опаздываем."
            s "Как скажешь."
        "Нет":
            $ alcohol = False
            m "Давай, может ещё в пятёрочку сходим?"
            m "Пошли уже."
    scene bg black with Dissolve(1)
    "Покинув дюти-фри, они направились в сторону посадочного трапа."
    "Борт самолёта оказался на удивление пустым для обоих."
    scene plane with dissolve
    m "А почему тут так пусто, вылет же через несколько минут?"
    m "Мы случайно не ошиблись самолётом?"
    show sausage normal
    s "Нет, не ошиблись."
    m "Тогда очень странно, что тут так пусто, не думаешь?"
    s "{cps=*2}Да не, всё заебумба, это точно не сюжетный ход, чтобы не убивать кучу людей при авиакатастрофе.{/cps}{nw}" #фраза сама себя скипнет.
    m "Что ты сейчас сказал?"
    if registration:
        s "Да хз. Короче все просто, наверное, боятся пиратов карибского моря."
        m "Возможно."
    else:
        s "Да какая разница, зато можно сесть рядом, как и хотели."
        m "И вправду."
    p "Уважаемые пассажиры, усаживайтесь по удобней, мы начинаем взлёт."
    p "Просьба не покидать ваши места, пока мы не поднимимся в воздух."
    "Артём с Никитой садятся в кресла и пристёгиваются."
    s "Ну что ж, полетели."
    "Самолёт разгоняется на взлётной полосе и поднимается в небо."
    s "Полёт будет долгим, поэтому я на боковую, тебе того же советую."
    s "Увидимся уже на карибах."
    m "Добрых снов."
    "Никита надевает подушку на шею и погружается в сон."

    m "\"Неужели мы летим отдыхать?\""
    m "\"Даже не верится, что вот так вот идут события.\""
    m "\"2 месяца назад, мы даже думать о совместном отдыхе не могли, а сейчас летим вместе на курорт.\""
    m "\"Всё складывается так хорошо, что даже не верится в это.\""
    m "\"Надеюсь, что это всё же не сон.\""
    m "\"Попробую тоже уснуть.\""
    hide sausage with dissolve
    "Самолёт начинает сильно трясти."
    p "Уважаемые пассажиры, внимание! Мы находимся в зоне турбулентности, поэтому судно будет трясти."
    p "Просьба ппристегнутся и оставаться на своих местах, а также сохранять спокойствие."
    "Никита проснулся от тряски."
    show sausage
    s "Ох уж эта непогода, поскорее бы прилететь."
    s "Хочу лежать на пляже и пить этот коньяк."
    m "Хотел бы я тоже думать о хорошем в такой ситуации."
    s "Да не парься, ты думаешь, что из-за какой-то турбулентности самолёт упадёт?"
    m "Ну не знаю, по крайней мере я пока умирать не хочу."
    scene bg avaria with hpunch
    "Свет в кабине начал мигать и выпали кислородные маски."
    p "Уважаемые пассажиры, один из двигателей вышел из строя и нам придётся совершить аварийную посадку."
    m "Блять, ахуенный отпуск."
    s "Надевай кислородную маску быстрее."
    p "Пожалуйста, наденьте маски и оставайтесь на своих...{w}"
    #*упали*
    scene bg black #with
    show text "20 декабря 2019 года 15:37.{p} Падение самолёта в Атлантическом океане.{p} Ведутся поиски, но безуспешно." with dissolve:
        xalign 0.5
        yalign 0.5
    pause 3

    return
