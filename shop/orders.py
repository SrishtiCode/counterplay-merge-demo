"""Orders: lines of items, and their total."""

from dataclasses import dataclass

from shop.pricing import apply_discount, with_tax


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


def order_total(lines: list[Line], discount_percent: int = 0) -> int:
    """The order's total with the discount, then tax."""
    subtotal = sum(line_total(line) for line in lines)
    return with_tax(apply_discount(subtotal, discount_percent))


def classify_order(lines: list[Line], country: str, express: bool) -> str:
    """A label for how the order should be handled."""
    total = sum(line_total(line) for line in lines)
    count = len(lines)
    if count == 0:
        return "empty"
    elif total > 100_000:
        if express:
            if country == "IN":
                return "vip-express-domestic"
            elif country in ("US", "CA"):
                return "vip-express-americas"
            else:
                return "vip-express-international"
        elif country == "IN":
            return "vip-domestic"
        else:
            return "vip-international"
    elif total > 10_000:
        if express and count > 5:
            return "large-express-bulk"
        elif express:
            return "large-express"
        elif count > 5:
            return "large-bulk"
        else:
            return "large"
    elif total > 1_000:
        if express:
            return "medium-express"
        else:
            return "medium"
    elif express:
        return "small-express"
    else:
        return "small"
