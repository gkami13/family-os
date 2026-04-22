# Story 04: Google Calendar → Notion Sync

## As a
Go

## I want
My personal Google Calendar events to appear in a unified Notion "Family Calendar" view for the current week

## So that
Jillian and I can see my schedule without me narrating it — reducing "are you free Thursday?" friction

## Acceptance Criteria
- [ ] Google Calendar MCP is installed and authenticated with Go's Google account
- [ ] Running "sync calendar" pulls this week's events from Google Calendar
- [ ] Events are written to a Notion "Family Calendar" database with: Title, Date/Time, Duration, Calendar Source (Google), Person (Go)
- [ ] Sync is idempotent — running it twice doesn't duplicate entries
- [ ] Past events are not re-synced on subsequent runs

## Technical Notes
- Requires Google Calendar MCP (likely @anthropic/google-calendar-mcp or equivalent)
- Notion database schema for Family Calendar: Title | Date | Start Time | End Time | Person | Source | All-Day flag
- Idempotency key: event ID from Google Calendar
- Week scope for MVP — no need for month-long lookback on first pass
- OAuth credentials for Google Calendar must be stored securely (not committed to repo)

## Dependencies
- Story 01 establishes the pattern; this is independent in terms of Notion schema
- Google Calendar MCP must be available (may require build/configure step)

## Estimated Effort
4–5 hours (MCP setup + auth + sync logic + idempotency)

## Status
Not Started
