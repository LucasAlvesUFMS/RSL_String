from obj import Artigo


def continua_():
    entrada = input().upper()
    if entrada.find('N') != -1:
        print()
        print("Obrigado pela escolha!")
        return True

def entrada_caixaAlta():
    return input().upper()

def sepEntrada(s:str):
    return input().upper().split(s)

artigosBD = []

while True:

    print("Deseja continuar:")
    print('Sim - s ou Não - n')
    
    if continua_():
        break
    
    print("Qual o titulo do trabalho?")
    titulo =  entrada_caixaAlta()
    print()
    print("Qual o nome do autor?")
    autor =  entrada_caixaAlta()
    print()
    print("Quais os topicos? (separe por virgulas)")
    topicos =  sepEntrada(',')
    print()
    print('Ano da publicação:')
    anoPub = int(input())
    print()
    print('Quais são as respostas trazidas pelo artigo? (Separe por pontos finais .)')
    resp = sepEntrada('.')
    print()
    print('Quais foram as perguntas trazidas pelo artigo? (Separe por pontos de interrogação ?)')
    perguntas = sepEntrada('?')
    print()

    artigo = Artigo.Artigo(titulo,autor,topicos,anoPub,perguntas,resp)
    print(f'Titulo:{titulo},{autor}-{anoPub}\nTopicos:{topicos}\n\nPerguntas:{perguntas}\n Respostas:{resp}')
    print()
    artigosBD.append(artigo)
