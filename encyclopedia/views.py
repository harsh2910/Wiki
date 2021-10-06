from django.shortcuts import render
from random import randint
from . import util
from markdown2 import Markdown

markdowner = Markdown()

def index(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        if title in (util.list_entries()):
            return render(request, "encyclopedia/create.html",{
                "message": "Page already exists"
            })
        util.save_entry(title, content)
        content = util.get_entry(title)
        return render(request, "encyclopedia/title.html", {
        "content": markdowner.convert(content),
        "title": title
        })

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/not_found.html", {
        "title": "Page not found"
        })

    return render(request, "encyclopedia/title.html", {
        "content": markdowner.convert(content),
        "title": title
    })

def create(request):
    return render(request, "encyclopedia/create.html")


def random(request):
    entries = util.list_entries()
    title = entries[randint(0, len(entries)-1)]
    content = util.get_entry(title)
    return render(request, "encyclopedia/title.html", {
        "content": markdowner.convert(content),
        "title": title
    })

def edit(request):
    title = request.POST["title"]
    content = request.POST["content"]
    util.save_entry(title, content)
    return render(request, "encyclopedia/title.html", {
        "content": markdowner.convert(content),
        "title": title
    })

def editing(request):
    title = request.POST["title"]
    content = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
    })

def search(request):
    searchquery = request.GET["q"].lower()
    entries = util.list_entries()
    files=[filename for filename in entries if searchquery in filename.lower()]

    if len(files) == 0:
        return render(request, "encyclopedia/search_result.html")

    elif len(files) == 1 and files[0].lower() == searchquery.lower():
        title = files[0]
        content = util.get_entry(title)
        return render(request, "encyclopedia/title.html", {
        "content": markdowner.convert(content),
        "title": title
        })
    
    else:
        title = [filename for filename in files if searchquery.lower() == filename.lower()]

        if len(title) > 0:
            return render(request, "encyclopedia/title.html", {
            "content": util.get_entry(title[0]),
            "title": title
            })
        else:
            return render(request, "encyclopedia/index.html", {
        "entries": files
        })
