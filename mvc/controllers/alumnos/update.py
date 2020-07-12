import web
render = web.template.render('mvc/views/alumnos/')
class Update():

    def GET(self):
        return render.update()

    def POST(self):
        try:
            form=web.input()
            print(form)     
        except Exception as error:
            return "Error" +str(error)