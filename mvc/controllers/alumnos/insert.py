import web
render = web.template.render('mvc/views/alumnos/')
class Insert():

    def GET(self):
        return render.insert()

    def POST(self):
        try:
            form=web.input()
            print(form)
            
        except Exception as error:
            return "Error" +str(error)
            
            