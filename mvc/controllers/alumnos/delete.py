import web
render = web.template.render('mvc/views/alumnos/')
class Delete():

    def GET(self):
        return render.delete()

    def POST(self):
        try:
            form=web.input()
            print(form)     
        except Exception as error:
            return "Error" +str(error)