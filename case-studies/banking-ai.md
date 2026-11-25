# AI agents in regulated banking

[Back to case studies](README.md)

## Context

A regional bank needed AI-assisted workflows for tasks such as mobile release review and compliance reporting. Reviewers needed enough evidence to check a draft or recommendation before acting.

## My role

I contributed to the architecture and advised on how reviewers would use agent outputs. The design had to answer two questions. Could someone follow a recommendation back to its evidence? Who had authority to act on it?

## How the system worked

- **Stable client APIs.** Model calls ran behind Laravel queues. The React Native and Next.js clients used the same application APIs when a model changed.
- **Review before action.** A mobile release check returned a confidence score and flagged screenshots. A compliance workflow drafted a report with an evidence trail. People made the release and filing decisions.
- **Regression checks.** Before a model swap, I'd rerun cases that exposed known failures, such as invented required fields or high confidence scores on builds that still failed release checks.

## Result

My July 2026 write-up describes five workflows running in production at the time. Their outputs supported a person making the final decision.

[Public engineering write-up](https://yabasha.dev/blog/ai-agents-ate-my-boilerplate-what-actually-works-in-enterprise-banking)
