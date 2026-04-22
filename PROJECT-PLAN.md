# Family OS — Project Plan

*Last updated: April 21, 2026*
*Capacity: ~5–7 hours/week*

---

## Build Sequence Rationale

The original CLAUDE.md proposed Recipe Capture as the first working feature. **That's wrong for this project.** Here's why:

1. **Task fallthrough is the live pain right now.** Recipe chaos is annoying. Missed household commitments affect real people in real time.
2. **Notion MCP is already wired.** Task coordination requires zero new infrastructure — we can ship value this week.
3. **Jillian becomes a real user immediately.** A shared task board makes this a two-person system from day one, not a demo for one person.
4. **Recipe scraping is higher-risk.** Web scraping + parsing has more failure modes. Tackle it once the project has momentum, not as the opening bet.

Sequence: **Tasks → Calendar → Meals.** Each workstream builds on the pattern of the previous one.

---

## Weekly Plan

### Week 1 — Foundation + First Feature (Stories 01–02)
**Goal:** Have a working shared task system by end of week.

**Hours 1–2: Foundation**
- Initialize GitHub repo (public, from day one)
- Commit this file, ARCHITECTURE.md, all story files, and folder structure
- Write README.md with honest, clear description of what this project is and isn't
- Commit message: `feat: project foundation — architecture, stories, folder structure`

**Hours 3–5: Story 01 — Shared Task Dashboard**
- Verify Notion MCP is working (test read call against existing recipe database)
- Design and create Family Tasks database in Notion (manual creation in Notion UI, then confirm schema via MCP)
- Wire Claude CLI to create a task from natural language input
- Test with 3–5 real household tasks
- Commit: `feat(tasks): story-01 — create tasks via Claude CLI`

**Hours 6–7: Story 02 — Task Status Updates**
- Build update flow: "mark X as done"
- Add fuzzy match for task title lookup
- Test update + completion flows
- Commit: `feat(tasks): story-02 — update task status via Claude CLI`

**Week 1 checkpoint:** Both Go and Jillian can create and complete household tasks through Notion. The system is live and being used.

---

### Week 2 — Task Digest + GitHub Hygiene (Story 03)
**Goal:** Close the loop on the task workstream. Make the repo portfolio-worthy.

**Hours 1–3: Story 03 — Weekly Task Digest**
- Build weekly summary query: open tasks grouped by Overdue / This Week / Upcoming
- Format output for readability in terminal
- Optional: write summary to a Notion page
- Add `/scripts/weekly-digest.sh` cron wrapper
- Commit: `feat(tasks): story-03 — weekly task digest`

**Hours 4–5: Repo hygiene**
- Write a proper README.md (project story, architecture diagram sketch, tech stack, setup instructions)
- Add an Architecture Decision Record (ADR) for the Notion-as-hub decision
- Review all story files — tighten acceptance criteria where vague
- Commit: `docs: README, ADR-001 Notion as hub`

**Week 2 checkpoint:** Task workstream is complete. Repo is presentable. Someone landing on the GitHub page understands what this project is and why it's built this way.

---

### Week 3 — Calendar Sync Begins (Story 04)
**Goal:** Go's personal Google Calendar appears in Notion Family Calendar.

**Hours 1–2: Setup + research**
- Identify the right Google Calendar MCP (evaluate @anthropic or community options)
- Set up OAuth credentials (do NOT commit to repo — document in docs/setup-google-calendar.md)
- Validate MCP can read calendar events

**Hours 3–6: Story 04 — Google Calendar → Notion**
- Design Family Calendar database in Notion (field schema per ARCHITECTURE.md)
- Build sync logic: fetch this week's events → write to Notion
- Implement idempotency check (no duplicate entries on repeat runs)
- Test with real calendar data
- Commit: `feat(calendar): story-04 — Google Calendar sync to Notion`

**Hour 7: Reflection**
- Note any surprises in the Google Calendar MCP API shape
- Update ARCHITECTURE.md if schema needed to change
- Commit: `docs: update architecture after story-04`

**Week 3 checkpoint:** Go's personal calendar is visible in Notion. The calendar sync pattern is proven.

---

### Week 4 — Outlook + Conflict Detection (Stories 05–06)
**Goal:** Full calendar picture for both Go and Jillian. Conflicts are surfaced automatically.

**Hours 1–3: Story 05 — Outlook → Notion**
- Validate corporate Outlook OAuth is feasible (may need IT check first)
- If blocked: document workaround (iCal feed export), ship that instead
- Build sync using same pattern as Story 04 (different Source value)
- Commit: `feat(calendar): story-05 — Outlook work calendar sync`

**Hours 4–7: Story 06 — Conflict Detection**
- Coordinate with Jillian: she authorizes her Google Calendar
- Sync Jillian's calendar into Notion Family Calendar (Person: Jillian)
- Build conflict detection query: time range intersection across both people
- Build family window query: free periods for both simultaneously
- Test with a real week of calendar data
- Commit: `feat(calendar): story-06 — conflict detection and family windows`

**Week 4 checkpoint:** Calendar workstream is complete. "Any conflicts this week?" is a real, answerable question.

---

### Week 5 — Meal Planning Begins (Story 07)
**Goal:** Save a recipe from a URL to Notion in under 30 seconds.

**Hours 1–2: Research + risk validation**
- Test 5 different recipe site URLs manually with web_fetch
- Identify which sites use JSON-LD schema.org/Recipe (NYT Cooking, AllRecipes, etc.) vs. which require HTML heuristics
- Document findings in docs/recipe-scraping-notes.md

**Hours 3–6: Story 07 — Recipe URL Capture**
- Build URL scraper with JSON-LD extraction as primary path, HTML heuristics as fallback
- Wire to Notion recipe database (existing, ID in ARCHITECTURE.md)
- Add duplicate URL detection
- Test with 10 real recipe URLs including at least 2 expected-to-fail paywalled ones
- Commit: `feat(meals): story-07 — recipe URL capture to Notion`

**Hour 7: Buffer**
- Fix any scraping edge cases found during testing
- Add clear error messages for failure modes

**Week 5 checkpoint:** Recipe capture works on the most common recipe sites. The database is being populated with real recipes.

---

### Week 6 — Meal Plan + Grocery List (Story 08)
**Goal:** Full meal planning loop. Recipe selection → grocery list in Notion.

**Hours 1–2: Prerequisite**
- Ensure at least 10 real recipes are in the Notion database (populate if needed using Story 07)
- Review existing recipe schema — confirm ingredient field is populated consistently

**Hours 3–6: Story 08 — Weekly Meal Plan**
- Build recipe lookup by name (fuzzy match)
- Build ingredient aggregation + deduplication logic
- Build category assignment heuristics (Produce / Protein / Dairy / Pantry / Other)
- Write output to Notion Grocery List page + Meal Plan page
- Test with a real week's worth of meals
- Commit: `feat(meals): story-08 — weekly meal plan and grocery list`

**Hour 7: End-to-end test**
- Run all three workstreams back-to-back: create a task, check the calendar, plan meals
- Note friction points — create follow-up stories or backlog items for anything that needs refinement
- Commit: `chore: end-to-end integration test notes`

**Week 6 checkpoint:** All three workstreams are functional. The system is being actively used by both Go and Jillian for real household management.

---

## Backlog (Post-MVP)

These are real, good ideas that are explicitly out of scope for the first 6 weeks:

| Feature                          | Reason Deferred                                      |
|----------------------------------|------------------------------------------------------|
| Amazon basket auto-fill          | Depends on grocery list being reliable first         |
| Push notifications (task assign) | Nice-to-have, adds complexity before core is stable  |
| Next.js frontend                 | Notion is the frontend — no separate app needed      |
| Jillian direct CLI access        | Coordinate after system is proven to be useful       |
| Voice input                      | Phase 6+ — out of scope for core workflows           |
| AI recipe suggestions            | Not the problem we're solving                        |
| Multi-family / SaaS version      | Personal-first, product maybe later                  |

---

## Portfolio Checkpoints

For anyone reviewing this repo as a portfolio artifact, the commits that best demonstrate systems and ops thinking are:

- `feat: project foundation` — shows structured thinking before writing code
- `docs: README, ADR-001` — shows documentation discipline
- `feat(tasks): story-01–03` — shows incremental vertical slice delivery
- `docs: update architecture after story-04` — shows willingness to update design based on reality
- Any commit where the story acceptance criteria drove the implementation (look at story files vs. commit diffs)

The goal is not a polished product. The goal is a repo that tells a coherent story about how a systems thinker builds software: deliberately, incrementally, with documented decisions.
