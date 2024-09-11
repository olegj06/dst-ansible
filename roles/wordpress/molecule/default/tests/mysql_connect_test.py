import testinfra

def test_wordpress_has_access_to_database(host):
    # Get the IP addresses of the Molecule containers
    #wordpress_ip = os.getenv('MOLECULE_INSTANCE_IP')
    #database_ip = os.getenv('MOLECULE_DATABASE_INSTANCE_IP')
    wordpress_ip = "172.17.0.3"
    database_ip = "172.17.0.2"
    # Create Testinfra hosts using the container IP addresses
    wordpress_host = testinfra.get_host('ssh://' + wordpress_ip)
    database_host = testinfra.get_host('ssh://' + database_ip)
    
    # test pour determiner l'accès a la base de données
    assert wordpress_host.socket("tcp://{}:3306".format(database_ip)), "Wordpress n'a pas accès a la base de données"
