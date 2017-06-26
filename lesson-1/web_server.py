from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

def getRestaurants():
    return session.query(Restaurant).all()

def addRestaurant(restaurant_name):
    restaurant = Restaurant(name=restaurant_name)
    session.add(restaurant)
    session.commit()

def editRestaurantName(restaurant_name, new_name):
    restaurant = session.query(Restaurant).filter_by(name=restaurant_name).one()
    restaurant.name = new_name
    session.add(restaurant)
    session.commit()

def deleteRestaurant(restaurant_name):
    restaurant = session.query(Restaurant).filter_by(name=restaurant_name).one()
    seesion.delete(restaurant)
    seesion.commit


class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.endswith('/hello'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "<html><body>"
            message += "<h1>Hello!</h1>"
            message += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            message += "</body></html>"
            self.wfile.write(message)
            print message
            return
        if self.path.endswith("/hola"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "<html><body>"
            message += "<h1>Hola!</h1>"
            message += '''<form method='POST' enctype='multipart/form-data' action='/hola'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            message += "</body></html>"
            self.wfile.write(message)
            print message
            return
        if self.path.endswith("/restaurants"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "<html><body>"
            message += '''<a href="/new">Add new restaurant</a><br>'''
            for restaurant in getRestaurants():
                message += "<h1> %s </h1>" % restaurant.name
                message += '''<a href="/edit_restaurant_name">Edit</a> '''
                message += '''<a href="/delete_restaurant">Delete</a>'''
            message += "</body></html>"
            self.wfile.write(message)
            return
        if self.path.endswith("/new"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "<html><body>"
            message += '''<form method='POST' enctype='multipart/form-data' action='/new'><h1>Add new restaurant?</h1><input name="message" type="text" ><input type="submit" value="Add"> </form>'''
            message += "</body></html>"
            self.wfile.write(message)
            return
        if self.path.endswith("/edit_restaurant_name"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "<html><body>"
            message += '''<form method='POST' enctype='multipart/form-data' action='/edit_restaurant_name'><input name="message" type="text"><input type="submit" value="Edit name"></form>'''
            message += "</body></html>"
            self.wfile.write(message)
            return
        if self.path.endswith("/delete_restaurant"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "<html><body>"
            message += '''<h1>Are you sure you want to delete?</h1>'''
            message += '''<input type="submit" value="Delete">'''
            message += "</body></html>"
            self.wfile.write(message)
            return
        else:
            self.send_error(404, 'File Not Found %s' % self.path)

    def do_POST(self):
        try:
            if self.path.endswith("/new"):
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('message')
                addRestaurant(messagecontent[0])
                message = ""
                message += "<html><body>"
                message += "<h1> %s added!</h1>" % messagecontent[0]
                message += '''<form method='POST' enctype='multipart/form-data' action='/new'><h1>Add new restaurant?</h1><input name="message" type="text" ><input type="submit" value="Add"> </form>'''
                message += "</body></html>"
                self.wfile.write(message)
                self.wfile.write(output)
                print output
            if self.path.endswith("/edit_restaurant_name"):
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('message')
                addRestaurant(messagecontent[0])
                message = ""
                message += "<html><body>"
                message += '''<form method='POST' enctype='multipart/form-data' action='/edit_restaurant_name'><input name="message" type="text"><input type="submit" value="Edit name"></form>'''
                message += "</body></html>"
                self.wfile.write(message)
                self.wfile.write(output)
                print output
            if self.path.endswith("/delete_restaurant"):
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('message')
                addRestaurant(messagecontent[0])
                message = ""
                message += "<html><body>"
                message += '''<h1>Added!</h1>'''
                message += '''<form method='POST' enctype='multipart/form-data' action='/new'><h1>Add new restaurant?</h1><input name="message" type="text" ><input type="submit" value="Add"> </form>'''
                message += "</body></html>"
                self.wfile.write(message)
                self.wfile.write(output)
                print output


        except:
            pass

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print "Web Server Running on port %s " % port
        server.serve_forever()
    except KeyBoardInterrupt:
        print "^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()
