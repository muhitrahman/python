

# error handling

try:
    age = int(input("age: "))
    income = 20000
    risk = income / age
    print(risk)

except ZeroDivisionError:
    print("zero can not be divide")
except ValueError:
    print("invalid value")












