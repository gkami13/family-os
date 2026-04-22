# Story 10: Granola Meeting Notes → Notion Sync

## As a
husband

## I want
My Granola meeting transcripts and summaries to automatically sync into Notion, organized by date and project, so my meeting notes live in the same place as my tasks and plans

## So that
I have a complete picture of my work life in one place — what I decided in meetings is connected to the tasks those meetings created

## Acceptance Criteria
- [ ] Granola MCP is connected and can fetch husband's recent meeting transcripts
- [ ] A cron job (or manual trigger) fetches meetings from the last 24 hours and creates Notion pages for each
- [ ] Each Notion page contains: Meeting title, Date, Attendees, Transcript or summary, Action items (extracted)
- [ ] Meetings are stored in a "Meeting Notes" section of husband's existing Notion workspace
- [ ] Action items extracted from meetings can optionally be pushed to the Family Tasks database as P2 tasks assigned to husband
- [ ] If Notion AI is available (subscription active): meeting content is summarized via Notion AI before saving. If not: raw Granola summary is used as-is.

## Technical Notes
- Granola MCP is already available in this environment (list_meetings, get_meeting_transcript tools)
- Notion AI summarization requires Notion AI add-on — design the story to work with OR without it (graceful degradation)
- Cron job lives in /scripts/granola-sync.sh — runs nightly or on demand
- Action item extraction: simple heuristic scan for "I'll", "we'll", "follow up", "action:" patterns in transcript
- This story touches husband's personal Notion only — not the shared Family OS workspace unless an action item gets assigned

## Dependencies
- Story 01 must be complete (so extracted action items can be pushed to Family Tasks)
- Granola account must be active and MCP authenticated

## Estimated Effort
4–5 hours (Granola MCP integration + Notion write + action item extraction + cron setup)

## Build Timing
Week 6+ — after core workstreams are stable. This is a quality-of-life feature, not a foundation piece.

## Status
Not Started
