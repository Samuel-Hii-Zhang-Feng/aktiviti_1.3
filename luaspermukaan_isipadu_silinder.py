pi = 3.142
jejari = float(input("Masukkan jejari:"))
tinggi = float(input("Masukkan tinggi:"))

luaspermukaan = 2 * pi * (jejari) ** 2 + 2 * pi * jejari * tinggi 
isipadu = pi * (jejari) ** 2 * tinggi

print("Luas permukaan tangki air ialah",round(luaspermukaan,2))
print("Isi padu tangki air ialah",round(isipadu,2))
