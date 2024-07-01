import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def convert_hyperlinks(value):
    # Pattern to match [HYPERLINK: url] and [HYPERLINK: mailto:email]
    pattern = re.compile(r'(\b[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b|\b\w+)\s*\[HYPERLINK:\s*(https?://[^\]]+|mailto:[^\]]+)\]')
    
    # Replace the pattern with the appropriate HTML anchor tag
    def replace(match):
        word_before = match.group(1)
        url = match.group(2)
        return f'<a href="{url}">{word_before}</a>'
    
    value = pattern.sub(replace, value)
    return mark_safe(value)
