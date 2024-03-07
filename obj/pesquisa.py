import obj.q_pesquisa as p

class artigos_rev:
     def __init__(self,est:None,perguntas:p,instrumento:None) -> None:
        self.est_pesq =est
        self.perguntas= perguntas
        self.instrumento =instrumento
        self.string = ''
    
     def setString(self,s:str) ->None:
        self.string = s
     def setEstrategia(self, e:str)->None:
         self.est_pesq = e
     def setInstrumento(self,i:str)->None:
         self.instrumento = i
     