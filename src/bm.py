def arr(pattern): #array temp
	arr_bm = {}
	for i in range(len(pattern)): 
		arr_bm[pattern[i]] = i
	return arr_bm 

def boym(pattern, text): #mencari pattern dalam teks dengan algoritma boyer moore
	pat = pattern.lower()
	txt = text.lower()
	
	m = len(pat) 
	n = len(txt)

	arr_bm = arr(pat) 
	arr_match = []
	# s is shift of the pattern
	s = 0
	while(s <= n-m): 
		j = m-1

		while j>=0 and txt[s+j] == pat[j]: 
			j -= 1

		if j<0:
			arr_match.append(s)
			if s+m<n:
				if (txt[s+m] in arr_bm):
					s += m-arr_bm[txt[s+m]]
				else:
					s += m+1
			else:
				s += 1
		else:
			if (txt[s+j] in arr_bm):
				s += max(1, j-arr_bm[txt[s+j]]) 
			else:
				s += max(1, j+1) 
	return len(arr_match)>0
