# from enum import Enum, auto
import datetime
import json
import random
import time

import numpy as np
from faker import Faker
from google.cloud import pubsub_v1

from message import Message, OrderStatus, Product, ProductId

fake = Faker()


def send_message_to_pubsub(message: str) -> None:
    project_id = "cloud-portfolio-dev"
    topic_id = "ReceiveOrder"
    # print(message)
    publisher = pubsub_v1.PublisherClient()

    topic_path = publisher.topic_path(project_id, topic_id)

    data = message.encode("utf-8")

    future = publisher.publish(topic_path,
                               data=data)
    # print(future)


def generate_parameters():
    creation_date = fake.date_time_between(start_date=datetime.datetime.now() - datetime.timedelta(days=45),
                                           end_date=datetime.datetime.now() + datetime.timedelta(days=45))

    order_status = random.choice([OrderStatus.OPEN,
                                  OrderStatus.CLOSED_WAITING_PAYMENT,
                                  OrderStatus.PAID,
                                  OrderStatus.DELIVERED])

    order_id = np.random.randint(low=11111,
                                 high=532403)

    customer_id = fake.user_name()

    product_id = random.choice([ProductId.BOOK,
                                ProductId.PENCIL,
                                ProductId.PEN,
                                ProductId.NOTEBOOK,
                                ProductId.ERASER,
                                ProductId.CASE,
                                ProductId.BACKPACK])

    product_price = float(np.random.randint(low=5,
                                            high=32))

    product = Product(product_id, product_price)

    return (creation_date, order_status, order_id, customer_id, product)


def main(n: int = 10000,
         delay: int = 0) -> None:
    """Main function"""
    for _ in range(n):
        message = Message(*generate_parameters())
        body = json.dumps(message.get_message(), indent=4)
        body = str(body)
        time.sleep(delay)
        send_message_to_pubsub(body)


if __name__ == "__main__":
    main()
