from catalogo import Catalogo, Filme


def teste():
    try:
        filme_1 = Filme(titulo="O Analista", diretor="Jonatas", ano=2010, genero="romance")
        filme_2 = Filme(titulo="Um Sonho de Liberdade", diretor="Marcio", ano=2003, genero="drama")

        catalogo_1 = Catalogo()
    
        catalogo_1.adicionar_filme(filme_1)
        catalogo_1.adicionar_filme(filme_2)
    
        catalogo_1.listar_filmes()
        
        catalogo_1.remover_filme("Um Sonho de Liberdade")
    
        catalogo_1.listar_filmes("drama")
        
    except (ValueError, TypeError) as e:
        print(e)

    
def menu(opcoes: list[str]):
    for i, opcao in enumerate(opcoes):
        print(f"{i + 1} - {opcao}")
    print("\n")

def entrada(msg: str, e_texto: bool=False) -> int | str:
    while True:
        try:
            valor = input(msg)
            if not e_texto:
                valor = int(valor)
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.") 
            continue

def formulario(cabecalho: str, campos: list[tuple[str, type]]):
    print(f"\n{cabecalho}\n")
    saida = {}

    for campo, tipo in campos:
        valor: int | str | None = None
        
        if tipo is int:
            valor = entrada(f"{campo}: ", e_texto=False)
        if tipo is str:
            valor = entrada(f"{campo}: ", e_texto=True)
        if valor is None:
            raise TypeError(f"Erro! Tipo inserido no campo: {campo} é inválido!") 
        
        saida[campo] = valor
        
    return saida
        

def sistema():
    catologo = Catalogo()
    while True:
        print("Bem vindo ao sistema de catalógos de filmes: \n")
        menu(opcoes=["Adicionar", "Remover", "Listar", "Sair"])

        opcao_selecionada = entrada("Escolha uma das opções: ")

        if opcao_selecionada == 1:
            informacoes = formulario(
                cabecalho="Adicionar filme: ",
                campos=[
                    ("Título", str),
                    ("Diretor", str),
                    ("Ano", int),
                    ("Gênero", str),
                ]
            )

            catologo.adicionar_filme(
                filme=Filme(
                    titulo=informacoes["Título"], 
                    diretor=informacoes["Diretor"], 
                    ano=informacoes["Ano"], 
                    genero=informacoes["Gênero"]
                )
            )
            continue

        if opcao_selecionada == 2:
            informacoes = formulario(
                cabecalho="Remover filme: ",
                campos=[
                    ("Título", str),
                ]
            )
            catologo.remover_filme(informacoes["Título"])
            continue
            
        if opcao_selecionada == 3:
            menu(
                opcoes=[
                    "Todos",
                    "Por gênero"
                ]
            )
            
            genero = entrada("Insira a opção: ")
            
            if genero == 1:
                catologo.listar_filmes()
                continue
                
            if genero == 2:
                dados = formulario(
                    cabecalho="",
                    campos=[("Insira o gênero: ", str)]
                )
                catologo.listar_filmes(dados["Insira o gênero: "])
                continue
                
        if opcao_selecionada == 4:
            print("Saindo...")
            break
            
if __name__ == "__main__":
    sistema()
            