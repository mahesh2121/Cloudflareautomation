import CloudFlare
import csv

def authenticate_with_cloudflare(api_token):
    return CloudFlare.CloudFlare(token=api_token)

def fetch_dns_records(cf, zone_name):
    zone_id = cf.zones.get(params={'name': zone_name})[0]['id']
    dns_records = cf.zones.dns_records.get(zone_id, params={'per_page': 100})  # Adjust per_page as needed
    return dns_records

def write_dns_records_to_csv(dns_records, output_file):
    """
    Write DNS records to a CSV file.

    Args:
    - dns_records: List of DNS records fetched from Cloudflare.
    - output_file: Path to the output CSV file.
    """
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Domain', 'Type', 'Content', 'TTL'])
        for record in dns_records:
            writer.writerow([record['name'], record['type'], record['content'], record['ttl']])

def main():
    api_token = 'XXX'
    domain = 'XXX'
    output_csv_file = 'dns_entries.csv'

    cf = authenticate_with_cloudflare(api_token)
    dns_records = fetch_dns_records(cf, domain)
    write_dns_records_to_csv(dns_records, output_csv_file)
    print(f"All DNS records written to {output_csv_file}")

if __name__ == "__main__":
    main()
