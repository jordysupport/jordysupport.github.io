---
hide_support_outro: true
description: >-
  Prompt Academy is the free Jordy Support newsletter about using AI. Read the archive or choose to receive future issues by email.
---

# Prompt Academy

Short notes on using AI, with a task to try or a habit to improve. Every issue is available here for free. Email signup is optional.

<div class="signup-panel">
  <h2>Get future issues by email</h2>
  <p>We use Kit to manage subscriptions and send the newsletter. Your email address is sent to Kit when you subscribe. You can unsubscribe using the link in an issue.</p>
  <form class="signup-form" action="https://app.kit.com/forms/9786057/subscriptions" method="post">
    <input class="signup-input" type="email" name="email_address" placeholder="Email address" aria-label="Email address" autocomplete="email" required>
    <button class="signup-button" type="submit">Subscribe</button>
  </form>
  <p class="signup-status" role="status" aria-live="polite" hidden></p>
</div>

<script>
(function () {
  var form = document.querySelector(".signup-form");
  if (!form) return;
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var status = document.querySelector(".signup-status");
    var button = form.querySelector(".signup-button");
    var fail = "That didn't go through. Check the address and try again.";
    button.disabled = true;
    fetch(form.action, {
      method: "POST",
      body: new FormData(form),
      headers: { Accept: "application/json" }
    }).then(function (r) { if (!r.ok) throw new Error("Request failed"); return r.json(); }).then(function (d) {
      if (d && (d.status === "success" || d.subscription)) {
        form.querySelector(".signup-input").value = "";
        status.textContent = "Done. Check your email to confirm your subscription.";
      } else {
        status.textContent = fail;
      }
    }).catch(function () {
      status.textContent = fail;
    }).finally(function () {
      status.hidden = false;
      button.disabled = false;
    });
  });
})();
</script>

## What to expect { #every-issue }

A practical example, a question worth checking, or an update to a guide. Read the archive below to see the format before subscribing.

## The archive

- [Issue #001: Ask it twice](001.md) · August 2026
