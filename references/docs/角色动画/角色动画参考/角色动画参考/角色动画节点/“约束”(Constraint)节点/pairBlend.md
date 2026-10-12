# pairBlend

当同时将关键帧动画和约束应用到对象时，将自动生成 [pairBlend](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Tech-Docs/Nodes/pairBlend.html) 节点。一旦动画和约束被链接到 [pairBlend](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Tech-Docs/Nodes/pairBlend.html) 节点，可以修改动画约束融合的权重来生成各种效果。请参见[通道盒中的融合权重](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-E296FB24-D58A-4196-861D-DDB39E3B8E28.htm#WS17956D7ADBC6E7363438120E117AE30D38F-7FDA)。

在依存关系图 (DG) 中，pairBlend 节点可作为约束、关键帧动画以及应用约束和关键帧动画的对象之间的链接。pairBlend 节点连接类似于：所有目标对象连接到约束节点、约束节点和关键帧动画连接到 pairBlend 节点，以及 pairBlend 节点连接到对象。

将多个约束应用到同一对象时，将为每个约束创建单独的 pairBlend 节点，同时将受约束对象的关键帧动画通道连接到 pairBlend 节点作为它们的相关约束。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-8C628074-F48C-4958-AC74-FC7BE774F289.png) <!-- baize:img-hook downloaded=false reason="正文 2074 字 ≥300，非承重" -->

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-61091718-DFCC-4E35-9571-CF7605723EBF.png) <!-- baize:img-hook downloaded=false reason="正文 2074 字 ≥300，非承重" -->

## 相关主题

- [动画约束融合](../../../../约束/约束/融合动画和约束/动画约束融合.md)

- [设置受驱动关键帧约束融合](../../../../约束/约束/融合动画和约束/设置受驱动关键帧约束融合.md)

- [为对象设置动画并约束对象](../../../../约束/约束/融合动画和约束/为对象设置动画并约束对象.md)

  **注**

  输入 1 始终代表受约束对象上的关键帧动画，输入 2 则始终代表约束节点。

## pairBlend 属性(pairBlend Attributes)

#### 平移 X 模式(Translate X Mode)

选择下列选项之一：

#### 融合输入(Blend Inputs)

输入 1 和输入 2 的融合 X 平移用于控制受驱动对象的 X 平移。

#### 仅输入 1 (Input 1 only)

输入 1 的 X 平移用于控制受驱动对象的 X 平移。

#### 仅输入 2 (Input 2 only)

输入 2 的 X 平移用于控制受驱动对象的 X 平移。

#### 平移 Y 模式(Translate Y Mode)

选择下列选项之一：

#### 融合输入(Blend Inputs)

输入 1 和输入 2 的融合 Y 平移用于控制受驱动对象的 Y 平移。

#### 仅输入 1 (Input 1 only)

输入 1 的 Y 平移用于控制受驱动对象的 Y 平移。

#### 仅输入 2 (Input 2 only)

输入 2 的 Y 平移用于控制受驱动对象的 Y 平移。

#### 平移 Z 模式(Translate Z Mode)

选择下列选项之一：

#### 融合输入(Blend Inputs)

输入 1 和输入 2 的融合 Z 平移用于控制受驱动对象的 Z 平移。

#### 仅输入 1 (Input 1 only)

输入 1 的 Z 平移用于控制受驱动对象的 Z 平移。

#### 仅输入 2 (Input 2 only)

输入 2 的 Z 平移用于控制受驱动对象的 Z 平移。

#### 旋转模式(Rotate Mode)

通过融合沿所有轴的指定输入的旋转来计算旋转。

#### 融合输入(Blend Inputs)

输入 1 和输入 2 的融合 X、Y 和 Z 旋转用于控制受驱动对象沿所有轴的旋转。

#### 仅输入 1 (Input 1 only)

输入 1 的 X、Y 和 Z 旋转用于控制受驱动对象沿所有轴的旋转。

#### 仅输入 2 (Input 2 only)

输入 2 的 X、Y 和 Z 旋转用于控制受驱动对象沿所有轴的旋转。

#### 旋转插值(Rot Interpolation)

有关详细信息，请参见 [Maya 中的动画旋转](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-CBD30A0A-1166-4076-A564-1ADC946A15F3)。

#### Euler 角

当“pairBlend”权重值介于 0（由关键帧驱动）和 1（由约束驱动）之间时，可以使用“Euler 角度”(Euler Angles)。“Euler 角度”(Euler Angles)是默认的旋转插值。

**注**

在用于关键帧和约束之间的插值时，Euler 角度可能会导致翻转。如果出现这种情况，建议切换到四元数旋转。

#### 四元数(Quaternion)

四元数会对关键帧约束融合进行平滑插值，而不会产生异常（如翻转）。当“pairBlend”权重值为 1 或 0 时，请使用“四元数”(Quaternion)。

#### 当前驱动者(Current Driver)

设定当前驱动选定对象的选项。

从下列选项中进行选择：

#### 输入 1 (Input 1)

受约束对象由其关键帧动画驱动。

#### 输入 2 (Input 2)

受约束对象由约束驱动。

#### 权重(Weight)

显示融合值（决定约束和关键帧动画对受约束对象的影响程度）。该字段为只读类型。请参见[融合约束 n (Blend Constraintn)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-E296FB24-D58A-4196-861D-DDB39E3B8E28.htm#WS73099CC142F48755-7B21313411809411AE9-5863)。

#### 输入平移(In Translate)

“输入平移”(In Translate)字段显示输入 1 和输入 2 的 X、Y 和 Z 平移值。n 表示输入编号。

#### 输入旋转(In Rotate)

“输入旋转”(In Rotate)字段显示输入 1 和输入 2 的 X、Y 和 Z 旋转值。n 表示输入编号。

#### 缓存(Caching)

与 Maya 中的其他缓存数据（例如，动力学、Maya® nCloth™、Maya® 经典布料™和 Maya® 流体效果™ 中的缓存）不同，对“pairBlend”的缓存数据还是一个动画曲线。请参见[缓存](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-145E46A2-A770-4BD5-8381-9AE91C687E57.htm#WS73099CC142F48755-7B21313411809411AE9-59A5)。

#### 节点状态(Node State)

请参见[节点状态](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-145E46A2-A770-4BD5-8381-9AE91C687E57.htm#WS17956D7ADBC6E7363438120E117AE30D38F-7FE0)。

## 通道盒(Channel Box)中的融合权重(Blend Weights)

**注**

选择受驱动对象后，可以在

“形状 > objectn_typeConstraintn”(SHAPES > objectn_typeConstraintn)

或

“输入 > pairBlend”(INPUTS > pairBlendn)

下的

“通道盒”(Channel Box)

查看其所有目标与融合权重值。

#### 融合约束 n (Blend Constraintn)

关键帧动画约束融合值决定了约束和关键帧动画对受约束对象的影响程度。如果该值为 0，关键帧动画可完全控制受约束对象的变换。如果该值为 1，约束可完全控制受约束对象的变换。

如果有超过一个同类型约束被应用于对象，n 即代表约束编号。该值在 [pairBlend](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Tech-Docs/Nodes/pairBlend.html) 节点的属性中显示为“权重”(Weight)。
