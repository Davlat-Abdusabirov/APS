import flet as ft
#! https://flet.dev/docs/guides/python/large-lists

# def main(page: ft.Page):
#     lv = ft.ListView(width=100, height=300, spacing=10)
#     for i in range(5000):
#         lv.controls.append(ft.Text(f"Line {i}"))
#     page.add(lv)




#! def main(page: ft.Page):
#     r = ft.Row(wrap=True, scroll="always", expand=True)
#     page.add(r)

#     for i in range(5000):
#         r.controls.append(
#             ft.Container(
#                 ft.Text(f"Item {i}"),
#                 width=100,
#                 height=100,
#                 alignment=ft.alignment.center,
#                 bgcolor=ft.colors.BLUE,
#                 border=ft.border.all(1, ft.colors.RED_400),
#                 border_radius=ft.border_radius.all(5),
#             )
#         )
#     page.update()




def main(page: ft.Page):

    # add ListView to a page first
    lv = ft.ListView(expand=1, spacing=10, item_extent=50)
    page.add(lv)

    for i in range(5100):
        lv.controls.append(ft.Text(f"Line {i}"))
        # send page to a page
        if i % 500 == 0:
            page.update()
    # send the rest to a page
    page.update()

ft.app(target=main)
