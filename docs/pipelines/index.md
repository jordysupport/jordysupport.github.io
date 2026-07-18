# Automation Pipelines

A **pipeline** is work that runs the same way every time without you babysitting it: gather → process → output → deliver. AI slots into pipelines as the processing step — but the plumbing around it (scheduling, error handling, delivery) is what makes it *automation* instead of *a chore you do with AI*.

Pages here, added as questions come up:

- Anatomy of a pipeline: trigger → fetch → AI step → output → notify
- Scheduling: making things run daily without you (Task Scheduler, cron, GitHub Actions)
- Content pipelines: turning one input into many outputs automatically
- When a pipeline breaks silently — logging and alerts for non-developers

## Ground rules

1. **Manual first, automated second.** If you can't do the task by hand with AI, automating it just produces garbage faster.
2. **Every pipeline needs a "it broke" signal.** A pipeline that fails silently is worse than no pipeline.
3. **Start with one step.** Automate the single most annoying part of a workflow, prove it, then chain the next step.
4. **Outputs need a home.** Decide where results land (folder, sheet, channel) before building anything.

*Want a specific pipeline walked through? Ask in Discord.*
