from django.db import models

class Category(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Name of Category'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Region(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Name of Region'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'


class News(models.Model):
    title = models.CharField(
        max_length= 100,
        unique=True,
        verbose_name='Name of News'
    )
    summary = models.CharField(max_length=150, verbose_name='Summary', blank=True, null=True)
    content = models.TextField(verbose_name='Content')
    images = models.ImageField(upload_to='images/', verbose_name='IMG')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    view_count = models.PositiveIntegerField(default=0, verbose_name='Views')
    is_published = models.BooleanField(default=True, verbose_name='Is Published')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True , verbose_name='Region')


    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-created_at']
        verbose_name = 'New'
        verbose_name_plural = 'News'
