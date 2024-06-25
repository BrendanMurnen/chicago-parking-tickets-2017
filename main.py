import csv
import json

# Step 1: Read the CSV file and store data in a dictionary
csv_data = {}
with open('data/2017_ward_ticketing_stats.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        ward = row['ward']
        csv_data[ward] = {
            'issued_tickets_count': row['issued_tickets_count'],
            'paid_tickets_count': row['paid_tickets_count'],
            'collected_tickets_pct': row['collected_tickets_pct'],
            'net_payments_usd': row['net_payments_usd']
        }

# Step 2: Load the GeoJSON file
with open('data/BOUNDARIES - WARDS (2015-2023).geojson', mode='r') as geojson_file:
    geojson_data = json.load(geojson_file)

# Step 3: Perform the left join
for feature in geojson_data['features']:
    ward = feature['properties']['ward']
    if ward in csv_data:
        for key, value in csv_data[ward].items():
            feature['properties'][key] = value
    else:
        # Optionally handle wards not found in the CSV
        pass

# Step 4: Output the modified GeoJSON
with open('ticketing_wards_2017.geojson', mode='w') as updated_geojson_file:
    json.dump(geojson_data, updated_geojson_file, indent=4)