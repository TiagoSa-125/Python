class Livro:
    def __init__(self, titulo, autor, anoPublica, estadoDispo = "disponivel"):
        self.titulo = titulo
        self.autor = autor
        self.anoPublica = anoPublica
        self.estadoDispo = estadoDispo
        
        
    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.anoPublica} - {self.estadoDispo}"

    def emprestar(self):
        if self.estadoDispo == "disponivel":
            self.estadoDispo = "emprestado"
            return True
        return False

    def devolver(self):
        self.estadoDispo = "disponivel"