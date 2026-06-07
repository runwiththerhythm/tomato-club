/* global Stripe */
/* jshint esversion: 11 */

(function () {
  "use strict";

  function getCookie(name) {
    let cookieValue = null;

    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");

      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();

        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }

    return cookieValue;
  }

  document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll(".join-tier-btn");

    if (!buttons.length) {
      return;
    }

    const csrftoken = getCookie("csrftoken");

    buttons.forEach((btn) => {
      btn.addEventListener("click", async (e) => {
        e.preventDefault();

        const checkoutUrl = btn.dataset.checkoutUrl || btn.getAttribute("href");

        if (!checkoutUrl) {
          console.error("Missing checkout URL", { btn });
          alert("Checkout could not be started. Please try again.");
          return;
        }

        try {
          const response = await fetch(checkoutUrl, {
            method: "POST",
            headers: {
              "X-Requested-With": "XMLHttpRequest",
              "X-CSRFToken": csrftoken,
            },
          });

          if (!response.ok) {
            const text = await response.text();
            console.error("Checkout error", response.status, text);
            alert("Something went wrong when starting the checkout.");
            return;
          }

          const data = await response.json();

          if (data.checkoutUrl) {
            window.location.href = data.checkoutUrl;
            return;
          }

          if (!data.publicKey || !data.sessionId) {
            console.error("Missing Stripe response data", data);
            alert("Checkout could not be started. Please try again.");
            return;
          }

          const stripe = Stripe(data.publicKey);

          const { error } = await stripe.redirectToCheckout({
            sessionId: data.sessionId,
          });
          
          if (error) {
            console.error(error);
            alert(error.message);
          }
        } catch (err) {
          console.error("Network or JavaScript error", err);
          alert("Network error. Please try again.");
        }
      });
    });
  });
})();