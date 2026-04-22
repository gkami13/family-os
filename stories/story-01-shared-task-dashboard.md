# Story 01: Shared Task Dashboard

## As a
Go or Jillian

## I want
To create a household task in Notion with a title, assignee (Go or Jillian), due date, and category (Home, Kids, Admin, Dog)

## So that
Nothing falls through the cracks — every task has an owner and a deadline, visible to both of us

## Acceptance Criteria
- [ ] A Notion database exists called "Family Tasks" with fields: Title, Assignee, Due Date, Category, Status, Notes
- [ ] Go can create a task via Claude CLI in natural language (e.g. "Add task: schedule Hiro's vet appointment, assigned to Jillian, due Friday")
- [ ] Task appears in Notion with correct fields populated
- [ ] Both Go and Jillian can view all open tasks in one Notion view
- [ ] Tasks are filterable by Assignee and Status

## Technical Notes
- Uses existing Notion MCP (read/write)
- Notion database schema must be defined before any task creation
- Status field: Not Started | In Progress | Done
- Category field: Home | Kids | Admin | Dog | Other
- Assignee field: Go | Jillian | Both
- This story establishes the Notion data model that all task stories depend on

## Dependencies
- None (first story, foundational)

## Estimated Effort
3–4 hours (schema design + MCP wiring + test with real tasks)

## Status
Not Started
