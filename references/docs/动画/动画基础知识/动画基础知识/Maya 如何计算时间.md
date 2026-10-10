# Maya 如何计算时间

在设置动画时，Maya 需要跟踪关键帧的计时。Maya 在内部将每个帧的时间值转换为 64 位整数表示（称为“标记”）。

## 标记

标记是 Maya 中最小的时间增量，每个标记表示 1/141,120,000 秒。这意味着 Maya 以 24 帧/秒 (fps) 的速率计量 141,120,000 标记/秒 (tps)，即 5,880,000 标记/帧 (tpf)。

尽管 Maya 始终使用相同的每秒标记数，但每帧标记数会根据您选择的播放速度发生变化。要计算每帧的标记数，Maya 将应用您选定的播放速度，即将 tps (141,120,000) 除以使用的播放速度。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-9DA5C87F-7734-4888-BCFA-CE8FDD54B61C.png) <!-- baize:img-hook downloaded=false reason="正文 630 字 ≥300，非承重" -->

例如，对于 15 fps，tpf 数为 9,408,000 (141,120,000/15)。

对非整数（或约整数）帧速率（例如 29.97 fps）使用此公式时，得到的结果并不总是为整数（例如整数 5）。这是因为 Maya 不能表示每个有小数的帧速率（如 25.55）。任何时候，Maya 都需要对标记值进行近似计算，时间显示时带星号 *。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-D541BB3B-1D4A-437C-A953-FF8F993A7A13.png) <!-- baize:img-hook downloaded=false reason="正文 630 字 ≥300，非承重" -->

但是，Maya 标记非常小（1/141,120,000 秒），因此，即使使用有小数的帧速率（例如 24.976 或 29.97 fps），也依然极其精确。

**注**

为了避免出现数字上溢或下溢问题，将标记强制限制在 64 位（带符号）整数范围内。

## 时间精度和二进制文件格式

为了向后兼容，我们建议您先将您的场景保存为 Maya ASCII (.*ma*) 文件。从 Maya 2018 起，二进制文件以 64 位格式保存，这导致 Maya * 二进制*文件 (*.*mb*) 与先前版本的 Maya 不兼容。
