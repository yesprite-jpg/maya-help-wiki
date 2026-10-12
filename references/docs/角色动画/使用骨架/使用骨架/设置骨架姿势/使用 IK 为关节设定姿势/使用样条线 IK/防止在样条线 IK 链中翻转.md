# 防止在样条线 IK 链中翻转

防止关节链沿其曲线滑动时翻转

1. 在“装备”(Rigging)菜单集中，选择“骨架 > 创建 IK 样条线控制柄”(Skeleton > Create IK Spline Handle) > ![图：在“装备”(Rigging)菜单集中，选择“骨架 创建 IK 样条线控制柄”(Skeleton Create IK Sp…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 837 字 ≥300，非承重" -->，以打开 [IK 样条线控制柄工具](IK%20样条线控制柄工具%28IK%20Spline%20Handle%20Tool%29.md)设置。

2. 禁用“根在曲线上”(Root on Curve)、“自动将曲线结成父子关系”(Auto Parent Curve)、“自动创建曲线”(Auto Create Curve)和“将曲线捕捉到根”(Snap Curve to Root)。

3. 启用“自动创建根轴”(Auto Create Root Axis)。

4. 单击起始关节、末关节，然后单击 NURBS 曲线。

  这样便创建了样条线 IK 控制柄，并且父变换节点在起始关节的上方。在以下步骤中，您将节点放置在运动路径上，从而防止起始关节翻转。

5. 选择父变换节点，然后按住 Shift 键并单击该曲线。

  可以通过围绕起始关节拖动选择框来选择父变换节点。

6. 选择“约束 > 运动路径 > 连接到运动路径”(Constrain > Motion Paths > Attach to Motion Path) > ![图：选择“约束 运动路径 连接到运动路径”(Constrain Motion Paths Attach to Motion …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 837 字 ≥300，非承重" -->。

7. 在“连接到运动路径选项”(Attach to Motion Path Options)中，启用“开始/结束”(Start/End)。

8. 对于“开始时间”(Start Time)和“结束时间”(End Time)，为关节链的运动输入帧范围。

  父变换节点及其子关节链在指定的帧范围内从曲线的起点移动到曲线的终点。

9. 启用“跟随”(Follow)。

  如果曲线具有 3D 循环形状，则可能还需要为“向上方向”(Up Direction)启用“法线”(Normal)以避免不需要的翻转。

10. 使所有其他选项保持其默认设置，然后单击“附加”(Attach)。

  现在，当您播放动画时，父变换节点和关节链沿曲线路径移动。移动应避免意外翻转。但是，如果路径非常复杂，则翻转是不可避免的。

  **注**

  可以使用 IK 控制柄的侧滚和扭曲操纵器来侧滚和扭曲关节链以获取额外的控制。请参见

  使用 IK 为关节设定姿势

  。

## 相关主题

- [“连接到运动路径”(Attach to Motion Path)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-69E8C704-1A7B-4C83-9333-80C3118541F6.htm)选项
