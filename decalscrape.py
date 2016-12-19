import urllib.request, re

# Find Decal urls
with urllib.request.urlopen('http://www.decal.org/courses') as response:
    html = response.read()
html = str(html)
z = re.findall('href=.(\d\d\d\d).', html)

# Write obtained emails to a local file
y = []
for url in z:
    with urllib.request.urlopen('http://www.decal.org/courses/'+url) as response:
        html = response.read()
    html = str(html)
    y += [re.search(r'Course Contact:</strong> ([\w .()-]+)', html).group()]
j = []
for email in y:
    k = re.sub('\w+(.AT.)\w+', '@', email) # Email formatting
    j += [k]
file = open('Decal Emails','w')
for email in j:
    file.write(email + '\n')
file.close()

# (Alternative) Print obtained emails 
# for url in z:
    # with urllib.request.urlopen('http://www.decal.org/courses/' + url) as response:
        # html = response.read()
    # html = str(html)
    # y = re.search(r'<h2>([\w :]+)</h2>',html)
    # if y:
        # print(y.group(1))
    # else:
        # print('\n')

