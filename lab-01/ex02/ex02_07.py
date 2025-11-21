print("Nhap dong van ban")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
       break
    lines.append(line)
    print("\nCac dong da nhap sau khi duoc in hoa:")
    for line in lines:
       print(line.upper()) 