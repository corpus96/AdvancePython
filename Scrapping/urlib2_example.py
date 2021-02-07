from urllib.request import urlopen

f = urlopen('http://www.python.org')

print(f.read(100))

response = urlopen('http://www.google.com')

for line in response:
    print(line.rstrip())