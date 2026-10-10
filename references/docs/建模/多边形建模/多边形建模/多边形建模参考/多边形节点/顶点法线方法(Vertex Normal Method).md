# 顶点法线方法(Vertex Normal Method)

用于为多边形设置默认的顶点法线方法。从下列方法中选择：

**注**

提示：

您可以使用

“建模”(Modeling)

首选项中的

“默认顶点法线方法”(Default Vertex Normal Method)

首选项，设置权重顶点法线的默认方法。

#### 未加权(Unweighted)

从每个连接的面获取法线，并将其加到一起。如果需要匹配来自较旧 Maya 版本的文件，请选择此方法。（“未加权”(Unweighted)是 Maya 2012 及更早版本中的默认方法）。

#### 加权角度(Angle Weighted)

计算多边形角点的角度，并将其用作权重。

#### 加权区域(Area Weighted)

使用每个相邻面的曲面面积作为权重。因此，小多边形对结果的影响很小，大多边形对结果的影响很大。

#### 加权角度和区域(Angle and Area Weighted)

（默认）将“加权角度”(Angle Weighted)和“加权区域”(Area Weighted)求值方法组合在一起。

## 相关主题

- [建模首选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-F40D8133-73D3-4A1B-8332-4C8E46FFA1E6)
