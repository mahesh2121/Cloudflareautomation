import CloudFlare
import csv

def authenticate_with_cloudflare(api_token):
    return CloudFlare.CloudFlare(token=api_token)

def fetch_dns_records(cf, zone_name):
    zone_id = cf.zones.get(params={'name': zone_name})[0]['id']
    dns_records = cf.zones.dns_records.get(zone_id)
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



def read_dns_entries_from_csv(file_path):
    """
    Read DNS entries from a CSV file.

    Args:
    - file_path: Path to the CSV file containing DNS entries.

    Returns:
    - A dictionary where keys are domain names and values are expected target IP addresses.
    """
    dns_entries = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2:
                domain = row[0].strip()
                expected_target = row[1].strip()
                dns_entries[domain] = expected_target
            else:
                print(f"Ignoring invalid row: {row}")
    return dns_entries


def check_dns_records(dns_records, expected_records):
    """
    Check if DNS records match the expected target IP addresses.

    Args:
    - dns_records: List of DNS records fetched from Cloudflare.
    - expected_records: Dictionary containing expected target IP addresses.

    Returns:
    - A dictionary where keys are domain names and values are tuples (is_valid, actual_target).
    """
    results = {}
    for record in dns_records:
        domain = record['name']
        if record['type'] == 'A' and domain in expected_records:
            actual_target = record['content']
            expected_target = expected_records[domain]
            is_valid = (actual_target == expected_target)
            results[domain] = (is_valid, actual_target)
    return results

def write_results_to_csv(results, expected_records, output_file):
    """
    Write validation results to a CSV file.

    Args:
    - results: Dictionary containing validation results.
    - expected_records: Dictionary containing expected target IP addresses.
    - output_file: Path to the output CSV file.
    """
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Domain', 'Expected Target', 'Actual Target', 'Validity'])
        for domain, (is_valid, actual_target) in results.items():
            validity = 'Valid' if is_valid else 'Invalid'
            writer.writerow([domain, expected_records[domain], actual_target, validity])


def main():
    api_token = 'XXX'
    domain = 'XXX'
    input_csv_file = 'dns_entries.csv'
    output_csv_file = 'validation_results.csv'

    cf = authenticate_with_cloudflare(api_token)
    dns_records = fetch_dns_records(cf, domain)
    expected_records = read_dns_entries_from_csv(input_csv_file)
    results = check_dns_records(dns_records, expected_records)
    write_results_to_csv(results, expected_records, output_csv_file)
    print(f"Validation results written to {output_csv_file}")
    
if __name__ == "__main__":
    main()
