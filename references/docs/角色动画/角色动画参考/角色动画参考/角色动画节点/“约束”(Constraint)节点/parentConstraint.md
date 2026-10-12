# parentConstraint

选择受约束或约束对象时，您可以在[属性编辑器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67A58D31-4722-4769-B3E6-1A35B5B53BED)中的 oarentConstraint 选项卡上查看或编辑父约束节点的属性。T

以下部分介绍了特定于“父”(Parent)约束节点 (parentConstraint) 的属性。请参见[常规约束节点属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-145E46A2-A770-4BD5-8381-9AE91C687E57.htm)。

## 父约束目标偏移

通过这些属性，可以修改受约束对象与目标对象之间的偏移。如果有多个目标对象，则每个对象与各自的“平移”(Translate)和“旋转”(Rotate)偏移值一起列出。请参见[修改父约束偏移](../../../../约束/约束/父约束/编辑父约束/修改父约束偏移.md)。

#### 平移(Translate)

为目标对象和受约束对象之间的偏移输入 XYZ 平移值。

#### 旋转(Rotate)

为目标对象和受约束对象之间的偏移输入 XYZ 平移值。

#### 更新(Update)

如果在场景中移动了受约束对象或目标对象，请单击以将目标偏移值更新到当前对象位置。

#### 关键帧(Key)

单击以为当前时间的目标偏移值设定关键帧。

## 父约束属性(Parent Constraint Attributes)

#### 锁定输出(Lock Output)

指定是否可以直接操纵对象的受约束通道。例如，如果父约束的“锁定输出”(Lock Output)属性处于禁用状态，则可以更改受约束对象的位置和方向，而不必移动或旋转驱动者对象。

如果受约束对象的“锁定输出”(Lock Output)属性处于启用状态，则只能通过变换其驱动者对象操纵其受约束通道。当受约束对象的“锁定输出”(Lock Output)属性处于禁用状态时，可以直接操纵其受约束通道，而无需变换其驱动者对象。

**注**

“动画融合”(Animation Blending)首选项影响“锁定输出”(Lock Output)属性的默认状态。

#### 插值类型(Interp Type)

为约束设定旋转插值类型。仅当受约束对象有多个目标时，“插值类型”(Interp Type)才相关。

#### 平均(Average)值

计算受约束对象和其目标之间的旋转平均值。

#### 最短(Shortest)

使用四元数插值查找从受约束对象到其目标的旋转之间的最短路径。

#### 最长(Longest)

使用四元数插值查找从受约束对象到其目标的旋转之间的最长路径。该路径方向与“最短”(Shortest)路径相反。

#### 无翻转和缓存(No Flip and Cache)

“无翻转”(No Flip)将当前旋转缓存到受约束对象上。一旦选择了“无翻转”(No Flip)，必须单击“缓存”(Cache)按钮创建缓存。当受约束对象上有缓存的插值时，缓存将出现在“插值类型”(Interp Type)菜单字段中。

#### 缓存创建按钮(Cache Create button)

将当前旋转插值缓存到受约束对象并为约束的节点上的当前旋转插值创建动画曲线。缓存可减少翻转的机会。仅当选择“无翻转”(No Flip)时可用。

#### 缓存删除按钮(Cache Delete button)

从受约束对象删除当前旋转插值缓存。只有当“缓存”(Cache)出现在“插值类型”(Interp Type)菜单字段时可用。

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
