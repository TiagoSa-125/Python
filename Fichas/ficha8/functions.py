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
            

for livro in teste:
    print(livro)
