## Source Control Guidelines

When working with Git, follow safe and clean version control practices.

---

## 1. Validate .gitignore

Before committing or pushing:

- Ensure `.gitignore` exists at the root
- Verify it includes at least:

    node_modules/
    dist/
    build/
    .env
    .DS_Store

If using a frontend setup inside `/frontend`, also ensure:

    frontend/node_modules
    frontend/dist

If anything is missing:
- Suggest updates
- Do not proceed blindly

---

## 2. Review Changes Before Commit

- Check modified files
- Avoid committing:
  - node_modules
  - build artifacts
  - unnecessary logs or temp files

- Keep commits focused and minimal
- Group related changes together

---

## 3. Commit Process

- Ask the user for a commit message if not provided
- Suggest a clean, descriptive message if needed
- Avoid vague messages like "update" or "fix"

---

## 4. Branch Awareness (IMPORTANT)

Before pushing:

- Check the current branch:

    git branch --show-current

- If unclear or not specified:
  - Ask the user which branch to push to

- Do NOT assume:
  - main
  - master
  - any default branch

---

## 5. Push Workflow

Before pushing:

- Confirm with the user:
  - target branch
  - intent to push

Example:

    "You're on branch 'feature/ui-setup'. Do you want to push to this branch?"

Only proceed after explicit user confirmation.

---

## 6. Execute Push

Once confirmed:

    git push origin <branch-name>

---

## Rules

- Never push without user confirmation
- Never assume branch or intent
- Never commit ignored or unnecessary files
- Always prioritize clean and safe version control

---

## Outcome

- Clean commit history
- Proper branch usage
- No accidental leaks or messy pushes