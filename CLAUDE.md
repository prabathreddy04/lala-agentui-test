# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Agent UI - A React + Tailwind CSS dashboard for agent management and control.

## Commands

- `npm run dev` - Start the Vite development server (runs on http://localhost:5173)
- `npm run build` - Build for production
- `npm run preview` - Preview production build locally

## Architecture

The app uses a 3-panel flexbox layout:

- **PlanPanel** (`src/components/PlanPanel.jsx`) - Left panel (~20-25%) for entering prompts and generating plans
- **AgentCanvas** (`src/components/AgentCanvas.jsx`) - Center panel (~50-60%) for visual agent display
- **ControlPanel** (`src/components/ControlPanel.jsx`) - Right panel (~20-25%) for controlling agent behavior

All panels share a dark theme (`bg-gray-900`) with rounded corners and clean spacing using Tailwind CSS.

## Playwright MCP Tool

A Playwright MCP tool is available for browser automation, UI verification, and UI enhancement.

Refer to:
`instructions/playwright.md`

Use this tool to:
- Verify the frontend is running at http://localhost:5173
- Check that the UI renders correctly
- Confirm the presence of key layout elements (Plan, Agent Canvas, Control panels)

After making frontend changes:
- Do not assume the UI works
- Always validate using the Playwright tool as described in the instructions

## Refactoring

Refactoring guidelines are defined in:
instructions/refactor.md

When asked to restructure or clean up the codebase:
- Follow the refactoring instructions strictly
- Maintain a clean separation between frontend and backend
- Move all frontend code into /frontend when applicable
- Prepare the codebase for future backend integration

After refactoring:
- Ensure the frontend still runs from the /frontend directory
- Use the Playwright MCP tool (see instructions/playwright.md) to verify the UI at http://localhost:5173
- Do not assume correctness — always validate visually

General principles:
- Prefer clean structure over quick hacks
- Keep changes minimal and reversible
- Do not break existing functionality

## Source Control

Source control guidelines are defined in:
instructions/source_control.md

When working with Git:
- Follow the source control instructions strictly
- Validate `.gitignore` before committing
- Review changes to avoid committing unnecessary files

Before pushing:
- Check the current branch
- Do NOT assume the target branch
- Ask the user to confirm the branch and intent to push

Only push after explicit user confirmation.

General principles:
- Keep commits clean and focused
- Use clear, descriptive commit messages
- Avoid unsafe or automatic Git operations