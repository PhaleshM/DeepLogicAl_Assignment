import pytesseract
from PIL import Image
import csv
import os
from pdf2image import convert_from_path
from extract_key_value import generate
import re
import ast


def extract_text_from_pdf(pdf_path):
    pages = convert_from_path(pdf_path)
    text=''
    for page in pages:
        text+=pytesseract.image_to_string(page,config='--psm 1')

    return text

def extract_text_from_image(image_path):
    with Image.open(image_path) as img:
        text = pytesseract.image_to_string(img,config='--psm 1')
    return text

def extract_key_value_pairs(text,doc_type):
    result_string=generate(text,doc_type)
    # print(result_string)
    if doc_type=='t':
        result_string=result_string.replace("\n"," ")
        # res= re.sub("\\`'", '', result_string)
        dic=ast.literal_eval(result_string.split("=")[1])
        return dic
    
    return result_string
        

def save_to_csv(data, csv_file_path):
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)

def save_to_text_file(text, file_path):
    with open(file_path, 'w') as file:
        file.write(text)

def extract_text(pdf_or_image_path):

    if pdf_or_image_path.lower().endswith(('.pdf')):
        text = extract_text_from_pdf(pdf_or_image_path)
    elif pdf_or_image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        text = extract_text_from_image(pdf_or_image_path)
    else:
        return None

    return text

def main(pdf_or_image_path,doc_type):

    text=extract_text(pdf_or_image_path)
    if text==None:
        print("File not supported")
        exit(1)

    # Extract key-value pairs from the extracted text
    response = extract_key_value_pairs(text,doc_type)

    if doc_type=="t":
        save_to_csv(response,'response.csv')
    else:
        save_to_text_file(response,"response.txt")



if __name__ == "__main__":
    

    pdf_or_image_path="Sample Files/sample2.jpg"
    doc_type="t"    # for table,invoice->t, text->T
    main(pdf_or_image_path,doc_type)
