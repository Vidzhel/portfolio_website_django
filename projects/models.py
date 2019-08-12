from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Represent category of a project item"""

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("projects_list", kwargs={"filtered": "filtered"}) + "?category=" + self.name


class Tag(models.Model):
    """Represent tags that can be attached to a project item"""
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("projects_list", kwargs={"filtered": "filtered"}) + "?tags=" + self.name


class ProjectItem(models.Model):
    """Represent a project with all necessary info"""
    alias = models.CharField(max_length=40, primary_key=True)
    title = models.CharField(max_length=40)
    img = models.ImageField(
        upload_to=f"project_item/images", help_text="Select image for this project")

    upload_date = models.DateField(auto_now=False, auto_now_add=True)
    in_progress = models.BooleanField(default=False,
                                      help_text="Determines if this project currently in progress")

    code_source = models.CharField(
        max_length=100, help_text="Link on this project's code source")
    categories = models.ManyToManyField(
        Category, help_text="Choose categories for this project")
    tags = models.ManyToManyField(
        Tag, help_text="Choose tags for this project")

    about = models.TextField()
    about_img = models.ImageField(
        upload_to=f"project_item/images", help_text="Select image for this section", null=True, blank=True)

    project_difficulties = models.TextField(null=True, blank=True)
    project_difficulties_img = models.ImageField(
        upload_to=f"project_item/images", help_text="Select image for this section", null=True, blank=True)

    solutions = models.TextField(null=True, blank=True)
    solutions_img = models.ImageField(
        upload_to=f"project_item/images", help_text="Select image for this section", null=True, blank=True)

    features = models.TextField(null=True, blank=True)
    technologies = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ["upload_date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "foo"
        # return reverse("projects", kwargs={"pk": self.pk})
