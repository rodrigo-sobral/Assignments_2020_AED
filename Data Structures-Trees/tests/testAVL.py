from re import split
from datetime import datetime
from random import randint

class Node():
    tot_palavras=0
    palavras_distintas=0
    numero_rotacoes=0
    def __init__(self, palavra, linha):
        self.palavra=palavra
        self.linha=[linha]
        self.fator_equi=0
        self.altura=1
        self.menor=None
        self.maior=None
        Node.tot_palavras+=1
        Node.palavras_distintas+=1
    
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
        Node.numero_rotacoes+=1
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
                Node.tot_palavras+=1
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
            start_time = datetime.now()
            num_linha=0
            texto=[]
            aux=input().strip("\n").upper()
            while (aux!="FIM."): 
                conteudo=split(r'[( ),.;]\s*',aux)
                texto.append(conteudo)
                arvore= adicionaPalavras(arvore, conteudo, num_linha)
                aux=input().strip("\n").upper()
                num_linha+=1
            resultados+= "GUARDADO.\n"
            now1=(datetime.now()-start_time).seconds
        elif comando=="TCHAU": break
    
    # 50 LINHAS
    start_time = datetime.now()
    for i in range(50):
        linha=texto[randint(0, 999)]
        arvore.procuraPalavraNaArvore(linha[randint(0, len(linha)-1)], None)
    now2=(datetime.now()-start_time).microseconds
    
    # ASSOC
    start_time = datetime.now()
    for i in range(50):
        linha=texto[randint(0, 999)]
        arvore.procuraPalavraNaArvore(linha[randint(0, len(linha)-1)], randint(0,999))
    now3=(datetime.now()-start_time).microseconds

    # 500 LINHAS
    palavras=[]
    for i in range(10):
        linha=texto[randint(0, 999)]
        palavras.append(linha[randint(0, len(linha)-1)])

    start_time = datetime.now()
    for i in range(500): arvore.procuraPalavraNaArvore(palavras[randint(0, len(palavras)-1)], None)
    now4=(datetime.now()-start_time).microseconds

    print("\nDADOS:\nPalavras: {}\nDistintas: {}".format(arvore.tot_palavras, arvore.palavras_distintas))
    print("Numero de rotacoes simples:", Node.numero_rotacoes)
    return now1, now2, now3, now4

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
    tempos=[0,0,0,0]
    for i in range(20): 
        aux=recebe_comandos()
        tempos[0]+=aux[0]
        tempos[1]+=aux[1]
        tempos[2]+=aux[2]
        tempos[3]+=aux[3]
    print("TEMPOS MEDIOS:\nCARREGAMENTO: {}\n50 LINHAS {}\n50 ASSOC: {}\n500 LINHAS: {}".format(tempos[0]/20, tempos[1]/20, tempos[2]/20, tempos[3]/20))
