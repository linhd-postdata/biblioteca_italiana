# biblioteca_italiana
This corpus is a subset in XML TEI format of the available poems in the poetry corpus from the Biblioteca Italiana

It contains more than 18000 works from over 159 authors

## XML folder statistics

- Authors: 214
- Works: 25341
- Verses: 1068284
- Words: 7107260
- Characters: 38030425

The file [`biblitaliana.zip`](./biblitaliana.zip) contains the compressed JSON corpus. The format of each entry is as follows:
```json
{
    "url": "https://github.com/linhd-postdata/biblioteca_italiana/blob/master/xml/bibit000213",
    "author": "Dante Alighieri",
    "collection": "Il Fiore",
    "title": "I",
    "manually_checked": false,
    "text": [
        [
            {
                "verse": "Lo Dio d'Amor con su' arco mi trasse",
                "words": [
                    "Lo",
                    "Dio",
                    "d'Amor",
                    "con",
                    "su'",
                    "arco",
                    "mi",
                    "trasse"
                ]
            },
            ...
        ],
        ...
    ]
},
...
```

Folder [`json`](./json) contains the works by author, and [`xml`](./xml) contains the XML TEI version of the text.

The script [`biblioteca_italiana.py`](./biblioteca_italiana.py) was used to build the json files.