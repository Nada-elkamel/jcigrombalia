from django.db import models


class Action(models.Model):
    STATUS_CHOICES = [
        ("draft", "Brouillon"),
        ("published", "Publié"),
    ]

    title = models.CharField("Titre", max_length=255)
    description = models.TextField("Description")
    action_date = models.DateField("Date de réalisation")
    year = models.PositiveIntegerField("Année")
    category = models.CharField("Catégorie", max_length=120)
    action_type = models.CharField("Type d'action", max_length=120)
    outcome = models.TextField("Bilan ou résultat (optionnel)", blank=True, default="")
    cover_image = models.ImageField("Image de couverture", upload_to="actions/covers/", blank=True, null=True)
    status = models.CharField("Statut", max_length=20, choices=STATUS_CHOICES, default="draft")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-action_date", "-id"]
        verbose_name = "Action"
        verbose_name_plural = "Actions"

    def __str__(self) -> str:
        return self.title


class ActionImage(models.Model):
    action = models.ForeignKey(Action, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("Photographie", upload_to="actions/gallery/")
    caption = models.CharField("Légende (optionnelle)", max_length=200, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Image d'action"
        verbose_name_plural = "Galerie d'actions"
