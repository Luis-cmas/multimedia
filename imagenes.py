from PIL import Image, ImageFilter,ImageDraw,ImageFont
import cv2

print('\nBienvenido al editor de imagenes\n')
#ruta = input('Ingrese la ruta de la imagen a editar\n')
imagen = Image.open("//uno.jpg")
#formato =ruta[-4:]
#print(formato)
copia = imagen
imagen.show()

op = "0"
while op != "6":
    print('\n1)Rotar imagen\n2)Redimensionar imagen\n3)Recortar imagen\n4)Agregar texto a una imagen\n5)Guardar imagen\n6)Salir\n')

    op = input('¿que desea realizar?')
    if op == '1':
        grados = input('cuantos grados la quiere rotar?')
        aux = copia.rotate(int(grados))
        aux.show()
        deshacer = input("desea mantener los cambios (s/n)?")
        if str(deshacer) == "n":
            aux = copia
        elif str(deshacer) == "s":
            copia = aux
        
    elif op == '2':
        ancho = input("\nAncho de la imagen:\n")
        alto = input("\nAlto de la imagen\n")
        aux = copia.resize((int(ancho), int(alto)))
        aux.show()
        deshacer = input("desea mantener los cambios (s/n)?")
        if str(deshacer) == "n":
            aux = copia
        elif str(deshacer) == "s":
            copia = aux

        
    elif op == '3':
        xi = input("\ncordenadas x de inicio\n")
        yi = input("\ncordenadas y de inicio\n")
        xf = input("\ncordenadas x de fin\n")
        yf = input("\ncordenadas y de fin\n")
        aux = copia.crop((int(xi), int(yi), int(xf), int(yf)))
        aux.show()
        deshacer = input("desea mantener los cambios (s/n)?")
        if str(deshacer) == "n":
            aux = copia
        elif str(deshacer) == "s":
            copia = aux

    elif op == '4':
        texto = input("\nTexto que desea agregar:\n")
        x = input("\ncoordenada x:\n")
        y = input("\ncoordenada y:\n")
        tam = input("\ntamaño de fuente:\n")
        aux =copia
        dibujo = ImageDraw.Draw(aux)
        fuente = ImageFont.truetype("arial.ttf", int(tam))
        dibujo.text((int(x), int(y)), texto, fill="gray", font=fuente)
        aux.show()
        deshacer = input("desea mantener los cambios (s/n)?")
        if str(deshacer) == "n":
            aux = copia
        elif str(deshacer) == "s":
            copia = aux
    elif op == '5':
        nombre = input("\nNombre a guardar:\n")
        copia.save(nombre + formato)
