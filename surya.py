def myer_exam(input1,input2):
    
    
    n=input1
    lst=input2
    new_list = set(lst)
    if len(new_list) == len(lst):
        return sum(new_list)
    else:
        new_list = list(new_list)
     
        for item in range(n-len(new_list)):
            new_list.append(new_list[-1]+1)
        print(new_list)
        return sum(new_list)


