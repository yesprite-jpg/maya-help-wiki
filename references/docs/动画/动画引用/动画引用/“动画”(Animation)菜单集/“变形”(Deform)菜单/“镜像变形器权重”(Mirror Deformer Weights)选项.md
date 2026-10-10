# “镜像变形器权重”(Mirror Deformer Weights)选项

- 在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 > (创建)镜像变形器权重”(Deform > (Create) Mirror Deformer Weights) > ![图：在“动画”(Animation)、“建模”(Modeling)和“绑定”(Rigging)菜单集中：“变形 (创建)镜像…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 733 字 ≥300，非承重" -->

打开“镜像变形器权重选项”(Mirror Deformer Weights Options)窗口，您可以在其中设置融合变形、簇、抖动和线变形器的权重镜像选项。请参见[镜像变形器权重](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8AAD9BE7-E331-4539-A40C-901F8CAC1A5C)。

### 镜像平面(Mirror across)

选择您希望镜像权重所穿过的平面。

#### XY

指定围绕全局 XY 平面（默认值）镜像权重。

#### YZ

指定围绕全局 YZ 平面镜像权重。

#### XZ

指定围绕全局 XZ 平面镜像权重。

#### 方向(Direction)

指定沿指定“镜像平面”(Mirror across)的镜像方向。该选项是否更新将取决于您选择的“镜像平面”(Mirror across)轴，例如：“正值到负值（+Z 到 -Z）”。

如果启用该选项，则将从正侧到负侧镜像权重。

#### 创建新变形器(Create New Deformer)

如果启用该选项，则创建新变形器。如果禁用该选项，则不会创建新变形器。

### 曲面关联(Surface Association)

确定如何将对象相反方向的两半部分曲面组件互相关联。从下列选项中选择：

#### 曲面上最近的点(Closest point on surface)

查找源曲面与目标曲面之间距离最近的点并在这些点处对权重平滑插值。这是默认设置。

#### 光线投射(Ray cast)

使用光线投射算法确定两个曲面网格之间的采样点。

#### 最近组件(Closest component)

查找每个采样点处最近的顶点组件（多边形）或控制顶点 (NURBS)，并使用其无插值的蒙皮权重值。

## 相关主题

- [绘制融合形变变形器权重](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-950716A4-19CF-4C14-96F1-FD6B4D48663C)

- [绘制簇变形器权重](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-43CE8C47-47E0-4AC5-9770-CE73EDA79E5F)

- [绘制抖动变形器权重](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-7496A4C7-4B78-4098-874A-F458E64A9D3F)

- [绘制线变形器权重](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DF0CCC32-C8BC-4C46-A0E3-4E349E738982)
