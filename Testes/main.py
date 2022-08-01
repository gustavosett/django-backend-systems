from bancoDeDados import bancoDeDados


cadastros = []
while True:
    cadastro = bancoDeDados(input("Nome: "), int(input("Idade: ")))
    cadastros.insert(cadastro)