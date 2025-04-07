from package.agenda import Agenda
import os

class Menu:
    def __init__(self):
        self.agenda = Agenda()

    def tela(self):
        while True:
            opcao = int(input('''
==============================================
              AGENDA DE CONTATOS
==============================================
MENU:
    [1] - ADICIONAR CONTATO
    [2] - LISTAR CONTATOS
    [3] - EDITAR CONTATO
    [4] - EXCLUIR CONTATO
    [5] - SAIR
=============================================
ESCOLHA A OPÇÃO: '''))

            if opcao == 1:
                self.agenda.adicionar_contato()
            elif opcao == 2:
                self.agenda.listar_contato()
            elif opcao == 3:
                self.agenda.editar_contato()
            elif opcao == 4:
                self.agenda.apagar_contato()
            elif opcao == 5:
                self.agenda.sair()
            else:
                print('Opção inválida. Tente novamente.')
                os.system('cls')