#!/usr/bin/env python
"""Utilitaire en ligne de commande Django pour JCI Grombalia."""
import os
import sys


def main():
    """Exécuter les tâches d'administration."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jci_project.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Impossible d'importer Django. Vérifiez que votre environnement virtuel "
            "est activé et que Django est installé via requirements.txt."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
