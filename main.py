import web, timerapp
'''the import web can be resolved using easy_install web.py'''

urls = ('/time_now', 'time_now_http', '/time_delta', 'time_delta_http', '/set_initial_time', 'set_initial_time_http')

app = web.application(urls, globals())

timer = timerapp.TimeApp()

class time_now_http:
    def GET(self):
        print "time_now GET >> running"
        return timer.get_time_now()

class time_delta_http:
    def GET(self):
        print "time_delta GET >> running"
        return timer.get_time_delta()

class set_initial_time_http:
    def GET(self):
        print 'setting initial time to now.'
        timer.set_initial_time()
        return 'OK'

def main():
    print "main starting"

if __name__ == "__main__":
    main()
    app.run()
