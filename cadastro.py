from PySimpleGUI import PySimpleGUI as sg

# Layout

sg.theme('Reddit') # Escolha do tema

layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar o login')],
    [sg.Button('Entrar')],
]

# Janela
janela = sg.Window('Tela de login', layout)

# Eventos da janela
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'anderson' and valores['senha'] == '30091985':
            print(f"Bem-vindo {valores['usuario']}")

