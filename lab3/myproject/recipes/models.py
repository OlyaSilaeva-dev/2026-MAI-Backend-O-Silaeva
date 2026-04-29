from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.username    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    avatar = models.URLField(blank=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    cooking_time = models.PositiveIntegerField(help_text='в минутах')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='recipes')
    favorited_by = models.ManyToManyField(User, through='Favorite', related_name='favorite_recipes')
    
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'recipe')