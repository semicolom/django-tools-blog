from django.test import TestCase
from django.urls import reverse_lazy

from djtools.blog.models import Post


class PostListViewTestCase(TestCase):
    url = reverse_lazy('blog:list')

    def test_list_order(self):
        post_1 = Post.objects.create(
            title="Test",
            body="Test Test test"
        )
        post_2 = Post.objects.create(
            title="Test2",
            body="Test Test test"
        )

        response = self.client.get(self.url)
        self.assertListEqual(
            list(response.context_data.get('post_list')),
            [post_2, post_1]
        )
