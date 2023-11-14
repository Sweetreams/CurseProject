# hf - HiddenFolks (поиск предметов)
# используется в паре с модулем 7dots.rpy

# пример использования:
init 1:
    
    # определим фон игры, время игры в секундах
    # и зададим параметры игры - спрайты и положение для собираемых предметов
    $ hf_init("search_key_bg", 200,
        ("key_for_door", 1013, 705, _("Мишка")),
        # НЕОБЯЗАТЕЛЬНЫЕ ПАРАМЕТРЫ:
        # включаем смену курсора при наведении
        mouse=True,
        # включаем инвентарь с убиранием из него найденных предметов
        inventory=False,
        # отключаем подсказки
        hint=False,
        # включаем подсветку предмета при наведении
        # уменьшаем размеры ячеек инвентаря, чтобы не мешали собирать предметы
        w=200,
        h=200
    )

# затем будет вызов игры:
    # $ hf_start()
    
    # количество несобранных предметов будет в hf_return

    # трансформ для перемещения подсказки
    transform hf_hint_at():
        anchor(.5, 1.25)
        function hf_hint_at_f

    # стиль для подсказки
    style hint_style is frame:
        # жёлтый фон растягивается под размеры текста
        background Frame("#fe9", 0, 0)
        # отступы от краёв до текста
        xpadding 20
        ypadding 15

    # стиль для текста подсказки
    style hint_style_text is text:
        color "#014"
        outlines []

init python:
    # автоматическое объявление спрайтов (включая webp)

    # координаты мышки
    def hf_hint_at_f(trans, st, at):
        trans.pos = renpy.get_mouse_pos()
        return 0

# НАСТРОЙКИ
    # надо ли менять курсор при наведении
    hf_mouse = True

    # нужно ли выводить подсказку
    hf_hint = False

    # True - найденные предметы добавляются в инвентарь
    # False - найденные предметы исчезают из инвентаря
    # None - инвентарь не отображается
    hf_inventory = None

    # трансформ для подсвечивания при наведении
    # может быть, например, brightness(.05)
    hf_hover = None

    # имя папки со спрайтами игры в директории images плюс пробел
    hf_dir = "sprite_for_search"

    # размеры предметов в инвентаре
    hf_w, hf_h = 300, 300

    # размеры таймбара
    hf_t_w, hf_t_h = 1040, 32

    # отступ предметов от краёв инвентаря
    hf_xpadding = 20
    hf_ypadding = 40

    # положение окна инвентаря
    hf_xalign = .5
    hf_yalign = .05

    # положение таймбара
    hf_t_xalign = .5
    hf_t_yalign = .01

# ВНУТРЕННИЕ ПЕРЕМЕННЫЕ
    # время, за которое нужно собрать предметы
    hf_time = 5

    # время, которое нужно обнулить для анимации
    hf_bar = 100

    # режим игры (False - режим фона)
    hf_game_mode = False

    # предметы, которые нужно найти
    hf_needed = []

    # предметы, которые уже нашли
    hf_picked = []

    # фон игры
    hf_back = "black"

    # нужно ли перекрашивать таймбар (осталась четверть времени)
    hf_warning = False

    # количество несобранных предметов
    hf_return = 0

    # изначальное количество предметов
    hf_max_count = 0

    # инициализация игры
    def hf_init(bg, time, *args, **kwargs):
        global hf_needed, hf_picked, hf_back, hf_time, hf_bar, hf_max_count
        # обнуляем списки и переменные
        hf_needed = []
        hf_picked = []
        hf_back = bg
        hf_time = time
        hf_bar = 100
        # добавляем в список предметы, которые нужно найти
        for item, x, y, h in args:
            hf_needed.append((item, x, y, h))
        hf_max_count = len(hf_needed)
        # применяем необязательные параметры игры
        # по сути меняем значения похожих переменных,
        # но только они должны начинаться с hf_
        for k, v in kwargs.items():
            kk = "hf_" + k
            if kk in globals().keys():
                globals()[kk] = kwargs.get(k)

    # показать игру в виде фона на слое master
    def hf_bg():
        store.hf_game_mode = False
        show_s("HiddenFolks")

    # спрятать игру-фон
    # но сначала показать, если игра экран скрыт
    def hf_hide():
        hf_bg()
        renpy.with_statement(None)
        hide_s("HiddenFolks")

    # запустить игру
    # если задан какой-то эффект, то сначала показать игру с ним
    def hf_start(effect=None):
        store.hf_game_mode = False
        store.hf_warning = False
        hf_bg()
        renpy.with_statement(effect)
        store.hf_game_mode = True
        store.hf_return = len(hf_needed)
        renpy.call_screen("HiddenFolks")
        hf_bg()

    # клик по предмету (перенести его в инвентарь или убрать оттуда)
    def hf_click(item, x, y, h):
        store.hf_picked.append(store.hf_needed.pop(hf_needed.index((item, x, y, h))))
        renpy.restart_interaction()
        # осталось собрать
        store.hf_return = len(hf_needed)
    HFClick = renpy.curry(hf_click)

    # меняем цвет таймера
    # или запускаем анимацию уменьшения времени
    def hf_go(warning=False):
        if warning:
            # меняем цвет
            store.hf_warning = True
        else:
            # запускаем анимацию
            store.hf_bar = 0
        renpy.restart_interaction()
    HFGo = renpy.curry(hf_go)


    # текст подсказки
    hf_hint_text = ""

    # меняем текст подсказки
    def hf_set_hint(t=""):
        if hf_hint and hf_hint_text != t:
            store.hf_hint_text = t
            renpy.restart_interaction()
    SetHint = renpy.curry(hf_set_hint)

screen HiddenFolks():
    # фон игры
    add hf_back

    # все предметы на экране
    for i, x, y, h in hf_needed:

        $ item = hf_dir + " " + i
        # предмет-кнопка
        imagebutton:
            style "empty"
            # спрайт предмета
            idle item
            # положение предмета (координаты его центра)
            pos(x, y)
            # наведение на пиксель
            focus_mask True
            # все действия только в режиме игры
            if hf_game_mode:

                # меняем курсор при необходимости
                if hf_mouse:
                    mouse "hand"

                # если включено выделение при наведении
                if not hf_hover is None:
                    # если есть картинка для выделенного объекта, то выводим ее
                    if has_image(item + " hover"):
                        hover item + " hover"
                    # иначе подсвечиваем заданным в настройках трансформом
                    else:
                        hover At(item, hf_hover)

                # меняем текст подсказки при наведении курсора
                hovered SetHint(h)
                unhovered SetHint()

                # обработка клика
                action HFClick(i, x, y, h)

    # анимация таймера
    if hf_game_mode and hf_time > 0:
        # активация таймера
        timer .01 action HFGo()
        
        # проигрыш по таймеру
        timer hf_time repeat True action SetHint(), Return()

        # всё собрали, уходим (Return()() из def больше не работает)
        if hf_return < 1:
            timer .01 repeat True action SetHint(), Return()

        

