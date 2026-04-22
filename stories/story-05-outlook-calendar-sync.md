# Story 05: Outlook Sync — CONDITIONAL

## Status
**On Hold — validate before building**

## Decision Gate
Before doing any work on this story, check: does husband's Oracle/NetSuite work calendar appear inside his Google Calendar (as a subscribed calendar or auto-synced events)?

- **If yes:** This story is dropped. Work events are already captured by Story 04.
- **If no:** This story is reinstated and built after Story 04.

## If Reinstated — What This Story Does
Syncs husband's Outlook/Microsoft 365 work calendar into the Notion Family Calendar using the same schema and pattern established by Story 04. Adds Source: Outlook and Person: Husband.

## Risk
Oracle corporate IT may block Microsoft Graph API OAuth for third-party applications. If that's the case, the fallback is an iCal subscription URL from Outlook (read-only, no OAuth required, less real-time but functional).

## Estimated Effort (if reinstated)
2–3 hours — same pattern as Story 04, just a different MCP and auth flow.

## Status
On Hold
