from django.db import models


class Cert(models.Model):
    certifier = models.CharField(
        verbose_name="Certifier", max_length=256)
    cert_name = models.CharField(default="Proficiency Certificate",
                                 verbose_name="Certificate Name", max_length=256)
    date_achieved = models.DateField(
        verbose_name="Date Achieved", default=None)
    link = models.URLField(verbose_name="Link",
                           max_length=256, default="https://mhealy.dev")

    def __str__(self):
        return self


class Code(models.Model):
    name = models.CharField(verbose_name="Name", max_length=256)
    description = models.CharField(
        verbose_name="Description", max_length=2048, default=None, blank=True)
    repository = models.URLField(
        verbose_name="Repository", max_length=256, default=None, blank=True)
    skills_used = models.ManyToManyField(
        'Skill', verbose_name="Skills Used", blank=True, related_name="skills")

    class Meta:
        verbose_name = "Code"

    def __str__(self):
        return self


class Exp(models.Model):
    company = models.CharField(
        verbose_name="Company", max_length=256)
    position = models.CharField(
        verbose_name="Position", max_length=256, default=None)
    description = models.CharField(
        verbose_name="Description", max_length=2048, default=None)
    start_year = models.CharField(
        verbose_name="Start Year", max_length=4)
    end_year = models.CharField(
        verbose_name="End Year", max_length=4, default="now")
    link = models.URLField(verbose_name="Link",
                           max_length=256, default="https://mhealy.dev")

    def __str__(self):
        return self


class Skill(models.Model):
    name = models.CharField(verbose_name="Name", max_length=256, name="name")
    years = models.IntegerField(verbose_name="Years")
    link = models.URLField(verbose_name="Link",
                           max_length=256, default="https://mhealy.dev")
    icon = models.URLField(verbose_name="Icon", max_length=256,
                           default="")

    class Meta:
        ordering = ["name", "years"]
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name
