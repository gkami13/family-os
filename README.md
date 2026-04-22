# Family OS

A personal operating system for a dual-career family with two kids and a dog.

Built on Claude CLI + Notion. No custom backend. No app to maintain. Just an agent layer that handles the thinking so we don't have to.

---

## What it does

Three workstreams, unified in Notion:

**Tasks** — Create and track household tasks with assignees and due dates. Nothing falls through. Go or Jillian can ask Claude to create, update, or summarize tasks in plain language.

**Calendar** — Syncs Go's Google Calendar and Outlook work calendar into a shared Notion view. Surfaces weeks where both parents are blocked simultaneously so we can arrange coverage before the morning it happens.

**Meals** — Save a recipe from any URL directly to Notion. Select recipes for the week and get a deduplicated, categorized grocery list — no re-reading five recipes to build a list in your head.

---

## How it works

```
Claude CLI  →  MCP Servers  →  Notion (shared workspace)
                    ↕
         Google Calendar / Outlook
```

- **Claude CLI** is the interface. Natural language in, structured Notion data out.
- **MCP servers** are the connectors — Notion, Google Calendar, Outlook.
- **Notion** is the database and the UI. Go and Jillian both have full access on all devices.

---

## Tech stack

- Claude CLI (Anthropic)
- Notion MCP
- Google Calendar MCP
- Microsoft 365 / Outlook MCP
- Notion (shared workspace, acts as both database and frontend)

---

## Want to run your own?

This repo is built as a reusable template. If you have Claude CLI and a Notion workspace, you can run your own Family OS:

1. Clone this repo
2. Set up the Notion MCP pointed at your workspace
3. Create the Family Tasks and Family Calendar databases in Notion (schemas in `ARCHITECTURE.md`)
4. Follow setup guides in `/docs` for Google Calendar and Outlook connections
5. Run your first task: `"Add task: [whatever's been on your mind], due [date]"`

Setup time: ~30 minutes for someone comfortable with CLI tools.

---

## Project structure

```
Family-OS/
├── README.md
├── ARCHITECTURE.md       # Data model, design decisions, MCP inventory
├── PROJECT-PLAN.md       # 6-week build sequence with rationale
├── CLAUDE.md             # Instructions for Claude when working in this repo
├── stories/              # User stories (one file per feature)
├── docs/                 # Setup guides, ADRs, research notes
├── agents/               # Agent prompt files
├── mcp-servers/          # Custom MCP server code (future)
└── scripts/              # Cron jobs and utility scripts
```

---

## Status

**Phase 1 — Foundation.** Repo initialized, architecture documented, all user stories written. Starting Story 01 (shared task dashboard) next.

Follow along: commits show the build progression, not just the finished state.

---

*Built by Go Kamiyama. Not a product — a working system for one family, open-sourced as a portfolio artifact.*
