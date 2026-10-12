# tangentConstraint

## 切线约束属性(Tangent Constraint Attributes)

#### 锁定输出(Lock Output)

指定是否可以直接操纵对象的受约束通道。例如，当切线约束的“锁定输出”(Lock Output)属性处于禁用状态时，可以将受约束对象的方向更改为与驱动者曲线不同的方向。

当受约束对象的“锁定输出”(Lock Output)属性处于启用状态时，只能通过变换其驱动者对象来操纵其受约束通道。当受约束对象的“锁定输出”(Lock Output)属性处于禁用状态时，可以直接操纵其受约束通道，而无需变换其驱动者对象。

**注**

“动画融合”(Animation Blending)首选项影响“锁定输出”(Lock Output)属性的默认状态。

#### 目标向量(Aim Vector)

指定目标向量相对于受约束对象局部空间的方向。目标向量 (aim vector) 与目的向量 (target vector) 对齐，强制受约束对象相应地确定其自身的方向。默认情况下指定对象的局部旋转正 X 轴与目标向量对齐，而目标向量与目的向量 (1.0000, 0.0000, 0.0000) 对齐。

#### 上方向向量(Up Vector)

指定上方向向量相对于受约束对象局部空间的方向。默认情况下指定对象的局部旋转正 Y 轴与上方向向量对齐。而默认情况下，上方向向量会尝试与世界上方向向量对齐。另外，默认情况下，世界上方向向量指向世界空间的正 Y 轴方向 (0.0000, 1.0000, 0.0000)。

如果将上方向向量定义为指向与目标向量相同的方向，受约束对象将与运动历史存在相关性。有关详细信息，请参见[运动历史相关性效果](../../../../约束/约束/目标约束.md#WS17956D7ADBC6E736-3392E17117AE30CC4B-7FF7)。

#### 世界上方向向量(World Up Vector)

指定世界上方向向量相对于场景世界空间的方向。由于默认情况下 Maya 的世界空间是“Y 轴向上”，因此默认世界上方向向量指向世界空间正 Y 轴的方向 (0.0000, 1.0000, 0.0000)。

#### 世界上方向类型(World Up Type)

指定世界上方向向量的作用。选项包括“场景上方向”(Scene Up)、“对象上方向”(Object Up)、“对象旋转上方向”(Object Rotation Up)、“向量”(Vector)和“无”(None)。

#### 场景上方向(Scene Up)

指定上方向向量尝试与场景上方向轴而不是世界上方向向量对齐。世界上方向向量将被忽略。

（若要指定场景的上方向轴，请选择“窗口 > 设置/首选项 > 首选项”(Windows > Settings/Preferences > Preferences)。在“首选项”(Preferences)窗口的“设置”(Settings)类别中，选择 Y 轴或 Z 轴作为“世界坐标系”(World Coordinate System)的“上方向轴”(Up Axis)。Y 轴是默认设置。）

#### 对象上方向(Object Up)

指定上方向向量尝试对准指定对象的原点，而不是与世界上方向向量对齐。世界上方向向量将被忽略。上方向向量尝试对准其原点的对象称为世界上方向对象。可以通过 [aimConstraint](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Tech-Docs/Commands/aimConstraint.html) MEL 命令（使用 -wuo 标志）指定世界上方向对象。如果未指定世界上方向对象，上方向向量将尝试对准场景世界空间的原点。

#### 对象旋转上方向(Object Rotation Up)

指定相对于某个对象的局部空间（而不是相对于场景的世界空间）定义世界上方向向量。在相对于场景的世界空间变换上方向向量后，其会尝试与世界上方向向量对齐。上方向向量尝试对准其原点的对象称为世界上方向对象。可以通过 [aimConstraint](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Tech-Docs/Commands/aimConstraint.html) MEL 命令（使用 -wuo 标志）指定世界上方向对象。如果未指定世界上方向对象，世界上方向向量将定义为相对于场景的世界空间。

#### 向量(Vector)

指定上方向向量尝试与世界上方向向量尽可能近地对齐。世界上方向向量是相对于场景的世界空间定义的。（这是默认设置。）

#### 无(None)

指定不会计算受约束对象相对于目标向量的方向。方向仍然保持为在指定“无”(None)前的相应方向。选择“无”(None)后，受约束对象将变为与运动历史存在相关性。有关详细信息，请参见[运动历史相关性效果](../../../../约束/约束/目标约束.md#WS17956D7ADBC6E736-3392E17117AE30CC4B-7FF7)。

#### 世界上方向对象(World Up Object)

指定上方向向量尝试对准指定对象的原点，而不是与世界上方向向量对齐。世界上方向向量将被忽略。上方向向量尝试对准其原点的对象称为世界上方向对象。可以通过 [aimConstraint](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Tech-Docs/Commands/aimConstraint.html) MEL 命令（使用 -wuo 标志）指定世界上方向对象。如果未指定世界上方向对象，上方向向量将尝试对准场景世界空间的原点。

#### 约束旋转(Constraint Rotate)

显示受约束对象的当前方向。

#### 约束向量(Constraint Vector)

通知当前的目的向量，即与目标向量对齐的向量。

#### 启用静止位置(Enable Rest Position)

请参见[静止位置属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-0DB1A8D5-DF02-46D6-B090-2122979EA403.htm)。

#### 静止旋转(Rest Rotate)

请参见[静止位置属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-0DB1A8D5-DF02-46D6-B090-2122979EA403.htm)。
