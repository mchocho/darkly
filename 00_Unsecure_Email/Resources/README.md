# Unsecure Email

In the recover password form there's a hidden input with a default value.

## Steps

* Go to the <a href="http://192.168.56.102/?page=recover">recover password page</a>.
* Open inspector (CTRL + SHIFT + I).
<img src="https://i.imgur.com/pyn1Mef.png" />

* Rename the hidden input type to email.
* Change the email value.
* Submit the form.

## Vulnerablilities
* An attacker can send an email with a script asking for a password reset (email spoofing).
* Change the address and get login credentials from the user.

## Ways to secure
* Don't store private information on the client.
* Validate all email addresses on the server.
