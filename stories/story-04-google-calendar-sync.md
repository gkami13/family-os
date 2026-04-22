# Story 04: Go's Google Calendar → Notion Sync

## As a
Go

## I want
All of my Google Calendar events (personal + work, since work is already in Google Cal) to sync into the Notion Family Calendar database

## So that
My full schedule — work meetings and personal commitments — is visible in the Family OS dashboard without me having to manually update anything

## Acceptance Criteria
- [ ] Google Calendar MCP is authenticated with Go's Google account
- [ ] All calendars visible in Go's Google Calendar are synced (personal + any subscribed work calendar)
- [ ] Events written to Notion Family Calendar with: Title, Date, Start/End Time, Person: Go, Source: Google, All-Day flag
- [ ] Sync covers current week + next week (rolling 2-week window)
- [ ] Sync is idempotent — running twice doesn't create duplicate entries (idempotency key: Google event ID)
- [ ] Work events Go wants to keep private can be marked "Busy" instead of showing the title (configurable per calendar, default: show title)

## Technical Notes
- Google Calendar MCP fetches all calendars the user has access to, not just primary
- Risk: Oracle/NetSuite may sync work events into Google Calendar automatically, OR Go may see them as a separate subscribed calendar. Validate before building — both cases are handleable, just different calendar IDs to query.
- If work calendar does NOT appear in Google Cal: Story 05 (Outlook) gets reinstated. If it does: Story 05 is dropped.
- Idempotency key: Google Calendar event ID stored in the External ID field
- Notion Family Calendar schema per ARCHITECTURE.md

## Dependencies
- None (first calendar story)

## Estimated Effort
4–5 hours (MCP auth + multi-calendar fetch + Notion write + idempotency)

## Status
Not Started
