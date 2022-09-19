import datetime
from dataclasses import dataclass
from enum import Enum, auto


class OrderStatus(Enum):
    """All possible events while ordering"""
    OPEN = auto()
    CLOSED_WAITING_PAYMENT = auto()
    PAID = auto()
    DELIVERED = auto()


class ProductId(Enum):
    """All products"""

    BOOK = auto()
    PENCIL = auto()
    PEN = auto()
    NOTEBOOK = auto()
    ERASER = auto()
    CASE = auto()
    BACKPACK = auto()


@dataclass
class Product:
    """Product structure"""
    product_id: ProductId
    price: float


@dataclass
class Message:
    """Message format"""
    creation_date: datetime.datetime
    order_status: OrderStatus
    order_id: int
    customer_id: str
    product: Product

    @property
    def set_message(self) -> dict:
        """Generating message schema"""
        message = {"CreationDate": self.creation_date.strftime("%Y-%m-%d %H:%M:%S"),
                   "OrderStatus": self.order_status.value,
                   "OrderId": self.order_id,
                   "CustomerId": self.customer_id,
                   "ProductId": self.product.product_id.value,
                   "ProductPrice": self.product.price
                   }
        return message

    def get_message(self) -> dict:
        return self.set_message
