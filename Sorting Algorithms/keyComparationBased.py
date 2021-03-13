def receiveCommands():
    # [ word , [all_searchers] , [distinct_searchers] ]
    database=[]
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
            mergeSort(database, 1)
            i=1
            results+=str(database[0][0])
            while i<len(database) and len(database[0][1])==len(database[i][1]): 
                results+=" "+str(database[i][0])
                i+=1
            results+="\n"
        elif command=="PESQ_UTILIZADORES": 
            mergeSort(database, 2)
            i=1
            results+=str(database[0][0])
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

#   Baseado em: https://www.geeksforgeeks.org/merge-sort/
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

if __name__ == "__main__":
    receiveCommands()
