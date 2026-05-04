import csv

def main():
    while True:
        product = input("Product name (Type 'break' to quit): ").lower()
        if product == "break":
            break
        else:
            pass
        while True:
            try:
                if product.endswith("s"):
                    f = int(input(f"How many seconds do {product} take to make in one cycle? "))
                else:
                    f = int(input(f"How many seconds does {product} take to make in one cycle? "))
            except ValueError:
                pass
            else:
                break
        time = f
        machines = int(input("How many machines are running? "))
        total = calculate(time, machines)
        with open("data.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["product", "cycle time", "parts per hour"])
            writer.writerow({"product": product, "cycle time": time, "parts per hour": total})

        print(f"Parts per hour: {total} {product} per hour.")

def calculate(t, m):
    singular_pph = (60 / t) * 60
    singular_pph = round(singular_pph)
    total = singular_pph * m
    return total

if __name__ == "__main__":
    main()