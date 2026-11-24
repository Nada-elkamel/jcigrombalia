from django.core.validators import FileExtensionValidator
from django.db import models


class Award(models.Model):
    LEVEL_CHOICES = [
        ("local", "Local"),
        ("zonal", "Zonal"),
        ("national", "National"),
        ("international", "International"),
    ]
    STATUS_CHOICES = [
        ("draft", "Brouillon"),
        ("published", "Publié"),
    ]

    title = models.CharField("Nom de la récompense", max_length=255)
    description = models.TextField("Description")
    year = models.PositiveIntegerField("Année d'obtention")
    level = models.CharField("Niveau", max_length=20, choices=LEVEL_CHOICES, default="local")
    image = models.FileField(
        "Photographie ou certificat",
        upload_to="awards/",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp", "pdf"])],
    )
    status = models.CharField("Statut", max_length=20, choices=STATUS_CHOICES, default="draft")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-year", "-id"]
        verbose_name = "Récompense"
        verbose_name_plural = "Récompenses"

    def __str__(self) -> str:
        return f"{self.title} ({self.year})"

    @property
    def is_pdf(self) -> bool:
        return bool(self.image and self.image.name.lower().endswith(".pdf"))
