# 褶皱工具(Wrinkle Tool)

- 在“建模”(Modelling)和“装备”(Rigging)菜单集中：“变形 > [褶皱](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-7E95427A-95D5-43E3-9B41-F9ADEC420BCC.htm)”(Deform > Wrinkle) > ![图：在“建模”(Modelling)和“装备”(Rigging)菜单集中：“变形 褶皱”(Deform Wrinkle)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1179 字 ≥300，非承重" -->

- 在“动画”(Animation)菜单集中：“动画变形 > 打开完整的变形菜单 > [褶皱](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-7E95427A-95D5-43E3-9B41-F9ADEC420BCC.htm)”(Anim Deform > Open Full Deform Menu > Wrinkle) > ![图：在“动画”(Animation)菜单集中：“动画变形 打开完整的变形菜单 褶皱”(Anim Deform Open Fu…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1179 字 ≥300，非承重" -->

若要创建褶皱变形器，请使用“褶皱工具”(Wrinkle Tool)。创建的褶皱变形器的特性取决于“褶皱工具”(Wrinkle Tool)的工具设置。

请参见[褶皱变形器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-B69D16EE-AF34-42DF-9C44-743FA64D51D6.htm)和[设置褶皱变形器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-69458E85-3291-428F-9732-55AB01E52AEE.htm)。

## 褶皱设置(Wrinkle Settings)

#### 类型(Type)

指定褶皱变形器的类型。选择“切向”(Tangential)、“径向”(Radial)或“自定义”(Custom)。默认设置为“径向”(Radial)。

#### 切向(Tangential)

组合将影响大致平行的线。切向褶皱变形器只能变形单个 NURBS 曲面。

#### 径向(Radial)

组合将影响从单个点分支的线，类似于车轮上的辐条。径向褶皱变形器只能变形单个 NURBS 曲面。

#### 自定义(Custom)

组合将影响您以最适合想要生成的效果的方式创建的线。自定义褶皱变形器可以变形任何可变形对象（NURBS 曲面、多边形曲面、晶格等）。

#### 数量(Amount)

指定褶皱变形器中父影响线的数量。影响线的总数中还可以包含由“径向分支数量”(Radial Branch Amt)和“径向分支深度”(Radial Branch Depth)指定的子影响线。使用相应滑块选择介于 0 到 20 之间的值。默认值为 3。

#### 厚度(Thickness)

指定曲面衰减。曲面衰减是受每条影响线影响的区域。使用相应滑块选择介于 0.0000 到 2.0000 之间的值。默认值为 1.0000。

#### 随机度(Randomness)

指定褶皱变形器与指定“数量”(Amount)、“强度”(Intensity)、“径向分支数量”(Radial Branch Amt)和“径向分支深度”(Radial Branch Depth)的一致程度。使用相应滑块选择介于 0.0000 到 1.0000 之间的值。默认值为 0.2000。

#### 强度(Intensity)

指定由影响线创建的折痕锐度。最小强度 (0) 指定平滑折痕。最大强度 (1) 指定尖锐、陡峭的折痕。使用相应滑块选择介于 0.0000 到 1.0000 之间的值。默认值为 0.5000。

#### 径向分支数量(Radial Branch Amt)

指定从每个父影响线分支的子影响线的数量。仅适用于径向褶皱变形器。使用相应滑块选择介于 0 到 10 之间的值。默认值为 2。

#### 径向分支深度(Radial Branch Depth)

指定影响线层次的深度，该深度是从每个父影响线分支的子影响线的级别数。增大“径向分支深度”(Radial Branch Depth)将使影响线的总数按指数级增加。仅适用于径向褶皱变形器。使用相应滑块选择介于 0 到 4 之间的值。默认值为 0。
