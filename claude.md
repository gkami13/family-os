# Family OS — Claude Instructions

## Project Overview

**Name:** Family OS
**Owner:** husband (Strategic Program Manager at Oracle/NetSuite)
**Users:** husband and wife (spouse, Director of New Business Mid-Market Sales at monday.com)
**Purpose:** A personal operating system that unifies meal planning, calendar management, and household task coordination for a dual-career family with two young children and a large dog.
**Secondary purpose:** Public portfolio project demonstrating practical AI/MCP engineering skills — positioning for Director-level GTM Strategy and Operations roles at innovative AI-forward companies (Anthropic, Databricks, MongoDB, Snowflake, etc.).

## Vision

Build a locally-run, agent-orchestrated system that reduces household mental load by unifying three core workstreams:

1. **Meal Planning** — Recipe capture (URL → Notion → ingredients → grocery list → Amazon basket)
2. **Calendar Aggregation** — Outlook + Google + Work calendars → unified Notion view, conflict detection, family time windows
3. **Task Coordination** — Shared Notion dashboard for household task delegation between husband and wife

The project is built publicly on GitHub to serve as a portfolio artifact. Commits should show progression, thinking, and architecture decisions — not just polished end states.

## Tech Stack

- **Primary interface:** Claude CLI + Cowork (local, file-based)
- **Source of truth:** Notion (tasks, meal plans, recipes database, shared dashboard)
  - Recipe database ID: `3332cb98-3974-80ed-9f8d-d37ffaf21f9c`
- **Calendar sources:** Outlook (work), Google Calendar (personal), Work Calendar
- **MCP servers:** Notion MCP (existing), Google Calendar MCP, custom calendar aggregator (to build)
- **Frontend (future):** Next.js app OR Notion dashboard as UI layer
- **Version control:** GitHub (public repo from day one)
- **Automation:** Cron jobs for periodic syncs (already in use for recipe processing)

## Architecture Principles

- **Incremental vertical slices.** Each phase ships one end-to-end feature. No big-bang builds.
- **Notion as hub.** All persistent state lives in Notion. MCPs read/write from there.
- **CLI-first, UI second.** Prove logic and flow in CLI before building frontend.
- **Small, focused user stories.** One function per story max. Ship, test, iterate.
- **Public repo from day one.** Rough code is fine. Progression matters more than polish.

## Project Phases

### Phase 1 — Foundation (Week 1)
- Set up GitHub repo with clear README describing Family OS vision
- Folder structure: `/docs`, `/agents`, `/mcp-servers`, `/stories`, `/scripts`
- Write project brief (this file is the kickoff)
- Commit zero: architecture sketch + project plan

### Phase 2 — User Stories & Architecture (Week 1)
- Workshop 5–7 focused user stories for MVP
- Store under `/stories` as individual markdown files
- Create `ARCHITECTURE.md` documenting data model and decisions
- No code yet — this phase is deliberate planning

### Phase 3 — First Vertical Slice (Weeks 2–3)
- **Feature:** Recipe URL → Notion entry with extracted ingredients
- Touches Notion MCP, proves the pipeline, immediately useful
- Test with real recipes, iterate

### Phase 4 — Second Slice (Weeks 3–4)
- **Feature:** Calendar aggregation from Outlook + Google + Work → unified Notion view
- Teaches MCP orchestration and multi-source data handling

### Phase 5 — Third Slice (Week 5)
- **Feature:** Task coordination layer in Notion with shared husband/wife dashboard
- Real-world test: both users actively using it for household tasks

### Phase 6 — Polish & UI (Week 6+)
- Optional Next.js frontend OR lean into Notion dashboard as UI
- Add quality-of-life features: notifications, voice input, mobile access

## Current Phase

**Phase 1 — Foundation.** Setting up repo structure and project documentation.

## User Story Format

Each story is a markdown file in `/stories/` with this structure:

```
# Story: [Short Title]

## As a
[user role]

## I want
[goal]

## So that
[benefit]

## Acceptance Criteria
- [ ] Specific, testable outcome 1
- [ ] Specific, testable outcome 2

## Technical Notes
- Relevant MCP, API, or library
- Data model touchpoints

## Status
Not Started | In Progress | Complete
```

## How to Work with Claude on This Project

When Claude is invoked in this directory (via Claude CLI or Cowork), it should:

1. **Read this file first** to understand the project context.
2. **Check `/stories`** to see active user stories and current phase.
3. **Ask which story or phase** the user wants to work on before writing code.
4. **Write small, focused changes.** One user story at a time. No scope creep.
5. **Commit often** with clear messages describing what and why.
6. **Update `ARCHITECTURE.md`** when architecture decisions are made or changed.
7. **Reference other open-source projects** for patterns, but build original work in this repo. Credit inspirations in README.

## Learning Goals for husband

This project is also a learning vehicle. Track progress against these skills:

- MCP server design and implementation
- Multi-source data orchestration
- Evals framework (potential future addition)
- Git workflow and public repo hygiene
- Next.js / frontend basics (Phase 6)
- Agent architecture and prompting patterns

## Non-Goals (For Now)

- Mobile native app — deferred until core works on desktop
- Multi-family SaaS — this is personal first, portfolio second, product maybe later
- Real-time collaboration — Notion handles this adequately for MVP
- AI-generated recipes — focus on capture and organization, not generation

## References & Inspiration

- Personal knowledge OS patterns (to study on GitHub before building)
- Notion MCP reference implementations
- Existing meal planning open source projects
- Family dashboard repos

## Communication Style

- **Auditory learner.** Podcast-format explanations work well. Avoid dense walls of text when discussing.
- **Direct and practical.** Skip excessive preamble. Get to the point.
- **Challenge assumptions.** Push back if scope is creeping or a decision seems off.
- **Celebrate shipping.** Each commit that moves a story forward is a win.

---

*Last updated: April 21, 2026*
*Project start: Phase 1*
