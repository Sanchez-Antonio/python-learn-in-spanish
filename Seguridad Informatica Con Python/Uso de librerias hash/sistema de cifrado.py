import hashlib

def main():
    contraseña = str(input("ingrese su contraseña para cifrar : "))
    print("")
    cifrado = hashlib.sha1(contraseña.encode('utf-8')).hexdigest()
    #-----------
    print(f"convertido a cifrado sha1-->  {cifrado}")
    cifrado = hashlib.md5(contraseña.encode('utf-8')).hexdigest()
    print("\n")
    print(f"convertido a cifrado md5-->  {cifrado}")
    cifrado = hashlib.sha224(contraseña.encode('utf-8')).hexdigest()
    print("\n")
    print(f"convertido a cifrado sha224-->  {cifrado}")
    cifrado = hashlib.sha256(contraseña.encode('utf-8')).hexdigest()
    print("\n")
    print(f"convertido a cifrado sha256-->  {cifrado}")
    cifrado = hashlib.sha384(contraseña.encode('utf-8')).hexdigest()
    print("\n")
    print(f"convertido a cifrado sha384-->  {cifrado}")
    cifrado = hashlib.sha512(contraseña.encode('utf-8')).hexdigest()
    print("\n")
    print(f"convertido a cifrado sha512-->  {cifrado}")
    cifrado = hashlib.blake2b(contraseña.encode('utf-8')).hexdigest()
    print("\n")
    print(f"convertido a cifrado blake2b-->  {cifrado}")
    cifrado = hashlib.blake2s(contraseña.encode('utf-8')).hexdigest()
    print("\n")
    print(f"convertido a cifrado blake2s-->  {cifrado}")

if __name__ ==  "__main__":
    main()




