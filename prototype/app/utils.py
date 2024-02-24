from script import extract_text,extract_key_value_pairs


def response(pdf_or_image_path,doc_type):

    text=extract_text(pdf_or_image_path)
    if text==None:
        return text
        
    # Extract key-value pairs from the extracted text
    result = extract_key_value_pairs(text,doc_type)

    return result