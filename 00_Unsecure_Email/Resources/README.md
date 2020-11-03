# Unsecure Email

In the recover password form there's a hidden input with an default value.

## Steps

Go to URL
* Open inspector (CTRL + SHIFT + I)
<img src="https://i.imgur.com/pyn1Mef.png" />

* Rename the hidden input type to email
* Change the email
* Submit the form

## Vulnerablilities
* Send an email with a script asking for a password reset (email spoofing).
* Change the address and get login credentials from the user.

## Ways to secure
* Don't store private information on the client
* Validate all email addresses on the server
