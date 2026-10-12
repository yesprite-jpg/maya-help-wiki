# orientConstraint

## 方向约束属性(Orient Constraint Attributes)

#### 锁定输出(Lock Output)

指定是否可以直接操纵对象的受约束通道。例如，当方向约束的“锁定输出”(Lock Output)属性禁用时，您无需旋转驱动者对象即可更改受约束对象的方向。

当受约束对象的“锁定输出”(Lock Output)属性启用时，您只能通过变换其驱动者对象来操纵其受约束通道。当受约束对象的“锁定输出”(Lock Output)属性处于禁用状态时，可以直接操纵其受约束通道，而无需变换其驱动者对象。

**注**

“动画融合”(Animation Blending)首选项影响“锁定输出”(Lock Output)属性的默认状态。

#### 偏移(Offset)

为相对于目标点的受约束对象指定偏移位置。请注意，目标点是目标对象旋转枢轴的位置，或是多个目标对象旋转枢轴的平均位置。默认值均为 0。

#### 插值类型(Interp Type)

为约束设定旋转插值类型。仅当受约束对象有多个目标时，“插值类型”(Interp Type)才相关。

#### 平均(Average)值

计算受约束对象和其目标之间的旋转平均值。

#### 最短(Shortest)

使用四元数插值查找从受约束对象到其目标的旋转之间的最短路径。

#### 最长(Longest)

使用四元数插值查找从受约束对象到其目标的旋转之间的最长路径。该路径方向与“最短”(Shortest)路径相反。

**注**

提示：

在“最短”(Shortest)和“最长”(Longest)旋转插值之间设定关键帧以防止翻转。

#### 无翻转(No Flip)

“无翻转”(No Flip)将当前旋转缓存到受约束对象上。一旦选择了“无翻转”(No Flip)，就必须单击“缓存”(Cache)按钮创建缓存。

#### 缓存(Cache)

如果在受约束对象上存在缓存插值，缓存会显示在“插值类型”(Interp Type)菜单字段中。

#### 创建(Create)

将当前旋转插值缓存到受约束对象上。缓存将减少翻转的机会。仅当选择“无翻转”(No Flip)时才可用。

#### 删除(Delete)

从受约束对象删除当前旋转插值缓存。仅当“缓存”(Cache)显示在“插值类型”(Interp Type)菜单场中时才可用。

#### 约束旋转(Constraint Rotate)

告知您受约束对象的当前方向。

#### 启用静止位置(Enable Rest Position)

请参见[静止位置属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-0DB1A8D5-DF02-46D6-B090-2122979EA403.htm)。

#### 静止平移(Rest Translate)

请参见[静止位置属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-0DB1A8D5-DF02-46D6-B090-2122979EA403.htm)。
