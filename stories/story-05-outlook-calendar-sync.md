# Story 05: Outlook (Work) Calendar → Notion Sync

## As a
Go

## I want
My Oracle/NetSuite Outlook work calendar to also sync into the same Notion Family Calendar view

## So that
Jillian can see when I'm in back-to-back meetings or traveling for work, without needing to text me

## Acceptance Criteria
- [ ] Microsoft 365 / Outlook MCP is installed and authenticated with Go's work account
- [ ] Work calendar events sync into the same Family Calendar Notion database as Story 04
- [ ] Events are tagged with Source: Outlook and Person: Go
- [ ] The unified Notion view shows both Google and Outlook events in chronological order
- [ ] Sensitive work meeting titles can optionally be redacted (configurable flag, default off for MVP)

## Technical Notes
- Requires Microsoft Graph API / Outlook MCP (likely MS365 MCP)
- Work account may have OAuth restrictions — validate corporate policy before building
- Same Notion schema as Story 04 — just a different Source value
- This story is intentionally narrow: no Jillian calendar sync yet (that's Story 06 scope)
- Risk: corporate Outlook may block OAuth for third-party apps — document workaround if needed

## Dependencies
- Story 04 must be complete (establishes Notion calendar schema and sync pattern)

## Estimated Effort
3–4 hours (MCP setup + auth + delta sync from Story 04 pattern)

## Status
Not Started
