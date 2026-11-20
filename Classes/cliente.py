class Cliente:
    #Atributos da classe
    totalClientes = 0
    
    def __init__(self,nome,peso,altura):
        #Atributos da instancia
        self.nome = nome
        self.peso = peso
        self.altura = altura
        Cliente.totalClientes +=1
        
        #Metodos Especiais dunder methods
        
        def __str__(self):
            return "O(A) cliente ", c1.nome , " tem ", c1.altura, " e pesa", c1.peso
        
        def __eq__(self, cl):
            return self.nome == cl.nome
        
        #Metodo da classe
        @classmethod
        
        def procurar(cls, clienteApesquisar):
            if clienteApesquisar == "Ana":
                return True
            return False
        
c1 = Cliente("Ana", 62, 1.65)
c2 = Cliente("Maria", 71, 1.85)
c3 = Cliente("Maria", 58, 1.67)
lista = [c1,c2,c3]

if c1 == c2:
    print("Ok")

if c2 == c3:
    print("Segundo OK")
    
print (f"Total de clientes: {Cliente.totalClientes}")

for c in lista:
    if Cliente.procurar[c.nome]:
        print(c)
    
