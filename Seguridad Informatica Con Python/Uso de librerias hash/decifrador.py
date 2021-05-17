import hashlib

def main():
    resolutionhash = input("input hash : ")
    resolution = open("paswoords.txt",'r')
    
    for x in resolution.readlines():
        a = x.strip("\n")
        a = hashlib.sha1(a.encode('utf-8')).hexdigest()
        if a == resolutionhash:
                print(f"contraseña se desifro correctamente  : {x}\n La contraseña cifrada fue la siguiente : {a}")

if __name__ ==  "__main__":
    main()
