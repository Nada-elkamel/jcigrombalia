from django.core.validators import FileExtensionValidator
from django.db import models


class SiteSettings(models.Model):
    org_name = models.CharField("Nom de l'organisation", max_length=150, default="JCI Grombalia")
    tagline = models.CharField(
        "Sous-titre",
        max_length=255,
        default="Jeune Chambre Internationale de Grombalia",
    )
    hero_title = models.CharField(
        "Titre principal (Hero)",
        max_length=255,
        default="Former des leaders citoyens pour un impact durable à Grombalia",
    )
    hero_subtitle = models.TextField(
        "Texte de présentation (Hero)",
        default=(
            "Organisation locale membre de la Jeune Chambre Internationale Tunisie, "
            "engagée pour le leadership, l'entrepreneuriat social et le développement communautaire."
        ),
    )
    history_intro = models.TextField(
        "Introduction de la rubrique Historique",
        default=(
            "Cet espace retrace le parcours institutionnel de la JCI Grombalia, "
            "ses moments fondateurs et les équipes dirigeantes qui ont porté ses projets."
        ),
    )
    founding_year = models.PositiveIntegerField(
        "Année de création officielle", null=True, blank=True
    )
    address = models.CharField("Adresse", max_length=255, default="Grombalia 8030, Nabeul, Tunisie")
    email = models.EmailField("Adresse e-mail", default="contact@jcigrombalia.tn")
    phone = models.CharField("Téléphone", max_length=50, default="+216 00 000 000")
    facebook_url = models.URLField("Lien Facebook", blank=True, default="")
    instagram_url = models.URLField("Lien Instagram", blank=True, default="")
    linkedin_url = models.URLField("Lien LinkedIn", blank=True, default="")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Paramètres du site"
        verbose_name_plural = "Paramètres du site"

    def __str__(self) -> str:
        return self.org_name

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class MediaAsset(models.Model):
    SECTION_CHOICES = [
        ("general", "Général"),
        ("history", "Historique"),
        ("awards", "Récompenses"),
        ("actions", "Actions"),
        ("manifestations", "Manifestations"),
    ]

    title = models.CharField("Titre / Description", max_length=200)
    file = models.FileField(
        "Fichier (Image ou PDF)",
        upload_to="library/%Y/%m/",
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp", "pdf"])],
    )
    section = models.CharField("Rubrique associée", max_length=30, choices=SECTION_CHOICES, default="general")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Média"
        verbose_name_plural = "Médiathèque"

    def __str__(self) -> str:
        return self.title
