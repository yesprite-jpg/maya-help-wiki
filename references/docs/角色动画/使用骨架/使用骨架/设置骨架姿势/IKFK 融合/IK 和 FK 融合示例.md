# IK 和 FK 融合示例

本实例介绍融合 FK 摆动臂动画和 IK 挥动臂动画。

1. 创建一个在循环行走期间摆动臂的简单动画：

  - 选择手臂关节链的根关节（肩部关节）。

  - 使其沿 Z 轴旋转。

  - 为关节设定关键帧

  这将生成一个初步的 FK 动画。

  ![图：创建一个在循环行走期间摆动臂的简单动画： 选择手臂关节链的根关节（肩部关节）。 使其沿 Z 轴旋转。 为关节设定关键帧 …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-0F35C77E-0BB1-481A-8BC7-D439A5EDD818.png) <!-- baize:img-hook downloaded=false reason="正文 472 字 ≥300，非承重" -->

2. 将该 FK 动画序列与手臂挥动的定向运动进行融合：

  - 在 FK 动画的开头和末尾处的 IK 控制柄和肩部关节上设置关键帧以创建一个融合区域。

    您可以将这些关键帧作为边界关键帧，因为它们可确保您在它们之间的融合范围中设置的任何关键帧都不会在该范围之外更改动画。

  - 将“IK 融合”(IK Blend)值更改为 1.000（纯 IK）。

  - 在肩部关节和 IK 控制柄上设置关键帧。

  ![图：将该 FK 动画序列与手臂挥动的定向运动进行融合： 在 FK 动画的开头和末尾处的 IK 控制柄和肩部关节上设置关键帧以…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-9F198FBF-25DE-4625-B814-04EED150D0F3.png) <!-- baize:img-hook downloaded=false reason="正文 472 字 ≥300，非承重" -->

  在纯 FK 和 IK 动画之间的区域（即融合区域）中，“IK 解算器”(IK Solver)在 0.000 到 1.000 之间插值动画。

  ![图：将该 FK 动画序列与手臂挥动的定向运动进行融合： 在 FK 动画的开头和末尾处的 IK 控制柄和肩部关节上设置关键帧以…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-8D11C665-22F9-461D-AF9B-1F9EC2C1F55D.png) <!-- baize:img-hook downloaded=false reason="正文 472 字 ≥300，非承重" -->

  “IK 融合”(IK Blend)值为 1.000 时，动画是纯 IK。

3. 在设定关键帧时平移和旋转 IK 控制柄以生成挥动手臂动画。

4. 将动画再次设置（使用其他融合区域并将 “IK 融合”(IK Blend)值更改为 0.000）到纯 FK。

  结果动画看起来像一个挥动的手臂 (FK)，举高挥动 (IK)，然后下降回到摆动动作（返回到 FK）。
