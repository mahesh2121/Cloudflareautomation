Cloudflare Automation: DNS Entry Validation

This project aims to automate the validation of DNS entries in Cloudflare, checking whether they are correctly pointing to the expected target IP addresses. It provides a Python script that fetches DNS records from Cloudflare, compares them with the expected targets specified in a CSV file, and generates a validation report.
Features

    Fetch DNS Records: The script connects to the Cloudflare API to fetch all DNS records for a specified domain.
    Read Expected Entries: It reads expected DNS entries (domain names and their corresponding target IP addresses) from a CSV file.
    Check Validity: It compares the fetched DNS records with the expected entries to determine whether they are valid or invalid.
    Generate Report: The script generates a CSV report containing validation results, indicating which DNS entries are valid and which ones are invalid.

Usage

    Clone the Repository:

    bash

git clone https://github.com/yourusername/cloudflare-automation.git

Install Dependencies:

pip install CloudFlare

Prepare CSV File:

Create a CSV file (dns_entries.csv) containing the domain names and their expected target IP addresses. Each row should contain two columns: the domain name and the expected IP address, separated by a comma.

Configure Script:

Open the Python script (cloudflaredns.py) in a text editor and replace the placeholder values with your Cloudflare API token, domain, input CSV file path, and output CSV file path.

Run the Script:

    python cloudflaredns.py

    Review Results:

    After the script completes execution, it will generate a new CSV file (validation_results.csv) containing the validation results. You can review this file to see which DNS records are valid or invalid.

Requirements

    Python 3.x
    CloudFlare Python library (pip install CloudFlare)
    Cloudflare API token with appropriate permissions

Contribution

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.
License

This project is licensed under the MIT License. See the LICENSE file for details.