import sys


def main():
    strinput = sys.argv[1]
    decrypted = ""
    for i in range(len(strinput)):
        c = chr(ord(strinput[i]) - i)
        decrypted += c
    print(decrypted)
if __name__=="__main__":
    main()