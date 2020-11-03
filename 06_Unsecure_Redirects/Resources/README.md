# Unsecure Redirects

The social media links in the footer component redirect to their respective platforms directly on the anchor tag.

## Steps
* Open inspector
* Change redirect parameter in the href to anything

## Vulnerabilities
* An attacker can spoof the redirect header to prevent the web server from collecting accurate data

<img src="https://i.imgur.com/GpDX4cI.png" />

## Ways to secure
* Don't redirect on the cient side
