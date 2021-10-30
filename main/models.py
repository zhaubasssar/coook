from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

User = get_user_model()


class Recipe(models.Model):
    title               = models.CharField(max_length=255)
    slug                = models.SlugField(unique=True, verbose_name='URL', null=True)
    cooking             = RichTextField(blank=True, null=True)
    ingridients         = RichTextField(blank=True, null=True)
    image               = models.ImageField(verbose_name='Изображение', blank=True, upload_to="images/posts/",
                                        default="images/posts/default-post-image.png")
    created_at          = models.DateTimeField(auto_now_add=True, editable=False)
    likes               = models.ManyToManyField(User, blank=True, related_name='Likes')

