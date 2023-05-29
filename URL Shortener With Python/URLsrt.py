import pyshorteners

# Initialize the URL shortener
shortener = pyshorteners.Shortener()

# Long URL to be shortened
long_url = 'https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/KPMG%20AU/m7W4GMqeT3bh9Nb2c_' \
           'KPMG%20AU_vuX7y7cLC2JkqAaoD_1679297411981_completion_certificate.pdf'

# Shorten the URL
short_url = shortener.tinyurl.short(long_url)

# Print the shortened URL
print("Shortened URL:", short_url)
