currency_rates = {'EUR': 0.85, 'GBP': 0.72, 'JPY': 109.35, 'CAD': 1.21}
orders = {} 

opened_file = open('global_daily_sales.txt')
for order in opened_file:
    order_list = order.split(",")
    order_number = int(order_list[0])
    sales_total = float(order_list[1])
    country_currency = order_list[2].rstrip()
    if order_number not in orders:
        orders[order_number] = {'sales_total': sales_total, 'currency': country_currency}
        
        currency = orders[order_number]['currency']
        total = orders[order_number]['sales_total']
        if orders[order_number]['currency'] != 'USD':
            conversion_rate = currency_rates[currency]
            orders[order_number]['sales_total'] = total / conversion_rate
            orders[order_number]['currency'] = 'USD'

print(orders)
        
opened_file.close()

currency_rates = {'EUR': 0.85, 'GBP': 0.72, 'JPY': 109.35, 'CAD': 1.21}

removed_gbp_value = currency_rates.pop('GBP')
removed_cad_value = currency_rates.pop('CAD')
print(removed_gbp_value)
print(removed_cad_value)

print(currency_rates)

currency_rates.clear()

print(currency_rates)