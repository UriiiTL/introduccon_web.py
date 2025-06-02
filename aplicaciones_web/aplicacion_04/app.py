import web

urls = (
    '/', 'Index',
    '/bienvenido', 'Bienvenido',
)
render = web.template.render('templates')
app = web.application(urls, globals())

class Index:
    def __init__(self):
        self.mensaje= "este es un mensaje de Index"
    
    def GET(self):
        return render.index(self.mensaje)

class Bienvenido:
    def __init__(self):
        pass

    def GET(self):
        mensaje= "este es un mensaje de bienvenida"
        return render.bienvenido(mensaje)

if __name__ == "__main__":
    app.run()

