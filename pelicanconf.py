AUTHOR = 'sanjay'
SITENAME = 'Sanjay Krishna H'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'
THEME = 'themes/custom-theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_TEMPLATE = 'article_custom.html'

STATIC_PATHS = ['static/css']
EXTRA_PATH_METADATA = {
    'theme/css/main.css': {'path': 'theme/css/main.css'},
    'theme/css/bookshelf.css': {'path': 'theme/css/bookshelf.css'},
    'theme/css/blog.css': {'path': 'theme/css/blog.css'},
    'theme/css/links.css': {'path': 'theme/css/links.css'},
    'theme/css/work.css': {'path': 'theme/css/work.css'}
}

ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

MENUITEMS = [
    ('Home', '/'),
    ('Bookshelf', '/bookshelf.html'),
    ('Blog', '/blog.html'),
    ('Work', '/work.html'),
    ('Links', '/links.html')
]

TEMPLATE_PAGES = {
    'bookshelf.html': 'bookshelf.html',
    'blog.html': 'blog.html',
    'work.html': 'work.html',
    'links.html': 'links.html',
}


# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

ARTICLE_EXCLUDES = ['pages']

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
