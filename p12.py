# wapp to read the marks of the students
# and print the sum and avg marks

marks = []

res = input(" do u want to enter sum marks y/n")
while res =="y":
	m= int(input(" enter marks "))
	marks.append(m)
	res = input("do u want to enter more y/n ")

sum = 0
for i in marks:
	sum = sum + i
avg = sum / len(marks)

print("sum = ", sum)
print("avg = ", avg)