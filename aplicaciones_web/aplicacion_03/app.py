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

