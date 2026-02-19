def c_to_f(c):
    return c * 9 / 5 + 32


def f_to_c(f):
    return (f - 32) * 5 / 9


def main():
    print("Temperature Converter")
    mode = input("Convert (1) C->F or (2) F->C? ").strip()
    try:
        val = float(input("Enter temperature: ").strip())
    except ValueError:
        print("Invalid number")
        return

    if mode == "1":
        print(f"{val} °C = {c_to_f(val):.2f} °F")
    elif mode == "2":
        print(f"{val} °F = {f_to_c(val):.2f} °C")
    else:
        print("Unknown option")


if __name__ == "__main__":
    main()
