#belajar perulangan :)

urutan = 13
for i in range(urutan):
    print(f"perualangan ke-{i}")

print("="*30)

bahan = ['gula','air','kopi','teh']
for i in bahan:
    print(i)

print("="*30)

jawab = "oke"
hitung = 0

while(True):
    hitung += 1
    jawab = input("lanjut lagi tidak?")
    if jawab == "tidak":
        break

print(f"jumlah perulangan",{hitung}) 
    
    
 
    
