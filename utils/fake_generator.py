# from enum import Enum, auto
import datetime
import json
import random
import time

import numpy as np
from faker import Faker

from message import Message, OrderStatus, Product, ProductId

fake = Faker()


def send_message_to_pubsub(message: dict):

    ...


def generate_parameters():
    creation_date = fake.date_time_between(start_date=datetime.datetime.now() - datetime.timedelta(days=45),
                                           end_date=datetime.datetime.now())
    order_status = random.choice([OrderStatus.OPEN,
                                  OrderStatus.CLOSED_WAITING_PAYMENT,
                                  OrderStatus.PAID,
                                  OrderStatus.DELIVERED])
    order_id = np.random.randint(low=11111,
                                 high=32335)
    customer_id = fake.user_name()
    product_id = random.choice([ProductId.BOOK,
                                ProductId.PENCIL,
                                ProductId.PEN,
                                ProductId.NOTEBOOK,
                                ProductId.ERASER,
                                ProductId.CASE,
                                ProductId.BACKPACK])
    product_price = np.random.randint(low=5,
                                      high=30)
    product = Product(product_id, product_price)

    return (creation_date, order_status, order_id, customer_id, product)


def main(n: int = 50,
         delay: int = 5) -> None:
    for _ in range(n):
        message = Message(*generate_parameters())
        body = json.dumps(message.get_message())
#        print(output)
        time.sleep(delay)

        # send_message_to_pubsub()


if __name__ == "__main__":
    main()
