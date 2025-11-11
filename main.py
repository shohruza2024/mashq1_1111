#1-misol
data = {'ism': 'Nozila', 'yosh': 20, 'kurs': 3}
keys = list(data.keys())
print("Kalitlar ro‘yxati:", keys)

#2-misol
raqamlar = {'a': 10, 'b': 20, 'c': 30}
yigindi = sum(raqamlar.values())
print("Qiymatlar yig‘indisi:", yigindi)

#3-misol
data = {'ism': 'Nozila', 'kurs': 3, 'yosh': 20}
kalit = 'kurs'
if kalit in data:
    print(f"'{kalit}' kaliti mavjud.")
else:
    print(f"'{kalit}' kaliti mavjud emas.")

#4-misol
raqamlar = {'a': 40, 'b': 10, 'c': 30}
saralangan = dict(sorted(raqamlar.items(), key=lambda x: x[1]))
print("Saralangan lug‘at:", saralangan)

#5-misol
matn = "nozila"
harflar = {}
for harf in matn:
    harflar[harf] = harflar.get(harf, 0) + 1
print("Harf takrorlanishi:", harflar)
