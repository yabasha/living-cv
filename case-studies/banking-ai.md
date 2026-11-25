# AI agents in regulated banking

[Back to case studies](README.md)

## Context

A regional bank needed AI-assisted workflows for tasks such as mobile release review and compliance reporting. Reviewers needed enough evidence to check a draft or recommendation before acting.

## What I worked on

- Used Laravel queue workers for model calls so web and mobile clients could keep their existing API contracts when models changed.
- Designed agent outputs for human review. Depending on the workflow, an agent returned a draft, a score, or a recommendation with evidence the reviewer could follow.
- Used evaluations to compare model changes before rollout. The evaluation work drew on actual failure modes, including missing fields and mobile release defects.

## Result

The public write-up describes five agents running in production at the time of writing. Each workflow kept the final decision with a person.

[Public engineering write-up](https://yabasha.dev/blog/ai-agents-ate-my-boilerplate-what-actually-works-in-enterprise-banking)
