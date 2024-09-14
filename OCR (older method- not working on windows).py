import requests
import pandas as pd
from PIL import Image
from io import BytesIO
import pytesseract

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/mnt/c/Program""Files/Tesseract-OCR/tesseract.exe'


# Adjust if necessary


def download_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return Image.open(BytesIO(response.content))
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
        return None


def perform_ocr(image):
    if image:
        text = pytesseract.image_to_string(image)
        return text
    return None


def process_images_from_csv(input_csv, output_csv):
    # Read the image links from the input CSV
    df = pd.read_csv(input_csv)

    # Ensure the 'image_link' column exists
    if 'image_link' not in df.columns:
        print("Error: 'image_link' column not found in the CSV.")
        return

    # List to store results
    results = []

    # Process each image link
    for index, row in df.iterrows():
        image_url = row['image_link']
        print(f"Processing image: {image_url}")

        image = download_image(image_url)
        extracted_text = perform_ocr(image)

        # Append result to the list
        results.append({'image_link': image_url, 'extracted_text': extracted_text})

    # Create a DataFrame from the results
    results_df = pd.DataFrame(results)

    # Write the results to the output CSV
    results_df.to_csv(output_csv, index=False)
    print(f"Results saved to {output_csv}")


if __name__ == "__main__":
    input_csv = '/mnt/c/Users/akhil/Downloads/ch/st/dataset/test.csv'  # Path to your input CSV file
    output_csv = '/mnt/c/Users/akhil/Downloads/ch/st/o.csv'  # Output CSV file

    process_images_from_csv(input_csv, output_csv)
