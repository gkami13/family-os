# Family OS — Architecture

*Last updated: April 21, 2026*

---

## System Overview

Family OS is a locally-run, agent-orchestrated household operating system. It reduces the mental load of managing a dual-career family by unifying three workstreams — tasks, calendars, and meal planning — into a single source of truth in Notion.

The system is intentionally simple: Claude CLI is the interface, Notion is the database, and MCP servers are the connectors. There is no custom backend, no deployed service, and no app to maintain. All state lives in Notion. All logic runs locally.

---

## Core Design Decisions

### Decision 1: Notion as the single source of truth

All persistent data lives in Notion. Tasks, calendar events, recipes, and meal plans are Notion database entries. Claude reads and writes through the Notion MCP.

**Why:** Notion gives both husband and wife a shared, always-accessible view without any custom frontend work. It handles multi-device sync, permissions, and UI for free. We build the logic layer; Notion handles persistence and presentation.

**Trade-off accepted:** Notion has API rate limits and occasional latency. For a household tool with low query volume, this is fine.

### Decision 2: MCP servers as the only integration layer

Every external system (Notion, Google Calendar, Outlook, future Amazon) is connected via an MCP server. Claude does not call APIs directly. All external calls go through MCP.

**Why:** MCP servers are composable, swappable, and testable in isolation. If Google Calendar changes its API, we update one MCP server — not every script that touches it. This also makes the architecture legible to engineers reviewing the repo for portfolio purposes.

**Trade-off accepted:** MCP server setup has upfront overhead vs. raw API calls. Worth it for long-term maintainability.

### Decision 3: Resequenced workstream priority

The original project plan led with Recipe Capture (Phase 3 in CLAUDE.md). After scoping, **Task Coordination ships first**. Rationale:

1. It solves the highest-pain problem immediately (task fallthrough)
2. The Notion MCP is already configured — no new auth or MCP setup required
3. It delivers value to wife immediately, making her a real user vs. a future one
4. Recipe capture requires web scraping + parsing work that is higher-risk for a first slice

### Decision 4: CLI-first, no frontend until Phase 6

Every feature is built and validated via Claude CLI before any UI is considered. Next.js or a Notion-as-UI approach is deferred until all three core workstreams are working end-to-end.

**Why:** Premature frontend work is the graveyard of side projects. Prove the logic first.

---

## Data Model

### Notion Database IDs

Two ID types exist — use the right one for the right tool:
- **Page ID** (from URL) — used by Python `notion-client` and direct REST API calls
- **Data Source ID** (collection ID) — used by Notion MCP internally

| Database      | Page ID (REST API / Python)              | Data Source ID (MCP only)              |
|---------------|------------------------------------------|----------------------------------------|
| Family OS hub | 34a2cb98-3974-8170-9c3e-c3746f6e9b8f    | —                                      |
| Projects      | c5ca349e-adad-491c-8a3f-16e2b82b506a    | dc95ad9e-28ed-4474-a904-882e65447128   |
| Family Tasks  | 395f395a-c3de-4dda-a8e8-6518e3c0377a    | accaebb5-6f39-4c98-9902-d5b5a6124643   |
| Meal Planner  | 3332cb98-3974-80ed-9f8d-d37ffaf21f9c    | 3332cb98-3974-808d-b6dc-000b742030b8   |

### Projects (Notion Database)

| Field       | Type          | Values                                    |
|-------------|---------------|-------------------------------------------|
| Name        | Title         | Free text                                 |
| Owner       | Select        | husband \| wife \| Both                    |
| Status      | Select        | Active \| On Hold \| Complete             |
| Description | Text          | Free text                                 |

Default projects: Home, Kids, Admin, Dog, Work. husband can create new projects at any time. Each project page shows a linked view of all tasks belonging to it.

### Family Tasks (Notion Database)

| Field       | Type          | Values                                        |
|-------------|---------------|-----------------------------------------------|
| Title       | Title         | Free text                                        |
| Project     | Relation      | → Projects database                              |
| Assignee    | Select        | husband \| wife \| Both                           |
| Priority    | Select        | P1 (do today) \| P2 (this week) \| P3 (someday) |
| Status      | Select        | Not Started \| In Progress \| Done \| Blocked   |
| Due Date    | Date          | Date picker                                      |
| Recurring   | Checkbox      | Boolean — task reappears after completion        |
| Notes       | Text          | Free text                                        |

Default sort: Priority ascending, then Due Date ascending. This powers the dashboard tasks view.

Three key Notion views: "My Tasks" (husband), "wife's Tasks", "All Open Tasks" grouped by Project.

### Family Calendar (Notion Database)

| Field       | Type          | Values                                    |
|-------------|---------------|-------------------------------------------|
| Title       | Title         | Event name                                |
| Person      | Select        | husband \| wife                            |
| Date        | Date          | Date + time                               |
| End Time    | Text          | ISO time string (MVP: text field)        |
| Source      | Select        | Google \| Outlook \| monday.com          |
| All-Day     | Checkbox      | Boolean                                   |
| External ID | Text          | Source system event ID (idempotency key) |

### Recipe Database (existing Notion Database — ID: 3332cb98-3974-80ed-9f8d-d37ffaf21f9c)

Existing schema — do not modify without confirming current field names via Notion MCP first.

Expected fields: Title, Source URL, Ingredients (text), Cuisine, Prep Time

### Work Notes (Notion Database)

| Field       | Type          | Values                                          |
|-------------|---------------|-------------------------------------------------|
| Title       | Title         | Free text                                       |
| Date        | Date          | Auto-populated to today on creation             |
| Content     | Text          | Rich text — the actual note                     |
| Tags        | Multi-select  | Work \| Personal \| Meeting \| Idea \| Follow-up|

Sorted by Date descending. Surfaces in the husband-only section of the Unified Dashboard.

### Meal Plan (Notion Page per week)

Simple structured page, not a database. Format:

```
Grocery List - Week of [date]

## Produce
- Garlic x3
- Spinach (2 bags)

## Protein
- Chicken thighs (2 lbs)
...
```

---

## MCP Server Inventory

| MCP Server          | Status        | Auth Required        | Used By           |
|---------------------|---------------|----------------------|-------------------|
| Notion MCP          | Configured    | Notion API key       | Stories 01–03, 07–08 |
| Google Calendar MCP | To configure  | Google OAuth (husband + wife separately) | Stories 04, 06 |
| MS365 / Outlook MCP | Conditional   | Only needed if work calendar is NOT in husband's Google Cal — validate first | Story 05 |
| Granola MCP         | Available     | Granola account      | Story 10             |

---

## Folder Structure

```
Family-OS/
├── CLAUDE.md             # Project instructions for Claude
├── ARCHITECTURE.md       # This file
├── PROJECT-PLAN.md       # Sequenced weekly build plan
├── README.md             # Public-facing project description (to be written)
├── stories/              # User stories (one file per story)
│   ├── story-01-shared-task-dashboard.md
│   ├── story-02-task-status-updates.md
│   ├── story-03-weekly-task-digest.md
│   ├── story-04-google-calendar-sync.md
│   ├── story-05-outlook-calendar-sync.md
│   ├── story-06-conflict-detection.md
│   ├── story-07-recipe-url-capture.md
│   └── story-08-weekly-meal-plan.md
├── docs/                 # Supplementary docs, ADRs, research notes
├── agents/               # Agent prompt files and orchestration logic
├── mcp-servers/          # Custom MCP server code (if/when we build custom ones)
└── scripts/              # Cron jobs, utility scripts, setup automation
```

---

## Known Risks

**Validate work calendar visibility in Google Calendar before building Story 05.** husband's Oracle/NetSuite work calendar may already appear in his Google Calendar as a subscribed calendar, making Outlook sync unnecessary. Check this first — if work events are in Google Cal, Story 05 is dropped entirely.

**Outlook OAuth may be blocked by Oracle corporate policy.** If Microsoft Graph API OAuth is restricted for third-party apps on husband's work account, Story 05 needs a workaround (manual export, iCal feed, or IT exception). Validate before building Story 05.

**Recipe scraping is unreliable.** Many recipe sites are JavaScript-heavy or paywalled. Story 07 should implement graceful fallback and explicit failure messaging rather than attempting to scrape everything.

**wife's buy-in is required for calendar sync (Story 06).** She needs to authorize her Google account. This is a coordination dependency, not a technical one — sequence accordingly.

---

## Future Considerations (Not In Scope)

- Amazon basket auto-fill from grocery list
- Push notifications (SMS/email) for task assignments
- Voice input via Siri Shortcut or similar
- AI recipe generation
- Native mobile app

## Frontend Decision: Notion as the UI

Notion is the frontend. Full stop.

husband and wife share the same Notion workspace and already have access on all their devices. Building a separate web app would recreate things Notion does for free: multi-device sync, shared views, permissions, mobile access, real-time updates.

The system Claude builds and maintains is the logic and orchestration layer — creating tasks, syncing calendars, generating grocery lists. Notion surfaces all of that to both users without any frontend work required.

Next.js is explicitly off the roadmap unless Notion stops being sufficient.
