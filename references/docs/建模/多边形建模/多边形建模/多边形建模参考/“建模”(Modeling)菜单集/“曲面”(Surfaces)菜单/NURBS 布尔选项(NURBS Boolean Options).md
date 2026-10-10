# NURBS 布尔选项(NURBS Boolean Options)

使用以下选项可设置在选择“曲面 > 布尔 > 并集工具/差集工具/交集工具”(Surfaces > Booleans > Union Tool/Difference Tool/Intersection Tool)时发生的情况。

#### 删除输入(Delete Inputs)

Maya 会从原始曲面保留构建历史输入，以便您可以对其进行变换来更改结果布尔曲面。如果不希望保留该历史输入，启用“删除输入”(Delete Inputs)。此外，必须在场景中禁用构建历史。如果启用构建历史，Maya 会不顾该选项而保留历史输入。

#### 工具行为(Tool Behavior)

启用时，“完成时退出”(Exit On Completion)在计算布尔运算后使您退出“布尔”(Boolean)工具。禁用时，布尔工具保留当前的工具，以便您可以继续执行其他“布尔”(Boolean)运算。

“层次选择”(Hierarchy Selection)选项确保您可以在前“布尔”(Boolean)运算结果上成功地执行布尔。启用时，Maya 在任何给定层次的根上选择并执行“布尔”(Boolean)运算。如果要在相同组内的对象上执行“布尔”(Boolean)运算，必须禁用“层次选择”(Hierarchy Selection)。

## 相关主题

- [对曲面执行布尔运算](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-8F4663A0-BD9C-46E5-BB04-21C98F1F0EF4.htm)
