---
title: "TUSK: CRM for Selling Websites"
hide_support_outro: true
description: >-
  TUSK is a free, self-hosted CRM for selling websites to local businesses. Track leads, follow-ups, mockups, clients, and invoices.
software_schema:
  name: TUSK
  operating_system: Windows, macOS, Linux
  category: BusinessApplication
  version: 0.3.0
  download_url: https://github.com/jordysupport/tusk/archive/refs/heads/main.zip
---

<div class="tusk-hero" markdown>

# TUSK: keep your website sales organized. { #the-crm-that-remembers-every-lead }

Track businesses you want to contact, the conversations you've had, and what needs to happen next. TUSK brings leads, website checks, mockups, and invoices into one self-hosted app.

[Get TUSK on GitHub](https://github.com/jordysupport/tusk){ .md-button .md-button--primary }
[Download the source ZIP](https://github.com/jordysupport/tusk/archive/refs/heads/main.zip){ .md-button }

</div>

<div class="vale-preview"><img src="/assets/tusk/tusk-01-dashboard.webp" alt="TUSK dashboard with lead statistics and follow-up tasks"></div>

The screenshots use the included demo businesses. They show the interface, rather than results from real sales.

## Set it up with your agent { #give-your-agent-one-prompt }

TUSK runs on Windows, macOS, or Linux with Node.js. Use a currently supported Node.js release that meets the repository's requirements.

```text
Set up https://github.com/jordysupport/tusk in a new permanent folder.

1. Confirm the location with me and check Node.js requirements.
2. Read README.md, package.json, and AGENT-SETUP.md before running
   installation commands. Explain the dependencies and scripts.
3. Install dependencies, seed the demo data, and start the app using
   npm install, npm run seed, and npm run dev.
4. Confirm the app opens at http://localhost:5173.
5. Explain the optional Google Places and SMTP settings. Leave them
   unconfigured, and keep AUTO_FOLLOWUPS=false.
6. Ask which personalizations I want before changing the defaults.
   Report the files you changed and any setup failures.

Do not send email, search for real leads, enable automated follow-ups,
or handle my passwords and API keys. Do not overwrite an existing
database, configuration, or attachments folder.
```

## Or install it by hand

Clone the repository or extract the source ZIP into a new folder. Read its setup instructions, then run these commands from that folder:

```bash
npm install
npm run seed
npm run dev
```

Open `http://localhost:5173`. On Windows, `tusk-start.cmd` handles installation and launch. The seed step adds eight fictional demo businesses so you can try the app.

Without integration keys, searches use labeled sample results and emails are logged rather than sent. Optional Google Places and SMTP connections enable real searches and email. Those services have their own accounts, rules, and possible charges.

## The screens

<div class="tusk-shot-grid">
  <figure><img loading="lazy" src="/assets/tusk/tusk-06-powerhour.webp" alt="TUSK Power Hour dialing view"><figcaption><strong>Call sessions.</strong> Work through a queue and record each outcome.</figcaption></figure>
  <figure><img loading="lazy" src="/assets/tusk/tusk-04-outreach.webp" alt="TUSK outreach screen with email preview"><figcaption><strong>Outreach.</strong> Review the lead and your message before sending.</figcaption></figure>
  <figure><img loading="lazy" src="/assets/tusk/tusk-09-mockup.webp" alt="TUSK homepage mockup editor"><figcaption><strong>Mockups.</strong> Create a homepage draft to discuss with a business.</figcaption></figure>
  <figure><img loading="lazy" src="/assets/tusk/tusk-03-territory.webp" alt="TUSK territory map with status markers"><figcaption><strong>Territory.</strong> View leads on a map, marked by status.</figcaption></figure>
  <figure><img loading="lazy" src="/assets/tusk/tusk-07-lead-score.webp" alt="TUSK lead score breakdown"><figcaption><strong>Lead scores.</strong> See the web presence, reviews, and contact details behind a score. A score doesn't predict a sale.</figcaption></figure>
  <figure><img loading="lazy" src="/assets/tusk/tusk-05-pipeline.webp" alt="TUSK sales pipeline columns"><figcaption><strong>Pipeline.</strong> Move leads through stages as conversations progress.</figcaption></figure>
</div>

## A typical workflow { #a-normal-day-in-tusk }

Choose a business type and area, review the leads and website findings, then decide who to contact. Keep notes on the conversation and schedule a follow-up. If a lead becomes a client, track the project and invoice in the same app.

## What else is inside

- Website checks with grades and findings. Treat them as a starting point for review, including any accessibility findings; they aren't a compliance assessment.
- Email templates that use lead details. Check the facts and wording before sending.
- Client records, project files, and invoices.
- An Excel export with dashboard, lead, and client information.

## Data and backups { #private-by-construction }

The app and database run on your computer. Optional Google Places searches and SMTP email send requests and data to those external services. Their credentials are kept in local configuration and used when connecting.

For a backup, stop the app and copy `server/crm.db`, `server/files/`, and your local configuration. Protect the configuration because it can contain credentials. A database copy alone doesn't include attachments or settings.

Email sends require your action with the default configuration. Automatic follow-ups are a separate option; leave `AUTO_FOLLOWUPS=false` unless you intend to enable them.

## License and support { #free-with-a-tip-jar }

The self-hosted source is free under the MIT license. You can [report a problem on GitHub](https://github.com/jordysupport/tusk/issues) or support the project through the optional [Ko-fi tip jar](https://ko-fi.com/support_jordy).

## Prefer it hosted?

A separate hosted version is available at [tuskcrm.com](https://tuskcrm.com/). Check that site for its current terms. The source download here remains free.
