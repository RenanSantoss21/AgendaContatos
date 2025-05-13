from package.pessoa import Pessoa
from time import sleep
import os
from random import randint


class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self):
        nome = str(input("Primeiro nome: "))
        sobrenome = str(input("Sobrenome: "))
        telefone = str(input("Telefone: "))
        email = str(input("Email: "))
        id = randint(100, 999)
        if any(contato['id'] == id for contato in self.contatos):
            id = randint(100, 999)

        contato = Pessoa(nome, sobrenome, telefone, email, id)
        self.contatos.append(contato.transformar_dict())
        print('Contato adicionado com sucesso!')
        sleep(1)
        os.system('cls')

    def listar_contato(self):
        if not self.contatos:
            print("Nenhum contato encontrado.")
        else:
            print('Lista de contatos:')
            for i, ctt in enumerate(self.contatos):
                print(f'''{i+1}.
    ID: {ctt['id']}
    Nome: {ctt['nome']} {ctt['sobrenome']}
    Tel: {ctt['telefone']}
    Email: {ctt['email']}''')
                print()
        sleep(1)
    input = ('Pressione Enter para continuar...')

    def editar_contato(self):
        if not self.contatos:
            print("Nenhum contato encontrado.")
        else:
            self.listar_contato()
            i = input('Digite o ID do contato que você deseja editar: ')
            for contato in self.contatos:
                if (
                    contato['id'] == int(i) or
                    contato['nome'] == str(i) or
                    contato['sobrenome'] == str(i)
                ):

                    edicao = int(input('''O que deseja editar?
        [1]-> Nome
        [2]-> Sobrenome
        [3]-> Telefone
        [4]-> Email
        [5]-> Todas as opções
    Opção: '''))
                    if edicao == 1:
                        novo_nome = (input("Novo nome: ")).strip()
                        contato['nome'] = novo_nome
                    elif edicao == 2:
                        novo_sobrenome = (input("Novo sobrenome: ")).strip()
                        contato['sobrenome'] = novo_sobrenome
                    elif edicao == 3:
                        novo_telefone = (input("Novo telefone: ")).strip()
                        contato['telefone'] = novo_telefone
                    elif edicao == 4:
                        novo_email = (input("Novo email: ")).strip()
                        contato['email'] = novo_email
                    elif edicao == 5:
                        novo_nome = input('Novo nome: ')
                        novo_sobrenome = (input("Novo sobrenome: "))
                        novo_telefone = (input('Novo telefone: '))
                        novo_email = (input('Novo email: '))

                        contato['nome'] = novo_nome
                        contato['sobrenome'] = novo_sobrenome
                        contato['telefone'] = novo_telefone
                        contato['email'] = novo_email

                    print('Contato atualizado com sucesso!')
                    return
                else:
                    print('Contato não encontrado.')
            sleep(1)
            os.system('cls')

    def apagar_contato(self):
        if not self.contatos:
            print("Nenhum contato encontrado.")
        else:
            self.listar_contato()
            i = int(input('Digite o ID do contato que você deseja editar: '))
            for contato in self.contatos:
                if (
                    contato['id'] == int(i) or
                    contato['nome'] == str(i) or
                    contato['sobrenome'] == str(i)
                ):

                    confirmar = str(input(
                        'Tem certeza que deseja excluir? [S/N]'
                        )).strip().upper()
                    if confirmar == 'S':
                        self.contatos.remove(contato)
                        print('Contato excluído com sucesso!')
                    else:
                        print('Operação cancelada.')
                    return
            print('Contato não encontrado.')
            sleep(1)
            os.system('cls')
