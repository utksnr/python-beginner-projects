def count(x):
    count = {}
    for i in x:
        if i in count:
            count[i] += 1
        else: count[i] = 1
    print(count)

word = input("Your text to count: ")
print(count(word))
    