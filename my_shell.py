python manage.py shell

from shop.models import Item, Purchase
items = Item.objects.all()
items
item = Item(name="phone", price=10000)
item.save()
item_1 = Item(name="headphones", price=400)
item_1.save()
item_2 = Item(name="case", price=200)
item_2.save()
item_3 = Item(name="charger", price=800)
item_3.save()
item_4 = Item(name="box", price=100)
item_4.save()
purchase = Purchase(name="Pepe", age=39, item_id=item.id)
purchase.save()
purchase_1 = Purchase(name="Ramos", age=37, item_id=item_3.id)
purchase_1.save()
purchase_2 = Purchase(name="Marcelo", age=38, item_id=item_4.id)
purchase_2.save()
purchase_3 = Purchase(name="Carvajal", age=31, item_id=item_2.id)
purchase_3.save()
purchase_4 = Purchase(name="Modric", age=37, item_id=item.id)
purchase_4.save()
purchases = Purchase.objects.all()
purchases
exit()