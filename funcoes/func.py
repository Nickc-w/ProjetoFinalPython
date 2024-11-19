c = ["\033[31m","\033[34m","\033[33m","\033[32m","\033[m"]
# vermelho      azul      amarelo   verde       nada

import os

def ArquivoExiste(nome):
    if os.path.exists(nome+".txt"):
        return True
    else:
        return False

def SalvarPedido(nome,descricao,precoTotal,mesa):
    try:
        with open(nome+'.txt','a') as file:
            file.write(f'------------{nome}--------------\n')
            file.write(f'Descricao: {descricao}\nPrecoTotal: {precoTotal} reais\nMesa: {mesa}')
            file.write(f'\n--------------------------------')
    except:
        print(f"\n{c[2]}Houve um erro ao adicionar ao pedido{c[4]}\n")
    else:
        print(f"\n{c[3]}Pedido adicionado com sucesso!{c[4]}\n")

def editarPedido(nome,descricao,precoTotal,mesa):
    try:
        with open(nome+'.txt','w') as file:
            file.write(f'------------{nome}--------------\n')
            file.write(f'Descricao: {descricao}\nPrecoTotal: {precoTotal} reais\nMesa: {mesa}')
            file.write(f'\n--------------------------------')
    except:
        print(f"\n{c[2]}Houve um erro ao editar o pedido{c[4]}\n")
    else:
        print(f"\n{c[3]}Pedido editado com sucesso!{c[4]}\n")

def LerPedido(nome):
    if ArquivoExiste(nome):
        try:
            with open(nome+'.txt','r') as file:
                conteudo = file.read()
        except:
            print(f"\n{c[2]}Houve um problema ao ler o pedido{c[4]}\n")
        else:
            print("\n")
            print(conteudo)
            print("\n")
    else:
        print(f"{c[0]}Pedido nao existe!{c[4]}")

def ExcluirPedido(nome):
    try:
        os.remove(nome+'.txt')
    except FileNotFoundError:
        print(f"\n{c[0]}Pedido nao existe!{c[4]}\n")
    except:
        print(f"\n{c[2]}Ocorreu um erro ao deletar o arquivo{c[4]}\n")
    else:
        print(f"\n{c[3]}Arquivo removido com sucesso!{c[4]}\n")

def ChecandoSeFloat(msg):
    while True:
        try:
            precoTotal = float(input(msg))
        except ValueError:
            print(f"\n{c[0]}Digite um numero válido!{c[4]}\n")
        else:
            return precoTotal

def Menu():
    print("-="*20)
    print(f"{c[2]}MENU{c[4]}".center(45))
    print("-=" * 20)
    print(f"{c[1]}[1]{c[4]} Adicionar pedido\n{c[1]}[2]{c[4]} Ler pedido\n{c[1]}[3]{c[4]} Excluir pedido\n{c[1]}[4]{c[4]} Editar\n{c[1]}[5]{c[4]} Sair")
    resp = int(input("O que deseja fazer ? "))
    return resp
