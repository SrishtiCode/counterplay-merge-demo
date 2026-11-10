"""Orders: lines of items, and their total."""

from dataclasses import dataclass

from shop.pricing import apply_discount, format_price, with_tax


@dataclass
class Line:
    item: str
    unit_cents: int
    quantity: int = 1


def line_total(line: Line) -> int:
    """One line's price before tax."""
    if line.quantity < 1:
        raise ValueError("a line has at least one item")
    return line.unit_cents * line.quantity


def format_line(line: Line) -> str:
    """Line("pen", 150, 4) -> 'pen x4 €6.00'."""
    return f"{line.item} x{line.quantity} {format_price(line_total(line))}"


def order_total(lines: list[Line], discount_percent: int = 0) -> int:
    """The order's total with the discount, then tax."""
    subtotal = sum(line_total(line) for line in lines)
    return with_tax(apply_discount(subtotal, discount_percent))
