# from enum import Enum, auto
import datetime
import random
import time

import numpy as np
from faker import Faker

from message import EventId, Message, Product, ProductId

fake = Faker()


def generate_parameters():
    creation_date = fake.date_time_between(start_date=datetime.datetime.now() - datetime.timedelta(days=45),
                                           end_date=datetime.datetime.now())
    event_id = random.choice([EventId.OPEN,
                              EventId.CLOSED_WAITING_PAYMENT,
                              EventId.PAID,
                              EventId.DELIVERED])
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

    return (creation_date, event_id, order_id, customer_id, product)


def main(n: int = 50,
         delay: int = 5) -> None:
    for _ in range(n):
        message = Message(*generate_parameters())
        print(message)

        output = message.get_message()

        time.sleep(delay)


if __name__ == "__main__":
    main()
