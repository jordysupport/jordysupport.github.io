<span class="kicker">Automation · Blueprint</span>

# Plan a workflow

Before you build anything, fill in seven boxes on paper. If you can't fill a box, you're not ready to build — and that's the blueprint working.

## The seven boxes

1. **Trigger** — what starts it? (A schedule? A new email? You clicking go?)
2. **Input** — what does it work on, and what does "valid input" look like?
3. **AI step** — the one job the AI does (use your [playbook](../playbooks/index.md) or a tested prompt).
4. **Check** — how is the output verified? (Format check, source check, sanity limits.)
5. **Approval** — where do *you* look at it before it counts?
6. **Delivery** — where does the result go?
7. **Failure plan** — what happens when a step breaks? Who finds out, and how?

## Worked example: weekly meeting digest

1. **Trigger:** Friday, 3pm.
2. **Input:** this week's meeting notes from one folder.
3. **AI step:** run the meeting playbook on each file.
4. **Check:** every action item must name a source meeting.
5. **Approval:** draft lands in my review folder; nothing sends itself.
6. **Delivery:** after my OK, the digest goes to the team channel.
7. **Failure plan:** if a file won't process, skip it, list it at the top of the draft, and never send a partial digest without saying it's partial.

## The order matters

People love designing boxes 1–3 and skip 4–7. Flip it: **design the failure plan and approval point first.** They're what make the rest safe to build.

[Make it reliable](reliability.md){ .md-button .md-button--primary }
