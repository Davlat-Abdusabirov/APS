from flet import *
import userAPS as userAPS

user = userAPS.UserAPS("Stiven")

# Размеры окна
window_Width = 1085
window_Height = 800

# Цвета
BG = "#222831"
FG = "#393E46"

# Иерархия здесь построена от больших/наружних контейнеров к мелким/внутреним контейнерам
# Для работы радительских контейниров нужно реализовать дочерний контейнер поэтому 
# самые главные контейнеры находятся внизу

def main(page: Page):
    page.title = "Anime Payment System"
    page.window_width = window_Width
    page.window_height = window_Height
    page.bgcolor = BG

    # Счет для денег
    Cash_Account = Container (
        width = 500,
        height = 250,
        bgcolor = FG,
        border_radius = 10,
        margin = margin.only(top = 30, bottom = 30),
        content = Column (
            controls = [
                Container ( 
                    Text("Счет: " + user.cards[0].currency , size = 40),
                    padding = padding.only(top = 20, left = 50)
                ),
                Container ( 
                    Text(user.cards[0].getMoney() , size = 30),
                    padding = padding.only(top = 11, left = 100)
                ),
                Container ( 
                    Text("ID: " + user.cards[0].ID , size = 35),
                    padding = padding.only(top = 16, left = 50)
                ),
            ]
        )   
    )

    # if len(user.cards) > 1:
    #     currency = user.cards[1].currency
    #     getMoney = user.cards[1].getMoney()
    #     id = user.cards[1].ID
    # else:
    currency = "*"
    getMoney = 0.00
    id = "____ ____ ____"

    # Депозит
    Second_Cash_Account = Container (
        width = 500,
        height = 250,  
        bgcolor = FG,
        border_radius = 10,
        content = Column (            
            controls = [
                Container ( 
                    Text("Счет: " + currency , size = 40),
                    padding = padding.only(top = 20, left = 50)
                ),
                Container ( 
                    Text(getMoney , size = 30),
                    padding = padding.only(top = 11, left = 100)
                ),
                Container ( 
                    Text("ID: " + id, size = 35),
                    padding = padding.only(top = 16, left = 50)
                ),
            ]
        )        
    )

    # 
    def transfer(e):
        page.go("/transfer")

    def transferToAccount(e):
        page.go("/transferToAccount")

    def pay(e):
        page.go("/pay")

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
                Second_Cash_Account
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


    def route_change(e):
        print("Route change:", e.route)
        page.views.clear()
        page.views.append(View("/",[page.add(Main_Window)]))
        if page.route == "/transfer" :
            page.views.append(View("/transfer", [page.add(Main_Window)]))
        if page.route == "/transferToAccount":
            page.views.append(
                View("/transferToAccount", [page.add(Main_Window)]))
        if page.route == "/pay":
            page.views.append(View("/pay", [page.add(Main_Window)]))
        page.update()

    def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        page.go("/")

    page.on_route_change = route_change
    page.on_view_pop = view_pop


    page.add(Main_Window)

app(target = main)