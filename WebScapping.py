#robots.txt                 >>>>  checking sites legal allowness for screping.
#py.exe -m pip install bs4  >>>>  for dowlanding beautufile soop.
from bs4 import BeautifulSoup #importing beautifulesoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="super_special">This list item is special.</li>
    <li>This list item is not special.</li>
    <li class="special">This list item is also special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""
soup = BeautifulSoup(html, "html.parser")                   #giving html data to Beautifulsoup and storing the parsed result.
#print(soup.body.div)
#print(soup.find_all("div"))                                #returns list of divs 
#print(soup.find_all(class_="special"))                     #returns list of matching objects.
#print(soup.find_all(attrs={"data-example":"yes"}))         #serching for matching atrabutes.
#print(soup.select("#first"))                               # select using for css search and returns list
#print(soup.select(".special"))                             # class selection

#================================Some Examples
'''
el = soup.select(".special")[0]
print(el.get_text())
print(el.name)
print(el.attrs)
print(soup.find("h3")["data-example"])
'''

#================================ Navigation Examples
#Navigation using for reaching to data by finding closes object and use navigation tool. 
data = soup.body.contents[1].next_sibling.next_sibling
print(data)
data = soup.find(class_="super_special").find_next_sibling(class_="special")
print(data)
data = soup.find(id='first').find_next_sibling().find_next_sibling()
print(data)
data = soup.select("[data-example]")[1].find_previous_sibling()
print(data)