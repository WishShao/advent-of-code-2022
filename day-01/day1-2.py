with open('input.txt', 'r') as infile:
    content = infile.read().strip()
    data = content.split('\n\n')

elfs = []
for elf in data:
    elf = map(int, elf.split())
    elfs.append(sum(elf))

elfs.sort(reverse = True)
print(sum(elfs[:3]))   

