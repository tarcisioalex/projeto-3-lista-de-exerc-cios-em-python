codUsuario = "sertanejo"
senha = "C3c@9999"

verifUsuario = input("Olá, para fazer o login digite o seu código de usuário: ")
if verifUsuario == codUsuario:
    verifSenha = input("Usuário confirmado.\nDigite sua senha: ")
    if verifSenha == "C3c@9999":
        print("Acesso permitido!")
    else:
        print("Acesso negado!")
else:
    print("Usuário não existente")
