from flet import *
import userAPS 

user = userAPS.UserAPS("Stiven")

Myfriend = [
    userAPS.UserAPS("Mai Sakurajima", "https://i.pinimg.com/736x/81/0a/89/810a89db531396978d7747078c4f0aee.jpg"),
    userAPS.UserAPS("Tomoe Koga", "https://i.pinimg.com/736x/2f/9d/d7/2f9dd79305c8c23fc20aab005e0495d0.jpg"),
    userAPS.UserAPS("Rio Futaba", "https://i.pinimg.com/originals/04/40/08/0440088288c1ebc5a6bfb55aa3e79a68.jpg"),
    userAPS.UserAPS("Kaede Azusagawa", "https://i.pinimg.com/736x/d7/cc/23/d7cc237becea125ec8ee55ead602235b.jpg"),
    userAPS.UserAPS("Nodoka Toyohama", "https://pbs.twimg.com/profile_images/1129012824649240576/nC46LsJl_400x400.jpg")
]


for i in Myfriend:
    user.addFriend(i)


# Размеры окна
window_Width = 1105
window_Height = 790

# Цвета
BG = "#222831"
FG = "#393E46"
TEXTCOLOR = "#FFFFFF"

# Иерархия здесь построена от больших/наружних контейнеров к мелким/внутреним контейнерам
# Для работы радительских контейниров нужно реализовать дочерний контейнер поэтому 
# самые главные контейнеры находятся внизу

def main(page: Page):
    page.title = "Anime Payment System"
    page.window_width = window_Width
    page.window_height = window_Height
    # page.bgcolor = BG
    
    # Счет для денег
    Cash_Account = Container(
        width = 500,
        height = 250,
        bgcolor = FG,
        border_radius = 3,
        margin = margin.only(top = 30, bottom = 30),
        content = Column(
            controls = [
                Container( 
                    Text("Счет: " + user.cards[0].currency , size = 40, color = TEXTCOLOR,),
                    padding = padding.only(top = 20, left = 50)
                ),
                Container( 
                    Text(user.cards[0].getMoney() , size = 30, color = TEXTCOLOR,),
                    padding = padding.only(top = 11, left = 100)
                ),
                Container( 
                    Text("ID: " + user.cards[0].ID , size = 35, color = TEXTCOLOR,),
                    padding = padding.only(top = 16, left = 50)
                ),
            ]
        )   
    )

    if len(user.cards) > 1:
        currency = user.cards[1].currency
        getMoney = user.cards[1].getMoney()
        id = user.cards[1].ID
    else:
        currency = "*"
        getMoney = 0.00
        id = "____ ____ ____"

    # Депозит
    Second_Cash_Account = Container(
        width = 500,
        height = 250,  
        bgcolor = FG,
        border_radius = 3,
        content = Column(            
            controls = [
                Container( 
                    Text("Счет: " + currency , size = 40, color = TEXTCOLOR,),
                    padding = padding.only(top = 20, left = 50)
                ),
                Container( 
                    Text(getMoney , size = 30, color = TEXTCOLOR,),
                    padding = padding.only(top = 11, left = 100)
                ),
                Container( 
                    Text("ID: " + id, size = 35, color = TEXTCOLOR,),
                    padding = padding.only(top = 16, left = 50)
                ),
            ]
        )        
    )

    # 
    def mainWindow(e):
        page.go("/")

    def transfer(e):
        page.go("/transfer")

    def transferToAccount(e):
        page.go("/transferToAccount")

    def pay(e):
        mainWindow(0)
        page.go("/pay")

    def TransferPay(e):
        mainWindow(0)
        page.update()

    def AddClient(e):
        page.update()

    def PutTheClient(e):
        pass
        

    # Окно с кнопками
    Button_Container = Container(
        content = Column(
            controls = [
                Container(
                    content = Text("Перевести на счет", size = 30, color = TEXTCOLOR,),
                    alignment = alignment.center,
                    margin = margin.only(top = 30),
                    bgcolor = FG,
                    width = 500,
                    height = 100,
                    border_radius = 3,
                    on_click = transfer
                ),

                Container(
                    content = Text("Перевести между счетами", size = 30, color = TEXTCOLOR,),
                    alignment = alignment.center,
                    margin = margin.only(top = 50),
                    bgcolor = FG,
                    width = 500,
                    height = 100,
                    border_radius = 3,
                    on_click = transferToAccount
                ),

                Container(
                    content = Text("Оплатить услуги", size = 30, color = TEXTCOLOR,), 
                    alignment = alignment.center,
                    margin = margin.only(top = 50, bottom = 100),
                    bgcolor = FG,
                    width = 500,
                    height = 100,
                    border_radius = 3,
                    on_click = pay
                )
            ]
        )
    )

    # Окно с данными о счетах и профиле
    Account_Window = Container( 
        width = 500,
        bgcolor = BG,
        margin = margin.only(right = 20, left = 20, top = 20),
        content = Column(
            controls = [
                # Профиль
                Row(
                    controls = [
                        Container(margin = margin.only(left = 10)),
                        Image(
                            src = user.avatarImg,
                            width = 100,
                            height = 100,
                            opacity = 0.8,
                            border_radius = 50,
                        ),
                        Container(
                            Text(user.userName, size = 40, color = TEXTCOLOR,),
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
    Pay_WindoW = Containers(
        content = Column(
            controls = [
                Container(
                    alignment = alignment.center,
                    width = 500, 
                    bgcolor = BG,
                    content = Text("Переводы / Платежи", size = 40, color = TEXTCOLOR,),
                    margin = margin.only(top = 40, bottom = 22),
                ),
                Container(height = 2, width = 500, bgcolor = FG),
                Button_Container
            ]
        )
    )

    #  Главное окно
    Main_Window = Container(
        height = 733,
        bgcolor= BG,
        content = Row(
            controls = [
                Account_Window,
                Pay_WindoW,
            ]
        )                 
    )

    Transfer_Header = Container(
        bgcolor = BG,
        content = Row(
            controls = [
                Container(
                    Text("<", size = 60, color = TEXTCOLOR,),
                    margin = margin.only(left = 20),
                    on_click = mainWindow
                ),
                Container(
                    Text("Перевести клиенту", size = 30, color = TEXTCOLOR,),
                    padding = padding.only(top = 10, left = 20)
                )
            ]
        )
    )

    
    List_View_Clients = Column(
        scroll = "auto",
        height = 500
    )

    for i in user.friends:
        List_View_Clients.controls.append(
            Container(
                on_click = PutTheClient(i),
                height = 70, 
                width = 500, 
                bgcolor = FG, 
                border_radius = 3,
                margin = margin.only(bottom=20),
                content = Row(
                    controls = [
                        Container(margin = margin.only(left = 5)),
                        Image(
                            src = i.avatarImg,
                            width = 60,
                            height = 60,
                            opacity = 0.8,
                            border_radius = 50,
                        ),
                        Text(i.userName, size = 30, color = TEXTCOLOR)
                    ]
                )
            )
        )

    List_Of_Clients = Container(
        width = 550,
        height = 733,
        content = Column(
            controls = [
                Container(
                    Text("Список друзей", size = 40, color = TEXTCOLOR,),
                    margin = margin.only(top = 10, left = 20, bottom = 15),
                ),
                Container(Stack(controls = [List_View_Clients]), margin= margin.only(left = 20))
            ]
        )
    )
    
    def ChangeCard(e):
        for i in range(0, len(user.cards)):
            if Dropdown_Card.value == user.cards[i].currency:
                t1.value = user.cards[i].currency
                t2.value = user.cards[i].getMoney
                print(t2.value)
                page.update()

    def DropdownCard(e):
        for i in range(0, len(user.cards)):
            Dropdown_Card.options.append(dropdown.Option(user.cards[i].currency))
            Dropdown_Card.value = user.cards[i].currency


    Dropdown_Card = Dropdown(
        border_color = FG,
        bgcolor = BG,
        color = TEXTCOLOR,
        width = 385,
        hint_text = "Выбрать карту",
        on_change = ChangeCard
    )
    
    t1 = Text("None", size = 30, color = TEXTCOLOR,)
    t2 = Text("None", size = 30, color = TEXTCOLOR,)
    tf1 = TextField(hint_text = "___ ___ ___", border_color = FG, color = TEXTCOLOR)

    def FrendOrClient(e, friend = None):
        if e == False:
            Container(
                content = Column(
                    controls = [
                        Container(
                            Text("Номер карты", size = 30, color = TEXTCOLOR,),
                            margin = margin.only(top = 20)
                        ),
                        Container(
                            tf1,
                            margin = margin.only(top = 15)
                        )
                    ]
                )
            )
        else:
            Container(
                content = Column(
                    controls = [
                        Container(
                            Text("Перевод другу", size = 30, color = TEXTCOLOR,),
                            margin = margin.only(top = 20)
                        ),
                        Container(
                            Text(friend.userName, size = 30, color = TEXTCOLOR,),
                            alignment = alignment.center,
                            width = 500,
                            height = 60,
                            border_radius = 3,
                            border = FG,
                            margin = margin.only(top = 15),
                        )
                    ]
                )
            )


    Transfer_For_Client = Container(
        height = 733,
        width = 500,
        content = Column(
            controls = [
                Container(
                    content = Row(
                        controls = [
                            Text("Карта", size = 40, color = TEXTCOLOR,),
                            Dropdown_Card
                        ]
                    ),
                    margin = margin.only(top = 10)
                ),
                Container(
                    bgcolor = FG,
                    width = 500,
                    height = 60,
                    border_radius = 3,
                    margin = margin.only(top = 15),
                    content = Row(
                        controls = [
                            Container(margin = margin.only(left = 10)),
                            t1,
                            Container(margin = margin.only(left = 50)),
                            t2,
                        ]
                    )
                ),
                Container(
                    content = Column(
                        controls = [
                            Container(
                                Text("Номер карты", size = 30, color = TEXTCOLOR,),
                                margin = margin.only(top = 20)
                            ),
                            Container(
                                tf1,
                                margin = margin.only(top = 15)
                            )
                        ]
                    )
                ),
                Container(
                    Text("Сумма перевода", size = 30, color = TEXTCOLOR,),
                    margin = margin.only(top = 20,)
                ),
                Container(
                    TextField(hint_text = "0.0", border_color = FG, color = TEXTCOLOR),
                    margin = margin.only(top = 15)
                ),
                Row(
                    controls = [
                        Container(
                            Text("Отправить", size = 30, color = TEXTCOLOR,),
                            alignment = alignment.center,
                            bgcolor = FG,
                            width = 420,
                            height = 60,
                            border_radius = 3,
                            margin = margin.only(top = 25),
                            on_click = TransferPay
                        ),
                        Container(
                            Container(Text("+", size = 30, color = TEXTCOLOR), padding = padding.only(top = 5, left = 20)),
                            bgcolor = FG,
                            width = 60,
                            height = 60,
                            border_radius = 3,
                            margin = margin.only(top = 25),
                            on_click = AddClient
                        ),
                    ]
                )
            ]
        )
    )

    Transfer_Menu = Row(
        controls = [
            List_Of_Clients,
            Transfer_For_Client
        ]
    )

    Transfer_Window = Container(
        height = 733,
        bgcolor = BG,
        content = Column(
            controls = [
                Transfer_Header,
                Container(height = 2, width = window_Width, bgcolor = FG),
                Transfer_Menu
            ]
        )                 
    )


    def route_change(e):
        print("Route change:", e.route)
        page.views.clear()
        page.views.append(View("/",[Main_Window]))

        if page.route == "/transfer" :
            page.views.append(View("/transfer", [Transfer_Window]))

        if page.route == "/transferToAccount":
            page.views.append(View("/transferToAccount", [Main_Window]))

        if page.route == "/pay":
            page.bgcolor = BG
            page.views.append(View("/pay", [Main_Window]))
        page.update()

    def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        page.go("/")

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    #page.add(Transfer_Window)
    page.add(Main_Window)

app(target = main)
