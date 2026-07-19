<span class="kicker">Automation · Reliability</span>

# Make it reliable

Reliability isn't a technology — it's a short list of "what if" answers. Here's the list, in plain words.

## The checklist

- **What if the input is garbage?** Check inputs before the AI step. Wrong format or empty file → stop and flag, don't process.
- **What if the AI output is wrong-shaped?** Say exactly what shape you expect (sections, fields, length). If the output doesn't match, retry once, then flag.
- **What if a service is down?** Wait and retry once or twice, then stop and tell you. Never loop forever.
- **What if it runs twice?** Make re-runs harmless: check "was this already processed?" before acting. (This is the failure that sends the same email twice.)
- **What if it half-finishes?** Prefer all-or-nothing: build the whole result as a draft, deliver it in one final step.
- **How will you know it broke?** Every failure sends you a message that says *what* broke and *which* item. Silent failure is the only unacceptable failure.

## Logs, minus the jargon

A **log** is just a diary the automation keeps: "3:01 processed file A. 3:02 file B skipped — empty." When something's weird three weeks from now, the diary is how you find out what happened. Ask whatever tool you use to keep one.

## The maturity rule

New automations run with you approving every output. Only after weeks of clean runs do you let low-stakes steps through automatically — and the irreversible steps (sending, deleting, paying) keep approval forever.

[Ideas to steal](ideas.md){ .md-button .md-button--primary }
