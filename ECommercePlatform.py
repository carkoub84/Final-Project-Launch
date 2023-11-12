# Define team members and project leader
team_leader = "Project Leader: Chabha Arkoub"
team_members = "Team Member : Max Rafert"

# Define client information
client = """Client: OmegaSoft Retail
Description: OmegaSoft Retail is a leading online retail company with a diverse product range, including electronics, fashion, and home essentials."""

# Define system purpose
system_purpose = """The purpose of our system is to create a web-based e-commerce platform that allows users to purchase and sell various products, offering a wide selection of items to online shoppers. Our goal is to provide a user-friendly, secure, and efficient platform for online shopping and selling, enhancing the retail company's online presence and customer experience."""

# Define scope of the project
project_scope = """In defining the scope of our project, we are committed to a realistic approach. Our initial focus will be on building the core functionality of the e-commerce platform, which includes:
- User Registration and Authentication
- Product Catalog and Listings
- Shopping Cart
- Payment Processing
- Order Management
- User Reviews and Ratings
While we recognize the potential for additional features such as recommendation algorithms, seller analytics, and advanced search functionalities, these are outside the current scope of our project. We understand the importance of prioritizing a stable and well-tested core before expanding into advanced features."""

# Define general design of the system
system_design = """General Design of the System:
Our system will follow a multi-tier architecture for scalability and maintainability. We plan to use the following components:
1. Frontend: We will develop the user interface using React, ensuring a responsive and intuitive design that supports multiple devices.
2. Backend: The backend will be implemented using Node.js and Express.js to handle requests, manage user accounts, and interact with the database.
3. Database: We will utilize a relational database system, specifically PostgreSQL, to store user data, product information, orders, and reviews.
4. APIs: RESTful APIs will be designed to facilitate communication between the frontend and backend."""

class OmegaSoft :
    def __init__(self):
        self.users = []
        self.products = []
        self.orders = []

    def add_user(self, user):
        self.users.append(user)

    def add_product(self, product):
        self.products.append(product)

    def create_order(self, user, products):
        order = Order(user, products)  # Replace 'Order' with your actual 'Order' class.
        self.orders.append(order)

    def generate_sales_report(self):
        total_revenue = sum(order.calculate_total() for order in self.orders)
        print(f"Total Revenue: ${total_revenue}")

    def show_inventory(self):
        for product in self.products:
            print(f"{product.name} - Quantity: {product.quantity}")

class User:
    def __init__(self, username):
        self.username = username

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

class Order:
    def __init__(self, user, products):
        self.user = user
        self.products = products

    def calculate_total(self):
        total = sum(product.price for product in self.products)
        return total

class Cart:
    pass  # You can add functionality for the cart if needed.

class Payment:
    pass  # You can add functionality for payments if needed.

class Review:
    pass  # You can add functionality for reviews if needed.

class ProductCategory:
    pass  # You can add functionality related to product categories if needed.
