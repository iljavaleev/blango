from django.contrib.auth import get_user_model
from django import template
from django.utils.html import format_html

register = template.Library()
User = get_user_model()


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