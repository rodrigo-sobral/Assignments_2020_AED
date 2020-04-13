from re import split

class Node():
    def __init__(self, palavra, linha):
        self.palavra=palavra
        self.linha=[linha]
        self.need_up=True
        self.menor=None
        self.maior=None
    
    def tradeNodes(self, no_pai):
        if no_pai.menor==self: 
            no_pai.menor=self.maior
            self.maior=no_pai
        elif no_pai.maior==self:
            no_pai.maior=self.menor
            self.menor=no_pai
        return self

    def zigZaggingNodes(self, no_pai):
        if self.need_up==False and self.menor==None and self.maior==None: return 0, self
        if self.need_up==True: return 2, self.tradeNodes(no_pai)
        if self.menor!=None:
            aux=self.menor.zigZaggingNodes(self)
            if aux[0]==1: 
                self.menor= aux[1]
                if self.menor.need_up==True: return 1, self.menor.tradeNodes(self)
            elif aux[0]==2: 
                self= aux[1]
                return 1, self
        if self.maior!=None: 
            aux=self.maior.zigZaggingNodes(self)
            if aux[0]==1: 
                self.maior= aux[1]
                if self.maior.need_up==True: return 1, self.maior.tradeNodes(self)
            elif aux[0]==2: 
                self= aux[1]
                return 1, self
        
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
                    self.need_up=True
                    return ocorencias
                elif linha in self.linha: 
                    self.need_up=True
                    return "ENCONTRADA.\n"
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
                if comando[0]=="LINHAS" and len(comando)==2: 
                    aux=arvore.procuraPalavraNaArvore(comando[1].upper(), None)
                    resultados+=aux
                    if aux!="-1\n" and aux!="NAO ENCONTRADA\n": arvore=arvore.zigZaggingNodes(arvore)
                elif comando[0]=="ASSOC" and len(comando)==3: 
                    aux=arvore.procuraPalavraNaArvore(comando[1].upper(), int(comando[2]))
                    resultados+=aux
                    if aux!="-1\n" and aux!="NAO ENCONTRADA\n": arvore=arvore.zigZaggingNodes(arvore)
                else: print("Comando incorreto.")
    print(resultados, end='')

def adicionaPalavras(arvore: Node, linha, n_linha):
    if n_linha==0: 
        arvore=Node(linha[0], n_linha)
        arvore.need_up=False
        for palavra in range(1, len(linha)):
            if linha[palavra]!='': 
                arvore.adicionarElementosAVL(linha[palavra], n_linha)
                arvore=arvore.zigZaggingNodes(arvore)[1]
                arvore.need_up=False
    else:
        for palavra in range(len(linha)):
            if linha[palavra]!='': 
                arvore.adicionarElementosAVL(linha[palavra], n_linha)
                arvore=arvore.zigZaggingNodes(arvore)[1]
                arvore.need_up=False
    return arvore

if __name__ == "__main__":
    recebe_comandos()
