import flet as ft

def main(page: ft.Page):
    #page.add(ft.SafeArea(ft.Text(" hello, Flet...")))
    t = ft.Text()
    page.add(t) #é um atalho para page.controls.append(t) e posterior page.update()

    for i in range(10): 
        t.value = f'Step {i}'
        page.update()
        #time.sleep(1)

    page.add(   #permite organizar em linha os componentes do container
        ft.Row(
            controls=[
                ft.Text('A'),
                ft.Text('B'),
                ft.Text('C'),
             ]
        )  
    )

ft.app(main)