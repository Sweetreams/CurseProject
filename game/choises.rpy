label choise_1:
    nvl clear
    menu (nvl = True):
        "Пойти в столовую":
            jump go_to_dining_room
        "Осмотреть кабинет":
            jump go_to_cabinet
        "Осмотреть прихожу":
            jump go_to_hallway
        "ОБЕД" if (complete_cabinet == True and complete_dining_room == True and complete_hallway == True):
            jump end_1_chapter

label choise_2:
    nvl clear
    menu (nvl = True):
        "Спросить про Никиту":
            jump to_ask_about_nikita
        "Спросить про Сергея":
            jump to_ask_about_sergey
        "Спросить про Василису":
            jump to_ask_about_vasilisa
        "Выйти" if (complete_ask_vasilisa == True and complete_ask_sergey == True and complete_ask_nikita == True):
            jump continue_after_choise_2