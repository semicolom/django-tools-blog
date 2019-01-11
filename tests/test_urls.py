from django.test import TestCase
from django.urls import reverse_lazy

from djtools.blog.models import Post


class URLTestCase(TestCase):
    def test_blog_list_url(self):
        self.assertEqual(reverse_lazy('blog:list'), "/blog/")

    def test_blog_detail_url(self):
        post = Post.objects.create(
            title="Test",
            body="Test Test test"
        )

        self.assertEqual(
            reverse_lazy('blog:detail', kwargs=dict(slug=post.slug)),
            "/blog/test/"
        )
