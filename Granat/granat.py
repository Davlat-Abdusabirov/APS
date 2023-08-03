# import flet as ft
# #! Скачай плагин для VS Code - Better Comments
# #! Для любого действия связоного с виджитами нужна отдельная функция!

# #^ Создание окна программы
# def main (page: ft.Page): # Главная функция
#     pass

# ft.app(target=main) # Запуск 
# view=ft.AppView.WEB_BROWSER #добавить в ft.app() чтобы открылся браузер
# page.update() # Обновление изменений
# page.add() # Добовление чего либо в окно приложения
# page.title = "APS" # Название приложения
# txt_number = ft.TextField(value="0", text_align="right", width=100) #окно с изменяемым числом



# #^ Поле ввода текста (Имя, Фамилия, Отчество и т.д)
# def btn_click(e):
#     if not txt_name.value:
#         txt_name.error_text = "Впишите свое имя"
#         page.update()
#     else:   
#         name = txt_name.value 
#         page.clean()
#         page.add(ft.Text(f"Hello, {name}!"))
# txt_name = ft.TextField(label="Your name") # Поле с вводом текста
# page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))



# #^ Чек-боксы (поля с галочками)
# def checkbox_changed(e):
#     output_text.value = (f"You have learned how to ski :  {todo_check.value}.")
#     page.update()

# output_text = ft.Text() # добавление текста (после прожатия чек-бокса)
# todo_check = ft.Checkbox(label="ToDo: Learn how to use ski", value=False, on_change=checkbox_changed) # Создание чек-бокса
# page.add(todo_check, output_text)




# #^ Поле с выбором
# def button_clicked(e):
#     output_text.value = f"Dropdown value is:  {color_dropdown.value}"
#     page.update()
    
# output_text = ft.Text()
# submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
# color_dropdown = ft.Dropdown(width=100, # Создание поля
#                             options=[ft.dropdown.Option("Red"), # Создание разделов для выбора
#                                     ft.dropdown.Option("Green"),
#                                     ft.dropdown.Option("Blue")])
# page.add(color_dropdown, submit_btn, output_text)


# #^ Создание списков
# lv = ft.ListView(width=100, height=300, spacing=10) # Создание списка
# for i in range(5000):
#     lv.controls.append(ft.Text(f"Line {i}")) # Добавление в список
# page.add(lv)



# r = ft.Row(wrap=True, scroll="always", expand=True) # Сеточный список
# page.add(r)
# for i in range(5000):
#     r.controls.append(
#         ft.Container( # Создлание обочки для каждого элемента списка
#             ft.Text(f"Item {i}"),
#             width=100,
#             height=100,
#             alignment=ft.alignment.center,
#             bgcolor=ft.colors.BLUE,
#             border=ft.border.all(1, ft.colors.RED_400),
#             border_radius=ft.border_radius.all(5)))
# page.update()


# # Передача данных пакетами (все еще списки)
# # add ListView to a page first
# lv = ft.ListView(expand=1, spacing=10, item_extent=50)
# page.add(lv)
# for i in range(5100):
#     lv.controls.append(ft.Text(f"Line {i}"))
#     # send page to a page
#     if i % 500 == 0:
#         page.update()
# # send the rest to a page
# page.update()



# #^ Переключение страниц
# #! https://flet.dev/docs/guides/python/navigation-and-routing
# import flet
# from flet import AppBar, ElevatedButton, Page, Text, View, colors


# def main(page: Page):
#     page.title = "Routes Example"

#     print("Initial route:", page.route)

#     def route_change(e):
#         print("Route change:", e.route)
#         page.views.clear()
#         page.views.append(View("/", [AppBar(title=Text("Flet app")), ElevatedButton("Go to settings", on_click=open_settings)]))
        
#         if page.route == "/settings" or page.route == "/settings/mail":
#             page.views.append(View("/settings",
#                                                 [AppBar(title=Text("Settings"),
#                                                 bgcolor=colors.SURFACE_VARIANT),
#                                                 Text("Settings!", style="bodyMedium"),
#                                                 ElevatedButton("Go to mail settings",
#                                                 on_click=open_mail_settings)]))
        
#         if page.route == "/settings/mail":
#             page.views.append(View("/settings/mail",
#                                                     [AppBar(title=Text("Mail Settings"),
#                                                     bgcolor=colors.SURFACE_VARIANT),
#                                                     Text("Mail settings!")]))

#         page.update()


#     def view_pop(e):
#         print("View pop:", e.view)
#         page.views.pop()
#         top_view = page.views[-1]
#         page.go(top_view.route)

#     page.on_route_change = route_change
#     page.on_view_pop = view_pop

#     def open_mail_settings(e):
#         page.go("/settings/mail")

#     def open_settings(e):
#         page.go("/settings")

#     page.go(page.route)

# flet.app(target=main)

