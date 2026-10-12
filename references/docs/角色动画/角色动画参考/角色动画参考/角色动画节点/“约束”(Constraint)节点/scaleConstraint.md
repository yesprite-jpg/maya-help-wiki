# scaleConstraint

## 缩放约束属性(Scale Constraint Attributes)

#### 锁定输出(Lock Output)

指定是否可以直接操纵对象的受约束通道。例如，如果禁用缩放约束的“锁定输出”(Lock Output)属性，则可以更改受约束对象的大小，无需缩放驱动者对象。

如果启用受约束对象的“锁定输出”(Lock Output)属性，则只能通过变换其驱动者对象来操纵其受约束通道。当受约束对象的“锁定输出”(Lock Output)属性处于禁用状态时，可以直接操纵其受约束通道，而无需变换其驱动者对象。

**注**

“动画融合”(Animation Blending)首选项影响“锁定输出”(Lock Output)属性的默认状态。

#### 偏移(Offset)

为受约束对象指定相对于目标点的偏移位置（平移 X、Y 和 Z）。请注意，目标点是目标对象旋转枢轴的位置，或是多个目标对象旋转枢轴的平均位置。默认值均为 0。

#### 约束缩放(Constraint Scale)

通知您有关受约束对象的当前缩放。

#### 启用静止位置(Enable Rest Position)

请参见[静止位置属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-0DB1A8D5-DF02-46D6-B090-2122979EA403.htm)。

#### 静止缩放(Rest Scale)

请参见[静止位置属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-0DB1A8D5-DF02-46D6-B090-2122979EA403.htm)。
