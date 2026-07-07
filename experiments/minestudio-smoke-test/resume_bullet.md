# Resume Bullet Drafts

## Version A: T2 Passed

- Ran a bounded MineStudio simulator / rollout smoke test, including environment setup, module inventory, and a 1-5 step minimal interaction record, providing a toolchain baseline for later OpenHA/CrossAgent-style experiments.

## Version B: T0/T1 Passed But T2 Blocked

- 完成 MineStudio 安装、import 与核心模块入口 smoke test，并通过小规模依赖补齐解决 `cv2` 阻塞、定位 simulator import 的下一阶段 `torch` blocker；未运行训练、checkpoint 推理或 Minecraft rollout。

## Version B2: Blocker-Reduction Pass

- 对 MineStudio 工具链进行 bounded blocker-reduction：在 `/root/autodl-tmp` 环境中补齐小型 import 依赖与 OpenJDK，验证 `minestudio.utils` / `minestudio.online` 可导入，并记录 simulator reset 前仍受 `torch`、display / Xvfb 约束。

## Version C: Setup Blocked

- 对 MineStudio 工具链进行环境审计，定位安装、依赖或系统层 blocker，并整理后续最小复现路径。
