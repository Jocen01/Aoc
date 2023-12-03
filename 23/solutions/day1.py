f = open(r"C:\Users\Jonathan\code@lth\AOC\23\input\1\input")
nums = ["one","two","three","four","five","six","seven","eight","nine"]
elfs = f.read().split("\n")
tot = 0
for elf in elfs:
    a =""
    for i in range(len(elf)):
        f = True
        
        for n in nums:
            if elf[i].isdigit():
                a = elf[i]
                f= False
                break
            if elf[i:].startswith(n):
                a = str(nums.index(n)+1)
                f= False
                break
        if not f: break
    for i in range(len(elf)):
    
        f=True
        for n in nums:
            if elf[-i-1].isdigit():
                tot += int(a+elf[-i-1])
                f=False
                break
            if elf[:-i].endswith(n) or elf.endswith(n):
                tot += int(a+str(nums.index(n)+1))
                f=False
                break
        if not f: break
print(tot)
