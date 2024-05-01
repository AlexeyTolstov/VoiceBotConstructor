def generate_commands(mat: list) -> list:
    res = []
    for i in mat[0]:
        for j in mat[1]:
            res.append(i + " " + j)
    return res

if __name__ == "__main__":
    data = generate_commands()
    print(data)