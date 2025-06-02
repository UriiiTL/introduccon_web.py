# 1. Hola mundo 

ejemplo basico de web.py

```
import web

urls = (
    '/', 'Index'
)
render = web.template.render('templates')
app = web.application(urls, globals())

class Index:
    def __init__(self):
        self.mensaje= "este es un mensaje"
    
    def GET(self):
        return render.index(self.mensaje)

if __name__ == "__main__":
    app.run()

```
# 1.1 Importar libreria

```

import web

```
esta linea nos permite 

## 1.2 cada linea permite manejar la ruta y la clase que contorla cada una de las paginas web de la aplicacion

 indica la ruta de acceso a la pagina web
  Index Indica el nombre de la clase