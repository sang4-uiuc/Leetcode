def generateParenthesis(n):
    if not n:
        return []
    left, right, ans = n, n, []
    dfs(left,right, ans, "")
    return ans, len(ans)

def dfs(left, right, ans, string):
    if right < left:
        return
    if not left and not right:
        ans.append(string)
        return
    if left:
        dfs(left-1, right, ans, string + "(")
    if right:
        dfs(left, right-1, ans, string + ")")


print(generateParenthesis(4))