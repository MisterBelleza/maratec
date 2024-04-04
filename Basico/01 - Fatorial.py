def main():
	n = int(input())
	def fat(n):
	    if n==0: return 1
	    return fat(n-1)*n
	print(fat(n))
if __name__ == "__main__":
    main()