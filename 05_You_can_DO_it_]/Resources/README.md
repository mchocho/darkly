#Unsecure Page Requests

If you mess around with page parameter in the URL address bar, the website will respond with alerts. It's also evident that pages are included without validating or sanitizing the input.
	
## Table of Contents

- [Steps](#Steps)
- [Vulnerablities](#Vulnerabilities)
- [Ways to secure](#Ways to secure)

### Steps

Go to the <a href="http://192.168.56.102/?page=member">member page</a> or <a href="http://192.168.56.102/?page=survey">server page</a> (Any page except the home page).

In URL address bar keep appending '../' to the page parameter until the alert reads 'You can DO it!!! :]'.

Then append 'etc/passwd' to the page query.

#### Vulnerabilities

An attacker could include and view a file sensitive information such as auth accounts or credit card information.

##### Ways to secure
Always validate and sanatize client input
Never include files directly using client input, use prepared procedures instead.
