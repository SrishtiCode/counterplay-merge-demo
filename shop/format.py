"""Formatting prices for display."""


def format_price(cents: int, symbol: str = "$") -> str:
    """A price in cents as text, like "$1,234.50" or "-$0.05"."""
    sign = "-" if cents < 0 else ""
    whole, rest = divmod(abs(cents), 100)
    return f"{sign}{symbol}{whole:,}.{rest:02d}"
