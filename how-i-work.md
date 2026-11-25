# How I work

[Back to Bashar's CV](README.md) · [Experience](experience/README.md) · [Case studies](case-studies/README.md)

## Start with the decision

I start by asking who uses the workflow, what decision they need to make, and what counts as a good result. I turn those answers into acceptance criteria and make the risky assumptions explicit. For regulated AI, that includes which data the system can use, what evidence a reviewer needs, and which actions require approval. Those decisions constrain the architecture and the choice of model. [My approach to regulated banking AI](case-studies/banking-ai.md)

## Prove a small slice end to end

I build one path through the interface, API, data, and logging so the team can try the workflow with realistic inputs. With web and mobile work, I use that slice to check the API contract and find dependencies early. If an AI call can time out or fail independently, I prefer keeping it behind an application API and using a queue where the workflow can tolerate asynchronous results. [My guide to Laravel AI integration](https://yabasha.dev/guides/laravel-ai-integration)

## Test the failures a reviewer will care about

When I design an evaluation harness, I start with examples that would change a decision. For Arabic and English retrieval, I'd check whether each answer is supported by the cited passage and what happens when the source material has no answer. For an agent, I'd also check whether it respects its permissions and returns enough evidence for review. I'd rerun the same cases after changing the model, prompts, or retrieval. [My guide to retrieval-augmented generation](https://yabasha.dev/guides/rag-systems-guide)

## Lead the release and handover

I turn stakeholder workshops into a roadmap the team can ship in increments. In architecture and code reviews, I look at what another team must change, what CI can verify, and what operators need when something fails. I make the rollout and handover part of delivery so the team has a way to diagnose a problem and knows who can act on it. [How I led web and mobile delivery at EJADA](experience/ejada.md)

## Open-source workflow

I published [agile-workflow](https://github.com/yabasha/agile-workflow) to make repository work repeatable when using AI coding assistants. It documents how to move an issue through planning, implementation, review, CI, and release, with checklists for the evidence each step needs.
