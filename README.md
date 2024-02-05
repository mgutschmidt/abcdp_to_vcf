# abcdp_to_vcf
Python script to convert contact information from Mac OS Address Book Backups (`.abcdp`) to vCard format (`.vcf`). 

Problem is, you can't reimport `.abcdp` files into Contacts as mentioned here: 
  - https://discussions.apple.com/thread/254511950?sortBy=best
  - https://discussions.apple.com/thread/8239433?sortBy=best
  - https://discussions.apple.com/thread/250532928?sortBy=best

It is designed to work on macOS, where these types of plist files are commonly used for storing contact information.

## Features

- Converts multiple `.abcdp` files in a batch.
- Extracts information such as names, job titles, organizations, notes, phone numbers, email addresses, URLs, and addresses.
- Handles empty fields.

## Requirements

- Python 3
- macOS (due to the nature of `.abcdp` files)

## Usage

1. Download this Script to your local machine.
2. Replace the `input_folder` and `output_folder` paths in the script with your desired directories.
3. Run the script using Python

## Disclaimer

This script is provided as-is, and it might require modifications to work
