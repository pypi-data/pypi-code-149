import time

from gdshoplib.apps.crm.on_request import (OnRequestTable,
                                           OnRequestTableInvalidRow)
from gdshoplib.apps.product import Product
from gdshoplib.apps.products.price import Price
from gdshoplib.core.settings import CRMSettings
from gdshoplib.services.notion.database import Database
from gdshoplib.services.notion.notion import Notion
from gdshoplib.services.notion.page import Page


class Order(Page):
    SETTINGS = CRMSettings()

    def __init__(self, *args, **kwargs):
        self._on_request = None
        self._products = None

        super(Order, self).__init__(*args, **kwargs)

    def __len__(self):
        return len(self.products) + sum([row.quantity for row in self.on_request])

    @classmethod
    def get(cls, id):
        page = [
            page
            for page in Database(cls.SETTINGS.CRM_DB).pages(
                params={
                    "filter": {
                        "property": "ID заказа",
                        "rich_text": {
                            "equals": id,
                        },
                    }
                }
            )
        ]
        if not page:
            return
        if len(page) > 1:
            raise OrderIDDuplicate

        page = page[0]

        return cls(page["id"], notion=page.notion, parent=page.parent)

    @classmethod
    def query(cls, filter=None, params=None, notion=None):
        for page in Database(cls.SETTINGS.CRM_DB, notion=notion).pages(
            filter=filter, params=params
        ):
            yield cls(page["id"], notion=page.notion, parent=page.parent)

    @property
    def on_request(self):
        if not self._on_request:
            self._on_request = OnRequestTable(
                [block for block in self.blocks(filter={"type": "table_row"})],
                notion=self.notion,
                parent=self,
            )

        return self._on_request

    @property
    def products(self):
        if not self._products:
            self._products = [Product(page.id) for page in self.products_field]
        return self._products

    def requested_price(self, product):
        return product.price.profit - product.price.profit * (self.discount * 0.01)

    @property
    def delivery(self):
        return

    @property
    def pay(self):
        return

    @property
    def discount_sum(self):
        return round(self.full_price - self.price, 2)

    @property
    def price(self):
        result = self.on_request.price()
        for product in self.products:
            result += product.price.now

        return result - result * (self.discount * 0.01)

    @property
    def full_price(self):
        result = self.on_request.price()
        for product in self.products:
            result += product.price.profit

        return result

    @property
    def profit(self):
        base_price = self.on_request.price("gross")
        for product in self.products:
            base_price += product.price.gross
        return self.price - base_price

    def generate_id(self):
        return f"{self.platform.key.lower()}.{int(time.time())}"

    def description_on_request_product(self, row):
        quantity = f"({row.quantity} шт.)"
        return f"{row.name} {quantity if row.quantity > 1 else ''} : {Price(row)['neitral'] * row.quantity} ₽"

    def description_basic_product(self, product):
        return f"{product.name} : {product.price.profit} ₽"

    @property
    def description(self):
        result = ["Ваш заказ\n"]
        counter = 1

        for row in self.on_request:
            if isinstance(row, OnRequestTableInvalidRow):
                continue
            result.append(f"{counter}. {self.description_on_request_product(row)}")
            counter += 1

        for product in self.products:
            result.append(f"{counter}. {self.description_basic_product(product)}")
            counter += 1

        if self.delivery or self.discount_sum:
            result.append(f"\nТовары ({len(self)}): {self.full_price}")
        if self.discount_sum:
            result.append(f"Скидка: {self.discount_sum} ₽")
        if self.delivery:
            result.append(f"Стоимость доставки: {self.delivery.price} ₽")

        result.append(f"\nОбщая стоимость: {self.price} ₽")

        return "\n".join(result)

    def set_id(self):
        # Установить ID
        if not self.platform:
            return

        self.notion.update_prop(
            self.id,
            params={
                "properties": {"ID заказа": [{"text": {"content": self.generate_id()}}]}
            },
        )

    def set_price_description(self):
        # Установка описания расчетов цены
        self.notion.update_prop(
            self.id,
            params={
                "properties": {
                    "Расчеты": [{"text": {"content": self.description or ""}}]
                }
            },
        )

    def set_price(self):
        # Установка итоговой цены
        self.notion.update_prop(
            self.id,
            params={"properties": {"Итого": {"number": self.price}}},
        )

    def set_profit(self):
        # Установка итоговой цены
        self.notion.update_prop(
            self.id,
            params={"properties": {"Прибыль": {"number": self.profit}}},
        )

    def load_tasks(self):
        # Загрузка задач в CRM из источников
        ...

    @classmethod
    def update(cls):
        # Обновление карточки Order
        for order in cls.query(notion=Notion(caching=True)):
            order.on_request.update()
            order.set_price()
            order.set_profit()
            order.set_price_description()
            if not order.order_id:
                order.set_id()

    def notification(self):
        # Отправка уведомлений
        ...


class OrderIDDuplicate(Exception):
    ...
