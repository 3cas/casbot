from datetime import timedelta

class Effects:
    def __init__(self, effects: dict):
        self.fx = effects

class SaleValue:
    def __init__(self, value: int):
        self.value = value

ITEMS = {
    "hamburger": "Yummy! Found at restaurants and sometimes randomly around",
    "berries": "Yummy! Found in forests and bushes",
    "alcohol": [
        "Induces Risk and Drunk for 90 minutes, allowing risky gambling decisions and distorted perception",
        Effects({
            "risk": timedelta(minutes=90), 
            "drunk": timedelta(minutes=90)
        }),
        SaleValue(15)
    ],
    "slot_token": "Can be used in casinos to gamble.",
    "stinky_cheese": "Can be eaten. Or, you could try giving it to a mouse.",
    "cookie": [
        "Sellable and edible. You could try either one.",
        SaleValue(3)
    ],
    "thc_cart": [
        "You Could Get HIgh//.,",
        Effects({
            "high": timedelta(minutes=90)
        }),
        SaleValue(35)
    ]
}
