# 使用“采样器信息”(Sampler Info)工具

有关“采样器信息”(Sampler Info)工具的描述，请参见[采样器信息(Sampler Info)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-5134339F-6F76-4193-9F94-713D0A88AAC2.htm)。

使用“采样器信息”(Sampler Info)工具

1. 一旦您创建了材质和纹理并将其指定给某个对象，即可创建“采样器信息”(Sampler Info)工具节点。

2. 选择 SamplerInfo 节点，然后单击 3 以在完全模式下显示该节点。

  有关节点的视图模式的详细信息，请参见[在节点编辑器和 Hypershade 中更改视图模式](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8BB2DBCA-FB8B-4F7A-A4C3-1BACE18E5879)。

3. 将任一 SamplerInfo 节点输出属性连接到任一纹理输入属性。试验不同的连接，然后在材质查看器中预览结果。

  在第一个示例中，将“SamplerInfo”的[正面比](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-5134339F-6F76-4193-9F94-713D0A88AAC2.htm#WS73099CC142F48755-3D114B7511812357EFE-59B9)属性连接到“大理石”(Marble)纹理的“脉络宽度”(Vein Width)。

  ![图：将任一 SamplerInfo 节点输出属性连接到任一纹理输入属性。试验不同的连接，然后在材质查看器中预览结果。 在第一…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-87779135-EE26-41AC-8C47-A115062296E0.png) <!-- baize:img-hook downloaded=false reason="正文 384 字 ≥300，非承重" -->

  在下面的示例中，将“SamplerInfo”的[点对象](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-5134339F-6F76-4193-9F94-713D0A88AAC2.htm#WS73099CC142F48755-3D114B7511812357EFE-59D0)属性连接到“大理石”(Marble)纹理的“涟漪”(Ripples)属性。

  ![图：将任一 SamplerInfo 节点输出属性连接到任一纹理输入属性。试验不同的连接，然后在材质查看器中预览结果。 在第一…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-8F1685FA-85A6-4555-85FB-DFF80433EE3C.png) <!-- baize:img-hook downloaded=false reason="正文 384 字 ≥300，非承重" -->
