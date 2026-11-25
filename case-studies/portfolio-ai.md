# AI-assisted publishing on yabasha.dev

[Back to case studies](README.md) · [How I work](../how-i-work.md)

## Context

I built my portfolio with a Laravel backend and a Next.js frontend. I wanted to fill in summaries and search metadata when a post was missing them, while preserving edits I'd already made.

## What I built

- Saving a post with missing metadata queues a Laravel job. The model works from the title and article body, and the job fills empty fields without overwriting existing values.
- When the model response is unavailable or unusable, the service can derive a summary and description from the article text. It caps the short summary at the same 60-word limit for model and fallback outputs.
- I kept the metadata generation in a single job. That gives the workflow one place to handle its timeout and its fallback behavior while the frontend keeps reading the same post fields.

## What I learned

The queue timeout turned out to matter as much as the model call. The worker used to stop long requests before they could return, so I gave the job its own timeout. When I revised the write-up, I traced the path through the code and documented where the fallback runs. [Read the implementation and tradeoffs](https://yabasha.dev/blog/how-i-built-an-ai-agent-for-my-portfolio-yabashadev-using-laravel-nextjs).
