
# ResumeRevealer

This project is designed to extract text from various types of files including text, images, PDFs, DOCX, and HTML documents. It utilizes several libraries such as `pytesseract`, `PIL`, `pdf2image`, `docx`, `textract`, and `spacy` for text extraction and entity recognition from resume files.

## Installation

1. Clone the repository:
   ```bash
   https://github.com/shrut-vanpariya/Mined2024-ResumeRevealer.git
   cd Mined2024-ResumeRevealer
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).

4. Download and install Poppler from [here](http://blog.alivate.com.au/poppler-windows/).

5. Download the pre-trained SpaCy model and place it in the project directory.

## Usage

To use this tool, simply run the `main.py` file with the path to the file you want to extract text from as an argument.

Example:
```bash
python main.py path/to/your/file
```

Supported file formats: `.txt`, `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.pdf`, `.docx`, `.html`, `.htm`.

## Output

The extracted text will be printed to the console along with any recognized entities using SpaCy's named entity recognition.

## Disclaimer

This tool may not be perfectly accurate and may require fine-tuning for specific use cases. Use it at your own discretion.
