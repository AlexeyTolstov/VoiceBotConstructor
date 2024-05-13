def generate_commands(l1: list, l2: list) -> list:
    res = []
    for i in l1:
        for j in l2:
            res.append(i + " " + j)
    return res

if __name__ == "__main__":
    data = generate_commands(l1=["1", "2", "3"], l2=["4", "5", "6"])
    print(data)