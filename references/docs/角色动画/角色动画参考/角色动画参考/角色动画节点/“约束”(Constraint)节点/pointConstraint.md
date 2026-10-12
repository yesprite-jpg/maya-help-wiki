# pointConstraint

## 点约束属性(Point Constraint Attributes)

#### 锁定输出(Lock Output)

指定是否可以直接操纵对象的受约束通道。例如，当点约束的“锁定输出”(Lock Output)属性处于禁用状态时，可以在不移动驱动者对象的情况下更改受约束对象的位置。

当受约束对象的“锁定输出”(Lock Output)属性处于启用状态时，只能通过变换受约束对象的驱动者对象来操纵其受约束的通道。当受约束对象的“锁定输出”(Lock Output)属性处于禁用状态时，可以直接操纵其受约束通道，而无需变换其驱动者对象。

**注**

“动画融合”(Animation Blending)首选项影响“锁定输出”(Lock Output)属性的默认状态。

#### 偏移(Offset)

为受约束对象指定相对于目标点的偏移位置（平移 X、Y 和 Z）。请注意，目标点是目标对象旋转枢轴的位置，或是多个目标对象旋转枢轴的平均位置。默认值均为 0。

#### 偏移极性(Offset Polarity)

指定“约束偏移”(Constraint Offset)的极性。实际上，“约束偏移”(Constraint Offset)的值与“偏移极性”(Offset Polarity)相乘，从而确定受约束对象的位置。默认值是 1。

#### 约束平移(Constraint Translate)

通知您受约束对象的当前位置。指定“约束偏移”(Constraint Offset)和“偏移极性”(Offset Polarity)时需要知道该属性。

#### 启用静止位置(Enable Rest Position)

请参见[静止位置属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-0DB1A8D5-DF02-46D6-B090-2122979EA403.htm)。

#### 静止平移(Rest Translate)

请参见[静止位置属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-0DB1A8D5-DF02-46D6-B090-2122979EA403.htm)。
