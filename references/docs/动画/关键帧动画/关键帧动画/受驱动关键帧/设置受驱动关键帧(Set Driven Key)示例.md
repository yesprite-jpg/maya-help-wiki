# 设置受驱动关键帧(Set Driven Key)示例

此示例说明了如何使用“设置受驱动关键帧”(Set Driven Key)将门对象属性链接到球属性，以便球的移动驱动门的移动。

您可以轻松设置相似场景，以便自己尝试该示例：

- 创建一个多边形立方体或平面，并命名为 Door。

  （缩放并放置，使其大致沿 X 轴。）

- 创建一个小型多边形球体，并命名为 Ball。

  （缩放并将其放置在门前面，大致位于 0,1,10。）

将门的移动链接到球的移动

1. 选择门，然后选择“关键帧 > 设置受驱动关键帧 > 设置”(Key > Set Driven Key > Set)。

  “设置受驱动关键帧”(Set Driven Key)窗口将显示，并在“受驱动”(Driven)列表中包含该门。

2. 在场景视图中选择球，然后单击“加载驱动者”(Load Driver)。

  球会显示在“驱动者”(Driver)列表中。

3. 在“受驱动”(Driven)列表（由球的移动驱动的属性）中选择“平移 Y”(Translate Y)，并在“驱动者”(Driver)列表（驱动门的属性）中选择“平移 Z”(Translate Z)，然后单击“关键帧”(Key)。

  ![图：在“受驱动”(Driven)列表（由球的移动驱动的属性）中选择“平移 Y”(Translate Y)，并在“驱动者”(D…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-67992685-8DBD-4696-B358-0F32C73BC48F.png) <!-- baize:img-hook downloaded=false reason="正文 1260 字 ≥300，非承重" -->

  这会设置受驱动关键帧关系，以将球的当前“平移 Z”(Translate Z)值链接到门的当前“平移 Y”(Translate Y)值。每当球的“平移 Z”(Translate Z)值位于该位置时，门的“平移 Y”(Translate Y)值都将在其当前位置。

4. 使用“移动工具”(Move Tool)（热键 **W**）将球直接放置在门上，然后将门移动到球上方。

  ![图：使用“移动工具”(Move Tool)（热键 W）将球直接放置在门上，然后将门移动到球上方。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-29F005B3-887C-422E-AF97-1BFF7B3C367C.png) <!-- baize:img-hook downloaded=false reason="正文 1260 字 ≥300，非承重" -->

5. 在“设置受驱动关键帧”(Set Driven Key)窗口中，单击“关键帧”(Key)。

  这会设定另一个受驱动关键帧，以将球的当前“平移 Z”(Translate Z)值链接到门的“平移 Y”(Translate Y)值。

6. 将球移过门，然后将门下降到先前的位置。

  ![图：将球移过门，然后将门下降到先前的位置。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-0B98252A-BE34-460E-843B-58538534E7A7.png) <!-- baize:img-hook downloaded=false reason="正文 1260 字 ≥300，非承重" -->

7. 在“设置受驱动关键帧”(Set Driven Key)窗口中，单击“关键帧”(Key)。

  您设置了三个受驱动关键帧来链接不同位置的属性值。如果从任一侧朝门方向拖动球，门会平滑上升。在“设置受驱动关键帧”(Set Driven Key)窗口中，选择“关键帧 > 转到下一个”(Key > Go To Next)或“关键帧 > 转到上一个”(Key > Go To Previous)，以浏览受驱动关键帧。

  注意，从“时间滑块”(Time Slider)播放动画不会移动球或门。这是因为受驱动关键帧虽将属性链接到其他属性，但未将属性链接到“时间滑块”(Time Slider)中的时间。但是，如果您继续设置关键帧并设置放置球的动画，门仍会基于受驱动关键帧关系自动移动。

8. （可选）要在球接近门时使门上升得更快、更慢或更高，您可以使用“曲线图编辑器”(Graph Editor)编辑表示受驱动关键帧关系的曲线的形状。请参见[在“曲线图编辑器”(Graph Editor)中查看和编辑受驱动关键帧关系](在“曲线图编辑器”%28Graph%20Editor%29中查看和编辑受驱动关键帧关系.md)。

  在“曲线图编辑器”(Graph Editor)中，Y 轴表示受驱动属性值，X 轴表示驱动者属性值，因此曲线表示，在球的“平移 Z”(Translate Z)值接近 0 时，门的“平移 Y”(Translate Y)值如何变化。
