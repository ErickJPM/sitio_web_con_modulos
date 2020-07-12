import web
render = web.template.render('mvc/views/alumnos/')
class List():
    
    def GET(self):
        return render.list()