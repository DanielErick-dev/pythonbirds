class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'olá {self.nome} and you are {self.idade} years old'



if __name__ == '__main__':
    renzo = Pessoa(nome='renzo')
    luciano = Pessoa(renzo, nome='luciano')
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'ramalho'
    print(luciano.__dict__)
    print(renzo.__dict__)
