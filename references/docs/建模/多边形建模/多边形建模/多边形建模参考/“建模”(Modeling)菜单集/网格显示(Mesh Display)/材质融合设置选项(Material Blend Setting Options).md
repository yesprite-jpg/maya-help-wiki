# 材质融合设置选项(Material Blend Setting Options)

选择“网格显示 > 材质融合设置”(Mesh Display > Material Blend Setting)时，以下选项可用。

**注**

![图：在分层纹理上选择“CPV 调制”(CPV Modulate)将断开 CPV 组件与指定材质上的颜色通道的连接。因此，将忽…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 501 字 ≥300，非承重" --> [在分层纹理上选择“CPV 调制”(CPV Modulate)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-770E22B9-E32A-4E14-A4DC-23656D885AEE)将断开 CPV 组件与指定材质上的颜色通道的连接。因此，将忽略此设置以及“网格显示 > 对材质通道上色”(Mesh Display > Color Material Channel)设置。

#### 覆盖(Overwrite)

使用 CPV 值替换指定的着色材质值。

#### 相加(Add)

根据“对材质通道上色”(Color Material Channel)设置，将 CPV 值与指定的材质着色值相加。

#### 相减(Subtract)

根据“对材质通道上色”(Color Material Channel)设置，通过从指定的材质着色值减去 CPV 值来融合 CPV 值。

#### 相乘(Multiply)

通过将 CPV 值与指定的着色值相乘来融合 CPV 值。

#### 相除(Divide)

通过将指定着色值除以 CPV 值来融合 CPV 值。

#### 平均(Average)

通过首先平均 CPV 值与指定的着色值来融合 CPV 值。

#### 相乘再乘 2 (Modulate2X)

通过将 CPV 值与指定的着色值相乘，然后将乘积乘以 2 来融合 CPV 值。这用于某些游戏控制台。
