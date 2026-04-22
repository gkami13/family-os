# Story 03: Weekly Task Digest

## As a
Go

## I want
A weekly summary of all open and overdue tasks, grouped by assignee, delivered as a Notion page or CLI output every Sunday evening

## So that
We start each week with full situational awareness — no surprises about what's fallen behind

## Acceptance Criteria
- [ ] Running "weekly digest" via Claude CLI generates a summary of all open tasks
- [ ] Summary groups tasks by: Overdue | Due This Week | Upcoming
- [ ] Each group shows assignee and task count
- [ ] Overdue tasks are explicitly flagged (not buried)
- [ ] Output is readable in terminal AND optionally written to a Notion page
- [ ] Can be triggered manually or on a schedule (cron)

## Technical Notes
- Reads from Notion Family Tasks database (Story 01 schema)
- Date comparison logic: today vs. Due Date field
- Optional: cron job in /scripts to auto-trigger Sunday at 6pm
- This story validates that the task database is actually being used consistently

## Dependencies
- Story 01 and Story 02 must be complete (need real tasks to summarize)

## Estimated Effort
2–3 hours (query + grouping logic + formatting)

## Status
Not Started
