label choise_1:
    menu (nvl = True):
        "Пойти в столовую":
            jump go_to_dining_room
        "Осмотреть кабинет":
            jump go_to_cabinet
        "Осмотреть прихожу":
            jump go_to_hallway
        "ОБЕД" if (complete_cabinet == True and complete_dining_room == True and complete_hallway == True):
            "ХУЙ"

label choise_2:
    nvl clear
    menu (nvl = True):
        "Спросить про Никиту":
            jump to_ask_about_nikita
        "Спросить про Сергейя":
            jump to_ask_about_sergey
        "Спросить про Василису":
            jump to_ask_about_vasilisa
        "Выйти":
            jump continue_after_choise_2