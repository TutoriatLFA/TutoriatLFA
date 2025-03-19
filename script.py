#!/usr/bin/env python3

import os
import argparse
import PyPDF2
from pathlib import Path


def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file and return it."""
    try:
        # Open the PDF file in read-binary mode
        with open(pdf_path, "rb") as pdf_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Extract text from all pages
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() + "\n\n"

            print(f"Successfully extracted text from {pdf_path}")
            return text
    except Exception as e:
        print(f"Error processing {pdf_path}: {str(e)}")
        return None


def process_directory(input_dir, output_file):
    """Recursively process all PDF files in the input directory."""
    # Get all PDF files in the directory and subdirectories
    pdf_files = list(Path(input_dir).rglob("*.pdf"))

    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(os.path.abspath(output_file)), exist_ok=True)

    # Open the output file
    with open(output_file, "w", encoding="utf-8") as out_file:
        # Process each PDF file
        successful = 0
        failed = 0
        for pdf_path in pdf_files:
            # Write separator and file name
            out_file.write(f"\n\n{'='*80}\n")
            out_file.write(f"FILE: {pdf_path}\n")
            out_file.write(f"{'='*80}\n\n")

            # Extract and write text
            text = extract_text_from_pdf(pdf_path)
            if text:
                out_file.write(text)
                successful += 1
            else:
                out_file.write("[ERROR: Text extraction failed for this file]\n")
                failed += 1

    print(f"\nProcessing complete.")
    print(f"Total PDF files: {len(pdf_files)}")
    print(f"Successfully processed: {successful}")
    print(f"Failed: {failed}")
    print(f"Output saved to: {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract text from PDF files in a directory and save to a single file."
    )
    parser.add_argument("input_dir", help="Directory containing PDF files")
    parser.add_argument(
        "--output-file",
        default="pdf_extracted_text.txt",
        help="Output file to save all extracted text",
    )
    args = parser.parse_args()

    process_directory(args.input_dir, args.output_file)
