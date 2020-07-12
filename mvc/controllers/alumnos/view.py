import web
render = web.template.render('mvc/views/alumnos/')
class View():

    def GET(self):
        return render.view()

    def POST(self):
        try:
            form=web.input()
            print(form)     
        except Exception as error:
            return "Error" +str(error)