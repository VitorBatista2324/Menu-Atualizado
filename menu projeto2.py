noticias = []
admins = {}
users = {}
usuario_logado = None

def cadastrar_admin():
    username = input("Digite o nome de usuário do administrador: ")
    password = input("Digite a senha do administrador: ")

    if username in admins:
        print("Nome de usuário já existente. Escolha outro.")
    else:
        admins[username] = password
        print("Administrador cadastrado com sucesso.")

def cadastrar_usuario():
    username = input("Digite o nome de usuário do usuário: ")
    password = input("Digite a senha do usuário: ")

    if username in users:
        print("Nome de usuário já existente. Escolha outro.")
    else:
        users[username] = password
        print("Usuário cadastrado com sucesso.")

def login():
    global usuario_logado
    username = input("Nome de usuário: ")
    password = input("Senha: ")

    if username in admins and admins[username] == password:
        print("Login bem-sucedido como administrador.")
        usuario_logado = username
    elif username in users and users[username] == password:
        print("Login bem-sucedido como usuário.")
        usuario_logado = username
    else:
        print("Nome de usuário ou senha incorretos. Tente novamente.")

# ... (rest of your code remains unchanged)

while True:
    print("\nMenu Geral")
    print("1. Cadastrar Administrador")
    print("2. Login")
    print("3. Cadastrar Usuário")
    print("0. Sair")
    choice = input("Escolha uma opção: ")

    if choice == '1':
        cadastrar_admin()
    elif choice == '2':
        login()
    elif choice == '3':
        cadastrar_usuario()
    elif choice == '0':
        break
    else:
        print("Opção inválida. Tente novamente.")

    if usuario_logado in admins:
        menu_admin()
    elif usuario_logado in users:
        menu_usuario()
