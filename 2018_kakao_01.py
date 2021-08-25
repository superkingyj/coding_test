def solution(n, arr1, arr2):
    '''
    answer = []
    binaryStrArr, map = [],[]

    for i in range(n):
        binaryStrArr.append((bin(arr1[i]), bin(arr2[i])))

    for str1, str2 in binaryStrArr:
        str_ = ""
        str1 = "0"*(16-len(str1[2:]))+str1[2:] 
        str2 = "0"*(16-len(str2[2:]))+str2[2:]
        for i in range(16):
            str_ += str(int(str1[i])|int(str2[i]))
        map.append(str_)

    for item in map:
        str_ = ""
        for i in range(16-n, 16):
            if item[i] == "1": str_ += "#"
            else: str_ += " "
        answer.append(str_)
    '''
    
    arr = []
    for i in range(n):
        # bin(5|7) # ==> '0b111'
        # 111 --> 00111
        arr.append(
            bin(arr1[i] | arr2[i])[2:]
                .zfill(n)
                .replace("1", "#")
                .replace("0", " ")
        )
    return arr


print(solution(5,[9,20,28,18,11],[30,1,21,17,28])==["#####","# # #", "### #", "# ## ", "#####"])
print(solution(6,[46,33,33,22,31,50],[27,56,19,14,14,10])==["######", "### #", "## ##", " #### ", " #####", "### # "]
)


'''
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
'''