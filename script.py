from xmlrpc import client

# Set up the Odoo server URL and database name
url = 'http://localhost:8069'
db = 'odoo_database_name'

# Set up the username and password for accessing the Odoo database
username = 'odoo_username'
password = 'odoo_password'

# Connect to the Odoo database
common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

# Create a new client object for accessing the Odoo API
models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Set up the report parameters for the Sales Analysis report
sales_params = {
    'date_from': '2022-01-01',
    'date_to': '2022-12-31',
    'groupby': ['product_id'],
}

# Generate the Sales Analysis report
sales_data = models.execute_kw(db, uid, password, 'report.sale.analysis', 'get_report_data', [sales_params])

# Display the sales report data
for row in sales_data:
    product_name = row['product_name']
    quantity = row['qty_delivered']
    revenue = row['price_total']
    print(f"Product: {product_name}, Quantity: {quantity}, Revenue: {revenue}")

# Set up the report parameters for the Inventory Analysis report
inventory_params = {
    'date_from': '2022-01-01',
    'date_to': '2022-12-31',
    'groupby': ['product_id', 'location_id'],
}

# Generate the Inventory Analysis report
inventory_data = models.execute_kw(db, uid, password, 'report.inventory.analysis', 'get_report_data', [inventory_params])

# Display the inventory report data
for row in inventory_data:
    product_name = row['product_name']
    location_name = row['location_name']
    quantity = row['qty_available']
    cost = row['standard_price']
    print(f"Product: {product_name}, Location: {location_name}, Quantity: {quantity}, Cost: {cost}")
