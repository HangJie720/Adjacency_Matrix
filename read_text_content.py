import numpy as np

def main():
    data = []
    ID = []
    length = 10310 # the length of txt content
    f = open("new_adjedges.txt")
    for file in f.readlines():
        row = [int(line) for line in file.strip().split(" ")]
        while(len(row) < length):
            row.append(0)
        data.append(row)

    data_array = np.array(data)

    for i in range(length):
        ID.append(data_array[i][0])

    adj_mat = np.zeros((length,length), dtype=np.int)

    for i in range(length):
        for j in range(1,length):
            k = ID[i]
            n = data_array[i][j]
            if n != 0:
                adj_mat[k][n]=1

    np.save("new_adjedges.npy", adj_mat)


if __name__ == "__main__":
    main()