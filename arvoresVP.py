from re import split

class Node():
    def __init__(self, palavra, linha):
        self.palavra=palavra
        self.linha=[linha]
        self.isRed=True
        self.menor=None
        self.maior=None
    
    def equilibrarArvore(self, no_pai):
        if no_pai.maior==self:
            if no_pai.menor!=None and no_pai.menor.isRed==True:
                no_pai.isRed, no_pai.menor.isRed, no_pai.maior.isRed= True, False, False
                return 1, self
            else:
                if self.menor!=None and self.menor.isRed==True:
                    aux_meio=self
                    self=self.menor
                    no_pai.maior, aux_meio.menor=self.menor, self.maior
                    self.maior, self.menor=aux_meio, no_pai
                    self.isRed, self.maior.isRed, self.menor.isRed= False, True, True 
                elif self.maior!=None and self.maior.isRed==True: 
                    no_pai.maior=self.menor
                    self.menor=no_pai
                    self.isRed, self.maior.isRed, self.menor.isRed= False, True, True
                return 2, self
        elif no_pai.menor==self:
            if no_pai.maior!=None and no_pai.maior.isRed==True:
                no_pai.isRed, no_pai.menor.isRed, no_pai.maior.isRed= True, False, False
                return 1, self
            else:
                if self.maior!=None and self.maior.isRed==True:
                    aux_meio=self
                    self=self.maior
                    no_pai.menor, aux_meio.maior=self.maior, self.menor
                    self.menor, self.maior= aux_meio, no_pai
                    self.isRed, self.menor.isRed, self.maior.isRed= False, True, True
                elif self.menor!=None and self.menor.isRed==True:
                    no_pai.menor=self.maior
                    self.maior=no_pai
                    self.isRed, self.maior.isRed, self.menor.isRed= False, True, True 
            return 2, self

    def atualizaCores(self, no_pai):
        if self.menor==None and self.maior==None: return -1, self
        if self.menor!=None:
            resultado= self.menor.atualizaCores(self)
            if resultado[0]==-1: pass
            elif resultado[0]==0 or resultado[0]==1: self.menor=resultado[1]
            elif resultado[0]==2: self=resultado[1]
        if self.maior!=None:
            resultado= self.maior.atualizaCores(self)
            if resultado[0]==-1: pass
            elif resultado[0]==0 or resultado[0]==1: self.maior=resultado[1]
            elif resultado[0]==2: self=resultado[1]

        if self.maior!=None and self.isRed==True and self.maior.isRed==True: 
            return self.equilibrarArvore(no_pai)
        if self.menor!=None and self.isRed==True and self.menor.isRed==True:
            return self.equilibrarArvore(no_pai)
        return 0, self
        
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
        arvore.isRed=False
        for palavra in range(1, len(linha)):
            if linha[palavra]!='': 
                arvore.adicionarElementosAVL(linha[palavra], n_linha)
                arvore= arvore.atualizaCores(arvore)[1]
                arvore.isRed=False
    else:
        for palavra in range(len(linha)):
            if linha[palavra]!='': 
                arvore.adicionarElementosAVL(linha[palavra], n_linha)
                arvore= arvore.atualizaCores(arvore)[1]
                arvore.isRed=False
    return arvore

if __name__ == "__main__":
    recebe_comandos()
