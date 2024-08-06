import PyPDF2

def extract_pdf_text(file_path):
    """
    This function extracts text from a PDF file using the PyPDF2 library.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF.
    """
    # Open the PDF file in binary read-only mode.
    with open(file_path, 'rb') as file:
        # Create a PDF reader using PyPDF2.
        reader = PyPDF2.PdfReader(file)
        # Initialize an empty string to store the extracted text.
        text = ""
        # Iterate over all the pages in the PDF.
        for page in reader.pages:
            # Extract text from each page and add it to the text string.
            text += page.extract_text()
    # Return the extracted text from the PDF.
    return text