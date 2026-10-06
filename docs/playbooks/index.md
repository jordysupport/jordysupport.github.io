---
title: "Free AI Playbooks"
description: >-
  Four reusable AI tasks with free downloads, copy-paste prompts, worked examples, and checks for research, writing, meetings, and reference notes.
---

<div class="playbook-hero" markdown>

<span class="kicker">Playbooks</span>

# Give your agent a useful task { #teach-your-ai-a-job-once-use-it-forever }

Choose a task, bring your own material, and use the instructions to guide the work. We include an example and a review checklist with each playbook so you can judge the result.

All four are free. You can download the instructions or start with a chat prompt.

</div>

## How it works

<div class="playbook-steps">
  <div><strong>1 · Choose a task</strong><span>Open the playbook and compare its example with what you need.</span></div>
  <div><strong>2 · Use the instructions</strong><span>Paste the prompt, or review the ZIP and save it with a file-capable agent.</span></div>
  <div><strong>3 · Check the result</strong><span>Review the sources, missing details, and draft before using it.</span></div>
</div>

The downloads contain plain-text Markdown files. Saving one gives you a reusable reference; it does not make an agent remember it automatically. In a new conversation, tell the agent which file to read.

## The library

<div class="library-list">
  <div class="library-row">
    <div class="library-info">
      <strong>Research a topic</strong>
      <span>Investigate a question and get a short brief with linked evidence and clear unknowns.</span>
    </div>
    <p class="library-actions">
      <a class="md-button md-button--primary" href="research-brief/">Open playbook</a>
      <a class="md-button" href="research-brief-example/">See example</a>
    </p>
  </div>
  <div class="library-row">
    <div class="library-info">
      <strong>Repurpose content</strong>
      <span>Adapt an article, transcript, or set of notes into drafts for the formats you use.</span>
    </div>
    <p class="library-actions">
      <a class="md-button md-button--primary" href="content-repurpose/">Open playbook</a>
      <a class="md-button" href="content-repurpose-example/">See example</a>
    </p>
  </div>
  <div class="library-row">
    <div class="library-info">
      <strong>Process a meeting</strong>
      <span>Separate agreed decisions, assigned work, and open questions, then draft a follow-up.</span>
    </div>
    <p class="library-actions">
      <a class="md-button md-button--primary" href="meeting-follow-up/">Open playbook</a>
      <a class="md-button" href="meeting-follow-up-example/">See example</a>
    </p>
  </div>
  <div class="library-row">
    <div class="library-info">
      <strong>Build a knowledge base</strong>
      <span>Keep a source or decision as a short note with its origin, date, and useful context.</span>
    </div>
    <p class="library-actions">
      <a class="md-button md-button--primary" href="knowledge-base/">Open playbook</a>
      <a class="md-button" href="knowledge-base-example/">See example</a>
    </p>
  </div>
</div>

<div class="signup-panel">
  <span class="kicker">Optional email updates</span>
  <p>Subscribe for new guides and playbooks. We use Kit to manage the list; your email address is sent to Kit when you subscribe. Everything is available here without joining, and you can unsubscribe from any issue.</p>
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

## Review and scope { #two-rules-that-never-change }

The instructions ask the agent to keep outputs as drafts, use the material you provide, and ask before saving files or working outside your chosen scope. Check the tool's permissions too: written instructions alone do not restrict its access.

You decide what to save, send, or publish. Use the checklist on each playbook page before taking that step.
