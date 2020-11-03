# XSS media 

The form in the feedback page is vulnerable to <a href="https://owasp.org/www-community/attacks/xss/">Cross-site scripting attacks</a>

## Steps
* Go to the <a href="http://192.168.56.102/?page=member">feedback page</a>.
* In the name text input enter
	<br />
	script
* Submit the form.

## Vulnerabilities
* An attacker can inject malicious content into the client's form.

## As a bonus:
* Open the inspector.
* Remove the maxlength attribute from the name input.
* You can add anything you like e.g \<button> \<img /> or \<video> tags.

## Ways to secure
* Always validate and sanitize client input.
