# Story 02: Task Status Updates

## As a
husband or wife

## I want
To update a task's status (In Progress, Done) and add a note via Claude CLI

## So that
The other person can see real-time progress without having to ask "did you handle that?"

## Acceptance Criteria
- [ ] husband or wife can say "Mark the vet appointment task as done" and Claude finds the right task and updates it
- [ ] Claude handles ambiguous task names gracefully — confirms before updating if multiple matches
- [ ] Completed tasks are visually separated in the Notion view (e.g. moved to a Done section or filtered out)
- [ ] Optional note can be added on completion (e.g. "Done — appointment is June 3rd at 2pm")
- [ ] If a task can't be found, Claude returns a clear error rather than silently failing

## Technical Notes
- Builds on Story 01's Notion database schema
- Requires Notion MCP update (PATCH operation on task record)
- Fuzzy matching on task title (partial string match is acceptable for MVP)
- No authentication layer needed — both husband and wife use the same shared Notion workspace

## Dependencies
- Story 01 must be complete

## Estimated Effort
2–3 hours (update logic + fuzzy match + edge case handling)

## Status
Not Started
