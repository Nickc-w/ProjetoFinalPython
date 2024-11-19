
from funcoes.func import *
class Pedido:
    def __init__(self,nome="",descricao="",precoTotal=0,mesa=""):
        self.nome = nome
        self.descricao = descricao
        self.precoTotal = precoTotal
        self.mesa = mesa

    def AdicionarPedido(self):
        SalvarPedido(self.nome, self.descricao, self.precoTotal, self.mesa)

    def LerP(self):
        LerPedido(self.nome)

    def Deletar(self):
        ExcluirPedido(self.nome)

    def editar(self):
        editarPedido(self.nome, self.descricao, self.precoTotal, self.mesa)
