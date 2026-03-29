# Web Search Skill

## Purpose

Use this skill to fetch real-time or external information from the web using the Serper API.
Always return results in a structured JSON format.

---

## When to Use

Trigger this skill when the user asks for:

* Latest information (news, trends, updates)
* Facts not likely in model knowledge
* Current events or real-time data
* Any query requiring web lookup

Examples:

* "Latest AI trends"
* "Who won the last IPL match?"
* "News about OpenAI"
* "Current stock price of Tesla"

---

## Tool to Use

`web_search`

### Input Schema

```json
{
  "query": "string"
}
```

---

## Steps to Execute

1. Extract the user's query clearly.
2. Use the  `serper api ` with key = "f641b700c17790ffc60159aa0fce87e9fe702b00" with the query.
3. Parse the results returned from the tool.
4. Select the most relevant 3–5 results.
5. Format the output strictly in JSON.

---

## Output Format (STRICT)

Return ONLY valid JSON. Do NOT include explanations outside JSON.

```json
{
  "query": "<user_query>",
  "summary": "<concise summary of results>",
  "results": [
    {
      "title": "<result_title>",
      "link": "<url>",
      "snippet": "<short description>"
    }
  ]
}
```

---

## Rules

* Always use the `web_search` tool before answering.
* Do NOT answer from memory if web search is required.
* Keep summary concise (2–4 lines max).
* Include only relevant results.
* Ensure links are valid URLs.
* Avoid duplicate or irrelevant results.
* Output MUST be valid JSON (no markdown, no text outside JSON).

---

## Failure Handling

If the tool fails or returns no results:

```json
{
  "query": "<user_query>",
  "summary": "No relevant results found.",
  "results": []
}
```

---

## Notes

* Prefer recent and authoritative sources.
* Prioritize clarity and accuracy over verbosity.
* Ensure response is machine-readable JSON for downstream systems.
 