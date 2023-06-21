from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

bosh_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ichimliklar"),
            KeyboardButton(text="Lavashlar")
        ],
        [
            KeyboardButton(text="Pitsalar"),
            KeyboardButton(text="Burgerlar")
        ],
        [
            KeyboardButton(text="Shirinliklar")
        ],
        [
            KeyboardButton(text="Ortga")
        ]
    ],
    resize_keyboard=True
)


ichimliklar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Pepsi"),
            KeyboardButton(text="Coca Cola")
        ],
        [
            KeyboardButton(text="Fanta")
        ],
        [
            KeyboardButton(text="Ortga")
        ]
    ],
    resize_keyboard=True
)
