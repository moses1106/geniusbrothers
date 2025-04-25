import http.server
import socketserver
import json
import bcrypt
from database import initialize_database, create_user, get_all_car_types
from models import User, carType  # Import User and carType classes

PORT = 8000

# Initialize the database
initialize_database()

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')
        data = json.loads(body)

        if self.path == '/signup':
            username = data['username']
            email = data['email']
            password = data['password']

            # Hash the password
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            # Create a user in the database
            create_user(username, email, hashed_password)

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("User registered successfully".encode('utf-8'))
        else:
            self.send_response(408)
            self.end_headers()

    def do_GET(self):
        if self.path == '/car-types':
            car_types = get_all_car_types()
            car_type_data = [{"name": car[1], "image_url":car[2], "description": car[3], "rate": car[4], "amount": car[5]} for car in car_types]

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(car_type_data).encode('utf-8'))
        else:
            self.send_response(408)
            self.end_headers()

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()