-----
About
-----

**django-flatpages-tinymce** provides on-site editing of "Flat Pages" with minimal
impact on the rest of code.

django-flatpages-tinymce is available under the MIT license.


-----
Usage
-----

First of all, you need to have **django-flatpages-tinymce**  and
**django-tinymce** installed; for your convenience, recent
versions should be available from PyPI.

::

        pip install django-tinymce django-flatpages-tinymce

To use, just add these applications to your INSTALLED_APPS **after**
**django.contrib.flatpages** app::

	INSTALLED_APPS = (
	    ...
            'django.contrib.staticfiles',
            'django.contrib.flatpages',
            ...
            'tinymce',
            'flatpages_tinymce',
	)

As instructed by the **flatpages** guide, add this to your MIDDLEWARE_CLASSES::

        MIDDLEWARE_CLASSES = (
            ...
            'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
        )

Remember that this little addition to your **urls.py** is required
by **django-tinymce**::

        urlpatterns = patterns('',
            ...
            (r'^tinymce/', include('tinymce.urls')),
            ...
        )

Finally create the tables for **flatpages** and install the JS/CSS files using

::

        ./manage.py syncdb
        ./manage.py collectstatic

If you want on-site editing of templates, you must edit **flatpages**
templates: change {{flatpage.content} to {% flatpage_admin flatpage %}
from flatpage_admin template library. So

::

       {% extends "base.html" %}
       {% block body %}
       {% endblock %}
       {% block body %}
       <h1>{{flatpage.title}}</h1>
       {{flatpage.content}}
       {% endblock %}

will become

::

       {% extends "base.html" %}
       {% load flatpage_admin %}
       {% block body %}
       <h1>{{flatpage.title}}</h1>
       {% flatpage_admin flatpage %]
       {% endblock %}


If you are bothered with <script>/<link> tags, being inserted in <body> tag and your
template has something like {% block extrahead %}, you can move all plugin media in head,
using {% flatpage_media %} tag.

::

       {% extends "base.html" %}
       {% block extrahead %}
       {% flatpage_media %}
       {% endblock %}
       {% block body %}
       <h1>{{flatpage.title}}</h1>
       {% flatpage_admin flatpage %}
       {% endblock %}

--------
Settings
--------


Default settings are in flatpages_tinymce.settings.py file. Also, you can
override them in site-wide settings.py file. The main of them are:

  * FLATPAGES_TINYMCE_ADMIN (default True) - use TinyMCE widget in admin area
  * FLATPAGES_TINYMCE_FRONTEND (default True) - use TinyMCE widget in frontend
  * FLATPAGES_TEMPLATE_DIR (default: TEMPLATE_DIRS[0] + 'flatpages') - directory where
    flatpages templates are placed
  * FLATPAGES USE_MINIFIED (defalut: not settings.DEBUG) - use minified versions of JS/CSS

Further, you will want to change default settings of TinyMCE Editor.

::

 	 TINYMCE_DEFAULT_CONFIG = {
	     # custom plugins
             'plugins': "table,spellchecker,paste,searchreplace",
	     # editor theme
	     'theme': "advanced",
	     # custom CSS file for styling editor area
             'content_css': MEDIA_URL + "css/custom_tinymce.css",
             # use absolute urls when inserting links/images
             'relative_urls': False,
         }

-------
Changes
-------


Changes in version 0.1
======================

  * First public release.
