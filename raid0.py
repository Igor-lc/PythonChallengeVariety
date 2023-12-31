import sys
num_files, num_chars = int(sys.argv[1]), int(sys.argv[2])
data = {}

for y in range(num_files):
    with open("data-" + str(y + 1) + ".txt", 'r', encoding='utf8') as f:
        text = f.read()

        for i in range(len(text)):
            index = i * num_files + y
            data[index] = text[i]


data = sorted(data.items())
text = ''.join(l for i, l in data)
print(text[:num_chars])


num_files = int(sys.argv[1])
num_chars = int(sys.argv[2])

files_data = []
for f in range(1, num_files + 1):
    files_data.append(open(f"data-{f}.txt", "r", encoding='utf8').read())

char = 0
data = ""
i = 0
while char < num_chars:
    for file in files_data:
        if char == num_chars:
            break
        data += file[i]
        char += 1
    i += 1

print(data)
