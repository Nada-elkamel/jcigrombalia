from django.db import models


class History(models.Model):
    STATUS_CHOICES = [
        ("draft", "Brouillon"),
        ("published", "Publié"),
    ]
    CATEGORY_CHOICES = [
        ("Événement", "Événement marquant"),
        ("Présidence", "Ancien Président"),
        ("Bureau", "Bureau Exécutif"),
    ]

    title = models.CharField("Titre", max_length=255)
    description = models.TextField("Description")
    event_date = models.CharField("Date ou période", max_length=100)
    category = models.CharField("Catégorie", max_length=50, choices=CATEGORY_CHOICES, default="Événement")
    president_name = models.CharField("Nom du Président (optionnel)", max_length=150, blank=True, default="")
    board_members = models.TextField("Composition du bureau (optionnel)", blank=True, default="")
    image = models.ImageField("Photographie d'archive", upload_to="history/", blank=True, null=True)
    display_order = models.PositiveIntegerField("Ordre d'affichage", default=0)
    status = models.CharField("Statut", max_length=20, choices=STATUS_CHOICES, default="draft")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "-event_date", "-id"]
        verbose_name = "Événement historique"
        verbose_name_plural = "Historique"

    def __str__(self) -> str:
        return f"{self.event_date} — {self.title}"
