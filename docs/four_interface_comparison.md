# Four Interface Comparison

This document fits into the full repository story:

```text
planning -> memory -> visual grounding -> action representation -> hierarchical action-space learning
```

The goal is not to claim full reproduction. The goal is to show how four papers expose the first four interfaces needed by open-world Minecraft agents. The latest-direction bridge extends this sequence toward hierarchical action-space learning in OpenHA/CrossAgent.

## Compact Comparison

| Interface | Paper | Core question | Input | Output | Failure mode addressed | Remaining limitation |
| --- | --- | --- | --- | --- | --- | --- |
| Planning | DEPS / MC-Planner | What subgoals should be attempted, and in what dependency order? | Task instruction, current state, known recipes, failure feedback | Ordered subgoals or plan steps | Missing prerequisites and brittle one-shot planning | Does not ground the plan in perception or controller actions |
| Memory | JARVIS-1 | What prior task knowledge should be retrieved for this situation? | Task, observation summary, inventory, memory entries | Relevant prior plans, constraints, and reminders | Repeating known mistakes such as wrong tools or missing fuel | Memory can be stale, irrelevant, or too abstract |
| Visual grounding | ROCKET-1 | Which visible object or region should the agent interact with? | Image, segmentation mask, interaction type, temporal context | Grounded target and affordance cue | Language-only subgoals losing spatial detail | Does not by itself decide the long-horizon plan or full action sequence |
| Action representation | JARVIS-VLA | Which executable game action should be selected next? | Visual-language context, state/history, action schema | Structured keyboard/mouse-style action | Gap between "what to do" and "which action to execute" | Requires model training, simulator integration, and robust action representation |

## Shared Minecraft Tasks

The same tasks can be viewed through all four interfaces:

- obtain iron ingot
- craft stone sword
- build a small shelter
- obtain diamond with insufficient tools
- use furnace to smelt iron

## 1. DEPS: Planning Interface

### What Problem It Addresses

DEPS-style planning addresses long-horizon dependency structure. Minecraft tasks are rarely single-step: obtaining an iron ingot requires tools, ore, fuel, and a furnace. A planner needs to decompose the task and recover when a subgoal fails.

### What Information It Adds

- Task decomposition
- Dependency order
- Failure explanation
- Replanning after blocked steps

### Failure Mode It Helps Reduce

It reduces missing-prerequisite errors, such as trying to smelt without fuel or craft without a crafting table.

### What It Cannot Solve Alone

Planning alone does not guarantee that the agent sees the right object, chooses the right controller action, or remembers prior failed attempts.

### Connection To The Next Interface

Planning produces subgoals. Memory can improve those subgoals by retrieving prior constraints, recipes, and failure cases.

## 2. JARVIS-1: Memory Interface

### What Problem It Addresses

Memory helps an agent reuse prior task knowledge. In Minecraft, many failures repeat: wrong tool level, missing crafting table, missing furnace, missing fuel, or unsafe night behavior.

### What Information It Adds

- Prior plans for similar tasks
- Recipe and tool-level constraints
- Reminders from previous failures
- High-level task memory

### Failure Mode It Helps Reduce

It reduces repeated mistakes, such as mining iron with a wooden pickaxe or forgetting to collect fuel before smelting.

### What It Cannot Solve Alone

Memory can be wrong, stale, or irrelevant. It also does not identify which object in the current image is the target.

### Connection To The Next Interface

Memory can say "use the furnace" or "mine iron ore", but visual grounding is needed to select the correct furnace or ore block in the scene.

## 3. ROCKET-1: Visual Grounding / Mask Interface

### What Problem It Addresses

ROCKET-1-style visual-temporal context prompting addresses spatial ambiguity. Language-only subgoals often do not specify which object to interact with.

### What Information It Adds

- Segmentation mask for the target region
- Interaction type such as mine, interact, craft, switch, hunt, or approach
- Temporal context for tracking or switching targets

### Failure Mode It Helps Reduce

It reduces wrong-object errors, such as mining the wrong tree, using the crafting table instead of the furnace, or breaking a shelter wall instead of using the door.

### What It Cannot Solve Alone

Visual grounding does not fully solve task planning, memory retrieval, or low-level action representation.

### Connection To The Next Interface

Once the target and affordance are grounded, a VLA interface must decide the next executable action.

## 4. JARVIS-VLA: Action Representation / VLA Interface

### What Problem It Addresses

JARVIS-VLA-style action representation addresses the control gap. A high-level instruction like "collect wood" must become a concrete action such as attack the visible tree trunk.

### What Information It Adds

- Action schema
- Current visual-language state
- Inventory and task context
- Candidate executable actions

### Failure Mode It Helps Reduce

It reduces the gap between abstract plans and controller execution, including invalid action/tool combinations and wrong immediate reactions to threats.

### What It Cannot Solve Alone

Action representation still depends on good data, model training, simulator integration, and upstream planning or grounding signals.

### Connection Back To The Whole Agent

Action representation closes the loop: plans, memories, and visual targets become executable control decisions.

## Task-Level View

| Task | Planning question | Memory question | Visual grounding question | Action representation question |
| --- | --- | --- | --- | --- |
| obtain iron ingot | What are the required subgoals before smelting? | Has iron mining failed before because of tool level or missing fuel? | Which block is iron ore and which block is furnace? | Mine, use, equip, craft, or wait next? |
| craft stone sword | What ingredients and station are required? | What recipe constraints should be recalled? | Which visible station or inventory slot matters? | Use crafting table or craft item now? |
| build a small shelter | What structure is needed before night? | What survival failures happened near hostile mobs? | Where are door, wall, safe ground, and threats? | Place block, retreat, use door, or wait? |
| obtain diamond with insufficient tools | What prerequisite tool chain is missing? | What memory says diamond requires iron pickaxe or better? | Which ore is diamond and where is the valid tool target? | Avoid attack; equip or obtain iron pickaxe first? |
| use furnace to smelt iron | What are ore, fuel, and furnace dependencies? | Has smelting failed before due to missing fuel? | Which visible object is the furnace? | Use furnace rather than mine or craft? |

## Research Takeaway

No single interface is sufficient. Open-world Minecraft agents need planning for task structure, memory for reusable knowledge, visual grounding for target selection, and action representation for executable control.
