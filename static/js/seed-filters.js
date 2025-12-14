`/* jshint esversion: 11 */`

(function () {
  const form = document.getElementById("filter-form");
  if (!form) return;

  const hiddenInputs = {
    colour: document.getElementById("filter-colour"),
    habit: document.getElementById("filter-habit"),
    sort: document.getElementById("filter-sort"),
  };

  const DEFAULT_SORT = "name";

  function setHiddenValue(filterName, value) {
    const input = hiddenInputs[filterName];
    if (!input) return;
    input.value = value || "";
  }

  function clearPageParam() {
    const pageInput = form.querySelector('input[name="page"]');
    if (pageInput) {
      pageInput.remove();
    }
  }

  function autoSubmit() {
    clearPageParam();
    if (form.requestSubmit) {
      form.requestSubmit();
    } else {
      form.submit();
    }
  }

  form.addEventListener("click", function (event) {
    // -----------------------------
    // Clear-all filters pill
    // -----------------------------
    const clearBtn = event.target.closest("[data-clear-filters]");
    if (clearBtn) {
      event.preventDefault();

      // Reset hidden inputs: clear all, set sort back to default
      Object.keys(hiddenInputs).forEach(function (name) {
        if (name === "sort") {
          hiddenInputs[name].value = DEFAULT_SORT;
        } else {
          hiddenInputs[name].value = "";
        }
      });

      // Clear search input
      const searchInput = form.querySelector('input[name="q"]');
      if (searchInput) {
        searchInput.value = "";
      }

      // Reset visual state of all pills
      const allPills = form.querySelectorAll("[data-filter-name]");
      allPills.forEach(function (btn) {
        const filterName = btn.getAttribute("data-filter-name");
        const filterValue = btn.getAttribute("data-filter-value");
        const isDefaultSort = filterName === "sort" && filterValue === DEFAULT_SORT;

        btn.classList.toggle("btn-primary", isDefaultSort);
        btn.classList.toggle("btn-outline", !isDefaultSort);
        btn.setAttribute("aria-pressed", isDefaultSort ? "true" : "false");
      });

      autoSubmit();
      return;
    }

    // -----------------------------
    // Individual filter pills
    // -----------------------------
    const btn = event.target.closest("[data-filter-name]");
    if (!btn) return;

    event.preventDefault();

    const filterName = btn.getAttribute("data-filter-name");
    const filterValue = btn.getAttribute("data-filter-value");
    const hidden = hiddenInputs[filterName];
    if (!hidden) return;

    const currentlyActive = hidden.value === filterValue;

    // Toggle value: clicking an active pill clears it
    if (currentlyActive) {
      setHiddenValue(filterName, "");
    } else {
      setHiddenValue(filterName, filterValue);
    }

    // Update styles for all buttons in this group
    const groupButtons = form.querySelectorAll(
      '[data-filter-name="' + filterName + '"]'
    );

    groupButtons.forEach(function (b) {
      const val = b.getAttribute("data-filter-value");
      const isActive = !currentlyActive && val === filterValue;
      b.classList.toggle("btn-primary", isActive);
      b.classList.toggle("btn-outline", !isActive);
      b.setAttribute("aria-pressed", isActive ? "true" : "false");
    });

    autoSubmit();
  });
})();
