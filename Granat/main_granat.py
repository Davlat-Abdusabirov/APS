import flet as ft
from flet import IconButton, Page, Row, TextField, icons

def main(page: ft.Page): #main function
    page.title = "APS" #name application
    
    # #! https://flet.dev/docs/guides/python/getting-user-input
    page.vertical_alignment = ft.MainAxisAlignment.CENTER #центрирование
    txt_number = ft.TextField(value="0", text_align="right", width=100) #окно с изменяемым числом

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1) #отнимание
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1) #прибавление
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),   
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    # btn = ft.ElevatedButton("Click me!") #creating a button
    # page.add(btn) # adding a button

ft.app(target=main) #closing