def sort(list):

   for i in range(5):
       minpos = i
       for j in range(i,6):
           if list[j] < list[minpos]:
               minpos = j


       temp = list[i]
       list[i] = list[minpos]
       list[minpos] = temp

       print(list)


list=[2,1,6,9,0,3,]
sort(list)
print(list)
