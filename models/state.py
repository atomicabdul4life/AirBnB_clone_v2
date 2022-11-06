def bubble(list):
    leng = len(list)
    for j in range(leng):
        for i in range(leng - 1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
    return list

def merge(list):
    leng = len(list)
    if leng > 1:
        mid = leng//2
        list1 = list[:mid]
        list2 = list[mid:]
        
        merge(list1)
        merge(list2)
        i=j=k=0
        while (i < len(list1) and j < len(list2)):
            if(list1[i] < list2[j]):
                list[k] = list1[i]
                i+=1
            else:
                list[k] = list2[j]
                j+=1
            k+=1
        while(i<len(list1)):
            list[k] = list1[i]
            i+=1
            k+=1
        while(j<len(list2)):
            list[k] = list2[j]
            j+=1
            k+=1

def insertion(list):
    leng = len(list)
    for i in range(1, leng):
        j = i
        while(list[j-1] > list[j] and j>0):
            list[j-1], list[j] = list[j], list[j-1]
            j-=1

def selection(list):
    leng = len(list)
    for i in range(leng - 1):
        j = i+1
        while(j < leng):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
            j+=1
    
            

list = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(bubble(list))
print(list)
#insertion(list)
#merge(list)
#selection(list)
#quicksort(list)
print(list)