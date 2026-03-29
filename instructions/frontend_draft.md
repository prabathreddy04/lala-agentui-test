Build a minimal web UI layout using React + Tailwind CSS.

Goal:
Create a simple 3-panel dashboard layout. No functionality, no state, no mock data. Just static UI.

Layout:

- Full screen height
- Split into 3 vertical sections using flexbox

1. LEFT PANEL (Plan)
- Width: ~20–25%
- Title: "Plan"
- Add a simple textarea (placeholder: "Enter prompt...")
- Add a button below it: "Generate Plan"

2. CENTER PANEL (Agent Canvas)
- Width: ~50–60%
- Title: "Agent Canvas"
- Empty container box (this is where agents will go later)
- Add a placeholder text in center: "Canvas Area"

3. RIGHT PANEL (Control)
- Width: ~20–25%
- Title: "Control"
- Add:
  - Label: "Reasoning Mode"
  - Toggle switch (static, no functionality)
  - Label: "Token Quota"
  - Input box (number)
  - Button: "Take Over Control"

Design:

- Use Tailwind CSS
- Dark theme (bg-gray-900 or similar)
- Panels separated with borders or subtle background differences
- Titles should be slightly bold and larger
- Clean spacing (padding, margin)
- Rounded corners for panels

Component structure:

- App (main layout)
- PlanPanel
- AgentCanvas
- ControlPanel

Important:

- Do NOT add any functionality or logic
- Do NOT simulate agents
- Do NOT over-engineer
- Keep everything static and clean