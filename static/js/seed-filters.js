/* jshint esversion: 11 */

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
    const clearBtn = event.target.closest("[data-clear-filters]");

    if (clearBtn) {
      event.preventDefault();

      Object.keys(hiddenInputs).forEach(function (name) {
        if (!hiddenInputs[name]) return;

        if (name === "sort") {
          hiddenInputs[name].value = DEFAULT_SORT;
        } else {
          hiddenInputs[name].value = "";
        }
      });

      const searchInput = form.querySelector('input[name="q"]');
      if (searchInput) {
        searchInput.value = "";
      }

      autoSubmit();
      return;
    }

    const btn = event.target.closest("[data-filter-name]");
    if (!btn) return;

    event.preventDefault();

    const filterName = btn.getAttribute("data-filter-name");
    const filterValue = btn.getAttribute("data-filter-value");
    const hidden = hiddenInputs[filterName];

    if (!hidden) return;

    const currentlyActive = hidden.value === filterValue;

    if (currentlyActive) {
      setHiddenValue(filterName, "");
    } else {
      setHiddenValue(filterName, filterValue);
    }

    autoSubmit();
  });
})();