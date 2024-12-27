# Drug-Label OCR

SpeedySui is a Python-based image processing toolkit designed for tasks such as decolorization, scaling, and optical character recognition (OCR).

## Features

- **Image Decolorization**: Convert colored images to grayscale while preserving essential details.
- **Image Scaling**: Resize images to desired dimensions without significant loss of quality.
- **Optical Character Recognition (OCR)**: Extract text from images using advanced OCR techniques.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Decolorization and Scaling](#decolorization-and-scaling)
  - [Optical Character Recognition](#optical-character-recognition)
  - [Image Downloading](#image-downloading)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation

To use SpeedySui, you need to have Python installed on your system. Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/AM-2304/SpeedySui.git
   cd SpeedySui
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Decolorization and Scaling

To decolorize and scale an image, run the following command:

```bash
python Decolorize_Scaling.py <input_image_path> <output_image_path> <scale_factor>
```

- `<input_image_path>`: Path to the input image file.
- `<output_image_path>`: Path where the processed image will be saved.
- `<scale_factor>`: Factor by which to scale the image (e.g., 0.5 for half size).

### Optical Character Recognition

To perform OCR on an image, use the command:

```bash
python OCR.py <input_image_path> <output_text_file>
```

- `<input_image_path>`: Path to the image file from which text will be extracted.
- `<output_text_file>`: Path where the extracted text will be saved.

**Note**: There is an older OCR method available (`OCR (older method- not working on windows).py`), but it may not function on all systems.

### Image Downloading

To download images from a specified source, use:

```bash
python download_images.py <source_url>
```

- `<source_url>`: URL of the image or webpage containing images to download.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request. 

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project does not currently have a specified license. Please check back later for updates.

## Acknowledgements

- Thanks to the original author, my colleague, Divyanshu Vashishth, of the [dvfn19/SpeedySui](https://github.com/dvfn19/SpeedySui) repository for their foundational work.
- Special thanks to the contributor, Vansh Dhar, who have helped enhance this project.

---

For any questions or issues, please open an issue in the repository.
```

Feel free to modify any sections as per your requirements!
