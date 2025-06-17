from server.app import app, db
from server.models import Restaurant, Pizza, RestaurantPizza

def seed_database():
    with app.app_context():
        print("Resetting database...")
        db.drop_all()
        db.create_all()
        
        print("Creating restaurants...")
        restaurants = [
            Restaurant(name="Pizza Palace", address="123 Main St"),
            Restaurant(name="Mario's Pizzeria", address="456 Oak Ave"),
            Restaurant(name="Luigi's Pizza", address="789 Pine Rd")
        ]
        
        print("Creating pizzas...")
        pizzas = [
            Pizza(name="Margherita", ingredients="Tomato sauce, Mozzarella, Basil"),
            Pizza(name="Pepperoni", ingredients="Tomato sauce, Mozzarella, Pepperoni"),
            Pizza(name="Vegetarian", ingredients="Tomato sauce, Mozzarella, Bell peppers, Mushrooms, Olives")
        ]
        
        db.session.add_all(restaurants + pizzas)
        db.session.commit()
        
        print("Creating restaurant pizzas...")
        restaurant_pizzas = [
            RestaurantPizza(price=10, restaurant_id=1, pizza_id=1),
            RestaurantPizza(price=12, restaurant_id=1, pizza_id=2),
            RestaurantPizza(price=15, restaurant_id=2, pizza_id=3),
            RestaurantPizza(price=8, restaurant_id=3, pizza_id=1)
        ]
        
        db.session.add_all(restaurant_pizzas)
        db.session.commit()
        
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()