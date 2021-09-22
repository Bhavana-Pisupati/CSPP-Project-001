print("You're in " + str(15-110))

def largest(a, b, c):
	if a > b:
		if a > c:
			print (a,"is greater")
	elif b > c:
		print (b, "is greater")
	else:
		print (c, "is greater")
largest(3,2,1)
# output: 3 is greater

def evenSum(num):
	i = 1
	s = 0
	while i <= num:
		if i % 2 == 0:
			s += i
		i += 1
	return s
print(evenSum(10))
# output: 30

def isPrime(num):
	for i in range(2,num):
		if num % i == 0:
		    return False
	return True
print(isPrime(5))
# output: True

def seperate(s):
	l = len(s)
	temp = s[0:l:2]+s[1:l:2]
	return temp

print(seperate("a-c-e-g-i-")) 
# output: acegi-----

s="Donald Knuth"
l= len(s)
print(s[7:l:1],s[0:6:1])

def contains(s1, s2):
	for i in range(len(s1)):
		if s1[i:i+len(s2)] == s2:
			return True
	return False

print(contains("Hello world", "world"))

# output: True

def getFirstName(fullname):
	for i in range(len(fullname)):
		if fullname[i]==" ":
			return fullname[0:i]
print(getFirstName("Bhavana Pisupati"))

def getFirstName(fullname):
	s=fullname.split()
	return s[0]
print(getFirstName("Bhavana Pisupati BP"))

def count(s1, s2):
	s1=s1.lower()
	s2=s2.lower()
	if(s2 in s1):
		return s1.count(s2)
	return 0

print(count("MissiSSippi", "Ss"))

# output: 2
