class SmartphoneManager:
    def __init__(self, connection):
        self.connection = connection

    def addSmartphone(self, id=None, brand=None, model=None, price=None, rom=None, cpu=None):
        if id is None:
            id = int(input("Enter smartphone ID: "))
        if brand is None:
            brand = input("Enter smartphone brand: ")
        if model is None:
            model = input("Enter smartphone model: ")
        if price is None:
            price = int(input("Enter smartphone price: "))
        if rom is None:
            rom = int(input("Enter smartphone ROM size: "))
        if cpu is None:
            cpu = input("Enter smartphone CPU: ")

        query = "INSERT INTO smartphones (id, brand, model, price, rom, cpu) VALUES (%s, %s, %s, %s, %s, %s)"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (id, brand, model, price, rom, cpu))
        self.connection.commit()
        print("Smartphone added successfully!")

    def showAllSmartphones(self):
        print("Here are all smartphones:")
        query = "SELECT * FROM smartphones ORDER BY id ASC"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            for record in cursor.fetchall():
                id, brand, model, price, rom, cpu = record
                print(f"ID: {id}, Brand: {brand}, Model: {model}, Price: ${price}, ROM: {rom}GB, CPU: {cpu}")

    def updateSmartphone(self, id=None, brand=None, model=None, price=None, rom=None, cpu=None):
        if id is None:
            id = int(input("Enter smartphone ID: "))
        if brand is None:
            brand = input("Enter new smartphone brand: ")
        if model is None:
            model = input("Enter new smartphone model: ")
        if price is None:
            price = int(input("Enter new smartphone price: "))
        if rom is None:
            rom = int(input("Enter new smartphone ROM size: "))
        if cpu is None:
            cpu = input("Enter new smartphone CPU: ")
        query = "UPDATE smartphones SET brand = %s, model = %s, price = %s, rom = %s, cpu = %s WHERE id = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (brand, model, price, rom, cpu, id))
        self.connection.commit()
        print("Smartphone updated successfully!")

    def deleteSmartphone(self, id=None):
        if id is None:
            id = int(input("Enter smartphone ID to delete: "))
        query = "DELETE FROM smartphones WHERE id = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (id,))
        self.connection.commit()
        print("Smartphone deleted successfully!")

    def searchSmartphone(self):
        brand = input("Enter the smartphone brand to search for: ")
        query = "SELECT * FROM smartphones WHERE brand = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (brand,))
            smartphones = cursor.fetchall()
            if smartphones:
                print("Search results:")
                for record in smartphones:
                    id, brand, model, price, rom, cpu = record
                    print(f"ID: {id}, Brand: {brand}, Model: {model}, Price: ${price}, ROM: {rom}GB, CPU: {cpu}")
            else:
                print("No smartphones found with the specified brand.")

    def ratingOfSmartphones(self):
        print("Choose the type of rating:")
        print("1. The most powerful smartphones")
        print("2. The cheapest smartphones")
        print("3. The most expensive smartphones")

        choice = input("Enter your choice: ")

        if choice == "1":
            self.topSmartphones("powerful")
        elif choice == "2":
            self.topSmartphones("cheapest")
        elif choice == "3":
            self.topSmartphones("expensive")
        else:
            print("Invalid choice. Please try again.")

    def topSmartphones(self, rating_type):
        if rating_type == "powerful":
            query = "SELECT * FROM smartphones ORDER BY id ASC LIMIT 3"
            rating_name = "The most powerful smartphones"
        elif rating_type == "cheapest":
            query = "SELECT * FROM smartphones ORDER BY price ASC LIMIT 3"
            rating_name = "The cheapest smartphones"
        elif rating_type == "expensive":
            query = "SELECT * FROM smartphones ORDER BY price DESC LIMIT 3"
            rating_name = "The most expensive smartphones"

        print(rating_name + ":")
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            smartphones = cursor.fetchall()
            for idx, record in enumerate(smartphones, start=1):
                id, brand, model, price, rom, cpu = record
                print(f"{idx}. Brand: {brand}, Model: {model}, Price: ${price}, ROM: {rom}GB, CPU: {cpu}")
