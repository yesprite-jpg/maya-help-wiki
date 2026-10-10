# 优化 nCloth

本部分详细介绍提高 nCloth 模拟播放速度的方法。

| 模拟低分辨率 nCloth 对象 | 修改和模拟非最终 nCloth 对象时保持低多边形计数。完成对模拟的更改后，对多边形网格进行平滑处理。如果必须使用高分辨率模型进行修改，请将输出布料网格用作包裹变形器。 |
|---|---|
| 适当地对 nCloth 执行建模 | 将 nCloth 建模为大小统一或尽可能接近统一的四边形。 |
| 在适当的情况下禁用碰撞 | 禁用任何不必要的碰撞以大大减少在模拟期间执行的计算量。 |
| 调整自碰撞设置 | 减少 nClothShape 节点的“厚度”(Thickness)属性以加快自碰撞速度。当“自碰撞标志”(Self Collision Flag)未设定为“顶点”(Vertex)时，这种改进尤为常用。如果“自碰撞标志”(Self Collision Flag)设定为“顶点”(Vertex)，则调整“自碰撞宽度比例”(Self Collide Width Scale)，以便碰撞球体几乎不会互相接触。 |
| 使用顶点向外推技术 | 对 nCloth 对象和所有 nRigid 或被动对象禁用所有碰撞。 对于每个 nRigid 对象，在“属性编辑器”(Attribute Editor)的“质量设置”(Quality Settings)区域中，将“向外推”(Push Out)值设定为 1。 运行模拟。 在模拟运行期间，调整“向外推影响半径”(Push Out Radius)值，以便该值在保持碰撞仍正确显示的同时尽可能小。 将 nRigid 对象的“厚度”(Thickness)调整为足够大，以便 nCloth 三角形不会穿透该对象。 如果碰撞显示不正确，则激活 nCloth 和 nRigid 对象的“质量设置”(Quality Settings)区域中的“陷阱检查”(Trapped Check)。 |
| 使用约束 | 如果一个布料区域需要具有刚度，则使用“组件到组件”(Component to Component)约束连接该区域中的顶点，而不是绘制布料属性。您可以通过将“连接方法”(Connection Method)设置为“在最大距离内”(Within Max Distance)并调整“最大距离”(Max Distance)属性来模拟刚度。如果一个布料区域需要接近角色的身体的一部分，请使用约束，而不是依赖“摩擦力”(Friction)和“拉伸阻力”(Stretch Resistance)。例如，使用“点到曲面”(Point to Surface)约束（该约束利用 nCloth 上的点和角色的身体）以及该约束的低“强度”(Strength)值。 |
| 将衣服绑定到骨架 | 为某个角色设置动画时，请在制作衣服 nCloth 之前对衣服网格和角色骨架使用“绑定蒙皮”(Bind Skin)命令。使用“输入网格吸引”(Input Mesh Attract)将布料拉向角色的结束位置，以此减少一些 nCloth 计算。 |
| 减少子步数 | 大多数情况下，减少 Nucleus 节点的“子步”(Substeps)数”和“最大碰撞迭代次数”(Max Collide Iterations)将加快播放速度，但质量却会降低。减少 nCloth 节点的“最大自碰撞迭代次数”(Max Self Collide Iterations)也可以加快播放速度。 |
| 减少输入网格吸引 | 避免“输入网格吸引”(Input Mesh Attract)值大于 1.2。 |
| 使用拉伸阻尼，而不是拉伸阻力 | 如果 nCloth 似乎拉伸过度，只要可能，就增加“拉伸阻尼”(Stretch Damp)属性，而不是增加“拉伸阻力”(Stretch Resistance)属性。 |
| 调整层的碰撞值 | 使用分层衣服时（如衬衫外面的夹克），使为外部衣服提供的“碰撞层”(Collision Layer)值高于内部衣服。这将允许您使用较低的质量设置。您还可以调整“碰撞层范围”(Collision Layer Range)值，以便外层衣服不会计算与内层衣服（例如，角色的身体）的碰撞。 |
| 缓存 | 缓存 nCloth 模拟后，在 Nucleus 节点中禁用“启用”。但是，当您希望附加到缓存或以后进行模拟时，请确保重新启用该选项。 |
