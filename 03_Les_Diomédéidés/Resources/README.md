# Unsecure Referer

If you click the link around copyright text in the footer you will be redirected to a page that provides information about albatross seabirds and plays delightful music
<br />
If you further inspect the page you'll notice the comments:
* You must be cumming from: "https://www.nsa.gov" to go to the next step
* Let's use this browser : "ft\_bornToSec". It will help you a lot

## Steps
* Open your terminal and run:
```bash
curl --referer "https://www.nsa.gov/" --user-agent "ft_bornToSec" http://192.168.56.102/\?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c | grep "flag"
```

## Ways to secure
* Information from headers may often be unreliable because they can be tampered.
* You can either exclude the Referer header in the .htaccess file or use it to compare with 3rd-party analytics.
