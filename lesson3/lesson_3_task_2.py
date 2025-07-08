from smartphone import Smartphone

catalog = [
    Smartphone(brand="OPPO", model="A60", number="+79122589363"),
    Smartphone(brand="Samsung", model="Galaxy", number="+79127739458"),
    Smartphone(brand="Xiaomi", model="13 Lite", number="+79124324978"),
    Smartphone(brand="POCO", model="M5", number="+79120954543"),
    Smartphone(brand="Redmi", model="Note 12", number="+79129182726"),
]


for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.namber}.")
