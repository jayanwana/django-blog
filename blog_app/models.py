from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    """
    Main Blog Post model.
    """
    author = models.ForeignKey('auth.User', models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comment(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("blog_app:post_detail", kwargs={'pk': self.pk})


class Comment(models.Model):
    """
    Comment object model. Linked to each
    """
    post = models.ForeignKey('blog_app.Post',
                             on_delete=models.CASCADE,
                             related_name='comments')
    author = models.CharField(max_length=32)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def approve(self):
        self.approved_comment = True
        self.save()

    @staticmethod
    def get_absolute_url():
        return reverse("blog_app:post_list")
