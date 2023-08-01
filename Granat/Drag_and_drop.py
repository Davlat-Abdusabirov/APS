# Drag and drop
import flet as ft


#? https://flet.dev/docs/guides/python/drag-and-drop


def main(page: ft.Page):
    page.title = "Drag and Drop example"

    def drag_accept(e):
        # get draggable (source) control by its ID / получить перетаскиваемый (исходный) элемент управления по его идентификатору 
        src = page.get_control(e.src_id)
        # update text inside draggable control / обновить текст внутри перетаскиваемого элемента управления
        src.content.content.value = "0"
        # update text inside drag target control / обновить текст внутри элемента управления перетаскиванием
        e.control.content.content.value = "1"
        page.update()

    page.add(
        ft.Row(
            [
                ft.Draggable(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.CYAN_200,
                        border_radius=5,
                        content=ft.Text("1", size=20),
                        alignment=ft.alignment.center,
                    ),
                ),
                ft.Container(width=100),
                ft.DragTarget(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.PINK_200,
                        border_radius=5,
                        content=ft.Text("0", size=20),
                        alignment=ft.alignment.center,
                    ),
                    on_accept=drag_accept,
                ),
            ]
        )
    )

ft.app(target=main)