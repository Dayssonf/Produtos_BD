from modelos import conectar

def exibir_menu():
    print("\n=== DIÁRIO DE CLASSE ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno por ID")
    print("0 - Sair")

def cadastrar():
    nome = input("Digite o nome: ")
    nota = float(input("Digite a nota: "))
    

    produto = Produto(nome, preco, categoria)
    produto.salvar()

def listar_alunos():
     for aluno in alunos:
       print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Média: {aluno[2]}")

    
def buscar_id():

while True:
    exibir_menu()
    opcao = input("Digite uma opção: ")

    if opcao == "0":
        break
    elif opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        buscar_id()
    else:
        print("Opção inválida! tente novamente. ")