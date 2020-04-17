from re import split
from datetime import datetime
from random import randint

def procuraLinhaDaPalavra(texto, palavraProcurada):
    linhas=""
    for linha in range(len(texto)):
        for palavra in texto[linha]:
            if palavraProcurada==palavra and str(linha) not in linhas: linhas+=str(linha)+" "
    if (linhas==""): return "-1\n"
    else: 
        linhas = linhas[:-1]
        return linhas+"\n"

def procuraPalavraNaLinha(texto, palavraProcurada, linha):
    for palavra in texto[linha]:
        if palavraProcurada==palavra: return "ENCONTRADA.\n"
    return "NAO ENCONTRADA.\n"

def recebe_comandos():
    resultados=""
    texto=[]
    while True:
        comando=input().strip("\n")

        if comando=="TEXTO": 
            start_time = datetime.now()
            aux=input().strip("\n").upper()
            while (aux!="FIM."): 
                texto.append(split(r'[( ),.;]\s*',aux))
                aux=input().strip("\n").upper()
            resultados+="GUARDADO.\n"
            now1=(datetime.now()-start_time).seconds
            break
        else: continue
    
    start_time = datetime.now()
    # LINHAS
    for i in range(50):
        linha=texto[randint(0,999)]
        palavra=linha[randint(0,len(linha)-1)]
        procuraLinhaDaPalavra(texto, palavra)
    now2=(datetime.now()-start_time).microseconds

    start_time = datetime.now()
    # ASSOC
    for i in range(50):
        num_linha=randint(0, 1000-1)
        linha=texto[num_linha]
        palavra=linha[randint(0,len(linha)-1)]
        procuraPalavraNaLinha(texto, palavra, num_linha)
    now3=(datetime.now()-start_time).microseconds

    # LINHAS
    lista_palavras=[]
    for i in range(10):
        linha=texto[randint(0, 1000-1)]
        lista_palavras.append(linha[randint(0,len(linha)-1)])
    start_time = datetime.now()
    for i in range(500): procuraLinhaDaPalavra(texto, lista_palavras[randint(0, len(lista_palavras)-1)])
    now4=(datetime.now()-start_time).microseconds

    return now1, now2, now3, now4

if __name__ == "__main__":
    tempos=[0,0,0,0]
    for i in range(20): 
        aux=recebe_comandos()
        tempos[0]+=aux[0]
        tempos[1]+=aux[1]
        tempos[2]+=aux[2]
        tempos[3]+=aux[3]
    print("TEMPOS MEDIOS:\nCARREGAMENTO: {}\n50 LINHAS {}\n50 ASSOC: {}\n500 LINHAS: {}".format(tempos[0]/20, tempos[1]/20, tempos[2]/20, tempos[3]/20))
