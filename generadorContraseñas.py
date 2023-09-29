import  string
import  random
caracteres =list(string.ascii_letters +string.digits + "!#&%$()/\+")

def dameclave():
    longitud =int(input("que longitud le damos a la clave? "))
    random.shuffle(caracteres)
    clave=[]
    for i in range(longitud):
        clave.append(random.choice(caracteres))
    random.shuffle(clave)
    return  ("".join(clave))


if __name__=="__main__":
    clave =dameclave()
    print(f"la clave seleccionada es : {clave}")
