# GPU Action Scorer Log

This is a toy GPU-backed action scorer. It is not JARVIS-VLA and it does not train.

## Runtime

- torch: `2.11.0+cu128`
- cuda_available: `True`
- device: `NVIDIA RTX PRO 6000 Blackwell Server Edition`

## Results

### tree_collect_wood

- selected_action: `attack`
- scores: `{'attack': 3.0, 'use': 0.0, 'equip_item': -0.3, 'place_block': -0.2, 'retreat': -0.2, 'wait': -0.2}`

### craft_table_planks

- selected_action: `use`
- scores: `{'attack': 0.0, 'use': 2.7, 'equip_item': -0.3, 'place_block': -0.2, 'retreat': -0.2, 'wait': -0.1}`

### furnace_smelt_iron

- selected_action: `use`
- scores: `{'attack': 0.0, 'use': 4.3, 'equip_item': -0.3, 'place_block': -0.2, 'retreat': -0.2, 'wait': -0.2}`

### iron_wooden_pickaxe

- selected_action: `equip_item`
- scores: `{'attack': 0.5, 'use': 0.0, 'equip_item': 1.3, 'place_block': -0.2, 'retreat': -0.2, 'wait': 0.6}`

### night_mob_survive

- selected_action: `retreat`
- scores: `{'attack': -1.0, 'use': 0.0, 'equip_item': -0.3, 'place_block': 1.6, 'retreat': 4.6, 'wait': -0.2}`
