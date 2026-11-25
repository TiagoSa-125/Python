class Veiculo:
    def __init__(self, matri, marca, num_pneus):
        self.__matricula = matri
        self.marca = marca
        self.num_pneus = num_pneus
        
    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, novaMatricula):
        self.__matricula = novaMatricula
    
    def fazerBarulho(self):
        print("MEOW MEOW")
        
class Moto(Veiculo):
    def __init__(self, matri, marca, num_pneus, cilindrada):
        super().__init__(matri, marca, num_pneus)
        self.cilindrada = cilindrada
        
    def __str__(self):
         return self.matricula ," - Moto da marca ", self.marca
     
    
    def __eq__(self, outra_moto):
        return self.marca == outra_moto.marca
        
    def fazerBarulho(self):
            print("MIGUEL MIGUEL")
        
v1 = Veiculo("34-AD-P0", "Mercedez", 4)
v1.matricula = "67-NI-GG"
v1.fazerBarulho()
print(v1.matricula)


v2  = Moto("13-32-AD", "Miguel", 2, 140 )
v3  = Moto("AF-14-AD", "Miguel", 2, 70000 )
v2.fazerBarulho()


if v2 == v3:
    print("Mesma marca")
    
    
x = "O alquimista;Paulo Coelho;1988;1"

lista = x.split(";")

print (lista)