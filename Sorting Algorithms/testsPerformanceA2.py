from datetime import datetime

def receiveCommands():
    database=[]     # [ word , [all_searchers] , [distinct_searchers] ]
    results=""
    while True:
        command=input().strip("\n")

        if command=="PALAVRAS": 
            startTime= datetime.now()
            totWords=0
            aux=input().strip("\n")
            while (aux!="FIM."): 
                totWords+=1
                aux=aux.split(" ")
                index= isIn(database, aux[0])
                if index== -1: database.append([aux[0], [aux[1]], [aux[1]]])
                elif aux[1] not in database[index][1]:
                    database[index][1].append(aux[1])
                    database[index][2].append(aux[1])
                else: database[index][1].append(aux[1])
                aux=input().strip("\n")
            loadingTextTime= (datetime.now()-startTime).seconds
            results+= "GUARDADAS\n"
        elif command=="PESQ_GLOBAL": 
            startTime= datetime.now()
            database= radixSorting(database, 1)
            sortGlobalTime= (datetime.now()-startTime).microseconds
            results+=str(database[0][0])
            i=1
            while i<len(database) and len(database[0][1])==len(database[i][1]): 
                results+=" "+str(database[i][0])
                i+=1
            results+="\n"
        elif command=="PESQ_UTILIZADORES": 
            startTime= datetime.now()
            database= radixSorting(database, 2)
            sortUtilizadoresTime= (datetime.now()-startTime).microseconds
            results+=str(database[0][0])
            i=1
            while i<len(database) and len(database[0][2])==len(database[i][2]): 
                results+=" "+str(database[i][0])
                i+=1
            results+="\n"
        elif command=="TCHAU": break
        else: print("Incorrect command.")

    #print(results, end='')
    return [database, loadingTextTime, sortGlobalTime, sortUtilizadoresTime, totWords]

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
     
def getDistinctUsers(database):
    tot_users=[]
    for search in database:
        for user in search[2]:
            if user not in tot_users: tot_users.append(user)
    return len(tot_users)
def getWordUserPair(database):
    counter=0
    for search in database: counter+=len(search[2])
    return counter
   
if __name__ == "__main__":
    [database, loadingTextTime, sortGlobalTime, sortUtilizadoresTime, totWords]= receiveCommands()
    for i in range(19): 
        results=receiveCommands()
        loadingTextTime+= results[1]
        sortGlobalTime+= results[2]
        sortUtilizadoresTime+= results[3]
    print("=================")
    print("DATA:")
    print("Loading Text Time:", loadingTextTime/20)
    print("Distinct Words:", len(database))
    print("Distinct Users:", getDistinctUsers(database))
    print("Distinct Word-User Pair:", getWordUserPair(database))
    print("Total Words:", totWords)
    print("Total Users:")

    print("Sorting Global Time:", sortGlobalTime/20)
    print("Sorting Utilizadores Time:", sortUtilizadoresTime/20)