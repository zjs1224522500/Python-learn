
# awk '{if(length($0)>length(a)) a = $0} END{print a}'
if __name__ == '__main__':
    path = r"C:\Users\Administrator\Desktop\mem_test.txt"
    with open(path) as f:
        print(max(f, key=len))
