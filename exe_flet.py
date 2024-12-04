import flet as ft

def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text(" hello, Flet")))

ft.app(main)