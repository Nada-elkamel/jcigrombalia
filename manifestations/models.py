from django.db import models


class Manifestation(models.Model):
    TYPE_CHOICES = [
        ("zonale", "Zonale"),
        ("nationale", "Nationale"),
    ]
    STATUS_CHOICES = [
        ("draft", "Brouillon"),
        ("published", "Publié"),
    ]

    name = models.CharField("Nom de la manifestation", max_length=255)
    type = models.CharField("Type", max_length=20, choices=TYPE_CHOICES, default="zonale")
    event_date = models.DateField("Date")
    year = models.PositiveIntegerField("Année")
    location = models.CharField("Lieu", max_length=200)
    description = models.TextField("Description")
    report = models.TextField("Compte rendu (optionnel)", blank=True, default="")
    cover_image = models.ImageField("Photographie principale", upload_to="manifestations/covers/", blank=True, null=True)
    status = models.CharField("Statut", max_length=20, choices=STATUS_CHOICES, default="draft")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-event_date", "-id"]
        verbose_name = "Manifestation"
        verbose_name_plural = "Manifestations"

    def __str__(self) -> str:
        return f"{self.name} ({self.year})"


class Participation(models.Model):
    manifestation = models.ForeignKey(Manifestation, on_delete=models.CASCADE, related_name="participations")
    participant_name = models.CharField("Nom du participant", max_length=150)
    role_info = models.CharField("Rôle ou fonction", max_length=200, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Participation"
        verbose_name_plural = "Participations"


class ManifestationImage(models.Model):
    manifestation = models.ForeignKey(Manifestation, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("Photographie", upload_to="manifestations/gallery/")
    caption = models.CharField("Légende (optionnelle)", max_length=200, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Image de manifestation"
        verbose_name_plural = "Galerie de manifestations"
