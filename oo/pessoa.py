class  Pessoa:

    def __init__(self,*filhos,  nome = None, idade=None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    sophia = Pessoa(nome='Sophia')
    david = Pessoa(sophia, nome = 'David', idade=29)
    print(f'Nome: {david.nome}')
    print(f'Idade: {david.idade}')
    for filho in david.filhos:
        print(f'Filhos: {filho.nome}')

