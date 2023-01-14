import logging
from django.contrib.auth import get_user_model
from django import template
from django.utils.html import format_html

from blog.models import Post

register = template.Library()
User = get_user_model()
logger = logging.getLogger(__name__)

@register.filter
def author_details(author: User, current: User = None) -> str:
  if isinstance(author, User):
    if author == current:
      return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
      name = f"{author.first_name} {author.last_name}"
    else:
      name = f"{author.username}"

    if author.email:
      return format_html("<a href='{}'>{}</a>", author.email, name) 
    else:
      return f"{name}"

  return ""

@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
    posts = Post.objects.exclude(pk=post.pk)[:5]
    logger.debug("Loaded %d recent posts for post %d", len(posts), post.pk)
    return {"title": "Recent Posts", "posts": posts}


@register.simple_tag
def row(extra_classes=""):
    return format_html('<div class="row {}">', extra_classes)


@register.simple_tag
def endrow():
    return format_html("</div>")

@register.simple_tag
def col(extra_classes=""):
    return format_html('<div class="row {}">', extra_classes)


@register.simple_tag
def endcol():
    return format_html("</div>")
