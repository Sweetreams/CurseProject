﻿# Вы можете расположить сценарий своей игры в этом файле.
# Определение персонажей игры.

init -2:
    image mm_bg = Movie(play="images/mm/main_manu_with_label.webm")
    image car_in_bg = "images/bg/notepad_in_car.png"
    image bg_in_car = "images/bg/bg_in_car.png"
    image bg_forest = "images/bg/bg_forest.png"
    image bg_for_ya_xz = "images/bg/bg_for_ya_xz.png"
    
    #style default:
        #outlines [ (absolute(1), "#fff", absolute(0), absolute(0)) ]
define narrator = nvl_narrator
define igor = Character('Игорь', kind=nvl)
define vladimir = Character('Владимир', kind=nvl)
define sergei = Character('Сергей', kind=nvl)
define vasilisa = Character('Василиса', kind=nvl)
define fedor = Character('Фёдор', kind=nvl)
define nikita = Character('Никита', kind=nvl)
define voditel = Character('Водитель', kind=nvl)
define menu = nvl_menu

init python:
    sound_vachine = "music/sound_vachine.mp3"
    off_sound_vachine = "music/off_sound_vachine.mp3"
    bg_sound = "music/bg_sound.mp3"
    sound_write = "music/asd.mp3"
    

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
label main_menu:
    scene mm_bg
    jump main_menu_screen
    play sound musnormal
# Игра начинается здесь:
label start:
    
    
    scene car_in_bg with fade:
        pause 10.0

    stop music fadeout 0.5
    play music bg_sound loop volume 5.0
    play sound sound_vachine noloop


    play sound sound_write loop

    narrator """{cps=20}Трепетные, белоснежные хлопья 
    снега медленно спускались с звёздного небосвода,
    обрамляя землю необычными, на вид,
    сугробами. Никогда ранее зеленые
    деревья не окутывала столь густая
    белоснежная пелена, и поражаешься,
    как так быстро мог измениться пейзаж.
    Непроходимая дорога встречала нас,
    куда не посмотришь – темень Январской зимы.
    Единственные звуки, которые проникали в эту
    мёртвую тишину, были шорох снега под шинами
    и задыхающийся мотор машины. Освещение фонарей
    стало более бледным, тусклым, словно его силы
    истрачивались с каждым километром пути.
    Три долгих дня истомленный хвойный лес окутывался
    смертельным молчанием.лес окутывался по смертельной
    мере белоснежным молчанием.{/cps}"""
    
    scene bg_in_car
    nvl clear
    stop sound
    play sound off_sound_vachine noloop
    # TODO: Добавить звук заглужение мотора
    narrator """Спустя какое-то время, звук двигателя заглох.
    Водитель обернулся на заднее сидение и произнёс"""
    
    voditel "\nПриехали"

    nvl clear


    narrator """Петров Игорь легким движением
    руки закрыл свой потрепанный на вид дневник,
    сделанный из телячьей кожи цвета черный тмин,
    с выгравированным на нём именем обладателя.
    Поправил своё тёмно-синее пальто и вышел из машины.
    """
    igor "\nСпасибо вам, всего доброго."

    scene bg_forest

    nvl clear
    jump mansion_main






label mansion_main:
    
    # TODO: Звук шагов
    narrator """Добравшись до особняка,
    он начал взбираться по засыпанной снегом белой лестнице.
    Перед ним пристал тамбур, где он быстро отряхнулся
    от прилипшего к нему снега.
    """

    narrator """За массивной дубовой дверью
    его поджидал Горелов Владимир, хозяин особняка.
    """

    scene bg_for_ya_xz

    nvl clear

    narrator """Владимир, обернувшийся,
    раскинул руки, чтобы обнять своего
    старого приятеля, с которым они не
    виделись пару лет.
    """

    vladimir """\nЗдравствуй!
    Давно не виделись, как семья?
    как поживает твоя женушка?
    Проходи, раздевайся,
    рассказывай, как доехал?
    """

    narrator """Игорь прошёл в просторную прихожую,
    скидывая с себя верхнюю одежду вместе с
    обувью и вешая на железный крючок мокрое пальто.
    """

    igor """\nЗдравствуй, Володя. Как видишь, всё хорошо.
    Сколько лет мы с тобой не виделись? Что о семье?
    Ты бы знал, как старший вырос, с меня ростом уже стал, в колледж пошёл.
    Младший только недавно в школу начал ходить.
    С Ларисой уже всё хорошо.
    Помнишь, я тебе писал, что она сильно заболела?
    Выздоровела, жива и здорова.
    """

    nvl clear

    vladimir """\nНу хорошо,
    проходи в гостиную, да-да, туда.
    Почти все уже в сборе.
    Я подойду попозже, дождусь Никиту Петрова.
    Да, того самого, с которым я служил.
    3 года не виделись.
    """

    nvl clear

    narrator """Игорь прошёл дальше в глубь особняка,
    где его встретила светлая гостиная с высокими трёхметровыми
    панорамными окнами и выходом на просторный заснеженный балкон.
    Внутри гостиной находился большой зажженный камин,
    возле которого на черном диване сидели Федор вместе с Василисой.
    Слева от Игоря находилась столовая с кухней, в которой на стуле, возле стола,
    сидел Сергей и разглядывал какую-то небольшую бутылочку.
    Справа находилась лестница на второй этаж.
    """

    nvl clear

    narrator """Федор и Василиса активно о чём-то разговаривали.
    """

    vasilisa """\nА Танечка ему говорит: 
    "Нечего тут ходить без дела, Антонина Петровна,
    займитесь делом уже, хватит уже трогать мою семью...".
    Неужели это Игорюша наш пришел?
    """

    narrator """Федор обернулся после слов Василисы.
    """

    igor """\nЗдравствуй, Василиса, Федор.
    """

    narrator """Игорь пожал руку Федору и плюхнулся на левый край дивана.
    """

    fedor """\nКак доехал? Рассказывай.
    """

    igor """\nКак доехал? Ужасно, полтора дня ехал,
    по кочкам, снег, холод, глохли несколько раз.
    """

    vasilisa """\nУжас, какой. А вот я ехала, так водитель вообще странным оказался. 
    В машине холодно было. Главное, я водителю говорю - "что-то у вас тут холодно, 
    не могли бы вы включить обогрев?", а он отвечает: 
    "дамочка, не придумываете. Видите, обогрев на максимум стоит, как я вам еще обогрею машину?". 
    А я вижу, что не повернут до конца обогрев, а он сидит напыщенный в своей дорогой шубе...". 
    А вот и опоздавший с именинником.
    """

    nvl clear

    narrator """Игорь посмотрел налево.
    Там в проеме стояли Владимир и Никита.
    """

    vladimir """\nПриглашаю всех пройти в столовую.
    """

    narrator """Владимир, дополняя своё приглашение,
    театрально жестом указал, куда идти.
    """

    nvl clear
    narrator """Кухня наполнилась приятным ароматом горячего вина
    и пряных блюд. На стол расположились разнообразные закуски,
    от сыров и колбас, до свежих овощей и маринованных грибов.
    """

    narrator """Все расселись по местам:
    в центре стола Владимир, Федор напротив Никиты,
    Василиса - напротив Игоря, Сергей - по соседству с Василисой.
    """

    nvl clear

    vladimir """\nВыражаю благодарность всем,
    кто присутствует в этот холодный вечер
    в моем скромном доме. Я решил отметить
    этот праздник вместе с вами, моими давними друзьями,
    с которыми я знаком уже не менее 25 лет.
    Давайте выпьем за это.
    """

    narrator """Застолье начиналось с медленного
    налива вина в стеклянные бокалы,
    которые, налитые до краев, звенели при каждом чоканье.
    Скромно сидя одна, Василиса расплакалась от нахлынувших чувств.
    """

    narrator """Очень впечатлительная женщина,
    то очень громко будет смеяться с какую-нибудь несмешной шутки,
    то расплачется на вручении дипломов за прохождение курсов "вышивания крестиком".
    """

    narrator """Стол поделился на группы.
    Владимир и Никита, жестикулируя,
    громко что-то обсуждали. Василиса
    неуклюже достала из кармана розовый платок,
    чтобы вытереть слезы.
    """

    narrator """Игорь даже не притронулся к бокалу,
    лишь сидел и глупо улыбался, тыкая вилкой в салат.
    """

    # TODO: Типо прошло время 

    nvl clear

    narrator """Владимир, пристав хлопнув в ладоши,
    все сидящие за столом обратили внимание на него.
    Владимир, продолжая держать руки, сказал:
    """

    vladimir """\nПредлагаю всем перейти в гостиную.
    """

    narrator """Звук скрежетания стульев раздался хором,
    и все зашагали в столовую, где уже кто-где сидели и общались.
    Владимир, Сергей и Василиса сидели за круглым столом.
    Игорь и Федор за диваном напротив камина, а Никита отошел на время.
    """

    narrator """Пробило 9 вечера
     и тогда Владимир сказал:
    """

    vladimir """\nНу хорошо, предлагаю всем заняться своими делами.
    Чувствуйте себя как дома.
    """

    narrator """Владимир удалился в направлении прихожей.
    Все разошлись по своим делам.
    """

    jump choise_1

    nvl clear

## TODO: Въебать карту бля



## РАЗГОВОР В СТОЛОВОЙ С ФЁДОРОМ
label go_to_dining_room:

    narrator """Игорь решил вернуться обратно в столовую.
    Лениво встав с дивана, он прошёл рядом с камином и папоротником.
    Повернув направо, он зашёл на кухню,
    где встретил Фёдора, который энергично ходил по кухне,
    держа в руках чистые тарелки и раскладывая их в открытые шкафчики.
    """

    narrator """На столе ещё лежали грязные столовые приборы,
    тарелки, недопитые бокалы вина, а также задутые свечи и декоративные цветы.
    Игорь подошёл к столу, в правую руку, промеж пальцев взял 4 бокала,
    а в другую поскладывал в горку посуду. Пройдя несколько метров до раковины,
    он сложил в неё всё, что было в руках. Фёдор, протирая стакан в руках,
    до сих пор не замечая Игоря, обернулся на звук.
    """

    fedor """\nОй, да не надо, я сам всё сложу и вымою.
    Сходи лучше в гостиную, поговори с друзьями, которых ты давно не видел.
    """

    igor """\nДа ладно тебе, мы все ели, я помогу прибраться,
    а поговорить смогу и попозже.
    """

    narrator """Игорь правой рукой крутил разные краники,
    пытаясь настроить оптимальную температуру, пару раз обжегся.
    """

    narrator """Они стояли в полной тишине ещё около минуты,
    и тогда Фёдор решил прервать молчание.
    """

    fedor """\nЯ недавно прочитал одну книгу, очень она меня впечатлила.
    Называется "Загадка Ситтафорда" от Агаты Кристи. Интригующая история,
    а развязка-то какая, до самого конца я не мог определить убийцу.
    """

    igor """\nКак странно, что ты заговорил на счёт этой книги,
    ведь я тоже недавно, вот буквально неделю назад прочитал её.
    Если она тебя так впечатлила, могу порекомендовать прочитать
    "Загадку Эндхауза". Необычный детективный роман,
    что-то похожее на "Загадку Ситтафорда", но немного другие лица и обстановка.
    """

    nvl clear

    narrator """Игорь, вымывая посуду, принялся её досконально вытирать,
    после чего он вернулся к столу, чтобы взять оставшуюся посуду и вымыть её.
    """

    fedor """\nЯ пока уберу свечи и цветы. Ты же давно не общался ни с кем,
    можешь у меня поспрашивать, как смогу, так и расскажу, что за эти годы изменилось.
    """
    
    $ complete_dining_room = True
    jump choise_2





label to_ask_about_nikita:
    igor """\nЧем закончилась история с Никитой?
    Помню, как он последние деньги пытался вернуть в покере.
    """
    fedor """\nКак закончилась?
    Видишь же, сейчас все хорошо,
    но вот пару лет назад он окончательно проиграл все деньги,
    начал пить, попал в тюрьму.
    Его жизнь была тяжелой в тот период времени.
    Мы узнали об этом, или, скорее, Владимир
    узнал и позвонил нам в панике: "Помогите собрать залог,
    Никите попало". Мы сразу приехали,
    заплатили и помогли ему встать на ноги. 
    Сейчас у него бизнес, какой-то бутик, и,
    кажется, все идет хорошо.
    """

    $ complete_ask_nikita = True
    jump choise_2

label to_ask_about_sergey:
    igor """\nМне интересно, как жизнь у Сергея?
    """
    fedor """\nКак? Он очень востребованный водопроводчик,
    особенно в эту дикую зиму.
    Наружная температура ниже 30 градусов,
    часто происходят снегопады, и трубы регулярно лопаются.
    Сергей ездит и чинит их с бригадой.
    """

    $ complete_ask_sergey = True
    jump choise_2

label to_ask_about_vasilisa:
    igor """\nМне интересно, как жизнь у Василисы?
    """
    fedor """\nНедавно она пошла учиться в университет на врача.
    Раньше она училась на модистку,
    но теперь решила сменить профессию.
    Она закончила много курсов по шитью разными техниками.
    И удивительно, она даже проходила "профессию сантехника
    для молодых женщин".
    """
    $ complete_ask_vasilisa = True
    jump choise_2



label continue_after_choise_2:
    narrator """Как только последняя посуда оказалась в шкафчике,
    Фёдор, отодвигая стул, сказал Игорю:
    """

    fedor """\nМожешь идти, я сам все закончу.
    Тут осталось протереть только стол.
    """

    narrator """Игорь вернулся в гостиную.
    """

    nvl clear

    jump choise_1




## РАЗГОВОР В КАБИНЕТЕ С НИКИТОЙ
label go_to_cabinet:

    narrator """Игорь решил пройти в личный кабинет хозяина особняка.
    Владимир несколько раз нахваливал свою личную библиотеку и заверял,
    чтобы тот не стеснялся заходить почитать разок-другой.
    """

    narrator """Игорь несколько раз повернул холодную
    металлическую ручку старой деревянной двери и отворил ее.
    Он заметил Никиту, который стоял на коленях рядом с шкафом с книгами,
    очень быстро перелистывая их, в надежде что-то найти. В комнате стоял стол
    на котором находилась печатная машинка, перо, листы бумаги и чернильница.
    Справа от Игоря стоял еще один шкаф с книгами, огромный, почти во всю стену,
    а рядом стоял довольно внушительных размеров сейф.
    """

    narrator """Первым, кто прервал тишину, был Игорь.
    """

    igor """\nЧто-то конкретное ищешь?
    """

    nikita """\nДа, точно, "Фауст" от Гёте.
    Влад нахваливал эту книгу, говорил: "У меня дома есть эксклюзивная версия Фауста,
    хочешь, я тебе ее покажу?" Вот я и ищу ее.
    """

    igor """\nМожет мне тебе помочь?
    Я пришел сюда посмотреть библиотеку,
    как раз помогу разыскать тебе Фауста.
    """

    nikita """\nНет, спасибо не надо, я уже ухожу.
    """

    narrator """Никита встал на ноги и быстрым движением направился вон из комнаты,
    после чего послышались удаляющиеся шаги по лестнице вверх.
    """

    narrator """Игорь еще какое-то время пробыл в кабинете, а после вышел из него.
    """

    $ complete_cabinet = True
    jump choise_1





## РАЗГОВОР В ПРИХОЖЕЙ С ВЛАДИМИРОМ
label go_to_hallway:
    narrator """Игорь видит, как Владимир ползает на корточках и ищет
    что-то на полу в прихожей.
    """
    igor """\nВлад, тебе помощь не нужна? Что потерял?
    """
    vladimir """\nДа ключи не могу найти, вроде бы закрывал дверь за Никитой,
    а теперь не знаю, куда положил. Помоги найти.
    """

    $ hf_init("search_key_bg", 200,
        ("key", 650, 960, _("123")),
    )

    window hide
    # покажем вместе с фоном и фигурки на нём
    $ hf_bg()
    with dissolve

    # запустим игру
    $ hf_start()

    # жёсткая пауза, чтобы игрок перестал кликать и не пропустил результаты
    $ renpy.pause(1, hard=True)

    $ hf_hide()
    with dissolve

    $ complete_hallway = True
    jump choise_1




label end_1_chapter:
    narrator """Владимир заходит в гостинную и объявляет всем:
    """
    vladimir """\nПредлагаю последний раз за этот вечер перейти
    на кухню и продолжить трапезничать.
    """
    narrator """Все согласились и отправились на кухню.
    """
    narrator """Сергей и Фёдор помогали Владимиру раскладывать посуду с едой на стол.
    Сергей отвечал за разливание выпивки, а Фёдор - за выставления еды.
    """
    igor """\nЧто-то меня сильно в сон клонит, пойду прилягу спать.
    """
    vladimir """\nХорошо, мы тоже скоро все пойдём спать,
    а то и правда сильно клонит.
    """
    narrator """Игорь направился к лестнице на второй этаж через гостинную.
    Лестница не была освещена и несколько раз Игорь запнулся о ступени.
    """
    narrator """Комната Игоря была сразу после подъема справа.
    После открытия двери его встречал гардероб, а также две двери:
    одна - ванная, другая - спальня.
    """
    narrator """Сбросив с себя всю одежду, Игорь направился сразу в спальню,
    где тут же плюхнулся на кровать и уснул.
    """
    jump beginning_second_chapter
   

