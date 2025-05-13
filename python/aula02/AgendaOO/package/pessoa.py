

class Pessoa:
    def __init__(self, nome, sobrenome, telefone, email, id):
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
        self.email = email
        self.id = id

    def transformar_dict(self):
        return {
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'telefone': self.telefone,
            'email': self.email,
            'id': self.id
        }
