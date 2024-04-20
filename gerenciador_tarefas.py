# Entrada_da_dados

class Tarefa:
    def __init__(self, nome, data_limite):
        self.nome = nome
        self.data_limite = data_limite
        self.concluida = False

def capturar_entrada():
    nome = input("Digite o nome da tarefa:")
    data_limite = input("Digite a data limite (em YYYY-MD-DD)")
    return nome, data_limite

def criar_tarefa():
    nome, data_limite = capturar_entrada()
    return Tarefa(nome,data_limite)

lista_de_tarefas = []

def adicionar_tarefas():
    tarefa = criar_tarefa()
    lista_de_tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso bonitão!!")
# lista a tarefa
def lista_tarefas():
    for index, tarefa in enumerate(lista_de_tarefas):
        print(f"{index +1 }. Nome: {tarefa.nome}, Data limite: {tarefa.data_limite}, Concluida {tarefa.concluida}")

def marcar_tarefa_feita():
    lista_tarefas()
    num_tarefa = int(input("Digite o número da tarefa que deseja marca como concluída: "))
    lista_de_tarefas[num_tarefa - 1].concluida= True
    print("Tarefa marcada como concluída Bonitão!!")

while True:
    print("O que você deseja fazer?")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        nova_sessao_adicao = True
        adicionar_tarefas()
    elif opcao == "2":
        lista_tarefas()
    elif opcao == "3":
        marcar_tarefa_feita()
    elif opcao == "4":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")







