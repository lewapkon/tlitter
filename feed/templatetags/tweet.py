from django import template

register = template.Library()

@register.filter
def is_liked(tweet, user):
    return tweet.liked(user)
