# Task Dependency Graph

## Example: Obtain Iron Pickaxe

```text
collect wood
  -> craft planks
  -> craft crafting table
  -> craft sticks
  -> craft wooden pickaxe
  -> mine stone
  -> craft stone pickaxe
  -> mine iron ore
  -> craft furnace
  -> collect fuel
  -> smelt iron ingots
  -> craft iron pickaxe
```

## Notes

- Some dependencies are strict, such as needing a stone pickaxe before mining iron.
- Some dependencies are opportunistic, such as collecting food before caving.
- Failure cases should be linked back to missing dependencies or bad ordering.
