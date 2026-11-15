from fastmcp import FastMCP

mcp = FastMCP("Restaurant")

# Simple in-memory menu and order data for demo purposes
MENU = {
    "pizza": 250,
    "burger": 150,
    "pasta": 200,
    "salad": 120,
    "coke": 50,
}

ORDERS = {}
next_order_id = 1


@mcp.tool()
def get_menu() -> str:
    """Get the restaurant menu with prices."""
    lines = [f"{item.title()}: Rs {price}" for item, price in MENU.items()]
    return "\n".join(lines)


@mcp.tool()
def place_order(item: str, quantity: int) -> str:
    """Place an order for a menu item and quantity."""
    global next_order_id
    item = item.lower()
    if item not in MENU:
        return f"'{item}' is not on the menu."

    order_id = next_order_id
    next_order_id += 1
    total = MENU[item] * quantity

    ORDERS[order_id] = {
        "item": item,
        "quantity": quantity,
        "total": total,
        "status": "placed",
    }
    return f"Order #{order_id} placed: {quantity} x {item} = Rs {total}"


@mcp.tool()
def get_order_status(order_id: int) -> str:
    """Get the status of an order by its order ID."""
    if order_id not in ORDERS:
        return f"No order found with ID {order_id}."
    order = ORDERS[order_id]
    return f"Order #{order_id}: {order['quantity']} x {order['item']} - {order['status']} (Rs {order['total']})"


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8002)
