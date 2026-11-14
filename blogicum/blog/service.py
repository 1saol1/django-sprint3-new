from django.utils import timezone

from blog.models import Post


def get_published_posts(posts=Post.objects):
    return posts.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )
