# Story 06: Joint Family Calendar View

## As a
Go and Jillian

## I want
A single unified calendar view in Notion showing both Go's and Jillian's events side by side, merged by day, so we can see the full family week at a glance

## So that
We replace the mental overhead of "let me check your calendar" — the answer is always one Notion view away, visible on any device

## Acceptance Criteria

### Jillian's Calendar Sync
- [ ] Google Calendar MCP is authenticated with Jillian's Google account (requires her to authorize)
- [ ] Jillian's events sync into the same Notion Family Calendar database as Go's, with Person: Jillian
- [ ] Same rolling 2-week sync window as Story 04

### Unified Calendar View
- [ ] A Notion view called "Family Calendar" shows all events grouped by date, sorted by start time
- [ ] Events are visually distinguishable by person (Notion filter + color by Person field)
- [ ] This view is accessible to both Go and Jillian from the shared workspace

### Conflict Detection
- [ ] A separate "Conflicts" view or query surfaces windows where both Go and Jillian have events at the same time
- [ ] Claude can answer "any conflicts this week?" by querying the Notion database and returning overlapping windows
- [ ] "Family windows" — blocks where both are free — can also be queried: "when are we both free this week?"

## Technical Notes
- Jillian's calendar sync uses the same Google Calendar MCP pattern as Story 04 — just authenticated with her account
- Conflict detection algorithm: for each hour slot, check if both Person: Go AND Person: Jillian have an event
- MVP conflict detection: same-day overlap is good enough (exact time overlap is a stretch goal)
- The Notion "Family Calendar" view is the calendar section of the Story 00 unified dashboard
- Coordinate with Jillian for Google OAuth — this is a people dependency, not just a technical one

## Dependencies
- Story 04 must be complete (establishes sync pattern and Notion schema)

## Estimated Effort
4–5 hours (Jillian calendar auth + sync + conflict query logic + Notion views)

## Status
Not Started
