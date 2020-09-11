#!/usr/bin/env python
# -*- coding: utf-8 -*-
# !pip install lxml python-slugify
import re
from lxml import etree
import json
from pathlib import Path
from slugify import slugify


def main():
    authors_works = {}
    work_list = []
    line_counter = 0
    word_counter = 0
    char_counter = 0
    for file in Path("./xml").glob('*'):
        xml_file = str(file)
        try:
            tree = etree.parse(xml_file)
        except etree.ParseError as e:
            pass
        else:
            root = tree.getroot()
            manually_checked = False
            collection_title = root.find(".//title").text
            author = root.find(f".//author")
            author_text = "unknown"
            if author is not None:
                author_text = author.text
            poem_list = root.findall(f".//div1[@type]")
            poem_list2 = root.findall(f".//div2[@type]")
            poem_list.extend(poem_list2)
            for poem_number, poem in enumerate(poem_list):
                poem_lg = poem.find("lg")
                if poem_lg is not None:
                    if author_text == "unknown":
                        poem_parent_head = poem.getparent().find("head")
                        if poem_parent_head is not None:
                            author_text = ''.join(poem_parent_head.itertext())
                            # all poems with 'unknown' author are from bibit000818 file
                    if author_text not in authors_works:
                        authors_works[author_text] = []
                    poem_head = poem.find("head")
                    poem_title = poem_number
                    if poem_head is not None:
                        if poem_head.text is not None:
                            poem_title = poem_head.text
                    stanzas = []
                    line_group_list = poem_lg.findall("lg")
                    if len(line_group_list) == 0:
                        line_group_list = poem.findall("lg")
                    for stanza in line_group_list:
                        lines = []
                        for line in stanza.findall("l"):
                            if line.itertext() is not None:
                                text = re.sub("\s\s+", " ", ''.join(line.itertext()))
                                lines.append({
                                    "verse": text,
                                })
                                line_counter += 1
                                word_counter += len(text.split())
                                char_counter += len(text)
                        if len(lines) > 0:
                            stanzas.append(lines)
                    authors_works[author_text].append({
                        "url": f"https://github.com/linhd-postdata/biblioteca_italiana/blob/master/{xml_file}",
                        "author": author_text,
                        "collection": collection_title,
                        "title": poem_title,
                        "manually_checked": manually_checked,
                        "text": stanzas,
                    })
                    work_list.append(
                        f"{author_text} - {collection_title} - {poem_title}")
    all_works = []
    for author_name, author_works in authors_works.items():
        author_slug = slugify(author_name, separator="_")
        with open(Path("json") / f"{author_slug}.json", "w",
                  encoding='utf-8') as author_json:
            json.dump(author_works, author_json, ensure_ascii=False, indent=4)
            all_works += author_works
    with open("biblitaliana.json", "w", encoding='utf-8') as all_authors:
        json.dump(all_works, all_authors, ensure_ascii=False, indent=4)
    print("Statistics\n----------")
    print("- Authors:", len(authors_works))
    print("- Works:", len(work_list))
    print("- Verses:", line_counter)
    print("- Words:", word_counter)
    print("- Characters:", char_counter)


if __name__ == "__main__":
    main()
