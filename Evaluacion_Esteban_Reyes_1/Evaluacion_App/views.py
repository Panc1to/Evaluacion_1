from django.shortcuts import render

# Create your views here.

def index(request):
    
    return render(request, 'templatesAPP/index.html')

def electronica(request):
    data ={"titulo":"Electronica",
           "foto1": "electronica1.jpg",
           "foto2": "electronica2.jpg",
           "foto3": "electronica3.jpg",
           "producto1": "PC gamer",
           "producto2": "Teclado gamer rgb ",
           "producto3": "Mouse logitech"}
    return render(request, 'templatesAPP/producto.html', data)

def juguete(request):
    data ={"titulo":"Juguetes",
           "foto1": "juguete1.jpg",
           "foto2": "juguete2.jpg",
           "foto3": "juguete3.jpg",
           "producto1": "",
           "producto2": "",
           "producto3": ""}
    return render(request, 'templatesAPP/producto.html', data)

def ropa(request):
    data ={"titulo":"Ropa",
           "foto1": "ropa1.jpg",
           "foto2": "ropa2.jpg",
           "foto3": "ropa3.jpg",
           "producto1": "",
           "producto2": "",
           "producto3": ""}
    return render(request, 'templatesAPP/producto.html', data)

def usuario(request):
    data ={"titulo":"Usuario",
           "foto1": "usuario1.jpg",
           }
    return render(request, 'templatesAPP/usuario.html', data)

def detalle(request, producto, pagina):  

    data ={"title":pagina}

    if pagina == "Electronica":
        if producto == "producto1":
            data["detalle"] = "Precio: 530.000" 
            data["producto"] = "PC Gamer"
            data["foto"] = "electronica1.jpg"
        elif producto == "producto2":
            data["detalle"] = "Precio: 20.000" 
            data["producto"] = "Teclado Gamer"
            data["foto"] = "electronica2.jpg"
        elif producto == "producto3":
            data["detalle"] = "Precio: 35.000" 
            data["producto"] = "Mouse Logitech"
            data["foto"] = "electronica3.jpg"

    if pagina == "Ropa":
        if producto == "producto1":
            data["detalle"] = "Precio: 55.000" 
            data["producto"] = "Poleron"
            data["foto"] = "ropa1.jpg"
        elif producto == "producto2":
            data["detalle"] = "Precio: 33.000" 
            data["producto"] = "Pantalon"
            data["foto"] = "ropa2.jpg"
        elif producto == "producto3":
            data["detalle"] = "Precio: 15.000" 
            data["producto"] = "Polera Fox"
            data["foto"] = "ropa3.jpg"


    if pagina == "Juguetes":
        if producto == "producto1":
            data["detalle"] = "Precio: 45.000"
            data["producto"] = "Lego Star Wars"
            data["foto"] = "juguete1.jpg"
        elif producto == "producto2":
            data["detalle"] = "Precio: 32.000" 
            data["producto"] = "Barbie"
            data["foto"] = "juguete2.jpg"
        elif producto == "producto3":
            data["detalle"] = "Precio: 130.000"  
            data["producto"] = "Terreneitor"
            data["foto"] = "juguete3.jpg"

    return render(request, 'templatesAPP/detalle.html', data)



