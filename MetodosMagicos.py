"""
Métodos Mágicos, são todos os métodos que utilizam dunder.
dunder init -> __init__
dunder é double underscore
dunder __repr__ é a representação do objeto
    def __repr__(self):
        return f'{self.titulo}\n{self.autor}\n{self.paginas}\n'
"""


class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    def __str__(self):
        return self.titulo
    def __len__(self):
        return self.paginas
    def __del__(self):
        print(f'Um objeto do tipo {self.__class__.__name__} foi deletado da memória')
    def __add__(self, other):
        return f'{self} - {other}'
    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += str(self) + ' '
            return msg
        else:
            raise TypeError(f"{other} not is int type.")
livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligência Artifical com Python', 'Geek University', 350)
print(livro1)
print(livro2)
print(livro1 + livro2)
print(livro1 * 'opa')