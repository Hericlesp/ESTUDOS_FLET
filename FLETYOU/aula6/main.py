#LISTA DE TAREFAS

import flet as ft

def main(page:ft.page):
    page.title ="ToDo"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 400
    page.window.heigth = 650
    page.padding = ft.padding.only(top=20,left=20,right=20,bottom=20)
    
    

    def add_task(e):
        print(new_taks.value)
        task_list.controls.append(ft.Checkbox(label=new_taks.value))
        page.add(ft.Checkbox(label=new_taks.value))
        new_taks.value = ''
        page.update()



    #BLOCO DE ENTRADA DE INFORMAÇÃO UM INPUT INDIRETO
    new_taks = ft.TextField(hint_text='INSIRA UMA TAREFA...', expand= True)
    #BOTÃO COM AÇÃO DE CLICK
    new_button = ft.FloatingActionButton(icon=ft.icons.ADD,on_click=add_task)

    task_list = ft.Column()

    card = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    new_taks,
                    new_button
                ]

            ),
            task_list,
        ]
    )

    page.add(card)
    

ft.app(target=main)