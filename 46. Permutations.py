
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
print(permute("CBASP"))