playlist ={
    "Title":"Cat vibe",
    "Author":"Bermel",
    "songs":[
        {"name":"cat1", "artist":["meoww"],"duration":5},
        {"name":"cat2", "artist":["djcat","djorange"],"duration":5.7},
        {"name":"cat3", "artist":["smelly"],"duration":2},
        {"name":"cat4", "artist":["meow1","meow"],"duration":6.25},
    ]
}
total_lenght=0
for song in playlist["songs"]:
    total_lenght+=song["duration"]
print(total_lenght)