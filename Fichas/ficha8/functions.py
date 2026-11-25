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


for livro in teste:
    print(livro)
