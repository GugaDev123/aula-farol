from nicegui import ui

@ui.page('/')
def principal() ->None:
    with ui.row().classes('items-center'):
        ui.label('Bem-vindos ao Farol na quebrada').classes('text-xl text-blue-900')
        ui.image('../logo_farol_na_quebrada-removebg.png')
    ui.query('body').classes('bg-sky-300')

ui.run(title= "Minha primeira pagina web em python",
        language='pt-BR', favicon='../img/logo_farol_na_quebrada.jpg'
)