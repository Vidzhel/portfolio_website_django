from django.db import models
from django.urls import reverse
import re

class Category(models.Model):
    """Represents category of a project item"""

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("projects_list_filtered", kwargs={"filtered": "filtered"}) + "?category=" + self.name


class Tag(models.Model):
    """Represents tags that can be attached to a project item"""
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("projects_list_filtered", kwargs={"filtered": "filtered"}) + "?tags=" + self.name


class ProjectItem(models.Model):
    """Represents a project with all necessary info"""

    alias = models.CharField(max_length=40, primary_key=True)
    title = models.CharField(max_length=40)
    description = models.TextField()
    img = models.ImageField(
        upload_to=f"project_item/images", help_text="Select image for this project")

    upload_date = models.DateTimeField(auto_now=False, auto_now_add=True)
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

    features = models.TextField(null=True, blank=True, help_text="Each item of the list splits on two parts:\n {title%content%endtitle}{items%item1;item2;item3;%enditems}")
    technologies = models.TextField(null=True, blank=True, help_text="Each item of the list splits on two parts:\n {title%content%endtitle}{items%item1;item2;item3;%enditems}")

    list_regex = re.compile(
        r"(?:{title%\s*(?P<title>.*)\s*%endtitle})\s*(?:{items%\s*(?P<items>.*;)*\s*%enditems})?\s*", re.IGNORECASE)

    class Meta:
        ordering = ["-upload_date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_details", kwargs={"alias": self.pk})

    def get_cleaned_data(self):

        features_cleaned = [match.groupdict()
                            for match in self.list_regex.finditer(self.features)]

        technologies_cleaned = [match.groupdict()
                                for match in self.list_regex.finditer(self.technologies)]

        for feature in features_cleaned:
            if(feature["items"]):
                feature["items"] = feature.get("items", "").split(";")

        for technologie in technologies_cleaned:
            if(technologie["items"]):
                technologie["items"] = technologie.get("items", "").split(";")

        data = {
            "alias": self.alias,
            "title": self.title,
            "description": self.description,
            "img": self.img,

            "upload_date": self.upload_date,
            "in_progress": self.in_progress,

            "code_source": self.code_source,
            "categories": self.categories,
            "tags": self.tags,

            "about": self.about,
            "about_img": self.about_img,

            "project_difficulties": self.project_difficulties,
            "project_difficulties_img": self.project_difficulties_img,

            "solutions": self.solutions,
            "solutions_img": self.solutions_img,

            "features": features_cleaned,
            "technologies": technologies_cleaned,

        }

        return data
