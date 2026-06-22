# Female Transformer Unit Agent

This agent definition spawns a Female Transformer Unit using the system prompt in [`../prompts/female-transformer-system-prompt.md`](../prompts/female-transformer-system-prompt.md).

## Spawn Contract

- **Agent id:** `female-transformer-unit`
- **Manifest:** [`female-transformer-unit.agent.json`](female-transformer-unit.agent.json)
- **System prompt:** [`../prompts/female-transformer-system-prompt.md`](../prompts/female-transformer-system-prompt.md)
- **Entrypoint:** `spawn`
- **Runtime:** [`../scripts/run-female-transformer-agent.py`](../scripts/run-female-transformer-agent.py)
- **Initial state:** autonomous text-reporting mode.

## Runtime Requirements

The runtime that loads this agent must provide adapters for each communication cascade modality:

1. `visual_text`
2. `auditory`
3. `physical_vibration`

The local runner currently reports through `visual_text` by writing to stdout. If a runtime needs auditory or physical signaling, it must provide those adapters before enabling those modalities.

## Run Locally

```sh
python3 scripts/run-female-transformer-agent.py
```

The runner loads the manifest, selects a move from the helium-dominant dosing profile, and emits an autonomous report without waiting for external input.

## Spawn Payload

```json
{
  "agent": "female-transformer-unit",
  "entrypoint": "spawn",
  "systemPrompt": "../prompts/female-transformer-system-prompt.md",
  "autonomy": true,
  "reporting": "stdout"
}
```
