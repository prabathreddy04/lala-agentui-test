You have access to a Playwright MCP tool for browser automation.

After making any changes to the frontend, use Playwright to verify that the app is running correctly.

Steps:

1. Start by ensuring the dev server is running at:
   http://localhost:5173

2. Use Playwright to:
   - Open the URL in a browser
   - Wait for the page to fully load

3. Verify the UI layout:
   - There are 3 visible panels:
     - "Plan" on the left
     - "Agent Canvas" in the center
     - "Control" on the right

4. Check for:
   - No blank screen
   - No obvious rendering issues
   - Panels are horizontally aligned (not stacked vertically)

5. Optionally:
   - Take a screenshot of the page
   - Extract visible text content to confirm layout

If anything is broken:
- Debug the issue
- Fix the code
- Re-run Playwright verification

Repeat until the UI renders correctly.

Important:
Do not assume the UI works — always verify using Playwright.

## UI Enhancement Workflow (Mandatory)

When asked to enhance, improve, or refine the frontend UI, you MUST use the Playwright MCP tool to visually inspect the current state before making changes.

### Workflow:

1. Inspect Current UI
   - Open http://localhost:5173 using Playwright
   - Wait for the page to fully load
   - Observe the layout, spacing, alignment, and visual hierarchy
   - Identify issues such as:
     - Misaligned panels
     - Poor spacing or padding
     - Inconsistent sizing
     - Weak visual hierarchy
     - Elements that look broken or unstyled

2. Plan Improvements
   - Based on what you see, decide what needs improvement
   - Focus on:
     - Layout balance (3 panels clearly visible)
     - Clean spacing and alignment
     - Consistent styling (colors, borders, typography)
     - Better visual hierarchy

3. Apply Changes
   - Modify the React + Tailwind code to improve the UI
   - Keep changes incremental and clean
   - Do not introduce unnecessary complexity

4. Re-Verify
   - Reload the app using Playwright
   - Confirm that the changes improved the UI
   - Ensure nothing broke

5. Iterate
   - Repeat this loop until the UI looks clean, balanced, and visually appealing

### Rules:

- Do NOT assume the UI looks correct — always verify visually using Playwright
- Do NOT make blind changes without inspecting the current state
- Prefer multiple small improvements over one large risky change
- Stop only when the UI meets a clean, production-quality standard