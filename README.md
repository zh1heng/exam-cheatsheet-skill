# Cheatsheet Master · 小抄高手

把课程资料整理成**看见题目就能找到入口、判断方法并写出答案**的考试小抄。

这是一个可复用的 AI skill 项目。适合制作、审查和迭代考试允许携带的 reference sheet，也可以用于考前复习。输入课程范围、讲义、题目和版面限制；输出小抄内容、可编辑源文件、打印文件（环境支持时）和验证记录。

## 方法

**课程证据与考试限制 → 可用 v1 初稿 → 用户反馈与逐步修改 → 独立 agent 做题 → 修复与复测 → 最终排版验收。**

先让使用者拿到初版，不必先回答一长串偏好问题，也不必等所有最终验收轮次结束。初版有基本内容与版面检查，待核实或待验收的部分明确标注；后续按实际需求修改，保留旧版和熟悉的编号。

每个条目的内部结构是：**题目原词 → 小抄入口 → 判断条件 → 操作步骤 → 作答模板。**

例如，题目说 `connect all sites with minimum total cable length`，小抄入口就应包含 `connect all / minimum total cost`，再桥接到 MST。只在正文里出现 MST，不足以证明学生能找到它。

每个条目回答六件事：

1. 题目出现什么词或情境时查这里？
2. 为什么选这个方法，什么情况下不能选？
3. 先看什么、再做什么？
4. 最终需要交什么：句子、代码、图、数组还是计算过程？
5. 可以套用什么答案句型，哪些内容必须随题改变？
6. 用哪道题验证过，尚有哪些不确定性？

默认示例采用“英文识题定位、中文理解与判断、英文作答”，让语言各自承担用途，避免整段重复翻译挤占版面；实际使用时按学生熟练度、题面语言与考试要求调整。代码和数学符号保留题设表示。

## 使用

项目中的 skill 位于 [`skills/cheatsheet-master`](skills/cheatsheet-master/SKILL.md)。把整个 `cheatsheet-master` 文件夹复制到所用 AI 工具支持的 skills 目录，或在对话中明确提供该 `SKILL.md` 和相邻参考文件。不同客户端的自动发现方式可能不同。

Codex 用户可以直接发送以下安装请求：

```text
使用 $skill-installer 安装 https://github.com/zh1heng/exam-cheatsheet-skill
中的 skills/cheatsheet-master 技能。
```

技能现名 **Cheatsheet Master（小抄高手）**，调用名为 `$cheatsheet-master`。已安装旧版的用户更新时应以新目录替换旧 `exam-cheatsheet` 目录，避免两套规则并存。GitHub 仓库地址保持不变。

示例请求：

> 使用 $cheatsheet-master，根据课程文件夹、老师录音转录和本次考试通知先出可用 v1，再按我的反馈慢慢修改。先确定是否只允许单面，不默认双面。中文用于判断步骤，英文用于考试答案，有效印刷字号不低于 5pt；重复代码可用定义清楚的 @ 片段压缩。按有依据的考试题型顺序分区；顺序证据不足两份时告诉我实际排序依据。最终版先把全部题目分类，每类选代表题独立实际作答；仅换数据的同类题不重复做，解法、条件或输出变化的题保留必要变式。实测题小抄支持率至少90%，复核关键项与定位；修改后只复测受影响部分，再验收打印布局。报告哪些实测、哪些仅分类。

已有小抄也可以直接审查：

> 使用 $cheatsheet-master，检查这些题目能否在我的小抄上直接找到入口。分别报告内容缺失、定位困难、步骤不足和排版问题，只修改我指定的部分。

## 项目内容

- [`SKILL.md`](skills/cheatsheet-master/SKILL.md)：何时使用、制作流程与交付要求。
- [`references/entry-and-audit.md`](skills/cheatsheet-master/references/entry-and-audit.md)：条目结构、覆盖表与验证标准。
- [`references/source-priority.md`](skills/cheatsheet-master/references/source-priority.md)：课程资料优先级、老师录音转录核验、单/双面等考试限制。
- [`references/language-design.md`](skills/cheatsheet-master/references/language-design.md)：不同语言在识题、理解、判断、术语与作答中的分工。
- [`references/peer-review-and-layout.md`](skills/cheatsheet-master/references/peer-review-and-layout.md)：独立 agent 做题、反馈修复循环、5pt 下限和标题/配色/打印验收。
- [`references/acceptance-harness.md`](skills/cheatsheet-master/references/acceptance-harness.md)：仅明确要求全量逐题验收时使用的严格状态、90%门槛与JSON证据契约。
- [`scripts/audit_harness.py`](skills/cheatsheet-master/scripts/audit_harness.py)：可选的严格全量账本检查器；默认代表题验收不运行此脚本，不支持分类映射或增量证据。
- [`references/code-shorthand.md`](skills/cheatsheet-master/references/code-shorthand.md)：用 `@名称` 引用相同代码，定义、原地展开与正确性核验。
- [`examples/keyword-to-answer.md`](skills/cheatsheet-master/examples/keyword-to-answer.md)：原创示例，展示如何从题目措辞找到方法与答案。
- [`docs/validation.md`](docs/validation.md)：本项目实际执行的验证及其限制。

## 几条关键取舍

- 默认全量分类、代表题实际作答，不逐题重做同类数据变式；保留真正改变解法的差异。
- 内容修改只复测受影响的代表题；排版修改只查最终渲染及受影响定位。全量逐题验收仅在明确要求时启用。

- 历史考题帮助识别问法、方法和变式；出现频率不等于今年的考题概率。
- 版面兼顾本学期范围、易错条件、查用价值和学生需求。不要因为某类题以前常考，就默认让它挤占其他内容。
- 先压缩重复表达，再处理布局。字体缩小不等于信息设计完成。
- 相同代码可以用 `@名称` 共用片段；定义在小抄上写全，展开后保持逻辑不变。考试需要完整代码时应展开，不能把未定义的 @ 标记直接抄进答案。
- 老师录音中的明确范围、纠错和答题要求要提取并定位；转录不清或与正式通知冲突时核实，不能把强调当成必考保证。
- 单面要求是硬性版面限制；一张纸不自动等于允许双面。最小有效印刷字号 5pt 是下限，不是全篇默认值。
- 大标题用字号、颜色与底色建立层级，解释和答案模板区分；黑白打印仍能靠文字标签和结构辨认。
- 独立 agent 要交出实际答案、查用路径和小抄外补充知识；根据具体失败修复并复测，不能用一句“内容完整”代替验收。
- 内容覆盖、查找可用、版面验证、真实打印和独立掌握分别记录。
- 已打印版本与节号应保持稳定；修改另存，清楚说明入口变化。

仓库提供通用方法和原创示例。具体课程的讲义、试卷、录音和个人学习记录由使用者在自己的工作区提供。

当前版本提供工作流程、示例和验收账本检查脚本；主 agent 负责调度独立解题与修复。PDF/DOCX 的生成依赖运行环境已有的文档工具，没有附带独立排版程序。支持率不是预计考试得分，也不是学生独立掌握率。
