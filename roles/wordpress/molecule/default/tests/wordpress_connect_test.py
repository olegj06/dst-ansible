import requests
import os

def test_wordpress_page_accessible(host):
    # Get the IP address of the Molecule container
   # wordpress_ip = os.getenv('MOLECULE_INSTANCE_IP')
    wordpress_ip = "172.17.0.3"
    # Create the URL using the container IP address
    url = "http://{}/".format(wordpress_ip)
    
    # Send a GET request to the Wordpress container
    response = requests.get(url)
    
    # Check if the response status code is 200
    assert response.status_code == 200  , "Wordpress page n'est pas accessible"
