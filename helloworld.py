import webapp2
from valid_month_eg import valid_month
from  valid_year import valid_year
from valid_day import valid_day





form="""
<form method="post">
    What is your birthday?
    <br>
    <label> Month
        <input type ="text" name="month">
    </label>
    
    <label> Day
        <input type ="text" name="day">
    </label>
    
    <label> Year
        <input type ="text" name="year">
    </label>
    <br>
    <br>
    <input type ="submit">   
</form>
"""
class MainPage(webapp2.RequestHandler):
    def get(self):
        print 'get'
        self.response.out.write(form)

    def post(self):
        print 'post'
        self.response.out.write("lash and banter")

        user_month = valid_month(self.request.get('month'))
        user_day = valid_day(self.request.get('day'))
        user_year = valid_year(self.request.get('year'))

        if not(user_month and user_day and user_year):
            self.response.out.write(form)
        else:
            self.response.out.write('gak')

        # q = self.request.get("q")
        # self.response.out.write(q)

        # self.response.headers['Content-Type']= 'text/plain'
        # self.response.out.write(self.request)

application = webapp2.WSGIApplication([('/', MainPage)]   
, debug=True)