# 使用样条线 IK 曲线为关节设定姿势

操纵 IK NURBS 样条曲线的 CV

1. 选择 NURBS 曲线。

2. 启用“显示 > NURBS > CV”(Display > NURBS > CVs)。

3. 启用“显示 > NURBS > 壳线”(Display > NURBS > Hulls)。

4. 在 NURBS 曲线上选择 CV。

  **注**

  提示：

  为了更便于操纵曲线，创建曲线 CV 的簇。请参见

  创建簇变形器

  。

5. 执行下列操作之一：

  - 从“工具箱”(Tool Box)中选择“移动工具”(Move Tool)（热键：W）。

  - 从“建模”(Modeling)菜单集中，选择“曲线 > 编辑曲线工具”(Curves > Edit Curve Tool)。

6. 拖动 CV。

  该操作将移动 IK 样条线关节链。

为 IK NURBS 样条曲线上的每个 CV 创建簇变形器

1. 选择 IK 样条曲线。

2. 从主菜单栏中，选择“选择 > 簇曲线”(Select > Cluster Curve)。

  这将为每个样条线 IK 曲线 CV 创建簇变形器。

扭曲和侧滚样条线 IK 关节链

1. 选择 IK 样条线控制柄。

2. 选择“修改 > 变换工具 > 显示操纵器工具”(Modify > Transformation Tools > Show Manipulator Tool)。

  将会在样条线 IK 链的起始关节和末关节显示扭曲和侧滚圆形操纵器。

3. 执行下列操作：

  - 若要侧滚整个关节链，请在起始关节处拖动圆形操纵器。

  - 若要扭曲关节链，请在末关节处拖动圆形操纵器。

  - 此外，还可以通过选择 IK 样条线控制柄，并在“通道盒”(Channel Box)或“属性编辑器”(Attribute Editor)中输入“侧滚”(Roll)和“扭曲”(Twist)值来调整扭曲和侧滚。

沿曲线滑动关节链

1. 选择 IK 样条线控制柄。

2. 在“属性编辑器”(Attribute Editor)中，选择“ikHandle 节点”选项卡。

3. 在“IK 解算器属性”(IK Solver Attributes)区域中，启用“根在曲线上”(Root On Curve)。

  这可以将样条线 IK 控制柄的起始关节约束到曲线上的某个位置。此外，还提供了一个可以沿着曲线滑动起始关节的偏移操纵器。

4. 选择“修改 > 变换工具 > 显示操纵器工具”(Modify > Transformation Tools > Show Manipulator Tool)。

  将在起始关节处显示偏移操纵器。

  ![图：选择“修改 变换工具 显示操纵器工具”(Modify Transformation Tools Show Manipul…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-9E0F6A13-3728-4958-8745-56A859B3E175.png) <!-- baize:img-hook downloaded=false reason="正文 1316 字 ≥300，非承重" -->

5. 执行下列操作之一：

  - 拖动操纵器以沿着曲线滑动关节链。

    如果将起始关节拖动到曲线末端，则子关节将沿直线移离曲线的末端。

    ![图：拖动操纵器以沿着曲线滑动关节链。 如果将起始关节拖动到曲线末端，则子关节将沿直线移离曲线的末端。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-ED61241E-F706-4769-9D37-230B74D70F60.png) <!-- baize:img-hook downloaded=false reason="正文 1316 字 ≥300，非承重" -->

  - 在“属性编辑器”(Attribute Editor)中输入“偏移”(Offset)值，以沿着曲线移动 IK 样条线链的根。

    **注**

    - 无法将操纵器拖过曲线的末端。

    - 如果禁用“根在曲线上”(Root On Curve)，则将忽略“偏移”(Offset)属性。

平移、旋转和缩放 IK 样条曲线

1. 选择样条线 IK 曲线，然后从[工具箱](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-B345E162-0149-4E09-AC98-48DCFC227F33)中选择“移动工具”(Move Tool)（热键：W）、“旋转工具”(Rotate Tool)（热键：E）或“缩放工具”(Scale Tool)（热键：R）。

  使用显示的操纵器平移、旋转或缩放曲线。另请参见[移动对象和组件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-ABF1A141-7860-4234-889B-00278F20B9A3)、[旋转对象和组件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-169906C5-CBC4-45CD-8DFB-F716D51D6168)和[缩放对象和组件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-09D0E733-74DF-44E2-937A-C857001E45B2)。

  **注**

  如果创建样条线 IK 控制柄时，在工具选项中禁用了

  “根在曲线上”(Root on Curve)

  ，则平移、旋转和缩放曲线均不会平移起始关节。

## 相关主题

- [IK 控制柄概述](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-8AFE1FEB-C69C-4841-9787-3C196FDA9A1F.htm)

- [IK 解算器](../IK%20解算器.md)

- [样条线 IK 解算器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-B4EF8784-92D1-4D83-9CA5-A692D06607B8.htm)
