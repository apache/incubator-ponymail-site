#!/usr/bin/python3

import markdown, codecs, os, sys, re, time


template = ""
with open("template.html", "r") as tmpl:
    template = tmpl.read()
    tmpl.close()
    
def runDir(path):
    files = os.listdir(path)
    for f in files:
        if os.path.isdir('%s/%s' % (path, f)):
            runDir('%s/%s/' % (path, f))
        elif f.find(".md") != -1:
            print("Processing %s" % f)
            input_file = codecs.open("%s/%s" % (path, f), mode="r", encoding="utf-8")
            outfile = f.replace(".md", ".html").lower().replace("//", "/")
            outfile = path.replace("markdown", "", 1) + outfile
            text = input_file.read()
            text = re.sub(r"~~~([\s\S]+?)~~~", "<pre>\\1</pre>", text, flags=re.MULTILINE)
            text = re.sub(r"([A-Z/]+)\.md", lambda x: x.group(1).lower() + ".html", text, flags =re.MULTILINE)
            html = markdown.markdown(text)
            html = template.replace("%CONTENT%", html, 1)
            print("Writing %s..." % outfile)
            bpath = os.path.dirname(outfile)
            if not os.path.isdir("../content/" + bpath):
                print("Making dir %s" % bpath)
                os.mkdir("../content/%s" % bpath)
            with open('../content/%s' % outfile, "w") as out:
                out.write(html)
                out.close()

runDir('markdown')
print("All done!")