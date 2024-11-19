from funcoes.func import *
from classess.Pedido import Pedido

while True:
    resp = Menu()
    if resp == 1:
        print("-"*20)
        while True:
            nome = str(input("Qual o nome do pedido que deseja adicionar? ")).strip().lower()
            if ArquivoExiste(nome):
                print(f"{c[0]} Pedido com o mesmo nome ja existe!! Escolha outro nome.{c[4]}")
            else:
                break
        descricao = str(input("descricao: "))
        precoTotal = ChecandoSeFloat("PrecoTotal: ")
        mesa = input(("O pedido pertende a qual mesa?: "))
        pedido = Pedido(nome,descricao,precoTotal,mesa)
        pedido.AdicionarPedido()
    elif resp == 2:
        nome = str(input("\nQual o nome do pedido que deseja ler? ")).strip().lower()
        pedido = Pedido(nome)
        pedido.LerP()
    elif resp == 3:
        nome = str(input("Qual o nome do pedido que deseja deletar? ")).strip().lower()
        pedido = Pedido(nome)
        pedido.Deletar()
    elif resp == 4:
        print("-" * 20)
        nome = str(input("Qual o nome do pedido que deseja editar? ")).strip().lower()
        if ArquivoExiste(nome):
            descricao = str(input("Nova descricao: "))
            precoTotal = ChecandoSeFloat("PrecoTotal: ")
            mesa = input(("O pedido pertende a qual mesa?: "))
            pedido = Pedido(nome, descricao, precoTotal, mesa)
            pedido.editar()
        else:
            print(f"{c[0]}Pedido nao existe!{c[4]}")
    elif resp == 5:
        print(f"\n{c[2]}VOLTE SEMPRE! ;) ")
        break
    else:
        print(f"\n{c[0]}Opcao invalida!{c[4]}\n")
