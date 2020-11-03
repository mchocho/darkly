# Unsecure File Upload

In the file upload page we can upload any file even if it isn't of the requested file type.

## Steps
* Open your terminal and run:
```bash
	py uploadFile.py http://192.168.56.102/index.php\?page=upload# 
```

## Vulnerabilites
* An attaker can upload malicious files to the server.

## Ways to secure
* Validate the uploaded file type on the server.
