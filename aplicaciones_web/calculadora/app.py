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
        num1 = (float(formulario.inp_numero1))
        num2 = (float(formulario.inp_numero2))

        if operacion=="suma":
            resultado= num1 + num2
        
        elif operacion=="resta":
            resultado= num1 - (num2)

        elif operacion=="multiplicacion":
            resultado= num1 * num2

        elif operacion=="division":
            if num2== 0:
                resultado:str="no_es_divisible_entre_0"
            else :
                resultado= num1/num2

        return render.calculadora(resultado,num1,num2)
        

if __name__ == "__main__":
    app.run()