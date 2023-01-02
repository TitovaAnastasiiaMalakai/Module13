price = 0
tickets = int(input("Укажите желаемое количество билетов: "))
for i in range(tickets):
    age = int(input('Укажите возраст посетителя №' + str(i + 1) + ': '))
    if 0 <= age <= 17:
        price += 0
    elif 18 <= age <= 24:
        price += 990
    elif age >= 25:
        price += 1390
print("Цена: ", price)
if tickets > 3:
    price_skidka = price - (price / 10)
    print("Итоговая цена с учётом скидки 10%: ", price_skidka)