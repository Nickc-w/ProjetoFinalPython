# ProjetoFinalPython

Sistema de Controle de Pedidos


O sistema utiliza arquivos de texto para armazenar os dados dos pedidos e permite realizar operações diretamente no console.

Funcionalidades
- Adicionar Pedido: Permite que o usuário adicione um novo pedido. O sistema verifica se o nome do pedido já existe para evitar duplicação.

- Ler Pedido: O usuário pode ler um pedido previamente salvo, visualizando as informações salvas em um arquivo de texto.

- Editar Pedido: O sistema permite editar um pedido já existente, alterando a descrição, preço e mesa associada ao pedido. (pelo nome)

- Excluir Pedido: Permite ao usuário excluir um pedido, removendo o arquivo de texto correspondente.


Estrutura do Projeto

 - Em funcoes:
   
   -> func.py: Contém as funções responsáveis por salvar, editar, ler, excluir os pedidos, Menu, ArquivoExiste, ChecandoSeFloat. A função ArquivoExiste verifica se um arquivo de pedido já existe no 
    sistema. A função ChecandoSeFloat valida se a entrada do usuário é um número flutuante (usada para o preço do pedido).
   
- Em main:
  
  -> mainzinho: Main, onde o código é executado

  -> Onde os arquivos de texto aparecerão


  
- Em classess:

  -> Pedido.py: Define a classe Pedido, que é utilizada para armazenar as informações de um pedido, como nome, descrição, preço total e mesa.

EXEMPLO DE USO:

MENU

[1] Adicionar pedido

[2] Ler pedido

[3] Excluir pedido

[4] Editar

[5] Sair


O que deseja fazer ? 1

Qual o nome do pedido que deseja adicionar? pedido1

descricao: pizza grande, 1 suco

PrecoTotal: 30.50

O pedido pertende a qual mesa?: mesa 10

Pedido adicionado com sucesso!
