from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.utils.text import slugify

User = get_user_model()


class Recipe(models.Model):
    checked             = models.BooleanField(default=False)
    author              = models.ForeignKey(User, default=1, verbose_name="Автор", on_delete=models.CASCADE)
    title               = models.CharField(max_length=255)
    slug                = models.SlugField(unique=True, verbose_name='URL', null=True)
    cooking             = RichTextField(blank=True, null=True)
    ingridients         = RichTextField(blank=True, null=True)
    image               = models.ImageField(verbose_name='Изображение', blank=True, upload_to="images/posts/",
                                        default="images/posts/default-post-image.png")
    created_at          = models.DateTimeField(auto_now_add=True, editable=False)
    likes               = models.ManyToManyField(User, blank=True, related_name='Likes')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)
