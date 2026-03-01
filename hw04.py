email = input("შეიყვანეთ ელფოსტის მისამართი: ")

if "@" in email:
    result = "ელფოსტა შეიცავს @ სიმბოლოს"
else:
    result = "ელფოსტა არ შეიცავს @ სიმბოლოს"

print(result.upper())


