# 使用“三元值切换”(Triple Switch)工具

有关“三元值切换”(Triple Switch)工具的描述，请参见[三元值切换](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-734708F6-0A57-4CF1-ACAB-664AD4A6FB62.htm)。

允许您将不同纹理映射到场景中的多个对象。可以切换任意三重浮点属性，例如 RGB 输出颜色。

在下面的示例中，因为需要粒状纹理，所以最初将“岩石”(Rock)纹理映射到对象（类似于碗的简单旋转曲面）。其他映射到选定对象的纹理会在显示特定纹理属性的同时保留该粒状纹理。

使用“三元值切换”(Triple Switch)工具

1. 创建材质并将其指定给场景中的所有对象。

2. 在材质的“属性编辑器”(Attribute Editor)中，将纹理映射到“颜色”(Color)属性。

  ![图：在材质的“属性编辑器”(Attribute Editor)中，将纹理映射到“颜色”(Color)属性。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-D132EF32-AE8A-462C-B74F-C6DE0B7163BD.png) <!-- baize:img-hook downloaded=false reason="正文 815 字 ≥300，非承重" -->

3. 在纹理的“属性编辑器”(Attribute Editor)中，将光标置于其中一个“颜色”(Color)属性上，然后在弹出菜单的“创建新纹理”(Create New Texture)上单击鼠标右键。

  ![图：在纹理的“属性编辑器”(Attribute Editor)中，将光标置于其中一个“颜色”(Color)属性上，然后在弹出…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-A04AEA6C-E167-4C93-B7E8-0BE962B127B5.png) <!-- baize:img-hook downloaded=false reason="正文 815 字 ≥300，非承重" -->

4. 在“创建渲染节点”(Create Render Node)窗口中，从“工具”(Utilities)类别中选择“三元值切换”(Triple Switch)。请注意，碗将丢失其初始颜色。使用“切换属性”(Switch Attributes)编辑器中的“默认”(Default)属性，可以将另一个纹理映射到对象，也可以更改颜色。

  ![图：在“创建渲染节点”(Create Render Node)窗口中，从“工具”(Utilities)类别中选择“三元值切换…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-CAF5EF7A-DE6C-4897-A21C-B6CF266A1C15.png) <!-- baize:img-hook downloaded=false reason="正文 815 字 ≥300，非承重" -->

5. 打开“大纲视图”(Outliner)，然后按住鼠标中键的同时将要显示另一个纹理的对象拖动到 [inShape](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-734708F6-0A57-4CF1-ACAB-664AD4A6FB62.htm#WS73099CC142F48755-3D114B7511812357EFE-587A) 列。

  ![图：打开“大纲视图”(Outliner)，然后按住鼠标中键的同时将要显示另一个纹理的对象拖动到 inShape 列。 只对以…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-EAA14BDE-36F0-4154-AD00-A3848201E9AD.png) <!-- baize:img-hook downloaded=false reason="正文 815 字 ≥300，非承重" -->

  只对以下碗中的四个碗映射纹理。顶部的碗将保留“默认”(Default)颜色设置。

  ![图：打开“大纲视图”(Outliner)，然后按住鼠标中键的同时将要显示另一个纹理的对象拖动到 inShape 列。 只对以…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-A9C9CFA1-B773-4117-8846-3A1461CB815C.png) <!-- baize:img-hook downloaded=false reason="正文 815 字 ≥300，非承重" -->

6. 若要将纹理映射到其他对象，请在“inShape”列中单击亮显旋转曲面，然后选择[映射项目(Map Item)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-734708F6-0A57-4CF1-ACAB-664AD4A6FB62.htm#WS73099CC142F48755-3D114B7511812357EFE-5870)按钮。

  ![图：若要将纹理映射到其他对象，请在“inShape”列中单击亮显旋转曲面，然后选择映射项目(Map Item)按钮。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-371D9510-E244-4F35-88E9-EF92BB503B74.png) <!-- baize:img-hook downloaded=false reason="正文 815 字 ≥300，非承重" -->

7. 从“创建渲染节点”(Create Render Node)窗口为每个对象选择其他纹理。

  以下显示了四个碗，并在“切换属性”(Switch Attributes)编辑器中显示了映射到碗上的纹理。

  ![图：从“创建渲染节点”(Create Render Node)窗口为每个对象选择其他纹理。 以下显示了四个碗，并在“切换属性…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-9C5577EE-745D-42FE-A051-271042793C9A.png) <!-- baize:img-hook downloaded=false reason="正文 815 字 ≥300，非承重" -->

  如有必要，可调整每个项目的纹理。以下内容可帮助您更好地了解如何将纹理映射到碗以及如何在“Hypershade”中显示连接。

  ![图：从“创建渲染节点”(Create Render Node)窗口为每个对象选择其他纹理。 以下显示了四个碗，并在“切换属性…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-BF6F5D69-D2AE-4053-A41E-66806A55DF5A.png) <!-- baize:img-hook downloaded=false reason="正文 815 字 ≥300，非承重" -->
