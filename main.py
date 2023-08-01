from flet import *
import userAPS

user = userAPS.UserAPS("Stiven")

# Размеры окна
window_Width = 1100
window_Height = 800

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

    def transfer(e):
        pass

    def transferToAccount(e):
        pass
    
    def pay(e):
        pass

    # Счет для денег
    Cash_Account = Container (
        width = 500,
        height = 250,
        bgcolor = FG,
        border_radius = 10,
        margin = margin.only(top = 30, bottom = 30)     
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
        bgcolor = BG,
        margin = margin.only(right = 20),
        content = Column (
            controls = [
                # Профиль
                Row (
                    controls = [
                        Container (margin = margin.only(left = 10)),
                        Image (
                            width = 100,
                            height = 100,
                            opacity = 0.8,
                            border_radius = 50,
                            src = user.avatarImg
                        ),
                        Container (
                            Text(user.userName, size = 40),
                            width = 600,
                            height = 100,
                            padding = padding.only(top = 20, left = 10), 
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
    
    # Окно с кнопками
    Button_Container = Container (
        content = Column (
            controls = [
                Container (
                    content = Text("Перевести на счет", size = 30),
                    alignment = alignment.center,
                    margin = margin.only(top = 30),
                    bgcolor = FG,
                    width = 500,
                    height = 100,
                    border_radius = 10,
                    on_click = transfer
                ),

                Container (
                    content = Text("Перевести между счетами", size = 30),
                    alignment = alignment.center,
                    margin = margin.only(top = 50),
                    bgcolor = FG,
                    width = 500,
                    height = 100,
                    border_radius = 10,
                    on_click = transferToAccount
                ),

                Container (
                    content = Text("Оплатить услуги", size = 30), 
                    alignment = alignment.center,
                    margin = margin.only(top = 50, bottom = 100),
                    bgcolor = FG,
                    width = 500,
                    height = 100,
                    border_radius = 10,
                    on_click = pay
                )
            ]
        )
    )

    # Окно платежи/переводы
    Pay_WindoW = Container (
        content = Column (
            controls = [
                Container (
                    alignment = alignment.center,
                    width = 500, 
                    bgcolor = BG,
                    content = Text("Переводы / Платежи", size = 40),
                    margin = margin.only(bottom = 22),
                ),
                Container(height = 2, width = 500, bgcolor = FG),
                Button_Container
            ]
        )
    )

    #  Главное окно
    Main_Window = Container (
        content = Row (
            controls = [
                Account_Window,
                Pay_WindoW,
            ]
        )                 
    )

    page.add(Main_Window)

app(target = main)