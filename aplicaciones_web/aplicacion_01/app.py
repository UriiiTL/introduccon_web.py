import web

urls = (
    '/', 'Index'
)
app = web.application(urls, globals())

class Index:
    def GET(self):
        return "hola mundo desde web.py y pyhton"

if __name__ == "__main__":
    app.run()