# DEPS-Style Task Examples

These are manually checked planning examples for a lightweight DEPS-style reproduction. They are meant to demonstrate planning understanding, not controller execution.

## Task 1: Obtain Wooden Pickaxe

### Describe

- Goal: obtain one wooden pickaxe.
- Starting assumption: new survival world, empty inventory.
- Required resources: logs, planks, sticks.
- Required station: crafting table.

### Explain

A wooden pickaxe depends on sticks and planks. Sticks require planks. A crafting table requires planks and is needed to craft the pickaxe. Therefore the plan must collect wood before crafting.

### Plan

| Step | Action | Required input | Expected output | Dependency / reason |
| --- | --- | --- | --- | --- |
| 1 | Punch tree | Tree nearby | Logs | Raw material for planks |
| 2 | Craft planks | Logs | Planks | Required for table and sticks |
| 3 | Craft crafting table | Planks | Crafting table | Required for wooden pickaxe recipe |
| 4 | Craft sticks | Planks | Sticks | Required handle component |
| 5 | Craft wooden pickaxe | Planks, sticks, crafting table | Wooden pickaxe | Final goal |

### Select

If inventory is empty and a tree is visible, select: punch tree.

### Success Check

Inventory contains `wooden_pickaxe`.

### Failure Cases

- No tree found nearby.
- Planks used incorrectly before crafting sticks or table.
- Crafting table not placed or available.

## Task 2: Craft Stone Sword

### Describe

- Goal: craft one stone sword.
- Starting assumption: empty inventory.
- Required resources: logs, planks, sticks, cobblestone.
- Required tools/stations: crafting table, wooden pickaxe.

### Explain

A stone sword requires cobblestone and sticks. Cobblestone is normally mined with a pickaxe, so the agent first needs a wooden pickaxe. This creates a nested dependency: wood -> crafting table/sticks -> wooden pickaxe -> cobblestone -> stone sword.

### Plan

| Step | Action | Required input | Expected output | Dependency / reason |
| --- | --- | --- | --- | --- |
| 1 | Collect logs | Tree | Logs | Base resource |
| 2 | Craft planks | Logs | Planks | Required for table and sticks |
| 3 | Craft crafting table | Planks | Crafting table | Required for tools |
| 4 | Craft sticks | Planks | Sticks | Required by pickaxe and sword |
| 5 | Craft wooden pickaxe | Planks, sticks, table | Wooden pickaxe | Required to mine cobblestone |
| 6 | Mine stone | Wooden pickaxe, stone block | Cobblestone | Sword blade material |
| 7 | Craft stone sword | Cobblestone, stick, table | Stone sword | Final goal |

### Select

If no logs are available, select: collect logs.

### Success Check

Inventory contains `stone_sword`.

### Failure Cases

- Attempts to mine stone before crafting a pickaxe.
- Not enough sticks for both pickaxe and sword.
- Cannot find exposed stone.

## Task 3: Obtain Iron Ingot

### Describe

- Goal: obtain at least one iron ingot.
- Starting assumption: empty inventory.
- Required resources: logs, planks, sticks, cobblestone, iron ore, fuel.
- Required tools/stations: crafting table, wooden pickaxe, stone pickaxe, furnace.

### Explain

Iron ore cannot be mined with a wooden pickaxe. The agent must first obtain stone and craft a stone pickaxe. Iron ingots also require smelting, so a furnace and fuel are needed after ore collection.

### Plan

| Step | Action | Required input | Expected output | Dependency / reason |
| --- | --- | --- | --- | --- |
| 1 | Collect logs | Tree | Logs | Base resource |
| 2 | Craft planks and sticks | Logs | Planks, sticks | Tool components |
| 3 | Craft crafting table | Planks | Crafting table | Required for tools |
| 4 | Craft wooden pickaxe | Planks, sticks, table | Wooden pickaxe | Required to mine cobblestone |
| 5 | Mine cobblestone | Wooden pickaxe | Cobblestone | Required for stone pickaxe and furnace |
| 6 | Craft stone pickaxe | Cobblestone, sticks, table | Stone pickaxe | Required to mine iron ore |
| 7 | Mine more cobblestone | Pickaxe | Cobblestone | Need 8 cobblestone for furnace |
| 8 | Craft furnace | 8 cobblestone, table | Furnace | Required for smelting |
| 9 | Collect fuel | Wood or coal | Fuel | Required for furnace |
| 10 | Mine iron ore | Stone pickaxe, iron ore block | Iron ore | Smelting input |
| 11 | Smelt iron ore | Furnace, fuel, iron ore | Iron ingot | Final goal |

### Select

If the inventory has logs but no crafting table, select: craft planks and crafting table.

### Success Check

Inventory contains `iron_ingot`.

### Failure Cases

- Uses wooden pickaxe on iron ore.
- Crafts furnace before keeping enough cobblestone for stone pickaxe.
- Finds iron ore but lacks fuel.
- Enters cave without food or safety preparation.

## Task 4: Build A Small Shelter

### Describe

- Goal: build a small enclosed shelter before night or hostile danger.
- Starting assumption: empty inventory in a new survival world.
- Required resources: blocks for walls, roof, and door or entrance closure.
- Optional resources: torches, bed, crafting table.

### Explain

Shelter building is less recipe-constrained than tool crafting, but it has spatial and safety dependencies. The agent needs enough blocks, a safe location, and a closed boundary. A door is useful but can be replaced by blocks in a minimal shelter.

### Plan

| Step | Action | Required input | Expected output | Dependency / reason |
| --- | --- | --- | --- | --- |
| 1 | Select flat safe location | Nearby terrain | Build site | Avoids water, cliffs, mobs |
| 2 | Collect wood or dirt | Trees or terrain | Building blocks | Wall and roof material |
| 3 | Craft planks | Logs if using wood | Planks | More efficient building blocks |
| 4 | Build walls | Blocks | Enclosed perimeter | Safety boundary |
| 5 | Build roof | Blocks | Covered shelter | Prevents mob entry from above |
| 6 | Close entrance | Door or blocks | Sealed shelter | Completes safety objective |
| 7 | Place optional crafting table/torch | Planks, coal/charcoal if available | Utility/safety | Improves next tasks |

### Select

If night is near and no safe structure exists, select: gather nearby dirt or wood blocks, then build a minimal enclosed box.

### Success Check

Player is inside a closed shelter with walls and roof.

### Failure Cases

- Builds without enough blocks to close the roof or entrance.
- Chooses unsafe terrain.
- Keeps crafting optional items while night danger increases.
