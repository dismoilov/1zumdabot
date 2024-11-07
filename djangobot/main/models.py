from django.db import models


class Resume(models.Model):
    file = models.FileField(upload_to='resumes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10)
    birthday = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    education_place = models.CharField(max_length=100)
    family_status = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    branch_desire = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    experience = models.CharField(max_length=25)
    worked_before = models.CharField(max_length=5)
    phone = models.CharField(max_length=15)
    extra_phone = models.CharField(max_length=15, blank=True, null=True)
    shirt_size = models.CharField(max_length=25, null=True, blank=True)
    is_studying = models.CharField(max_length=5)
    education_type = models.CharField(max_length=50, null=True, blank=True)
    languages = models.CharField(max_length=255)
    work_experience = models.TextField()
    programms_experience = models.CharField(max_length=100)
    about = models.TextField()
    salary = models.PositiveIntegerField()
    is_familiar_works_here = models.CharField(max_length=100)
    is_uzbek_citizen = models.CharField(max_length=5)
    is_working_now = models.CharField(max_length=5)
    from_vacancy_info = models.CharField(max_length=100)
    face_photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Rezyume "
        verbose_name_plural = "Rezyumalar "


class Branch(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Filial "
        verbose_name_plural = "Filiallar "

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Lavozim "
        verbose_name_plural = "Lavozimlar "

    def __str__(self):
        return self.name


class VacancyInfo(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Vakansiya Ma'lumot "
        verbose_name_plural = "Vakansiya Ma'lumotlar "

    def __str__(self):
        return self.name


class Chat(models.Model):
    name = models.CharField(max_length=100)
    chat_id = models.IntegerField()

    class Meta:
        verbose_name = "Chat "
        verbose_name_plural = "Chatlar "

    def __str__(self):
        return self.name
