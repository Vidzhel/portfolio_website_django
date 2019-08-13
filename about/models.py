from django.db import models
import re

# Create your models here.


class About(models.Model):
    about = models.TextField()
    about_img = models.ImageField(
        upload_to=f"about/images", help_text="Select image for this section", null=True, blank=True)

    education = models.TextField( null=True, blank=True,
        help_text="Each item of the article splits on three parts:\n {title%content%endtitle}{years%content%endyears}{text%content%endtext}")
    work_experience = models.TextField(null=True, blank=True,
        help_text="Each item of the article splits on three parts:\n {title%content%endtitle}{years%content%endyears}{text%content%endtext}")
    honors = models.TextField(null=True, blank=True,
        help_text="Each item of the article splits on three parts:\n {title%content%endtitle}{years%content%endyears}{text%content%endtext}")
    developer_skills = models.TextField(null=True, blank=True,
        help_text="Each item of the list splits on two parts:\n {title%content%endtitle}{items%item1;item2;item3;%enditems}")
    designer_skills = models.TextField(null=True, blank=True,
        help_text="Each item of the list splits on two parts:\n {title%content%endtitle}{items%item1;item2;item3;%enditems}")

 # Regexp
    article_regex = re.compile(
        r"(?:{title%\s*(?P<title>[\s\S]*)\s*%endtitle})\s*(?:{years%\s*(?P<years>[\s\S]*)\s*%endyears})?\s*(?:{text%\s*(?P<text>[\s\S]*)\s*%endtext})?\s*", re.IGNORECASE)

    list_regex = re.compile(
        r"(?:{title%\s*(?P<title>.*)\s*%endtitle})\s*(?:{items%\s*(?P<items>.*;)*\s*%enditems})?\s*", re.IGNORECASE)

    def get_cleaned_data(self):

        about = self.about
        about_img = self.about_img

        education = [match.groupdict()
                     for match in self.article_regex.finditer(self.education)]
        work_experience = [match.groupdict(
        ) for match in self.article_regex.finditer(self.work_experience)]
        honors = [match.groupdict()
                  for match in self.article_regex.finditer(self.honors)]

        developer_skills = [match.groupdict()
                            for match in self.list_regex.finditer(self.developer_skills)]

        designer_skills = [match.groupdict()
                           for match in self.list_regex.finditer(self.designer_skills)]

        for dev_skill in developer_skills:
            if(dev_skill["items"]):
                dev_skill["items"] = dev_skill.get("items", "").split(";")

        for des_skill in designer_skills:
            if(des_skill["items"]):
                des_skill["items"] = des_skill.get("items", "").split(";")

        data = {
            "about": about,
            "about_img": about_img,
            "education": education,
            "work_experience": work_experience,
            "honors": honors,
            "developer_skills": developer_skills,
            "designer_skills": designer_skills,
        }

        return data

    def __str__(self):
        return self.about

    # ^(?:(?:{title%(.*)%endtitle})?\s*(?:{years%(.*)%endyears})?\s*(?:{text%(.*)%endtext})?)*$
    # ^(?:(?:{title%(.*)%endtitle})?\s*(?:{items%(.*;)*%enditems})?)*$
