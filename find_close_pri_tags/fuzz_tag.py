#!/usr/bin/env python
# -*- coding: utf-8 -*
'''
Created on 2019-4-28

@author: q

'''
import sys

def fuzz_tags(help_tag="<img src=\"#/?", finame = "tags.txt", foname = "img"):
    f = open(foname, "w")
    f.write("<html><head><title>show tags</title></head><body>\n")
    t = open(finame, "r")
    # read all tags in "tags.txt"
    for tag in t.readlines():
        tag = tag.strip()
        start = "<"+ tag + ">"
        end = "</" + tag + ">"
        if tag == "!--" :
            start = "<" + tag
            end = "-->"
        
        # output in the format : <tag><img src="</tag>scripts..." /></tag>
        # and write to show.html
        f.write(start)
        #f.write("<img src=\"//x.xx/?"+end)
        f.write(help_tag + end)
        f.write("<script> console.log('" + tag + "')</script>\" />")
        f.write(end + "<p>&nbsp;<p>\n")
    t.close()
    f.write("</body></html>")
    f.close()
    pass

def fuzz_tags_with_img(help_tag="<img src=\"#/?", finame = "tags.txt"):
    fuzz_tags(help_tag="<img src=\"#/?", finame=finame, foname="show_img.html")

def fuzz_tags_with_svg(finame = "tags.txt"):
    fuzz_tags(help_tag="<svg version=\"#", finame=finame, foname="show_svg.html")
    pass

if __name__ == '__main__':
    if len(sys.argv) ==2 :
        fuzz_tags_with_img(sys.argv[1])
    else:
        fuzz_tags_with_img()
    pass
