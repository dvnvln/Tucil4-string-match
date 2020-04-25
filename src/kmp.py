def kmpArr(pat, m, x):#array dengan prefix dan suffix terpanjang
    pattern = pat.lower()
    len = 0 # length of the previous longest prefix suffix 
    i = 1
    while i < m: 
        if pattern[i] == pattern[len]: 
            len += 1
            x[i] = len
            i += 1
        else: #pattern[i]!= pattern[len]: 
            if len != 0: 
                len = x[len-1] 
            else: #len==0
                x[i] = 0
                i += 1
    return x
    
def kmp(pat, txt):#mencari pattern pada text menggunakan algoritma kmp
    pattern = pat.lower()
    text = txt.lower()
    n = len(text)
    m = len(pattern)
    x =[0 for y in range (m)] #arr of the longest length of prefix and suffix 
    arr = kmpArr(pattern,m,x)
    i = 0
    j = 0
    arr_match =[]
    while i<n:
        if text[i] == pattern[j]:
            i+=1
            j+=1
        
        if j == m :
            arr_match.append(i-j)
            j = arr[j-1]
        
        elif i < n and pattern [j] != text[i]:
            if j != 0:
                j = arr[j-1]
            else: #j==0
                i+=1
    return(len(arr_match)>0)
