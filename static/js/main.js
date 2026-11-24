document.addEventListener("DOMContentLoaded", function () {
  // Ajout dynamique de lignes de participants pour les manifestations
  const addParticipantBtn = document.getElementById("add-participant-btn");
  const participantsContainer = document.getElementById("participants-container");

  if (addParticipantBtn && participantsContainer) {
    addParticipantBtn.addEventListener("click", function () {
      const row = document.createElement("div");
      row.className = "row g-2 mb-2 participant-row";
      row.innerHTML = `
        <div class="col-md-6">
          <input type="text" name="participant_name" class="form-control form-control-sm" placeholder="Nom complet du participant" />
        </div>
        <div class="col-md-5">
          <input type="text" name="participant_role" class="form-control form-control-sm" placeholder="Rôle ou fonction (optionnel)" />
        </div>
        <div class="col-md-1 d-grid">
          <button type="button" class="btn btn-sm btn-outline-danger remove-participant-row" title="Retirer">
            <i class="bi bi-trash"></i>
          </button>
        </div>
      `;
      participantsContainer.appendChild(row);
    });

    participantsContainer.addEventListener("click", function (e) {
      const btn = e.target.closest(".remove-participant-row");
      if (btn) {
        btn.closest(".participant-row").remove();
      }
    });
  }

  // Modale de confirmation de suppression générique
  const deleteModal = document.getElementById("confirmDeleteModal");
  if (deleteModal) {
    deleteModal.addEventListener("show.bs.modal", function (event) {
      const button = event.relatedTarget;
      const actionUrl = button.getAttribute("data-delete-url");
      const itemLabel = button.getAttribute("data-item-label");
      const form = deleteModal.querySelector("#confirmDeleteForm");
      const text = deleteModal.querySelector("#confirmDeleteText");
      if (form && actionUrl) {
        form.setAttribute("action", actionUrl);
      }
      if (text && itemLabel) {
        text.textContent = "Confirmez-vous la suppression de : « " + itemLabel + " » ?";
      }
    });
  }
});
