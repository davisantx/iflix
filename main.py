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
    saida = ""
    for i, opcao in enumerate(opcoes):
        saida += (f"{i + 1} - {opcao}\n")
    print(f"{saida}\n")

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
        
def adicionar(catalogo: Catalogo) -> None:
    informacoes = {}
    
    try:
        informacoes = formulario(
            cabecalho="Adicionar filme: ",
            campos=[
                ("Título", str),
                ("Diretor", str),
                ("Ano", int),
                ("Gênero", str),
            ]
        )
    except TypeError as e:
        print(e)
        
    try:
        catalogo.adicionar_filme(
            filme=Filme(
                titulo=informacoes["Título"], 
                diretor=informacoes["Diretor"], 
                ano=informacoes["Ano"], 
                genero=informacoes["Gênero"]
            )
        )
    except ValueError as e:
        print(e)

def remover(catalogo: Catalogo) -> None:
    informacoes = {}
    try:
        informacoes = formulario(
            cabecalho="Remover filme: ",
            campos=[
                ("Título", str),
            ]
        )
    except TypeError as e:
        print(e)

    if catalogo.remover_filme(informacoes["Título"]):
        print(f"Livro {informacoes["Título"]} removido com sucesso!")
        return
        
    print(f"Livro {informacoes["Título"]} não foi encontrado!")

def listar(catalogo: Catalogo):
    menu(
        opcoes=[
            "Todos",
            "Por gênero"
        ]
    )
    
    genero = entrada("Insira a opção: ")

    match genero:
        case 1:
            catalogo.listar_filmes()
  
        case 2:
            dados = {}
            try:
                dados = formulario(
                    cabecalho="",
                    campos=[("Insira o gênero: ", str)]
                )
            except TypeError as e:
                print(e)
                
            try:
                catalogo.listar_filmes(dados["Insira o gênero: "])
            except ValueError as e:
                print(e)
        case _:
            print("Opção inválida!")
            
def sistema():
    catalogo = Catalogo()
    while True:
        print("Bem vindo ao sistema de catalógos de filmes: \n")
        menu(
            opcoes=[
                "Adicionar", 
                "Remover", 
                "Listar", 
                "Sair"
            ]
        )

        opcao_selecionada = entrada("Escolha uma das opções: ")

        match opcao_selecionada:
            case 1:
                adicionar(catalogo=catalogo)
                continue
            case 2:
                remover(catalogo=catalogo)
                continue
            case 3:
                listar(catalogo=catalogo)
                continue
            case 4:
                print("Saindo...")
                break
            case _:
                print("Opção inválida!\n")
                continue
            
if __name__ == "__main__":
    sistema()