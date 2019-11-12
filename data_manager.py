import random

def get_data_from_file(filename="students_data.csv"):
    data = []
    with open(filename) as r:
        line = r.readline()
        data.append(line)
        while line:
            line = r.readline()
            if len(line) != 0:
                data.append(line)
    noslashn = []
    for i in range(len(data)):
        line = ""
        for j in range(len(data[i])-1):
            line += data[i][j]
        noslashn.append(line.split(","))
    return noslashn
        
def write_data_to_file(filename="students_data.csv"):
    type_of_data = ["Name","Age","Active"]
    lego=get_data_from_file()
    table = []
    for i in range(len(lego)):
        table.append(lego[i][0])
    list_of_data = []
    generated = ''

    up = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
          "W", "X", "Y", "Z"]
    lo = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "w", "x", "y", "z"]
    nu = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sp = ["+", "!", "%", "/", "=", "(", ")", "|", "<", ">", "#", "&", "@", "{", "}", "*"]
    w = [1, 2, 3, 4, 5, 6, 7, 8]
    generated = ''
    while len(generated) != 8:
        generated = ''
        while len(w) != 0:
            random.shuffle(w)
            n = w[0]
            
            if n == 1 or n == 2:
                l = up[random.randint(0, len(up)-1)]
                generated += l

            if n == 3 or n == 4:
                l=lo[random.randint(0, len(lo)-1)]
                generated += l

            if n == 5 or n == 6:
                l=str(nu[random.randint(0, len(nu)-1)])
                generated += l

            if n == 7 or n == 8:
                l=sp[random.randint(0, len(sp)-1)]
                generated += l
                
            w.remove(w[0])
        if generated not in table:
            break
        else:
            continue
    list_of_data.append(generated)
    for i in range(len(type_of_data)):
        list_of_data.append(input((type_of_data[i]+":")))
    print(",".join(list_of_data))
    
    
    
    text=open(filename,"a")
    text.write(",".join(list_of_data))
    text.write("\n")
    text.close()


def write_table_to_file(file_name, table, mode='a'):

    with open(file_name, mode) as f:
        for student in table:
            row = ','.join(record)
            f.write(row + '\n')
