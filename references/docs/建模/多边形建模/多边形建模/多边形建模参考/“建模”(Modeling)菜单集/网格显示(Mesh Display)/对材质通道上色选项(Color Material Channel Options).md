# 对材质通道上色选项(Color Material Channel Options)

选择“网格显示 > 对材质通道上色”(Mesh Display > Color Material Channel)时，以下选项可用。

**注**

![图：在分层纹理上选择“CPV 调制”(CPV Modulate)将断开 CPV 组件与指定材质上的颜色通道的连接。因此，将忽…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 407 字 ≥300，非承重" --> [在分层纹理上选择“CPV 调制”(CPV Modulate)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-770E22B9-E32A-4E14-A4DC-23656D885AEE)将断开 CPV 组件与指定材质上的颜色通道的连接。因此，将忽略此设置以及“网格显示 > 材质融合设置”(Mesh Display > Material Blend Setting)。

#### 无(None)

不会使用指定给对象的着色器的任何材质属性。在这种情况下，照明也会被禁用。

#### 环境光(Ambient)

指定着色器的环境光材质通道被顶点颜色覆盖。

#### 环境光 + 漫反射(Ambient+Diffuse)

指定着色器的环境光和漫反射材质通道被顶点颜色覆盖。

#### 漫反射(Diffuse)

指定着色器的漫反射材质通道被顶点颜色覆盖。这是默认设置。

#### 镜面反射(Specular)

顶点颜色会覆盖指定的着色器的镜面反射材质通道。

#### 自发光(Emission)

指定着色器的自发光材质通道被顶点颜色覆盖。
