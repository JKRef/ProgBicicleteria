class Bicicleteria():
    def __init__(self, bicicletas=[] , ganancias=0, cantidad_de_ventas=0):
        self.bicicletas = bicicletas
        self.ganancias = ganancias                   
        self.cantidad_de_ventas = cantidad_de_ventas
    
    def vender_bicicleta(self, ganancias,cantidad_de_ventas): 
            if ganancias < 0 or cantidad_de_ventas < 0:
                return f"ingrese valores positivos"
            else:
                self.ganancias += ganancias
                self.cantidad_de_ventas += cantidad_de_ventas            
                print(f"Ganancia {self.ganancias} y Cantidad {self.cantidad_de_ventas}")
                return self.ganancias and self.bicicletas
                         
    def comprar_bicicleta(self, bicicletas):
        self.bicicletas.append(bicicletas) 
        print(f"Bicicletas {self.bicicletas}") 

    def get_tipo(self):
        print("Seleccione el tipo de bicleta para comenzar...")
        for index, bici in enumerate(self.bicicletas):
            print("Tipo #{} = {}".format(index+1, bici))
        tipo = input()
        return tipo

    class Bicicleta():
        def __init__(self, nro_de_serie="" , modelo="", anio=int , precio=int):
            self.__nro_de_serie = nro_de_serie
            self.__modelo = modelo 
            self.__anio= anio
            self.__precio= precio    

        def set_precio(self, precio):
            self.precio = precio
            return f"Se cambio el precio por: {self.__precio} "
        def get_precio(self):
            print("El precio en pesos es: ", self.__precio)
            return self.__precio
        def get_nro_de_serie(self):
            return f' El numero de serie es {self.__nro_de_serie}'

   
class main():
    
    bicicleteria=Bicicleteria(["Cross","Carrera","Montain","Desenso"],10000,150)
    bicicleta_Cross=Bicicleteria.Bicicleta("CROSS0090", "S", 2022,3000)
    bicicleta_Carrera=Bicicleteria.Bicicleta("CARRERA002", "L", 2022,3000)
    bicicleta_Montain=Bicicleteria.Bicicleta("MONTAIN003", "M", 2022,3000)
    bicicleta_Desenso=Bicicleteria.Bicicleta("DES001", "XL", 2022,3000)

    print("======= Cleta Market =======")
    tipo = bicicleteria.get_tipo()

    print("Menu \n1.Ventas\n2.Compras\n3.Consultas\n4.Editar")
    opc = input()
    if opc == "1":
        cantidad =int(input("Ingrese la cantidad de bicicletas a vender: "))
        if tipo == "1":
            precio = bicicleta_Cross.get_precio()*cantidad
            bicicleteria.vender_bicicleta(precio,cantidad)
        elif tipo == "2":
            precio = bicicleta_Carrera.get_precio()*cantidad
            bicicleteria.vender_bicicleta(precio,cantidad) 
        elif tipo == "3":
            precio = bicicleta_Montain.get_precio()*cantidad
            bicicleteria.vender_bicicleta(precio,cantidad)
        elif tipo == "4":
            precio = bicicleta_Desenso.get_precio()*cantidad
            bicicleteria.vender_bicicleta(precio, cantidad)
        else:
            print("El tipo seleccionado no existe") 
    elif opc == "2": 
        bicicleteria.comprar_bicicleta("montain")
    elif opc == "3":
        print("***Consultas*** \n1.Precio\n2.Numero de Serie")
        opc2 = input()
        if opc2 == "1":
            if tipo == "1":
                bicicleta_Cross.get_precio()
            elif tipo == "2":
                bicicleta_Carrera.get_precio()
            elif tipo == "3":
                bicicleta_Montain.get_precio()
            elif tipo == "4":
                bicicleta_Desenso.get_precio()
            else:
                print("El tipo seleccionado no existe") 
        elif opc2 == "2":
            if tipo == "1":
                print(bicicleta_Cross.get_nro_de_serie())
            elif tipo == "2":
                print(bicicleta_Carrera.get_nro_de_serie())
            elif tipo == "3":
                print(bicicleta_Montain.get_nro_de_serie())
            elif tipo == "4":
                print(bicicleta_Desenso.get_nro_de_serie())
            else:
                print("El tipo Seleccionado no existe") 
    elif opc == "4":
        if tipo == "1":
            bicicleta_Cross.set_precio(3500)
        elif tipo == "2":
            bicicleta_Carrera.set_precio(2900)
        elif tipo == "3":
            bicicleta_Montain.set_precio(4000)
        elif tipo == "4":
            bicicleta_Desenso.set_precio(5000)
        else:
            print("El tipo Seleccionado no existe")   