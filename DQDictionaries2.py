currency_rates = {'EUR': 0.85, 'GBP': 0.72, 'JPY': 109.35, 'CAD': 1.21}
# Update values for currency_rates here:


country_counts = {'EUR': 0, 'GBP': 0, 'JPY': 0, 'CAD': 0} 
opened_file = open('global_daily_sales.txt')
for order in opened_file:
    order_list = order.split(",")
    country_currency = order_list[2].rstrip()
    
    
    if country_currency in country_counts:
        country_counts[country_currency] += 1
    
print(country_counts)
print(currency_rates)


opened_file.close()
