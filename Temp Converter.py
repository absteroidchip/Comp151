def print_hi(temp):
    fahr_temp = input("what the current temperature in fahrenheit?:")
    print(f"Ooh, a balmy {fahr_temp}")
    celsius_temp = (float(fahr_temp)-32)*(5/9)
    print(f"{fahr_temp} degrees fahrenheit is {celsius_temp} degrees in celsius")


if __name__ == '__main__':
    print_hi('PyCharm')