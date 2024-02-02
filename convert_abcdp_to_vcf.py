import plistlib
import os
import glob

def extract_phone_numbers(plist_data):
    # Extracts phone numbers and their labels from the plist data.
    phone_data = plist_data.get("Phone", {})
    labels = phone_data.get("labels", [])
    values = phone_data.get("values", [])
    return [(label.strip("_$!<>&!$_"), value) for label, value in zip(labels, values)]

def extract_addresses(plist_data):
    # Extracts address data from the plist data.
    address_data = plist_data.get("Address", {})
    return [dict(City=addr.get("City", ""), Country=addr.get("Country", ""), ZIP=addr.get("ZIP", "")) 
            for addr in address_data.get("values", [])]

def plist_to_vcard(plist_file):
    # Converts a single plist file to a vCard format.
    with open(plist_file, 'rb') as file:
        plist_data = plistlib.load(file)

    info = {
        "First": plist_data.get("First", ""),
        "Last": plist_data.get("Last", ""),
        "Title": plist_data.get("Title", ""),
        "JobTitle": plist_data.get("JobTitle", ""),
        "Organization": plist_data.get("Organization", ""),
        "Note": plist_data.get("Note", ""),
        "UID": plist_data.get("UID", ""),
        "Phone": extract_phone_numbers(plist_data),
        "Email": next(iter(plist_data.get("Email", {}).get("values", [])), ""),
        "URLs": next(iter(plist_data.get("URLs", {}).get("values", [])), ""),
        "Addresses": extract_addresses(plist_data)
    }

    vcard = f"""
    BEGIN:VCARD
    VERSION:3.0
    N:{info['Last']};{info['First']};;{info['Title']};
    FN:{info['First']} {info['Last']}
    TITLE:{info['JobTitle']}
    ORG:{info['Organization']}
    NOTE:{info['Note']}
    UID:{info['UID']}
    EMAIL:{info['Email']}
    URL:{info['URLs']}
    """

    for label, number in info["Phone"]:
        vcard += f"TEL;TYPE={label}:{number}\n"

    for address in info["Addresses"]:
        vcard += f"ADR;TYPE=WORK:;;{address['City']};{address['Country']};{address['ZIP']}\n"

    vcard += "END:VCARD"
    return '\n'.join(line.strip() for line in vcard.strip().split('\n'))

def convert_folder_to_vcards(input_folder, output_folder):
    # Converts all plist files in the input folder to vCard format and saves them in the output folder.
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for plist_file in glob.glob(os.path.join(input_folder, '*.abcdp')):
        vcard = plist_to_vcard(plist_file)
        output_file = os.path.join(output_folder, os.path.basename(plist_file).replace('.abcdp', '.vcf'))
        with open(output_file, 'w', encoding='utf-8') as file: 
            file.write(vcard)

# Paths to the input folder containing plist files and the output folder for vCards
input_folder = '/path/to/input/folder'  # Change this to your input folder
output_folder = '/path/to/output/folder'  # Change this to your output folder

convert_folder_to_vcards(input_folder, output_folder)
