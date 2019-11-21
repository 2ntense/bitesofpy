from decimal import *


def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

       :param item_total: str (e.g. '$8.68')
       :param tax_rate: str (e.g. '4.75%)
       :param tip: str (e.g. '10%')
       :param people: int (e.g. 3)

       :return: tuple of (grand_total: str, splits: list)
                e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    sub_total = Decimal(item_total[1:])
    tax_multiplier = Decimal(tax_rate[:-1])
    tip_multiplier = Decimal(tip[:-1])

    total_w_tax = (sub_total * (1 + tax_multiplier / 100)).quantize(Decimal("1.00"), rounding=ROUND_HALF_EVEN)
    grand_total = (total_w_tax * (1 + tip_multiplier / 100)).quantize(Decimal("1.00"), rounding=ROUND_HALF_EVEN)
    grand_total_r = grand_total.quantize(Decimal("1.00"), rounding=ROUND_FLOOR)

    total_per_person = grand_total_r / people
    total_per_person_rd = total_per_person.quantize(Decimal("1.00"), rounding=ROUND_FLOOR)
    if total_per_person_rd * people == grand_total_r:
        return f"${grand_total_r:.2f}", people * [total_per_person_rd]

    missing_cents = int((grand_total_r - people * total_per_person_rd) * 100)

    splits = people * [total_per_person_rd]
    for i in range(missing_cents):
        splits[i] += Decimal("0.01")

    return f"${grand_total_r:.2f}", [s for s in splits]
