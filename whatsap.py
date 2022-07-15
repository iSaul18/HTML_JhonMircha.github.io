
print('Cuál es su telefono?:')
valorTelefono = int(input('> '))
print('Qué mensaje personalizado quieres enviar cuando tus clientes te contacten?:')
valorMensaje = str(input('> '))

print(f'https://api.whatsapp.com/send?phone={valorTelefono}&text={valorMensaje}')
