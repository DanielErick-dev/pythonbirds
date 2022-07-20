class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome



    def cumprimentar(self):
        return f'olá {self.nome} and you are {self.idade} years old'


if __name__ == '__main__':
    p = Pessoa('daniel')
    print(p.cumprimentar())


