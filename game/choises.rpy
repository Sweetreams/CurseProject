
label choise_2:
    window show
    nvl clear
    menu (nvl = True):
        ""
        ""
        ""
        "Спросить про Никиту":
            jump to_ask_about_nikita
        "Спросить про Сергея":
            jump to_ask_about_sergey
        "Спросить про Василису":
            jump to_ask_about_vasilisa
        "Выйти" if (complete_ask_vasilisa == True and complete_ask_sergey == True and complete_ask_nikita == True):
            jump continue_after_choise_2

label choise_3:
    window show
    nvl clear
    menu (nvl = True):
        ""
        ""
        ""
        "Выйти из комнаты":
            jump out_room
        "Не выходить из комнаты":
            jump not_out_room

label choise_4:
    window show
    nvl clear
    menu (nvl = True):
        ""
        ""
        ""
        "Осмотреть кабинет":
          jump search_cabinet
        "Осмотреть спальню Влада":
          jump search_bedroom_vlad
        "Осмотреть кухню":
           jump search_kitchen
        "Закончить осмотр" if(complete_seacrh_cabinet == True and complete_search_bedroom_vlad == True and complete_search_kitchen == True):
           jump continue_after_choise_4_second_chapter

label choise_5:
    window show
    nvl clear
    menu (nvl = True):
        ""
        ""
        ""
        "Обвинить Фёдора":
          jump accuse_fedor
        "Обвинить Сергей":
          jump accuse_sergei
        "Обвинить Никита":
           jump accuse_nikita
        # Концовка 1 - Обвинение Игоря
        "Обвинить Василиса" if(complete_seacrh_cabinet == True and complete_search_bedroom_vlad == True and complete_search_kitchen == True):
           jump accuse_vasilisa