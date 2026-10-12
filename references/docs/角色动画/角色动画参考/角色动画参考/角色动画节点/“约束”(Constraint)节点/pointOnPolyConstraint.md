# pointOnPolyConstraint

pointOnPolyConstraint 节点是在创建多边形上的点约束时创建的。请参见[创建多边形上的点约束](../../../../约束/约束/多边形上的点约束/创建多边形上的点约束.md)。

可以通过以下两种方式访问这些属性：当选择 pointOnPolyConstraint 节点时在“通道盒”(Channel Box)中进行访问，或在“多边形上的点约束属性”(Point On Poly Constraint Attributes)和“附加属性”(Extra Attributes)标题下“属性编辑器”(Attribute Editor)的 pointOnPolyConstraint 选项卡中进行访问。

#### 锁定输出(Lock Output)

当受约束对象的“锁定输出”(Lock Output)属性处于启用状态时，只能通过变换其驱动者对象来操纵它的受约束通道。当受约束对象的“锁定输出”(Lock Output)属性处于禁用状态时，可以直接操纵受约束的通道，无需变换其驱动者对象。

例如，如果多边形上的点约束的“锁定输出”(Lock Output)属性处于禁用状态，可以更改受约束对象的位置，无需移动约束网格对象。

#### 偏移平移(Offset Translate)

通过这些字段，可以从约束网格的位置偏移受约束对象的位置。

#### 偏移旋转(Offset Rotate)

通过这些字段，可以从约束网格的旋转来偏移受约束对象的旋转。

#### 约束平移(Constraint Translate)

显示受约束对象的当前位置。此值在指定“偏移平移”(Offset Translate)值时非常有用。此字段是只读字段。

#### 约束旋转(Constraint Rotate)

显示受约束对象的当前旋转。此值在指定“偏移旋转”(Offset Rotate)值时非常有用。此字段是只读字段。

#### 启用静止位置(Enable Rest Position)

请参见[静止位置属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-0DB1A8D5-DF02-46D6-B090-2122979EA403.htm)。

#### 静止平移(Rest Translate)

请参见[静止位置属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-0DB1A8D5-DF02-46D6-B090-2122979EA403.htm)。

#### 静止旋转(Rest Rotate)

请参见[静止位置属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-0DB1A8D5-DF02-46D6-B090-2122979EA403.htm)。

如果多边形上的点约束包括多个受约束对象，还可以为每个对象设定权重和 UV 属性。请参见[附加属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-145E46A2-A770-4BD5-8381-9AE91C687E57.htm#WS73099CC142F48755-7B21313411809411AE9-5996)。

## 相关主题

- [多边形上的点约束](../../../../约束/约束/多边形上的点约束.md)

- [编辑多边形上的点约束](../../../../约束/约束/多边形上的点约束/编辑多边形上的点约束.md)
