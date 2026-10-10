# 纹理模糊或“超出 GPU 纹理 RAM，纹理加载失败”错误消息疑难解答

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 709 字 ≥300，非承重" -->

如果场景中包含的高分辨率纹理超出您的显卡内存的处理能力，则纹理可能看起来模糊或根本不加载。这两个问题都与“最大纹理分辨率”(Max Texture Resolution)有关，可以采用不同的方式解决。

如果纹理看起来模糊...

1. 通过删除场景中一些包含大量纹理的对象或卸载具有大量纹理的引用，释放 GPU RAM。

2. 从[面板菜单](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-BD5D066A-4876-4B56-8A9F-96E2243E22A3)中，选择“渲染器 >“Viewport 2.0”> ![图：从面板菜单中，选择“渲染器 “Viewport 2.0” 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 709 字 ≥300，非承重" -->。

3. 在“最大纹理分辨率钳制”(Maximum Texture Resolution Clamping)下，单击“重新加载所有纹理”(Reload All Textures)。

  在带纹理的模式的场景视图中按 6。

**注**

提示：

如果纹理看起来仍然模糊，则需要释放更多 GPU RAM。

如果纹理根本不显示，并且出现一条错误消息，指明已超出纹理 RAM 限制...

1. 从[面板菜单](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-BD5D066A-4876-4B56-8A9F-96E2243E22A3)中，选择“渲染器 >“Viewport 2.0”> ![图：从面板菜单中，选择“渲染器 “Viewport 2.0” 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 709 字 ≥300，非承重" -->。

2. 在“最大纹理分辨率钳制”(Maximum Texture Resolution Clamping)下，将“最大纹理分辨率”(Max Texture Resolution)设置为“自动”(Automatic)。

3. 单击“重新加载所有纹理”(Re-load All Textures)。

  在带纹理的模式的场景视图中按 6。

**注**

您还可以将

“最大纹理分辨率”(Max Texture Resolution)

设置为

“自定义”(Custom)

，然后通过下面的滑块手动设置自己的分辨率。如果再次出现“超出 GPU 纹理 RAM”消息，请再次降低

“最大纹理分辨率”(Max Texture Resolution)

值。

**注**

“最大纹理分辨率钳制”(Maximum Texture Resolution Clamping)

设置将与场景一起保存。
