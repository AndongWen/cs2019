def violent_match(s, t):
	i, j = 0, 0
	m, n = len(s), len(t)
	while i < m and j < n:
		if s[i] == t[j]:
			i += 1
			j += 1
		else:
			i = i-j+1
			j = 0
	if j == n:
		return i-j
	return -1


def main():
	a = 'abcdefghjgblackjgtrehrtet'
	b = 'blackju'
	x = violent_match(a, b)
	print(x)



if __name__ == "__main__":
	main()
