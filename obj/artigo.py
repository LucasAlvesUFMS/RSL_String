import q_pesquisa 
class Artigo:
    def __init__(self,titulo:str,autor:str,topico:str,ano_pub:int,perguntas:q_pesquisa,respostas:None) -> None:
        self.titulo = titulo
        self.autor = autor
        self.topico = topico
        self.ano_pub = ano_pub
        self.perguntas = perguntas
        self.respostas =respostas
        
    def getTitulo(self):
        return self.titulo
    def getTopicos(self):
        return self.topico
    def getAutor(self):
        return self.autor
    def getAnoPublica(self):
        return self.ano_pub
    def getPerguntas(self):
        return self.perguntas
    def getRespostas(self):
        return self.respostas
    