# nParticle 弹簧疑难解答

本节说明了使用弹簧时可能遇到的一些问题的解决方法。

## 弹簧过度展开和收缩

通常可以通过增加动力学计算的过采样来解决弹簧展开或收缩过度的问题。增加过采样会减慢播放速度，但会提高弹簧的稳定性。

执行以下步骤以增加过采样：

1. 在“Fx”菜单集中，选择“字段/解算器 > 编辑过采样或缓存设置”(Fields/Solvers > Edit Oversampling or Cache Settings)。

  显示“属性编辑器”(Attribute Editor)。

2. 为“过采样”(Over Samples)输入一个值。

  **注**

  提示：

  增加过采样可以增强目标的吸引力。如果在包含目标的场景中增加过采样，则在必要时可以通过降低目标权重进行补偿。

  某些情况下，Maya 所使用的过采样率大于输入的值。这对于内部计算来说是必要的。

## 弹簧不会移动粒子，CV、顶点或点

粒子上未施加任何作用力，或“逐弹簧静止长度”已打开但未设定任何值。默认情况下，每根弹簧的静止长度均等于其原始长度。除非对其施加外力，否则它不会移动。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-SimulationEffects/images/GUID-C172964A-E84D-4979-B805-5A048A5B1CC6.png) <!-- baize:img-hook downloaded=false reason="正文 2245 字 ≥300，非承重" -->

若要使弹簧生效，请执行相应的操作，如下所示：

1. 例如，通过场为对象设定动画。

2. 使用“组件编辑器”(Component Editor)改变“逐弹簧静止长度”(Per-spring restLength)。请参见[编辑逐弹簧静止长度、刚度和阻尼](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-SimulationEffects/files/GUID-78F08033-903D-4CE5-BA57-8E5284202A2A.htm)。

3. 改为逐对象静止长度。

4. 如果弹簧在粒子上，且时间和粒子形状节点“当前时间”(Current Time)属性的默认连接已断开，则请重新将输入连接至“当前时间”(Current Time)。有一种简单的方法可以重新连接时间输入，即，选择粒子对象、选择“通道盒”(Channel Box)中的“当前时间”(Current Time)属性，然后选择“nParticle > 连接到时间”(nParticles > Connect to Time)。

## 缓慢播放含多根弹簧的动画

如果任意或所有粒子的年龄超出了寿命，则 Maya 会从对象中将这些粒子移除。为方便起见，我们将此类粒子描述为即将消亡的粒子。如果场景中包含一个粒子对象（该粒子对象中包含多根弹簧）但不包含即将消亡的粒子，则由于复杂的计算，所以无需缓慢播放动画。可以关闭“管理粒子消亡”(Manage Particle Death)属性，以排除计算并增强播放效率。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-SimulationEffects/images/GUID-BCAE940B-6571-42D3-BE97-4A40667238E5.png) <!-- baize:img-hook downloaded=false reason="正文 2245 字 ≥300，非承重" -->

简而言之，如果这些粒子未消亡，则这有助于关闭与以下对象相关的弹簧对象的“管理粒子消亡”(Manage Particle Death)：

- 柔体

- “粒子工具”(Particle Tool)制成的对象

- 发射的粒子

若对象中的所有粒子均已消亡，则请勿关闭“管理粒子消亡”(Manage Particle Death)。附加在粒子上的“弹簧”(Springs)不会正确运作。如果对象中存在曾今消亡的粒子，则会发生上述情况。如果在不再产生消亡粒子的那点上设定初始状态操作粒子的当前属性值，您仍然不得关闭“管理粒子消亡”(Manage Particle Death)。

若要关闭“管理粒子消亡”(Manage Particle Death)，请选择弹簧对象并显示“属性编辑器”(Attribute Editor)。关闭“弹簧属性”(Spring Attributes)区域中的“管理粒子消亡”(Manage Particle Death)属性。

## 您可以编辑逐弹簧属性，但并不能产生效果

您可能已经关闭“逐弹簧刚度”(Per-spring Stiffness)、“逐弹簧阻尼”(Per-spring Damping)或“逐弹簧静止长度”(Per-spring Rest Length)，这意表示 Maya 已改用逐对象对应属性。打开相应的“使用”(Use)属性。

## 包含弹簧的多边形或 NURBS 柔体会降低播放速度，并产生不真实的弹簧运作。

若将弹簧放置在包含多个顶点（和粒子）的多边形柔体或 NURBS 柔体上，则动画播放速度会变慢，且弹簧的展开和收缩可能会不真实。

若要避免出现此类问题，请将弹簧放置在对象的低分辨率副本上，如下所示：

1. 在采用默认选项的情况下，复制多边形（或 NURBS 对象）。

  请注意，整段动画的副本都必须位于原始位置。

2. 将对象的曲面分辨率大致降低至其原始分辨率的 10-50%。

  减少多边形对象的“X 向细分数”(Subdivisions X)和 Y 值。减少 NURBS 对象的“跨度数”(Spans)和“分段数”(Sections)值。

  剩余步骤中，原始对象称为低分辨率对象，副本称为高辨率对象。

3. 在采用默认选项的情况下，使低分辨率对象成为柔体。

4. 选择柔体粒子，并将其连接到所需的动力学中。

  例如，将粒子连接到重力，并使其与其他对象碰撞。

5. 在采用默认选项的情况下，在柔体粒子上创建弹簧。

6. 调整柔体动画外观。

  您可能需要将弹簧“刚度”(Stiffness)设定为 100 以上。您还可能需要选择“字段/解算器 > 编辑过采样或缓存设置”(Fields/Solvers > Edit Oversampling or Cache Settings)，并将“过采样”(Over Samples)设定在 2 和 4 之间。使用可给出所需柔体变形外观的最小值。

7. 使用“大纲视图”(Outliner)选择高分辨率对象的变换节点，然后按住 Ctrl 键（Linux 和 Windows）或按住 Command 键 (Mac OS X) 并选择低分辨率对象。

8. 从“动画”(Animation)菜单集中，选择“动画变形 > 打开完整的变形菜单 > 包裹”(Anim Deform > Open Full Deform Menu > Wrap)。

  播放动画时，这样可以强制使高分辨率对象的变形与低分辨率对象的变形相同。

9. 隐藏低分辨率对象。
