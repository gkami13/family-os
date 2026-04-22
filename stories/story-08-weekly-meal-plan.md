# Story 08: Weekly Meal Plan + Grocery List

## As a
Go or Jillian

## I want
To select recipes for the week and have the system generate a combined grocery list, deduplicated and organized by category

## So that
Grocery shopping takes 10 minutes instead of 30 — no more re-reading five recipes to build a list in my head

## Acceptance Criteria
- [ ] Go can say "plan meals for this week: Monday - Chicken Tikka, Wednesday - Pasta Primavera, Friday - Tacos"
- [ ] System looks up each recipe in Notion by name (fuzzy match acceptable)
- [ ] Combined ingredient list is generated, with duplicate ingredients merged (e.g. two recipes needing garlic → "garlic x3")
- [ ] Grocery list is organized by category: Produce | Protein | Dairy | Pantry | Other
- [ ] List is written to a Notion page titled "Grocery List - Week of [date]"
- [ ] Meal plan is also written to a Notion "Meal Plan" page showing which recipe is on which day

## Technical Notes
- Depends on Story 07 having populated the recipe database with real recipes
- Ingredient parsing: split multi-line ingredients field and extract item + quantity
- Deduplication is hard — MVP approach: same ingredient name = merge, don't try to parse units
- Category assignment: keyword-based heuristic (e.g. "chicken" → Protein, "spinach" → Produce)
- Amazon basket integration (auto-add to cart) is explicitly out of scope for this story

## Dependencies
- Story 07 must be complete and recipe database must have ≥5 real recipes saved

## Estimated Effort
5–6 hours (ingredient parsing + dedup logic + categorization + Notion write)

## Status
Not Started
