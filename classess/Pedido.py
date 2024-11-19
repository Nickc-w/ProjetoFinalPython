class Pedido:
    def __init__(self,nome="",descricao="",precoTotal=0,mesa=""):
        self.nome = nome
        self.descricao = descricao
        self.precoTotal = precoTotal
        self.mesa = mesa

    def AdicionarPedido(self):
        from funcoes.func import SalvarPedido
        SalvarPedido(self.nome, self.descricao, self.precoTotal, self.mesa)

    def LerP(self):
        from funcoes.func import LerPedido
        LerPedido(self.nome)

    def Deletar(self):
        from funcoes.func import ExcluirPedido
        ExcluirPedido(self.nome)

    def editar(self):
        from funcoes.func import editarPedido
        editarPedido(self.nome, self.descricao, self.precoTotal, self.mesa)
