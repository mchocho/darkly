# XSS Cookies

If you inspect the website's cookies with your browser, you'll find a cookie with an encrypted value.

## Steps
* Open inspector
* Open the cookies tab

<img src="https://i.imgur.com/3154vWC.png" />

* <a href="https://hashes.com/en/decrypt/hash">MD5 decrypt</a> the value
	<br/>
	68934a3e9455fa72420237eb05902327 --> false
* Open the terminal and run:
```bash
	cd ./Resources
	py md5encode.py true #Outputs "md5 encoded value of str: true -> b326b5062b2f0e69046810717534cb09"
```
* Replace cookie value with b326b5062b2f0e69046810717534cb09
* Refresh the page

## Ways to secure
* Always set cookies to http only, this way the client can't change stored information.
* You should always encrypt data for your cookies with a JWT or something similar.
