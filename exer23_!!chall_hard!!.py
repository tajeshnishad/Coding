# Challenge 9: Multi-Stage Order Pipeline
incoming = ['Order-101', '', 'Order-102 (VIP)', 'CANCELLED', 'Order-103']
processing = []
def validate_orders(raw_orders, valid_orders):
    for raw_order in raw_orders:
        if raw_order == '' or 'CANCELLED':
            raw_order.pop()
        else:
            valid_orders.append(raw_order)

# def tag_priority(valid_orders):
#     tagged_order = []
#     for valid_order in valid_orders: