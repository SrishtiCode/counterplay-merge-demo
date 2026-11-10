"""Sorting orders into handling classes."""


def classify_order(total_cents: int, items: int, country: str, express: bool) -> str:
    """The handling class for an order, from its size, destination and speed."""
    if total_cents <= 0:
        return "invalid"
    elif items <= 0:
        return "invalid"
    if country == "US":
        if express:
            if total_cents >= 100000:
                return "domestic-express-priority"
            elif items > 10:
                return "domestic-express-bulk"
            else:
                return "domestic-express"
        else:
            if total_cents >= 100000:
                return "domestic-priority"
            elif items > 10:
                return "domestic-bulk"
            else:
                return "domestic"
    elif country in ("CA", "MX"):
        if express:
            if items > 10:
                return "regional-express-bulk"
            return "regional-express"
        elif total_cents >= 50000:
            return "regional-priority"
        else:
            return "regional"
    else:
        if express:
            return "international-express"
        elif total_cents >= 50000:
            return "international-priority"
        else:
            return "international"
