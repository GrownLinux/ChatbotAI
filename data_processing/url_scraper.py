import requests
from bs4 import BeautifulSoup


def scrape_url(url):
    """
    Esta función recibe una URL, realiza una solicitud GET a dicha URL,
    analiza el contenido HTML de la respuesta utilizando BeautifulSoup
    y devuelve el texto extraído de la página web.
    
    Parámetros:
    url (str): La URL de la página web que se va a raspar.
    
    Devuelve:
    str: El texto extraído de la página web.
    """
    response = requests.get(url)  # Realiza una solicitud GET a la URL
    soup = BeautifulSoup(response.text, 'html.parser')  # Analiza el contenido de la respuesta
    return soup.get_text()  # Devuelve el texto extraído