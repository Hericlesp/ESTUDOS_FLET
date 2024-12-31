#LISTA DE TAREFAS

import flet as ft

def main(page:ft.page):
    

    def add_task(e):
        print(new_taks.value)
        page.add(ft.Checkbox(label=new_taks.value))
        new_taks.value = ''
        page.update()



    #BLOCO DE ENTRADA DE INFORMAÇÃO UM INPUT INDIRETO
    new_taks = ft.TextField(hint_text='INSIRA UMA TAREFA...', expand= True)
    #BOTÃO COM AÇÃO DE CLICK
    new_button = ft.FloatingActionButton(icon=ft.icons.ADD,on_click=add_task)



    card = ft.Column(
        controls=[
            ft.Row(
                controls=(
                    new_taks,
                    new_button
                )

            )
        ]
    )

    page.add(card)
    

ft.app(target=main)