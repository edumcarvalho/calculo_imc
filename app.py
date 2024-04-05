import PySimpleGUI as sg

# tema
sg.theme('Reddit')
# Defina layout das colunas

def calcular(peso,altura):
    x = (peso * 100)/altura
    x = (x * 100)/altura
    return x
    

cadastro = [
    [sg.Text(text='Altura (em centímetros): ',size=(20, 1)) , sg.Input(size=(5, 1),key='altura')],
    [sg.Text(text='Peso (em kilogras): ',size=(20, 1)), sg.Input(size=(5, 1),key='peso')],    
    [sg.Text(text='Aguardando informações!',size=(28, 1),
             text_color='green',justification='center',auto_size_text=20,
             key='msg')],
    [sg.Text(text='IMC: ??',size=(28, 1),text_color='green',justification='center',key='imc')],
]

layout_principal = [
    [sg.Frame('Calcular IMC',cadastro)],
    [sg.Button('Calcular')]
  
]
# janela
window = sg.Window('IMC', layout_principal)
# Ler eventos
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    else:        
        imc = calcular(float(values['peso'].replace(',', '.')),float(values['altura']))
        if imc <= 16.9:            
            window['msg'].update(text_color='red')
            window['msg'].update('Você está muito abaixo do peso.')
            window['imc'].update(text_color='red')
            window['imc'].update(f'IMC: {imc:.2f}')
        elif imc >16.9 and imc <= 18.4:            
            window['msg'].update(text_color='purple')
            window['msg'].update('Você está abaixo do peso.')
            window['imc'].update(text_color='purple')
            window['imc'].update(f'IMC: {imc:.2f}')
        elif imc >18.4 and imc <= 24.9:            
            window['msg'].update(text_color='green')
            window['msg'].update('Você está com o peso normal.')
            window['imc'].update(text_color='green')
            window['imc'].update(f'IMC: {imc:.2f}')
        elif imc >24.9 and imc <= 29.9:            
            window['msg'].update(text_color='purple')
            window['msg'].update('Você está acima do peso.')
            window['imc'].update(text_color='purple')
            window['imc'].update(f'IMC: {imc:.2f}')
        elif imc >29.9 and imc <= 34.9:            
            window['msg'].update(text_color='red')
            window['msg'].update('Você está com obesidade grau I.')
            window['imc'].update(text_color='red')
            window['imc'].update(f'IMC: {imc:.2f}')
        elif imc >34.9 and imc <= 39.9:
            window['msg'].update(text_color='red')
            window['msg'].update('Você está com obesidade grau II.')
            window['imc'].update(text_color='red')
            window['imc'].update(f'IMC: {imc:.2f}')
        elif imc >39.9:
            window['msg'].update(text_color='red')
            window['msg'].update('Você está com obesidade grau III.')
            window['imc'].update(text_color='red')
            window['imc'].update(f'IMC: {imc:.2f}')