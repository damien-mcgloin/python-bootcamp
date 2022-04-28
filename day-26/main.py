with open("file1.txt", "r") as f:
    list1 = f.read().splitlines()

with open("file2.txt", "r") as f:
    list2 = f.read().splitlines()

result = [int(x) for x in list1 if x in list2]
result = list(dict.fromkeys(result))

print(sorted(result))
