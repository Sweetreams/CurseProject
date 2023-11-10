# Вы можете расположить сценарий своей игры в этом файле.
# Определение персонажей игры.
init -2:
    image mm_bg = Movie(play="images/mm/main_manu_with_label.webm")
    image car_in_bg = "images/bg/notepad_in_car.png"
    #style default:
        #outlines [ (absolute(1), "#fff", absolute(0), absolute(0)) ]
define narrator = nvl_narrator
define igor = Character('Игорь', kind=nvl)
define vladimir = Character('Владимир', kind=nvl)
define sergei = Character('Сергей', kind=nvl)
define vasilisa = Character('Василиса', kind=nvl)
define fedor = Character('Фёдор', kind=nvl)
define men = nvl_menu

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
    narrator "{cps=20}Трепетные, белоснежные хлопья снега медленно спускались с звёздного небосвода, обрамляя землю необычными, на вид, сугробами. Никогда ранее зеленые деревья не окутывала столь густая белоснежная пелена, и поражаешься, как так быстро мог измениться пейзаж. Непроходимая дорога встречала нас, куда не посмотришь – темень Январской зимы. Единственные звуки, которые проникали в эту мёртвую тишину, были шорох снега под шинами и задыхающийся мотор машины. Освещение фонарей стало более бледным, тусклым, словно его силы истрачивались с каждым километром пути. Три долгих дня истомленный хвойный лес окутывался смертельным молчанием.лес окутывался по смертельной мере белоснежным молчанием.{/cps}"
    nvl clear
    
    sergei "qwe"
    vasilisa "qwe"
    fedor "qwe"

    nvl clear
    window show

    "safsdgfsd"
   

