from livro import Livro


def carregaLivros(ficheiro):
    with open(ficheiro, "r") as f:
        listaLivros = []
        linhas = f.readlines()
        for lin in linhas:
            linha = lin.split(";")
            if linha[3].strip() == "0":
                estado = "emprestado"
            else:
                estado = "disponivel"
            livro = Livro(linha[0], linha[1], int(linha[2]), estado)
            listaLivros.append(livro)
        return listaLivros
                
                
teste = carregaLivros("Fichas/ficha8/livros.txt")

def livros_dsp(ficheiro):
    livrosdisp = 0
    with open(ficheiro, "r") as f:
        for livro in len.ficheiro:
            livrosdisp += 1
            

def novo_livro():
    print("-----Novo Livro----")
    titulo = input("Titulo do livro:") 
    autor = input("Quem é o autor:") 
    anoPublica = input("Qual o ano de publicação:") 
    livro = Livro(titulo, autor, anoPublica)
    return livro


def livroMAisAntigo(lista:list[Livro]):
    ano_antigo = min(anoPublica)
    for livro in lista:
        if livro.anoPublica == ano_antigo:
            return livro


def guardarLivro(nomeFicheiro, lista: list[Livro]):
    with open(nomeFicheiro, "w") as f:
        for livro in lista:
            if livro.estado == "disponivel":
                estado = 1
            else:
                estado =0
            f.writeline(f"")

