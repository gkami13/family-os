# Story 01: Task Manager with Projects and Assignments

## As a
husband or wife

## I want
To create household and personal tasks that belong to specific projects, assign them to each other, and see everything in a single shared Notion view sorted by priority

## So that
We have one place that works like a real task manager — not a flat list, but organized by project, with clear ownership and priority so nothing falls through

## Acceptance Criteria

### Tasks Database
- [ ] A Notion "Family Tasks" database exists with: Title, Project (relation), Assignee, Priority, Status, Due Date, Recurring, Notes
- [ ] husband can create a task via Claude CLI: "Add task: call pediatrician, P1, assigned to wife, due Thursday, project: Kids"
- [ ] Task appears in Notion with all fields populated and linked to the correct project

### Projects Database
- [ ] A separate Notion "Projects" database exists with: Name, Owner, Status, Description
- [ ] Example projects pre-created: Home, Kids, Admin, Dog, Work — husband can add more
- [ ] Each project page in Notion shows all tasks belonging to it (linked view)
- [ ] husband can create a new project via Claude CLI: "Create project: Home Renovation"

### Shared Assignment View
- [ ] A "My Tasks" filtered view exists for husband (shows tasks assigned to husband or Both)
- [ ] A "wife's Tasks" filtered view exists (shows tasks assigned to wife or Both)
- [ ] A "All Open Tasks" view shows everything, grouped by Project, sorted by Priority then Due Date
- [ ] Both husband and wife can see all views in the shared Notion workspace

## Technical Notes
- Two Notion databases: Projects + Family Tasks (Tasks has a Relation field pointing to Projects)
- Notion relation field allows linking tasks to project pages — enables per-project rollup views
- Priority: P1 (do today) | P2 (this week) | P3 (someday/maybe) — default P2
- Status: Not Started | In Progress | Done | Blocked
- Recurring: checkbox — recurring logic (auto-recreate on completion) is deferred to Story 02
- Assignee: Husband | Wife | Both
- The "All Open Tasks" view grouped by Project is the primary dashboard feed for Story 00

## Dependencies
- None — this is the foundation story

## Estimated Effort
4–5 hours (two database schemas + relations + views + CLI wiring for both create task and create project)

## Status
Not Started
