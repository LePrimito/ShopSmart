from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    name: str
    quantity: int

class ShoppingList(BaseModel):
    category: str
    items: List[Item] = []