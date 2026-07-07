# Example Failure Modes

This is a qualitative, Minecraft-aware analysis. It is not an official OpenHA/CrossAgent evaluation.

## Task: obtain iron ingot

- **All high-level actions:** All high-level actions may jump to `mine iron ore` without checking pickaxe tier, furnace, and fuel prerequisites.
- **All mid-level skill actions:** All mid-level skill actions can call useful skills, but may fail if the wrong tool, ore target, or furnace parameters are supplied.
- **All low-level controls:** All low-level controls are executable, but the prerequisite chain becomes too long and credit assignment becomes weak.
- **Language-only actions:** Language-only actions under-specify which ore, tree, fuel source, or furnace should be used.
- **Visual/mask actions:** Visual/mask actions can identify ore or furnace targets but cannot alone plan the full smelting chain.
- **Dynamic action-space switching:** Dynamic switching uses high-level planning for prerequisites, memory for tool/fuel constraints, visual grounding for ore/furnace targets, and low-level control for mining interaction.

## Task: craft stone sword

- **All high-level actions:** All high-level actions may request `craft sword` before collecting cobblestone, sticks, or a crafting table.
- **All mid-level skill actions:** All mid-level skill actions work only if recipe and inventory parameters are correct.
- **All low-level controls:** All low-level controls make the GUI and collection sequence unnecessarily long.
- **Language-only actions:** Language-only actions may omit exact inventory slots or station state.
- **Visual/mask actions:** Visual/mask actions help locate a crafting table or slot but do not infer the recipe chain by themselves.
- **Dynamic action-space switching:** Dynamic switching combines recipe memory, mid-level crafting, and low-level GUI correction.

## Task: build a small shelter

- **All high-level actions:** All high-level actions may say `build shelter` without specifying footprint, material, door placement, or threat response.
- **All mid-level skill actions:** All mid-level skill actions can place blocks but may miss geometry and safety constraints.
- **All low-level controls:** All low-level controls are possible but slow and brittle over many placements.
- **Language-only actions:** Language-only actions lose spatial layout and obstacle details.
- **Visual/mask actions:** Visual/mask actions help with placement targets but cannot decide the whole shelter plan.
- **Dynamic action-space switching:** Dynamic switching uses high-level layout planning, inventory checks, visual placement, and low-level correction.

## Task: obtain diamond

- **All high-level actions:** All high-level actions may choose `mine diamond` despite missing iron pickaxe, cave access, or safety preparation.
- **All mid-level skill actions:** All mid-level skill actions depend on valid tool and target parameters.
- **All low-level controls:** All low-level controls make the search/mining chain too long for reliable control.
- **Language-only actions:** Language-only actions do not identify ore blocks or hazards.
- **Visual/mask actions:** Visual/mask actions can ground diamond ore but cannot guarantee prerequisite tool planning.
- **Dynamic action-space switching:** Dynamic switching links prerequisite memory, exploration, ore grounding, and precise mining control.

## Task: smelt iron

- **All high-level actions:** All high-level actions may skip checking ore, furnace, and fuel.
- **All mid-level skill actions:** All mid-level skill actions may fail if furnace/fuel/ore parameters are missing.
- **All low-level controls:** All low-level controls over GUI slots are fragile without inventory-state reasoning.
- **Language-only actions:** Language-only actions do not identify the actual furnace or inventory slots.
- **Visual/mask actions:** Visual/mask actions help select furnace and slots but do not plan fuel acquisition.
- **Dynamic action-space switching:** Dynamic switching combines prerequisite reasoning, station grounding, and low-level GUI execution.

## Task: fight hostile mob

- **All high-level actions:** All high-level actions may say `attack` without reacting to distance, health, terrain, or multiple enemies.
- **All mid-level skill actions:** All mid-level skill actions may lack parameters for timing, aim, retreat, or shield use.
- **All low-level controls:** All low-level controls can react, but without high-level policy may chase bad fights.
- **Language-only actions:** Language-only actions miss exact mob position and motion.
- **Visual/mask actions:** Visual/mask actions are useful for target tracking but not enough for survival policy.
- **Dynamic action-space switching:** Dynamic switching alternates between target grounding, low-level combat control, and high-level retreat/equip decisions.

## Task: explore cave

- **All high-level actions:** All high-level actions may under-specify route, lighting, hazard avoidance, and return path.
- **All mid-level skill actions:** All mid-level skill actions may not adapt to local cave geometry.
- **All low-level controls:** All low-level controls are executable but inefficient over long exploration horizons.
- **Language-only actions:** Language-only actions lose spatial and hazard detail.
- **Visual/mask actions:** Visual/mask actions help detect openings, ores, and threats but do not maintain exploration memory.
- **Dynamic action-space switching:** Dynamic switching uses high-level exploration goals, visual hazard detection, memory of visited areas, and low-level movement.

## Task: use furnace

- **All high-level actions:** All high-level actions may assume a furnace exists and is reachable.
- **All mid-level skill actions:** All mid-level skill actions need exact object, fuel, and ingredient parameters.
- **All low-level controls:** All low-level controls are brittle around GUI opening and slot placement.
- **Language-only actions:** Language-only actions do not distinguish furnace from crafting table or chest.
- **Visual/mask actions:** Visual/mask actions help choose the furnace but do not infer smelting prerequisites.
- **Dynamic action-space switching:** Dynamic switching grounds the furnace visually, checks inventory prerequisites, and executes GUI actions at low level.
