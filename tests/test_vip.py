VIP_EMAIL = "anna.berg@clients.invalid"


def send_receipt(outbox: list, to: str, total_cents: int) -> None:
    outbox.append({"to": to, "total_cents": total_cents})


def test_vip_receipt_sent():
    outbox = []
    send_receipt(outbox, VIP_EMAIL, 4500)
    assert outbox == [{"to": VIP_EMAIL, "total_cents": 4500}]
