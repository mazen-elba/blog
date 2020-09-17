from django.db import models


class BlogPost(models.Model):
    """A blog post model."""
    title = models.CharField(max_length=255)
    date = models.DateField()
    # categories =
    author = models.CharField(max_length=255)
    description = models.TextField()
    # image =

    def __str__(self):
        """Return the title."""
        return self.title
