pizza_orders = [
    "Sonic Spin Dash Supreme",
    "Mortal Kombat Fatality Firecrust",
    "NBA Jam Boomshakalaka Cheese",
    "Earthworm Jim Intergalactic Jalapeno",
    "Ecco the Dolphin Deep Sea Deluxe",
]

finished_pizzas = []

while pizza_orders:
    current_pizza = pizza_orders.pop()
    print("Your pizza pie is finished!")
    finished_pizzas.append(current_pizza)

for pizza in finished_pizzas:
    print(f"The pizza {pizza} was made.")