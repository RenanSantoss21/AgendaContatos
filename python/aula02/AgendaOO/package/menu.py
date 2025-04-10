from package.agenda import Agenda
import os

class Menu:
    def __init__(self):
        self.agenda = Agenda()
    
        self.menu = {
            1: self.agenda.adicionar_contato,
            2: self.agenda.listar_contato,
            3: self.agenda.editar_contato,
            4: self.agenda.apagar_contato,
            5: self.sair,
        }
        self.condition = True

    def loop(self):
        while self.condition:
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
            
            escolha = self.menu.get(opcao, self.opcao_invalida)
            escolha()

    def opcao_invalida(self):
        print('Opção inválida. Tente novamente.')

    def sair(self):
        print('Saindo...')
        self.condition = False