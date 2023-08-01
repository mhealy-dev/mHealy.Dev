from django.urls import path, include
from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.Home.as_view(), name="home"),

    # Code
    path("code/", views.Code.as_view(), name="code"),
    path("code/create", views.CodeCreate.as_view(), name="code_create"),
    path("code/<pk>/delete",
         views.CodeDelete.as_view(), name="code_delete"),
    path("code/<pk>/update",
         views.CodeUpdate.as_view(), name="code_update"),

    # Certs
    path("certs/", views.Certs.as_view(), name="certs"),
    path("certs/create", views.CertCreate.as_view(), name="certs_create"),
    path("certs/<pk>/delete",
         views.CertDelete.as_view(), name="certs_delete"),
    path("certs/<pk>/update",
         views.CertUpdate.as_view(), name="certs_update"),

    # Exp
    path("exp/", views.Exp.as_view(), name="exp"),
    path("exp/create", views.ExpCreate.as_view(), name="exp_create"),
    path("exp/<pk>/delete",
         views.ExpDelete.as_view(), name="exp_delete"),
    path("exp/<pk>/update",
         views.ExpUpdate.as_view(), name="exp_update"),

    # Skills
    path("skills/", views.Skills.as_view(), name="skills"),
    path("skills/create", views.SkillCreate.as_view(), name="skills_create"),
    path("skills/<pk>/delete",
         views.SkillDelete.as_view(), name="skills_delete"),
    path("skills/<pk>/update",
         views.SkillUpdate.as_view(), name="skills_update"),
]