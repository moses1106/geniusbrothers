import sqlite3

# Initialize the database
def initialize_database():
    connection = sqlite3.connect('db.sqlite')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL            
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS car_types (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            image_url TEXT NOT NULL,
            description TEXT NOT NULL,
            rate REAL NOT NULL,
            amount REAL NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            car_type_id INTEGER,
            quantity INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (car_type_id) REFERENCES car_types(id)
        )
    ''')

    # Insert handcorded car types
    car_types_data = [
       ("Mercedez benz", "https://unsplash.com/photos/black-mercedes-benz-coupe-on-gray-asphalt-road-8qYE6LGHW-c", "Description    .", 4.5, 250),
        ("Toyota", "https://unsplash.com/photos/a-white-sports-car-parked-in-front-of-a-building-zMGrPdjRoOU", "Description     .", 4.2, 300),
        ("Mazda", "https://pixabay.com/photos/car-vehicle-mazda-auto-automobile-6122175/", "Description      .", 4.8, 200),
        ("Nissan", "https://unsplash.com/photos/a-white-sports-car-parked-on-a-wet-road-ZNPVwTqhhHo", "Description       .", 4.7, 350),
        ("Porsche", "https://pixabay.com/photos/automobile-cayman-coupe-design-5330353/", "Description        .", 4.3, 275),
        ("Lamborghini", "https://unsplash.com/photos/an-orange-sports-car-parked-in-front-of-a-building-i0GAaus50es","Description    .", 4.6, 225),
        ("Lexus", "https://unsplash.com/photos/white-mercedes-benz-c-class-NR7urrOwkLE", "Description        .", 4.1, 320),
        ("Tesla", "https://unsplash.com/photos/a-futuristic-car-is-parked-on-the-side-of-the-road-VceGFFBjSrY", "Description      .", 4.0, 275),
        ("Ferarri", "https://pixabay.com/photos/automobile-ferrari-sports-car-3309967/", "Description       .", 4.4, 240),
        ("BMW", "https://unsplash.com/photos/a-black-car-parked-in-a-parking-lot-QSNRdQjqXpI", "Description     ", 4.9, 280)
        ("Audi", "https://unsplash.com/photos/gray-and-red-coupe-bKqNW5Dq6p8", "Description     ", 4.1, 290)
    ]


    cursor.executemany("INSERT INTO car_types (name, image_url, description, rate, amount) VALUES (?, ?, ?, ?, ?)", car_types_data)

    connection.commit()
    connection.close()

# Function to create a user
def create_user(username, email, password):
    connection = sqlite3.connect('db.sqlite')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    connection.commit()
    connection.close()

# Function to find a user by email
def find_user_by_email(email):
    connection = sqlite3.connect('db.sqlite')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    user = cursor.fetchone()
    connection.close()
    return user

# Function to retrieve all car types
def get_all_car_types():
    connection = sqlite3.connect('db.sqlite')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM car_types")
    car_types = cursor.fetchall()
    connection.close()
    return car_types

# Function to create an order
def create_order(user_id, car_type_id, quantity):
    connection = sqlite3.connect('db.sqlite')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO orders (user_id, car_type_id, quantity) VALUES (?, ?, ?)", (user_id, car_type_id, quantity))
    connection.commit()
    connection.close()

# Function to remove a car type
def remove_car_type(car_type_id):
    connection = sqlite3.connect('db.sqlite')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM car_types WHERE id=?", (car_type_id,))
    connection.commit()
    connection.close()

# Function to update a car type
def update_car_type(car_type_id, name, description, rate, amount, image_url):
    connection = sqlite3.connect('db.sqlite')
    cursor = connection.cursor()
    cursor.execute("UPDATE car_types SET name=?, description=?, rate=?, amount=?, image_url=? WHERE id=?",) (name, description, rate, amount, image_url, car_type_id)
    connection.commit()
    connection.close()