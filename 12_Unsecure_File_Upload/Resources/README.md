# Unsecure File Upload

In the file upload page we can upload any file that isn't the requested file type.

## Table of Contents

- [Steps](#Steps)
- [Vulnerabilities](#Vulnerabilities)
- [Ways to secure](#Ways to secure)

### Steps
* Open terminal
* Run
```bash
	py uploadFile.py http://192.168.56.102/index.php\?page=upload# 
```

#### Vulnerabilites
An attaker can upload malicious files to the server.

#### Ways to secure
Validate the uploaded file type on the server.
