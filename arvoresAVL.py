from re import split

class Node():
    def __init__(self, palavra, linha):
        self.palavra=palavra
        self.linha=[linha]
        self.fator_equi=0
        self.altura=1
        self.menor=None
        self.maior=None
    
    def equilibrarArvore(self):
        auxcima=self
        if self.fator_equi<-1:
            self=self.maior
            auxcima.maior=None
            if self.fator_equi==-1:
                if self.menor!=None:
                    auxcima.maior=self.menor
                    self.menor=None
            elif self.fator_equi==1: 
                auxmeio=self
                self=self.menor
                if self.menor!=None: 
                    auxcima.maior=self.menor
                if self.maior!=None:
                    auxmeio.menor=self.maior
                else: auxmeio.menor=None
                self.maior=auxmeio
            self.menor=auxcima
        elif self.fator_equi>1:
            self=self.menor
            auxcima.menor=None
            if self.fator_equi==1:
                if self.maior!=None:
                    auxcima.menor=self.maior
                    self.maior=None
            elif self.fator_equi==-1: 
                auxmeio=self
                self=self.maior
                if self.maior!=None: 
                    auxcima.menor=self.maior
                if self.menor!=None:
                    auxmeio.maior=self.menor
                else: auxmeio.maior=None
                self.menor=auxmeio
            self.maior=auxcima
        return self

    def atualizaAlturasFatores(self):
        if self.menor==None and self.maior==None: 
            self.altura=1
            self.fator_equi=0
            return self
        altura_menor, altura_maior= 0, 0
        if self.menor!=None:
            self.menor=self.menor.atualizaAlturasFatores()
            altura_menor=self.menor.altura
        if self.maior!=None: 
            self.maior= self.maior.atualizaAlturasFatores()
            altura_maior=self.maior.altura
        
        self.fator_equi= altura_menor-altura_maior

        if self.fator_equi>1 or self.fator_equi<-1:
            self=self.equilibrarArvore() 
            self.atualizaAlturasFatores() 
            if self.maior.altura>self.menor.altura: self.altura= 1+self.maior.altura
            else: self.altura= 1+self.menor.altura
            return self

        if altura_maior>altura_menor: self.altura= 1+altura_maior
        else: self.altura= 1+altura_menor
        return self
        
    def adicionarElementosAVL(self, palavra, linha):
        while True:
            if self.palavra>palavra:
                if (self.menor==None): 
                    self.menor=Node(palavra, linha)
                    break
                else: self=self.menor
            elif self.palavra<palavra:
                if (self.maior==None):
                    self.maior=Node(palavra, linha)
                    break
                else: self=self.maior
            else: 
                if linha not in self.linha: self.linha.append(linha)
                break

    def procuraPalavraNaArvore(self, palavra, linha):
        ocorencias=""
        while True:
            if self.palavra==palavra:
                if linha==None:
                    for i in range(len(self.linha)):
                        if i!=len(self.linha)-1: ocorencias+=str(self.linha[i])+" "
                        else: ocorencias+=str(self.linha[i])+"\n"
                    return ocorencias
                elif linha in self.linha: return "ENCONTRADA.\n"
                else: return "NAO ENCONTRADA.\n"
            elif self.palavra>palavra:
                if (self.menor==None): return "-1\n"
                else: self=self.menor
            elif self.palavra<palavra:
                if (self.maior==None): return "-1\n"
                else: self=self.maior

def recebe_comandos():
    arvore=None
    resultados=""
    while True:
        comando=input().strip("\n")

        if comando=="TEXTO": 
            linha=0
            aux=input().strip("\n").upper()
            while (aux!="FIM."): 
                arvore= adicionaPalavras(arvore, split(r'[( ),.;]\s*',aux), linha)
                aux=input().strip("\n").upper()
                linha+=1
            resultados+= "GUARDADO.\n"
        elif comando=="TCHAU": break
        else:
            # Ainda não recebeu um texto
            if arvore==None: print("Ainda não inseriu um texto.")
            else:
                comando=comando.split(" ")
                if comando[0]=="LINHAS" and len(comando)==2: resultados+=arvore.procuraPalavraNaArvore(comando[1].upper(), None)
                elif comando[0]=="ASSOC" and len(comando)==3: resultados+=arvore.procuraPalavraNaArvore(comando[1].upper(), int(comando[2]))
                else: print("Comando incorreto.")
    print(resultados, end='')

def adicionaPalavras(arvore: Node, linha, n_linha):
    if n_linha==0: 
        arvore=Node(linha[0], n_linha)
        for palavra in range(1, len(linha)):
            if linha[palavra]!='': 
                arvore.adicionarElementosAVL(linha[palavra], n_linha)
                arvore=arvore.atualizaAlturasFatores()
    else:
        for palavra in range(len(linha)):
            if linha[palavra]!='': 
                arvore.adicionarElementosAVL(linha[palavra], n_linha)
                arvore=arvore.atualizaAlturasFatores()
    return arvore

if __name__ == "__main__":
    recebe_comandos()
