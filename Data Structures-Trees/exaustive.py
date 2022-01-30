from re import split

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
    texto=[]
    resultados=""
    while True:
        comando=input().strip("\n")

        if comando=="TEXTO": 
            aux=input().strip("\n").upper()
            while (aux!="FIM."): 
                texto.append(split(r'[( ),.;]\s*',aux))
                aux=input().strip("\n").upper()
            resultados+= "GUARDADO.\n"
        elif comando=="TCHAU": break
        else:
            # Ainda não recebeu um texto
            if len(texto)==0: print("Ainda não inseriu um texto.")
            else:
                comando=comando.split(" ")
                if comando[0]=="LINHAS" and len(comando)==2: resultados+=procuraLinhaDaPalavra(texto, comando[1].upper())
                elif comando[0]=="ASSOC" and len(comando)==3: resultados+=procuraPalavraNaLinha(texto, comando[1].upper(), int(comando[2]))
                else: print("Comando incorreto.")
    print(resultados, end="")

if __name__ == "__main__":
    recebe_comandos()