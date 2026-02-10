import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page
import random

def populate():
    view_str = 'views'
    like_str = 'likes'

    python_pages = [
    {'title': 'Official Python Tutorial',
    'url':'http://docs.python.org/3/tutorial/', view_str:'65'},
    {'title':'How to Think like a Computer Scientist',
    'url':'http://www.greenteapress.com/thinkpython/', view_str:'22'},
    {'title':'Learn Python in 10 Minutes',
    'url':'http://www.korokithakis.net/tutorials/python/', view_str:'46'} ]

    django_pages = [{'title':'Official Django Tutorial',
    'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/', view_str:'61'},
    {'title':'Django Rocks',
    'url':'http://www.djangorocks.com/', view_str:'8'},
    {'title':'How to Tango with Django',
    'url':'http://www.tangowithdjango.com/', view_str:'93'} ]

    other_pages = [
    {'title':'Bottle',
    'url':'http://bottlepy.org/docs/dev/', view_str:'35'},
    {'title':'Flask',
    'url':'http://flask.pocoo.org', view_str:'72'} ]

    cats = {'Python': {'pages': python_pages},
    'Django': {'pages': django_pages},
    'Other Frameworks': {'pages': other_pages} }

    cat_stats = {'Python': {view_str: 128, like_str: 64},
             'Django': {view_str: 64, like_str: 32 },
             'Other Frameworks': {view_str: 32, like_str: 16}}

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_stats[cat][view_str], cat_stats[cat][like_str])

        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p[view_str])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()