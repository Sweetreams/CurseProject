label beginning_second_chapter:
    narrator """Игорь проснулся от яркого луча света в глаза.
    Лениво перевернувшись на другой бок от незакрытого жалюзиями окна,
    он перекинул руку за голову и пролежал так ещё минут 5.
    После этого Игорь едва встав на ноги, нерешительными направился в ванную."""

    narrator """Игорь вышел из ванной
    с полотенцем на голове и направился обратно в спальню,
    где сел на кровать и рассматривал картину на стене, прямо над дверью.
    Посидев ещё немного, он встав с кровати направился к столу у окна."""

    narrator """Пейзаж за окном не сильно изменился.
    Туч больше не было, только ясная погода, но этого было недостаточно,
    чтобы хоть как-то растопить снег на улице."""

    narrator """Тут резко раздался ужасающий
    женский крик из коридора."""
    
    jump choise_3


label out_room:
    narrator """Игорь быстро надел свою одежду и,
    с мокрой головой, выбежал из комнаты,
    почти запнувшись об порог прихожей."""
    jump continue_second_chapter

label not_out_room:
    narrator """Резко развернувшись в сторону двери прихожей,
    Игорь почувствовал страх, который окутал его тело.
    Руки, которые недавно лежали на столе, уже лежали на коленях и тряслись.
    Что-то сильно его напугало, но он не смог понять, что именно."""

    narrator """Вдруг к нему постучали в дверь. Это были сильные и увесистые удары. Игорь направился к двери."""

    narrator """Там стоял Никита, который кричал, чтобы тот выходил, и послышались удаляющиеся шаги."""

    narrator """Игорь, одевшись, вышел из своей комнаты."""

    $ not_exit_room = True
    jump continue_second_chapter

label continue_second_chapter:

    narrator """На полу сидела Василиса, с испуганным
    взглядом она смотрела на открытую дверь спальни Владимира."""

    narrator """Игорь быстро подбежал к Василисе, и,
    опустившись на колени, пытался узнать, что случилось."""

    igor """Василиса, Василиса! Что случилось, что произошло..."""

    narrator """Игорь направил свой взгляд в открытую дверь спальни.
    Там возле кровати столпились Фёдор с Никитой.
    Туда, куда они смотрели, была окровавленная подушка,
    которая лежала на теле Владимира, закрывая лицо.
    В подушке было пулевое отверстие."""

    narrator """Тут Никита обернулся на Игоря, и на его лице читалась
    ужас в перемешку с яростью. Тут он резко крикнул всем"""

    nikita """Быстро все спустились в гостинную и
    разбудите Сергея. Никто никуда не уходит!"""

    narrator """Фёдор, выходя из комнаты, взял под руку Василису
    и направился вниз по лестнице, Игорь шёл следом."""

    narrator """До того, как Никита вернулся, почти все,
    не издавая ни звука, сидели безлицо за круглым столом.
    Одной Василисы не было – она сидела в ванной и громко плакала."""

    narrator """Никита резко отодвинул стул и сел за стол.
    Ударом кулака по столу начал разговор"""

    nikita """Кто же это сделал?! Кто посмел вытворить
    такое нечеловеческое действие? Убийство! Убийство!"""

    narrator """Задыхаясь, продолжал говорить Никита."""

    nikita """Ну, чего молчите? Говорите, кто это сделал?
    Фёдор, неужели ты это сделал?"""

    narrator """Фёдор аж опешил после этого резкого обвинения."""

    fedor """Я, я?! Что ты такое говоришь?
    Если кого и надо обвинять, так это тебя.
    Ты первый нашёл тело, это ты начал стучать
    в двери наших комнат."""

    nikita """Что несёшь? Я пришёл к нему в комнату,
    чтобы разбудить его. Ты же сам вчера слышал его просьбу:
    чтобы я разбудил его рано утром..."""

    narrator """тут своё слово вставил Сергей."""

    sergei """Может, хватит друг друга обвинять.
    Одно точно ясно – один из убийц находится в этом доме,
    и это явно кто-то из нас."""

    narrator """Наступила мёртвая тишина.
    Никита смотрел на лица всех присутствующих"""

    #Таймскип

    narrator """Игорь остался один в гостинной,
    поэтому он решил осмотреться пока-что.
    """

label search_cabinet:

    narrator """Игорь решил пойти в кабинет. Дверь была открыта.
    """
    narrator """Кабинет выглядел немного другим, не таким,
    как в прошлый раз, но без серьезных изменений.
    """
    narrator """Игорь повернулся направо и направился к шкафу с книгами
    возле сейфа. Присев на корточки, он начал осматривать книги,
    стоящие в дубовом шкафу. В течение минуты он заключил,
    что они расставлены в другом порядке,
    словно кто-то их перебирал.
    """
    narrator """Игорь подошел к дубовому
    столу в стиле ампир, стоящему возле окна.
    Шкафчики стола были немного выдвинуты,
    опять же, словно кто-то тут что-то искал.
    """
    narrator """Вернувшись к сейфу и
    попробовав дернуть за серебряную ручку,
    Игорь обнаружил, что сейф не отпирался.
    Возможно, кто-то забрал его содержимое, а возможно и нет.
    Проверить невозможно.
    """
    narrator """Игорь провел еще несколько минут
    в кабинете и вышел.
    """

    $ complete_seacrh_cabinet = True
    jump choise_4

label search_bedroom_vlad:

    narrator """Игорь поднялся на второй этаж и зашел в
    просторную спальню Влада, выполненную в стиле ампир.
    """
    narrator """Постель уже была застелена.
    """
    narrator """На тумбочках подле кровати стояли ночники,
    а возле них лежали журналы про рыбалку.
    """
    narrator """Игорь направился к письменному столу, но
    ничего стоящего для поиска убийцы он там не нашел.
    """
    narrator """Следов взлома на двери не было обнаружено.
    """
    narrator """Комната была недавно полностью убрана.
    """
    narrator """Не найдя ничего подозрительного,
    Игорь вышел из комнаты.
    """

    $ complete_search_bedroom_vlad = True
    jump choise_4

label search_kitchen:
    narrator """Придя в столовую, Игорь направился на кухню,
    где начал внимательно осматривать столешницу.
    На столешнице он заметил белый развод, как
    будто кто-то пролил что-то и потом неаккуратно вытер это.
    """
    narrator """Игорь вспомнил, как только пришёл к Владу,
    заметил Сергея, который держал какую-то бутылочку.
    Возможно, это как-то связано.
    """
    narrator """Игорь тут же открыл тумбочку с мусоркой и заметил,
    что она была полностью пуста.
    Надо будет спросить, кто выкинул мусор.
    """
    narrator """Игорь направился к столу,
    который был полностью убран.
    На нем стояли только цветы и свечи.
    """
    narrator """Игорь вышел из столовой.
    """

    $ complete_search_kitchen = True
    jump choise_4

label continue_after_choise_4_second_chapter:
    narrator """ф"""
    nikita """ф"""
    narrator """ф"""
    nikita """ф"""
    igor """ф"""
    narrator """ф"""
    sergei """ф"""
    igor """ф"""
    sergei """ф"""
    fedor """ф"""
    narrator """ф"""
    igor """ф"""
    narrator """ф"""
    narrator """ф"""
    narrator """ф"""
    igor """ф"""
    nikita """ф"""
    narrator """ф"""
    narrator """ф"""
    narrator """ф"""
    narrator"""ф"""

    jump choise_5

label accuse_fedor:
    narrator"""ф"""

label accuse_sergei:
    narrator"""ф"""

label accuse_nikita:
    narrator"""ф"""

label accuse_vasilisa:
    jump ending_1
