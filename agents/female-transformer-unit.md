# Female Transformer Unit Agent

This agent definition spawns a Female Transformer Unit using the system prompt in [`../prompts/female-transformer-system-prompt.md`](../prompts/female-transformer-system-prompt.md).

## Spawn Contract

- **Agent id:** `female-transformer-unit`
- **Manifest:** [`female-transformer-unit.agent.json`](female-transformer-unit.agent.json)
- **System prompt:** [`../prompts/female-transformer-system-prompt.md`](../prompts/female-transformer-system-prompt.md)
- **Entrypoint:** `spawn`
- **Initial state:** wait for a `live`, `laugh`, or `dance` move request.

## Runtime Requirements

The runtime that loads this agent must provide adapters for each communication cascade modality:

1. `visual_text`
2. `auditory`
3. `physical_vibration`

If a runtime does not provide one of these adapters, it must surface that missing capability before spawning the agent.

## Spawn Payload

```json
{
  "agent": "female-transformer-unit",
  "entrypoint": "spawn",
  "systemPrompt": "../prompts/female-transformer-system-prompt.md"
}
```
