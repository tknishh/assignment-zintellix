import requests
from bs4 import BeautifulSoup


def scrape_gaming_chairs(url):
  """Scrapes product information from the Flipkart gaming chair search page.

  Args:
    url: The URL of the Flipkart gaming chair search page.

  Returns:
    A list of dictionaries, where each dictionary contains information for a product,
    or None if an error occurs.
  """

  try:
    response = requests.get(url)
    response.raise_for_status()  
    html_content = response.content
  except requests.exceptions.RequestException as e:
    print(f"Error: An error occurred while making the request - {e}")
    return None

  try:
    soup = BeautifulSoup(html_content, 'html.parser')
  except Exception as e:
    print(f"Error: An error occurred while parsing the HTML - {e}")
    return None

  # Find product elements based on current Flipkart structure
  products = soup.find_all('div', class_='_4ddWXP') 

  # Initialize empty list to store product information
  product_info = []

  for product in products:
    product_data = {}

    # Get product name
    try:
      name_element = product.find('a', class_='s1Q9rs')
      product_data['Name'] = name_element.text.strip() if name_element else None
    except Exception as e:
      print(f"Error: An error occurred while finding product name - {e}")
      continue  

    # Get product price
    try:
      price_element = product.find('div', class_='_30jeq3')
      product_data['Price'] = price_element.text.strip() if price_element else None
    except Exception as e:
      print(f"Error: An error occurred while finding product price - {e}")
      continue  

    # Extract rating information
    try:
      rating_element = product.find('div', class_='_3LWZlK')
      product_data['Rating'] = rating_element.text.strip() if rating_element else None
    except Exception as e:
      print(f"Error: An error occurred while finding product rating - {e}")
      continue  

    # Append product information to the list
    product_info.append(product_data)

  return product_info


# Set the URL for Flipkart's gaming chair search page
url = "https://www.flipkart.com/q/gaming-chair"

# Scrape product information
products = scrape_gaming_chairs(url)

# Handle the case where no products were scraped 
if not products:
  print("Error: No products were scraped. Check for website changes or internet connectivity issues.")
else:
  for i, product in enumerate(products):
    print(f"Product {i+1}:")
    for key, value in product.items():
      print(f"\t{key}: {value}")
    print()
