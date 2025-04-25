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
        ("Mercedez benz", "https://unsplash.com/photos/black-mercedes-benz-coupe-on-gray-asphalt-road-8qYE6LGHW-c", "This black Mercedes sedan exemplifies understated luxury with bold road presence. Likely from the C-Class or E-Class range, it features powerful inline engines, a smooth automatic gearbox, and top-tier safety and comfort tech—ideal for business-class driving..", 4.5, 250),
        ("Toyota", "https://unsplash.com/photos/a-white-sports-car-parked-in-front-of-a-building-zMGrPdjRoOU", "Built for fun, the Toyota GT86 is a lightweight coupe with a 2.0L flat-4 engine pushing 200 hp to the rear wheels. It’s not about straight-line speed—it’s about razor-sharp cornering and driver engagement, making every backroad feel like a racetrack..", 4.2, 300),
        ("Mazda", "https://pixabay.com/photos/car-vehicle-mazda-auto-automobile-6122175/", "A red hatchback with punch, the Mazda 3 offers sporty handling and sharp looks. Its 2.5L engine delivers 186 hp, paired with either manual or automatic transmissions. Perfect for urban agility and weekend escapes, it’s fun yet practical..", 4.8, 200),
        ("Nissan", "https://unsplash.com/photos/a-white-sports-car-parked-on-a-wet-road-ZNPVwTqhhHo", "The Nissan 370Z is a rear-wheel drive sports coupe that’s all about balance. Its 3.7L V6 puts out 332 hp and rockets from 0–100 km/h in around 5 seconds. With its classic proportions and analog feel, it's a favorite among purists..", 4.7, 350),
        ("Porsche", "https://pixabay.com/photos/automobile-cayman-coupe-design-5330353/", "The mid-engine Porsche 718 Cayman offers a blend of surgical handling and everyday refinement. With a turbocharged flat-4 producing 300 hp and a lightweight frame, it delivers a thrilling 0–100 km/h time under 5 seconds. German engineering at its finest..", 4.3, 275),
        ("Lamborghini", "https://unsplash.com/photos/an-orange-sports-car-parked-in-front-of-a-building-i0GAaus50es","Blazing in orange, the Lamborghini Huracán is pure Italian adrenaline. Its 5.2L V10 engine blasts out up to 640 hp, launching from 0–100 km/h in under 3 seconds. Built for speed, drama, and attention, it’s every bit the supercar fantasy.", 4.6, 225),
        ("Lexus", "https://unsplash.com/photos/white-mercedes-benz-c-class-NR7urrOwkLE", "Though labeled as Lexus, this is a Mercedes-Benz C-Class—an elegant white sedan known for its smooth ride and tech-packed interior. It typically runs on a 2.0L turbo engine with balanced power and efficiency, ideal for daily luxury driving..", 4.1, 320),
        ("Tesla", "https://unsplash.com/photos/a-futuristic-car-is-parked-on-the-side-of-the-road-VceGFFBjSrY", "This futuristic EV is designed for impact—literally and visually. With up to 857 hp, all-wheel drive, and a range exceeding 500 km, the Tesla Cybertruck blends off-road utility with electric performance. It's bold, unconventional, and distinctly next-gen..", 4.0, 275),
        ("Ferarri", "https://pixabay.com/photos/automobile-ferrari-sports-car-3309967/", "With iconic lines and retro charm, the Ferrari Testarossa carries a 4.9L flat-12 engine making 390 hp. This classic exudes 1980s speed with a 5-speed manual transmission and a top speed nearing 290 km/h—a raw, analog driving experience..", 4.4, 240),
        ("BMW", "https://unsplash.com/photos/a-black-car-parked-in-a-parking-lot-QSNRdQjqXpI", "Captured in grayscale, this BMW coupe handles snowy roads with confidence. Likely equipped with BMW’s xDrive all-wheel system and a turbocharged engine, it's both visually striking and winter-capable—proving performance isn't seasonal.", 4.9, 280)
        ("Audi", "https://unsplash.com/photos/gray-and-red-coupe-bKqNW5Dq6p8", "Sleek and aerodynamic, this Audi coupe sports aggressive lines and dual-tone styling. Backed by either a turbocharged four-cylinder or V6, Audi’s Quattro all-wheel drive ensures sharp grip and responsive handling on every turn.", 4.1, 290)
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