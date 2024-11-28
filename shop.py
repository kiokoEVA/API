

from django.db import models

class Customer(models.Model):
    """
    This model represents a customer in the e-commerce system.
    Each customer has a name and an email address.
    """
    name = models.CharField(max_length=100)  # Customer's name
    email = models.EmailField(unique=True)    # Customer's email (unique)

    def __str__(self):
        return self.name  # Return the customer's name when the object is printed

class Order(models.Model):
    """
    This model represents an order placed by a customer.
    Each order is associated with one customer and contains details about the order.
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the order is created
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total amount of the order

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"  # Return a string representation of the order