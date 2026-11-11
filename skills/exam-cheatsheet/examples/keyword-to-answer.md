# Original example: from question wording to a usable entry

This is an original instructional example, not a past exam question or an official marking guide. It illustrates sheet design; it does not establish any course's current syllabus.

## Question

Four sites A, B, C and D can be connected by undirected cables. Available cables and costs are AB=1, AC=4, BC=2, BD=5 and CD=3. Connect every site with minimum total cable cost. Show the selected edges and total cost.

## Weak entry

> MST: Prim / Kruskal. Minimum total weight.

The concept is present, but a student who searches for “connect every site” has no clear entry. The line also does not show what to do next or what to submit.

## Improved entry

### G1 — connect all sites / minimum total cost → MST

**中文判断：**所有地点要连通，目标是所有选中边的总成本最低；不是从某个起点到各点分别走最短路线。题设是连通、无向、带权图。

**Prim 步骤：**任选起点加入集合 S；每轮选连接 S 内外、权重最小的边；加入新顶点并记录该边；直到所有顶点都加入。不要选两个端点都已在 S 内的边。

**交付：**所选边与总权重；题目要树图或中间状态时一并画出。n 个顶点的生成树应有 n−1 条边。

**English template:** “Use Prim's algorithm to construct a minimum spanning tree. The selected edges are ____. Their total cost is ____.”

**区别：**若题目要求从单一起点出发到各点的最短距离，应转到 shortest paths 条目，并检查相应算法的前提。MST 最小化整棵树的总边权。

## Worked application

Start from A:

| Set S before the step | Crossing edges | Chosen edge |
|---|---|---|
| {A} | AB=1, AC=4 | AB |
| {A,B} | AC=4, BC=2, BD=5 | BC |
| {A,B,C} | BD=5, CD=3 | CD |

The chosen tree is A—B—C—D, with edge weights 1, 2 and 3. Total cost: 6.

> Use Prim's algorithm to construct a minimum spanning tree. The selected edges are AB, BC and CD. Their total cost is 6.

## What this checks

- “Connect every site” reaches the visible `connect all sites` alias.
- The decision step distinguishes a total network cost from source-to-vertex distances.
- The entry supports the algorithm's next action, not just its name.
- The answer includes both outputs requested by the question.

This is a guided demonstration. It provides no evidence of a student's independent mastery, timed lookup, or physical print readability. This Markdown example has not itself been laid out as an A4 sheet.
