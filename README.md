# abcdp_to_vcf
Python script to convert contact information from Address Book Backups (`.abcdp`) to vCard format (`.vcf`). 

It is designed to work on macOS, where these types of plist files are commonly used for storing contact information.

## Features

- Converts multiple `.abcdp` files in a batch.
- Extracts information such as names, job titles, organizations, notes, phone numbers, email addresses, URLs, and addresses.
- Handles empty fields gracefully.

## Requirements

- Python 3
- macOS (due to the nature of `.abcdp` files)

## Usage

1. Clone or download this repository to your local machine.
2. Replace the `input_folder` and `output_folder` paths in the script with your desired directories.
3. Run the script using Python
