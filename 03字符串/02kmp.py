def get_next(t, next):
	i, k, m = 0, -1, len(t)
	while i < m-1:
		if k == -1 or t[i] == t[k]:
			i += 1
			k += 1
			if t[i] == t[k]:
				next[i] = next[k]
			else:
				next[i] = k	
		else:
			k = next[k]
	return next


def kmp_match(s, t):
	i, j = 0, 0
	m, n = len(s), len(t)
	next = [-1] * n
	a = get_next(t, next)
	for i in a:
		print(i)
	while i < m and j < n:
		if s[i] == t[j]:
			i += 1
			j += 1
		else:
			j = a[j]
	if j == n:
		return i-j
	return -1


def main():
	a = 'abceabcdfghjgblackjgtrehrtet'
	b = 'abcd'
	x = kmp_match(a, b)
	print(x)



if __name__ == "__main__":
	main()
