import urllib.request,re

# Find Decal urls
with urllib.request.urlopen('https://decal-ucb.herokuapp.com/courses') as response:
    html = response.read()
html = str(html)
z = re.findall('href=./courses/(\d+)', html)
print(z)

# Extract emails
y = []
for url in z:
    with urllib.request.urlopen('https://decal-ucb.herokuapp.com/courses/'+url) as response:
        html = response.read()
    html = str(html)
    match = re.search(r'[\da-zA-Z\-\._]+@[\da-zA-Z\-\._]+', html)
    if match:    
        y.append(match.group())

# Output to file 
file = open('DecalEmails.txt','w')
for email in y:
    file.write(email + '\n')
file.close()
