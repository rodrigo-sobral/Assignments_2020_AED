def receiveCommands():
    database=[]     # [ word , [all_searchers] , [distinct_searchers] ]
    results=""
    while True:
        command=input().strip("\n")

        if command=="PALAVRAS": 
            aux=input().strip("\n")
            while (aux!="FIM."): 
                aux=aux.split(" ")
                index= isIn(database, aux[0])
                if index== -1: database.append([aux[0], [aux[1]], [aux[1]]])
                elif aux[1] not in database[index][1]:
                    database[index][1].append(aux[1])
                    database[index][2].append(aux[1])
                else: database[index][1].append(aux[1])
                aux=input().strip("\n")
            results+= "GUARDADAS\n"
        elif command=="PESQ_GLOBAL": 
            database= radixSorting(database, 1)
            results+=str(database[0][0])
            i=1
            while i<len(database) and len(database[0][1])==len(database[i][1]): 
                results+=" "+str(database[i][0])
                i+=1
            results+="\n"
        elif command=="PESQ_UTILIZADORES": 
            database= radixSorting(database, 2)
            results+=str(database[0][0])
            i=1
            while i<len(database) and len(database[0][2])==len(database[i][2]): 
                results+=" "+str(database[i][0])
                i+=1
            results+="\n"
        elif command=="TCHAU": break
        else: print("Incorrect command.")
    print(results, end='')

def isIn(database, word):
    for search in database:
        if word.upper()==search[0].upper(): return database.index(search)
    return -1
      
def radixSorting(database, command):
    searchesArray= [str(len(search[command])) for search in database]
    longestDigits= len(str(max(searchesArray, key=len)))
    for num_digits in range(longestDigits):
        digitsArray=[]
        for digits in searchesArray:
            if len(digits)-1-num_digits<0: digitsArray.append(-1)
            else: digitsArray.append(int(digits[len(digits)-1-num_digits]))
        database= countingSort(database, digitsArray)
        searchesArray=[str(len(search[command])) for search in database]
    return database

def countingSort(database, digitsArray):
    smaller=min(digitsArray)
    indexArray= [0 for i in range(max(digitsArray)-smaller+1)]
    sortedArray=[]
    for number in digitsArray: indexArray[number-smaller]+=1
    del smaller, number
    for occurrences in range(len(indexArray)-1, -1, -1):
        while indexArray[occurrences]!=0: 
            greater=digitsArray.index(max(digitsArray))
            indexArray[occurrences]-=1
            sortedArray.append(database[greater])
            digitsArray.pop(greater)
            database.pop(greater)
    return sortedArray
     
if __name__ == "__main__": receiveCommands()