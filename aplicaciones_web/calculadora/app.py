import web

urls = (
    '/', 'Calculadora',
)
render = web.template.render('templates')
app = web.application(urls, globals())

class Calculadora:
    def GET(self):
        return render.calculadora()

    def POST(self):
        formulario = web.input()
        operacion = formulario.btn_operacion
        self.num1 = (float(formulario.inp_numero1))
        self.num2 = (float(formulario.inp_numero2))

        if operacion=="suma":
            resultado= self.num1 + self.num2
        
        elif operacion=="resta":
            resultado= self.num1 - self.num2

        elif operacion=="multiplicacion":
            resultado= self.num1 * self.num2

        elif operacion=="division":
            resultado:float= self.num1 / self.num2

        return render.calculadora(resultado)
        

if __name__ == "__main__":
    app.run()