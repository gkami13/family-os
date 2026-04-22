# Story 00: Unified Daily Driver Dashboard

## As a
husband (primary) and wife

## I want
A single Notion page I open every morning that shows everything in one place: today's tasks by priority, this week's calendar events, the meal plan, and a section for work notes

## So that
I don't need to open five different apps to know what's happening today — one page gives me full situational awareness in under 60 seconds

## The Dashboard Layout

```
┌─────────────────────────────────────────────────────────────┐
│  FAMILY OS — [Today's Date]                                 │
├───────────────────┬─────────────────────────────────────────┤
│  TODAY'S TASKS    │  THIS WEEK'S CALENDAR                   │
│  ─────────────    │  ──────────────────────                 │
│  🔴 P1 items      │  Mon  husband: 9am standup                   │
│  🟡 P2 items      │       wife: 2pm QBR                  │
│  ⚪ P3 items      │  Tue  ...                                │
│                   │  Wed  CONFLICT: both blocked 2–4pm      │
├───────────────────┼─────────────────────────────────────────┤
│  THIS WEEK'S MEALS│  WORK NOTES                             │
│  ─────────────    │  ────────────                           │
│  Mon: Chicken...  │  [Quick capture, dated entries]         │
│  Wed: Pasta...    │                                         │
│  Fri: Tacos       │                                         │
└───────────────────┴─────────────────────────────────────────┘
```

## Acceptance Criteria
- [ ] A single Notion page exists called "Family OS Dashboard"
- [ ] Tasks section: linked view of Family Tasks database, filtered to open items, sorted by Priority then Due Date
- [ ] Calendar section: linked view of Family Calendar database, filtered to current week, grouped by day
- [ ] Conflicts flagged visually in the calendar section (both husband and wife blocked at same time)
- [ ] Meals section: linked view of current week's meal plan
- [ ] Work Notes section: inline database or linked notes database for quick capture
- [ ] Dashboard is pinned/favorited in Notion for both husband and wife
- [ ] Opening the dashboard takes under 3 seconds and requires no manual refresh

## Technical Notes
- This story is primarily Notion configuration, not code
- Linked database views are native Notion — no MCP calls needed to render the dashboard
- The dashboard is the destination; all other stories populate the data that feeds it
- Build this as a spec/wireframe in Notion first, then fill it in as each workstream ships
- Conflicts section depends on Story 06 (calendar sync for both husband and wife)
- Meals section depends on Story 08 (meal planning)

## Build Order Note
This story is Story 00 because it defines the destination. Build the skeleton Notion page in Week 1 alongside Story 01. Add sections to it as each subsequent story ships. By Week 6 it's fully populated.

## Dependencies
- Skeleton: none (create the page structure in Week 1)
- Tasks section: Story 01
- Calendar section: Stories 04–06
- Meals section: Stories 07–08
- Work Notes: Story 09

## Estimated Effort
2–3 hours total across the project (30 min setup in Week 1, then 20–30 min per workstream as each ships)

## Status
Not Started
