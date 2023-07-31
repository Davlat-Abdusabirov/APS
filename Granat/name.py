import flet as ft

#! def main(page):
#     def btn_click(e):
#         if not txt_name.value:
#             txt_name.error_text = "Впишитен свое имя"
#             page.update()
#         else:   
#             name = txt_name.value
#             page.clean()
#             page.add(ft.Text(f"Hello, {name}!"))

#     txt_name = ft.TextField(label="Your name")

#     page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))




#! def main(page):
#     def checkbox_changed(e):
#         output_text.value = (
#             f"You have learned how to ski :  {todo_check.value}."
#         )
#         page.update()

#     output_text = ft.Text()
#     todo_check = ft.Checkbox(label="ToDo: Learn how to use ski", value=False, on_change=checkbox_changed)
#     page.add(todo_check, output_text)




#! def main(page: ft.Page):
#     def button_clicked(e):
#         output_text.value = f"Dropdown value is:  {color_dropdown.value}"
#         page.update()

#     output_text = ft.Text()
#     submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
#     color_dropdown = ft.Dropdown(
#         width=100,
#         options=[
#             ft.dropdown.Option("Red"),
#             ft.dropdown.Option("Green"),
#             ft.dropdown.Option("Blue"),
#         ],
#     )
#     page.add(color_dropdown, submit_btn, output_text)

# ft.app(target=main)