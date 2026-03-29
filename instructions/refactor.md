## Codebase Refactoring Guidelines

When asked to refactor the project structure, follow clean and scalable full-stack conventions.

---

## Goal

Restructure the project to support both frontend and backend in a clear, maintainable way.

---

## Target Structure

Move from a single root-level frontend setup to:

    /frontend   → React + Vite app
    /backend    → Future backend (Node/Express or similar)
    /instructions
    CLAUDE.md
    README.md

---

## Refactoring Steps

### 1. Create Folder Structure

- Create a `/frontend` directory
- Move all existing frontend-related files into `/frontend`

This includes:
- src/
- public/ (if exists)
- index.html
- package.json
- vite.config.js
- tailwind.config.js
- postcss.config.js
- .gitignore (merge carefully if needed)

---

### 2. Fix Paths & Imports

- Ensure all imports still work after moving files
- Update any relative paths if broken
- Verify Tailwind content paths include:

    ./index.html
    ./src/**/*.{js,ts,jsx,tsx}

---

### 3. Update Root Structure

At the root level:
- Remove frontend-specific configs
- Keep only:
  - CLAUDE.md
  - instructions/
  - (future) /backend

---

### 4. Add Root README

Create or update README.md:

- Explain project structure
- Mention:
  - /frontend → UI
  - /backend → API (future)

---

### 5. Verify Frontend Still Works

After refactoring:

    cd frontend
    npm install
    npm run dev

Then use the Playwright MCP tool to:
- Open http://localhost:5173
- Confirm UI renders correctly
- Ensure no layout breakage

---

## Rules

- Do NOT break existing functionality
- Do NOT introduce unnecessary dependencies
- Keep changes minimal and clean
- Prefer clarity over cleverness

---

## Outcome

After refactoring:
- The project is ready for backend integration
- Frontend is isolated and maintainable
- Structure follows real-world engineering practices