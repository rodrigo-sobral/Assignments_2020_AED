from datetime import datetime

def receiveCommands():
    # [ word , [all_searchers] , [distinct_searchers] ]
    database=[]
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
            mergeSort(database, 1)
            sortGlobalTime= (datetime.now()-startTime).microseconds
            i=1
            results+=str(database[0][0])
            while i<len(database) and len(database[0][1])==len(database[i][1]): 
                results+=" "+str(database[i][0])
                i+=1
            results+="\n"
        elif command=="PESQ_UTILIZADORES": 
            startTime= datetime.now()
            mergeSort(database, 2)
            sortUtilizadoresTime= (datetime.now()-startTime).microseconds
            i=1
            results+=str(database[0][0])
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

def mergeSort(database, command): 
    if len(database)>1: 
        mid = len(database)//2
        left_array, right_array = database[:mid], database[mid:] 

        mergeSort(left_array, command) 
        mergeSort(right_array, command) 
        
        database.clear() 
        while len(left_array) > 0 and len(right_array) > 0: 
            if len(left_array[0][command]) >= len(right_array[0][command]): 
                database.append(left_array[0]) 
                left_array.pop(0)
            else: 
                database.append(right_array[0]) 
                right_array.pop(0) 
  
        for i in left_array: 
            database.append(i) 
        for i in right_array: 
            database.append(i)

#====================================

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
    print("Total Users:", totWords)

    print("Sorting Global Time:", sortGlobalTime/20)
    print("Sorting Utilizadores Time:", sortUtilizadoresTime/20)