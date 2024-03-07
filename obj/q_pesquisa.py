class perguntas:
    def __init__(self, index:int,pergunta:str) -> None:
        self.index =index
        self.texto = pergunta
    
    def get_index(self):
        return self.index
    
    def get_pergunta(self):
        return self.texto