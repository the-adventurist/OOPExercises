from typing import List

import pkg_resources.extern

from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        this_product = [p for p in self.products if p.name == product_name]
        if this_product:
            this_product = this_product[0]
            return this_product

    def remove(self, product_name: str) -> None:
        this_product = [p for p in self.products if p.name == product_name]
        if this_product:
            this_product = this_product[0]
            self.products.remove(this_product)

    def __repr__(self) -> str:
        return "\n".join([f"{p.name}: {p.quantity}" for p in self.products])