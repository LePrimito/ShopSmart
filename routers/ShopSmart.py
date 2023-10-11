from typing import List
from fastapi import APIRouter,HTTPException
from classes.schema_dto import Item, ShoppingList

router = APIRouter(
    tags=['Lists']
)


shopping_lists = [
    ShoppingList(category="Fruits", items=[Item(name="Pomme", quantity=4)]),
    ShoppingList(category="Legumes", items=[Item(name="Artichaut", quantity=2)])
]

@router.post('/lists/', response_model=ShoppingList)
async def create_shopping_list(shopping_list: ShoppingList):
    shopping_lists.append(shopping_list)
    return shopping_list

@router.get('/lists/{category}', response_model=List[ShoppingList])
async def get_shopping_lists_by_category(category: str):
    lists = [s for s in shopping_lists if s.category == category]
    return lists

@router.get('/lists/', response_model=List[ShoppingList])
async def get_all_shopping_lists():
    return shopping_lists

@router.post('/lists/{category}', response_model=ShoppingList)
async def add_item_to_shopping_list(category: str, item: Item):
    for shopping_list in shopping_lists:
        if shopping_list.category == category:
            shopping_list.items.append(item)
            return shopping_list
    raise HTTPException(status_code=404, detail="Shopping list not found")

@router.patch('/lists/{category}', response_model=ShoppingList)
async def patch_shopping_list(category: str,updated_name: str):
    for shopping_list in shopping_lists:
        if shopping_list.category == category:
            shopping_list.category = updated_name
            return shopping_list
    raise HTTPException(status_code=404, detail="Shopping list not found")

@router.delete('/lists/{category}', response_model=ShoppingList)
async def delete_shopping_list(category: str):
    for shopping_list in shopping_lists:
        if shopping_list.category == category:
            shopping_lists.remove(shopping_list)
            return shopping_list
    raise HTTPException(status_code=404, detail="Shopping list not found")

@router.patch('/lists/{category}/items/{item_name}', response_model=ShoppingList)
async def patch_item_from_shopping_list(category:int, item_name: str,updated_name: str):
    for shopping_list in shopping_lists:
        if shopping_list.category == category:
            for item in shopping_list.items:
                if item.name == item_name:
                    item.name = updated_name
                    return shopping_list
    raise HTTPException(status_code=404, detail="Item not found in the shopping list")

@router.delete('/lists/{category}/items/{item_name}', response_model=ShoppingList)
async def delete_item_from_shopping_list(category: str, item_name: str):
    for shopping_list in shopping_lists:
        if shopping_list.category == category:
            for item in shopping_list.items:
                if item.name == item_name:
                    shopping_list.items.remove(item)
                    return shopping_list
    raise HTTPException(status_code=404, detail="Item not found in the shopping list")