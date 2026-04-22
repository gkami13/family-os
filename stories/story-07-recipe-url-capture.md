# Story 07: Recipe URL → Notion Capture

## As a
husband or wife

## I want
To paste a recipe URL into Claude CLI and have the recipe automatically saved to our Notion recipe database with title, ingredients, and source URL

## So that
We stop bookmarking recipes in random places and lose them — everything lives in one place we can actually search

## Acceptance Criteria
- [ ] Running "save recipe https://..." extracts: Recipe Name, Ingredients list, Source URL, Cuisine tag (auto-inferred), Prep Time (if available)
- [ ] Recipe is saved to the existing Notion recipe database (ID: 3332cb98-3974-80ed-9f8d-d37ffaf21f9c)
- [ ] Duplicate detection: if the same URL already exists, Claude warns instead of creating a duplicate
- [ ] If extraction fails (paywalled site, JavaScript-heavy page), Claude returns a clear error with the URL
- [ ] Saved recipe is immediately viewable in Notion

## Technical Notes
- URL scraping: use web_fetch or a lightweight HTML parser (BeautifulSoup or similar)
- Recipe schema targets: JSON-LD structured data (schema.org/Recipe) first, then fallback to HTML heuristics
- Notion recipe database ID: 3332cb98-3974-80ed-9f8d-d37ffaf21f9c (already exists)
- Ingredients should be stored as a multi-line text field for MVP (not a structured list)
- Paywall detection: if extracted content is < 200 chars, flag as likely blocked

## Dependencies
- Stories 01–06 are independent of this; this is a separate workstream
- Notion MCP must be available (same as task stories)

## Estimated Effort
4–5 hours (scraping + schema.org parsing + Notion write + duplicate check)

## Status
Not Started
