import os

# Get the value of MOLECULE_INSTANCE_IP
wordpress_ip = os.getenv('MOLECULE_INSTANCE_IP')

# Print the value to see it
print("MOLECULE_INSTANCE_IP:", wordpress_ip)

