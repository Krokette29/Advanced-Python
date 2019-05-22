def deco(func):
	print('This is a log.')
	return func

@deco
def f1():
	print("Running f1.")

@deco
def f2():
	print("Running f2.")

def main():
	f1()
	f2()


if __name__ == '__main__':
	main()