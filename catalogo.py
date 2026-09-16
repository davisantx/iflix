class Filme:
    generos: tuple = ("DRAMA", "COMEDIA", "ACAO", "TERROR", "ROMANCE", "FICCAO")
    
    def __init__(self, titulo: str, diretor: str, ano: int, genero: str):
        self.__titulo = titulo.upper()
        self.__diretor = diretor.upper()
        self.__ano = ano

        if not genero.upper() in Filme.generos:
            raise ValueError("Erro! Gênero desconhecido!")
        
        self.__genero = genero.upper()

    @property
    def titulo(self) -> str:
        return self.__titulo
        
    @titulo.setter
    def titulo(self, valor) -> None:
        pass

    @property
    def diretor(self) -> str:
        return self.__diretor

    @diretor.setter
    def diretor(self, valor) -> None:
        pass

    @property
    def genero(self) -> str:
        return self.__genero

    @genero.setter
    def genero(self, valor) -> None:
        pass
        
    def __str__(self) -> str:
        return f"Título: {self.__titulo} | Diretor: {self.__diretor} | Ano: {self.__ano} | Gênero: {self.__genero}"


class Catalogo:
    def __init__(self):
        self.__filmes: list[Filme] = []

    def adicionar_filme(self, filme: Filme):
        if not isinstance(filme, Filme):
            raise TypeError("Apenas filme pode ser adicionado a lista de filmes do catologo!")
            
        self.__filmes.append(filme)
        
    def remover_filme(self, titulo: str):
        for filme in self.__filmes:
            if filme.titulo == titulo.upper():
                self.__filmes.remove(filme)
                return


    def listar_filmes(self, genero: str=""):
        saida: str = ""

        if len(self.__filmes) == 0:
            print("Não há filmes cadastrados!")
            return

        existe_filme_do_genero: bool = False
        
        for filme in self.__filmes:
            if genero.upper() in Filme.generos:
                saida = f"Filmes do gênero: {genero}: \n\n"
                if filme.genero.upper() == genero.upper():
                    saida += f"{filme}\n"
                    if not existe_filme_do_genero:
                        existe_filme_do_genero = True
                    print(saida)
                return
            else:
                saida = "Todos os filmes do catalogo: \n\n"
                saida += f"{filme}\n"
                print(saida)
                return
        if not existe_filme_do_genero:
            print("Não há filmes do gênero escolhido cadastrados!")
            return