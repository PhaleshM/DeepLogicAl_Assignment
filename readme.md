# DeepLogicaAl_Assignment

## Overview
This project, named DeepLocaAl_Assignment, is designed to address the requirements outlined in the Assignment: PDF Data Extraction and Rapid Prototyping. The project contains a Django application called `prototype`, which facilitates both PDF data extraction and rapid prototyping functionalities.

### Part 1: Data Extraction
For data extraction, the `prototype` main directory includes `script.py` and `extract_key_value.py`. These scripts are intended for extracting data from PDF files. To execute the extraction process, follow these steps:
1. Adjust the file path and document type parameters in `script.py`.
2. Run `script.py`.

To handle scanned documents in PDF format, the project utilizes the `pdf2image` library alongside `PIL`. Furthermore, data extraction is facilitated by `tesseract-ocr` and `pytesseract`. After processing and manipulating the data, the tabular data is saved in `response.csv`, and the textual data is saved in `response.txt`.

### Part 2: Rapid Prototyping
The rapid prototyping functionality largely mirrors the functionalities present in `script.py`. The `upload` function accepts a file and toggle from the POST request and renders the processed data.

## Challenges
During the development process, several challenges were encountered and overcome:
1. **Scanned Document PDF**: Initially, the project faced issues with extracting images from scanned document PDFs due to noise. This was resolved by using `pdf2image`.
2. **Prompting**: Extracting meaningful text from the data required experimentation with various prompts, with approximately 25 different prompts being tested.
3. **Data Extraction**: The data extraction process proved to be the most challenging aspect of the project. Despite spending significant time on training, prompting, and extraction, the desired results were achieved with lowered expectations. Given more time, improvements could be made in this area.

## Installation
To set up and run the project, follow these steps:
1. Clone the project repository.
2. Navigate to the project directory.
3. Create a virtual environment.
4. Install the dependencies listed in `requirements.txt`.
5. Install `tesseract` from [here](https://tesseract-ocr.github.io/tessdoc/Installation.html).
6. Install `Poppler` from [here](https://github.com/oschwartz10612/poppler-windows?tab=readme-ov-file).
7. Create a `.env` file and save the Gemini API key obtained from [here](https://aistudio.google.com/).
8. Run `python manage.py makemigrations` followed by `python manage.py migrate` in the terminal.
9. Finally, execute `python manage.py runserver` to start the server.

