from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()


class MyBaseModel(models.Model):
    is_active = models.BooleanField(
        default=True,
        verbose_name='Is active'
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created date'
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated date'
    )

    class Meta:
        abstract = True
        ordering = ('pk',)

    def __str__(self):
        raise NotImplementedError('Implement __str__ method')


class Category(MyBaseModel):
    title = models.CharField(max_length=250,
                             blank=False,
                             null=False,
                             verbose_name="Title",
                             )
    description = models.TextField(blank=False,
                                   null=False,
                                   verbose_name="Description",
                                   )

    @property
    def active_posts(self):
        return self.posts.filter(is_active=True).values(
            'id',
            'title',
            'description',
            'created_date',
            'updated_date',
        )

    @property
    def disabled_posts(self):
        return self.posts.filter(is_active=False).values(
            'id',
            'title',
            'description',
            'created_date',
            'updated_date',
        )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Post(MyBaseModel):
    category = models.ForeignKey(Category,
                                 related_name='posts',
                                 on_delete=models.PROTECT,
                                 verbose_name="Category",
                                 )
    title = models.CharField(max_length=250,
                             blank=False,
                             null=False,
                             verbose_name="Title",
                             )
    description = models.TextField(blank=False,
                                   null=False,
                                   verbose_name="Description",
                                   )
    author = models.ForeignKey(User,
                               related_name='phone_book_rows',
                               on_delete=models.PROTECT,
                               verbose_name="Author",
                               )

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f'{self.title}({self.category.title})'


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        related_name="comments",
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
