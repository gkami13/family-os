# Story 06: Family Conflict Detection

## As a
Go and Jillian

## I want
The system to detect when Go and Jillian are both blocked (in meetings or commuting) during the same window, and surface those gaps

## So that
We can proactively arrange childcare or coverage instead of discovering the conflict the morning it happens

## Acceptance Criteria
- [ ] Jillian's Google Calendar (monday.com work + personal) syncs into Notion Family Calendar with Person: Jillian
- [ ] System can query: "show me windows this week where both Go and Jillian are busy at the same time"
- [ ] Conflicts are surfaced as a list: Date | Time Window | Go's event | Jillian's event
- [ ] System also surfaces "family windows" — blocks where both are free simultaneously
- [ ] Output is available via CLI query ("any conflicts this week?")

## Technical Notes
- Requires Jillian's calendar to be connected (coordinate with Jillian for OAuth)
- Conflict algorithm: time range intersection across both people's events
- Family window algorithm: inverse of conflict — periods where neither has calendar blocks
- "Busy" definition for MVP: any event (no free/busy status parsing needed yet)
- Privacy consideration: Jillian's work events should be synced with her consent and awareness

## Dependencies
- Story 04 and Story 05 must be complete
- Requires Jillian's coordination for calendar auth

## Estimated Effort
4–5 hours (Jillian calendar sync + intersection logic + CLI query)

## Status
Not Started
