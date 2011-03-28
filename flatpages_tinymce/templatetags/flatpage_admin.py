import os
import simplejson

# Settings
from django.conf import settings
import tinymce.settings
from flatpages_tinymce import settings as local_settings

from django import template
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

register = template.Library()


@register.simple_tag(takes_context=True)
def flatpage_media(context):
    is_admin = ('user' in context
                and context['user'].is_superuser
                and local_settings.USE_FRONTED_TINYMCE)
    if not is_admin:
        return ""

    if context.render_context.get("flatpage_media_loaded", None):
        return ""

    media_url = settings.MEDIA_URL

    mce_config = tinymce.settings.DEFAULT_CONFIG.copy()
    mce_config['mode'] = 'exact'
    mce_config['elements'] = "%s_body" % local_settings.DIV_PREFIX
    mce_config['strict_loading_mode'] = 1

    media = {
        'js': [
            os.path.join(media_url, tinymce.settings.JS_URL),
            os.path.join(local_settings.MEDIA_URL, "edit.js"),
            ],
        'css': [
            os.path.join(local_settings.MEDIA_URL, 'edit.css'),
            ],
        }
    if tinymce.settings.USE_FILEBROWSER:
        mce_config['file_browser_callback'] = "djangoFileBrowser"
        media['js'].append(reverse('tinymce-filebrowser'))

    output_chunks = []
    for script in media['js']:
        output_chunks.append('<script type="text/javascript" src="%s" ></script>' % script)

    for stylesheet in media['css']:
        output_chunks.append('<link rel="stylesheet" href="%s" type="text/css" media="screen" />' % stylesheet)
    params = {
        'tinymce_config': mce_config,
        'prefix': local_settings.DIV_PREFIX,
        'url': reverse('admin:flatpages_ajax_save'),
        'error_message': _(u'Error while saving. Please try again.'),
        'csrf_token': unicode(context['csrf_token']),
        }
    output_chunks.append('<script type="text/javascript">$_STATICPAGES_INIT(%s)</script>' % simplejson.dumps(params))

    context.render_context["flatpage_media_loaded"] = 1
    return mark_safe("\n".join(output_chunks))


@register.inclusion_tag("flatpages_tinymce/_contentedit.htm", takes_context=True)
def flatpage_admin(context, flatpage):
    is_admin = 'user' in context and context['user'].is_superuser and local_settings.USE_FRONTED_TINYMCE
    media = flatpage_media(context)
    output_content = mark_safe(flatpage.content)
    return {
        'media': media,
        'page_id': flatpage.id,
        'admin': is_admin,
        'prefix': local_settings.DIV_PREFIX,
        'content': output_content,
        }
