from flet import *

# Размеры окна
window_Width = 1200
window_Height = 900

# Цвета
BG = "#222831"
FG = "#393E46"

# Иерархия здесь построена от больших/наружних контейнеров к мелким/внутреним контейнерам
# Для работы радительских контейниров нужно реализовать дочерний контейнер поэтому 
# самые главные контейнеры находятся внизу

def main(page: Page):
    page.window_width = window_Width
    page.window_height = window_Height
    page.bgcolor = BG

    # Счет для денег
    Cash_Account = Container (
        width = 500,
        height = 250,
        bgcolor = FG,
        border_radius = 10,
        margin = margin.only(top=30, bottom=30)     
    )
    # Депозит
    Deposit = Container (
        width = 500,
        height = 250,  
        bgcolor = FG,
        border_radius = 10,
        # margin = margin.only(top=30, bottom=30)
    )

    # Окно с данными о счетах и профиле
    Account_Window = Container ( 
        width = 500,
        height = 250,
        bgcolor = BG,
        
        content = Column (
            controls = [
                # Профиль
                Row (
                    controls = [
                        Container (margin = margin.only(left = 20)),
                        CircleAvatar (
                            width = 100,
                            height = 100,
                            opacity = 0.8,
                            foreground_image_url = 
                                "https://avatars.mds.yandex.net/i?id=73be893fc2426401139e3e0a7f09848bcf505aa2-9181306-images-thumbs&n=13"
                        ),
                        Container (
                            Text("Abdusabirov Davlat", size = 30),
                            width = 600,
                            height = 100,
                            padding = padding.only(top = 30, left = 20), 
                        )  
                    ],
                ), 
                Container(height = 2, width = 500, bgcolor = FG),
                # Даные счетов Cash_Account, Deposit
                Cash_Account,
                Deposit
            ]
        )        
    )

    # Окно платежи/переводы
    Pay_WindoW = Container (

    )

    #  Главное окно
    Main_Window = Container (
            Row (
                controls = [
                    Account_Window,
                    Pay_WindoW
                ]
            )                 
    )

    page.add(Main_Window)

app(target = main)