from datetime import date
from django.core.management.base import BaseCommand

from actions.models import Action
from awards.models import Award
from core.models import SiteSettings
from history.models import History
from manifestations.models import Manifestation, Participation


class Command(BaseCommand):
    help = "Charge des contenus de démonstration clairement identifiés pour JCI Grombalia."

    def handle(self, *args, **options):
        SiteSettings.get_solo()

        if History.objects.count() == 0:
            History.objects.create(
                title="[Démonstration] Événement fondateur de l'OLM",
                description=(
                    "Fiche de démonstration destinée à illustrer la chronologie historique. "
                    "Remplacez ce contenu depuis le dashboard par les archives officielles."
                ),
                event_date="2024",
                category="Événement",
                display_order=1,
                status="published",
            )
            History.objects.create(
                title="[Démonstration] Mandat & Bureau Exécutif",
                description="Exemple de fiche présentant un ancien président et son bureau.",
                event_date="2025",
                category="Présidence",
                president_name="Nom du Président (Exemple)",
                board_members="Secrétaire Général · Trésorier · Vice-Présidents (Exemple)",
                display_order=2,
                status="published",
            )

        if Award.objects.count() == 0:
            Award.objects.create(
                title="[Démonstration] Distinction Zonale — Exemple",
                description="Contenu de démonstration illustrant une distinction zonale.",
                year=2025,
                level="zonal",
                status="published",
            )

        if Action.objects.count() == 0:
            Action.objects.create(
                title="[Démonstration] Initiative Citoyenne & Développement Durable",
                description="Fiche exemple d'action communautaire réalisée à Grombalia.",
                action_date=date(2025, 4, 12),
                year=2025,
                category="Développement communautaire",
                action_type="Action civique",
                outcome="Exemple de bilan : mobilisation locale des membres.",
                status="published",
            )

        if Manifestation.objects.count() == 0:
            manif = Manifestation.objects.create(
                name="[Démonstration] Assises Zonales — Zone B (Exemple)",
                type="zonale",
                event_date=date(2025, 5, 10),
                year=2025,
                location="Cap Bon, Tunisie",
                description="Fiche de démonstration illustrant une participation zonale.",
                report="Compte rendu exemple de la délégation.",
                status="published",
            )
            Participation.objects.create(
                manifestation=manif,
                participant_name="Délégué Exemple",
                role_info="Chef de délégation (Exemple)",
            )

        self.stdout.write(self.style.SUCCESS("Contenus de démonstration chargés avec succès."))
