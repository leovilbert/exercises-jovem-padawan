usuario = str(input('Digite o usuário: ')).strip()

senha = str(input('Digite a senha: ')).strip()

while senha == usuario:
    print('Senha não pode ser igual ao nome de usuário. Tente novamente!')
    senha = str(input('Digite a senha: '))
