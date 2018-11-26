
def permuteHelper(a, l, r, output): 
    if l==r: 
        output.append("".join(a))
    else: 
        for i in range(l,r+1): 
            a[l], a[i] = a[i], a[l] 
            permuteHelper(a, l+1, r, output) 
            a[l], a[i] = a[i], a[l] # backtrack 

def permute(s):
    l = 0
    r = len(s) - 1
    output = []
    permuteHelper(list(s), l, r, output)
    return output

# print(permute("CDBAMC"))



def printCombination(arr, n, r): 
    data = [0]*r
    output = []
    combinationUtil(arr, data, 0,  
                    n - 1, 0, r, output)
    return output
def combinationUtil(arr, data, start,  
                    end, index, r, output): 
    t = []                      
    if (index == r): 
        for j in range(r): 
            t.append(data[j])
        output.append(t) 
        return
    i = start  
    while(i <= end and end - i + 1 >= r - index): 
        data[index] = arr[i]
        combinationUtil(arr, data, i + 1,  
                        end, index + 1, r, output)
        i += 1
s = "TH JH QC QD QS QH KH AH 2S 6S"
arr = s.split(' ')
r = 5; 
n = len(arr); 
combo = printCombination(arr, n, r)
for i in combo:
    print(i)
print(len(combo))
