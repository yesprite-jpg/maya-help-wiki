# Maya 矢量渲染器

可以使用 Maya 向量渲染器创建各种位图图像格式（如 IFF、TIFF 等）或 2D 向量格式的固定格式渲染（如卡通、艺术色调、艺术线条、隐藏线、线框）。

支持以下 2D 向量格式：

- Adobe® Flash®（非交互式）版本 3、4 或 5 (SWF)

- Adobe® Illustrator® 版本 8 (AI)

- 封装的 PostScript Level 2 (EPS)

- 可扩展向量图形 (SVG)。

若要选择 Maya 矢量渲染器，请参见[选择渲染器](../选择渲染器.md)。

若要设定 Maya 矢量渲染器的选项，请参见[“渲染设置”窗口](../../渲染参考/渲染参考/渲染窗口和编辑器/“渲染设置”%28Render%20Settings%29窗口.md)。

| 示例动画 |  |
|---|---|
|  |  |
|  |  |

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-F11D7945-AFF2-46ED-8EDB-77F792495E47.png) <!-- baize:img-hook downloaded=false reason="正文 1192 字 ≥300，非承重" -->

注释：

- Maya 矢量渲染器无法渲染某些 Maya 功能（请参见[无法矢量渲染的 Maya 功能](Maya%20矢量渲染器.md#WS17956D7ADBC6E73624B3985117AE33A2FE-7FF7)）。

- 如果要渲染用于联机传送的 SWF 或 SVG 文件，请确保已阅读[减小矢量渲染文件大小的策略](../../质量、渲染速度、诊断/质量、渲染速度、诊断/提高整体渲染速度/减小矢量渲染文件大小的策略.md)。否则，可能会导致创建的文件太大而无法进行联机传送。

- 由于技术（矢量渲染器所基于的技术）中的某些限制，提高渲染设置中的分辨率未必会产生更好的效果。

## 无法矢量渲染的 Maya 功能

Maya 矢量渲染器无法渲染以下 Maya 功能。

| Maya 功能 | 注释 |
|---|---|
| 凹凸贴图 |  |
| 置换贴图 | 使用修改 > 转化 > 置换到多边形(Modify > Convert > Displacement to Polygons)可以将置换贴图转化为多边形进行渲染。 |
| Maya® Fluid Effects™ | 使用修改 > 转化 > 流体到多边形(Modify > Convert > Fluid to Polygons)可以将流体效果转化为多边形进行渲染。 |
| 图像平面 |  |
| 灯光 | 渲染过程中只使用点光源。渲染过程中只考虑以下灯光属性：灯光位置、灯光颜色、灯光强度（对于点光源）、“发射镜面反射”(Emit Specular)、“使用深度贴图阴影”(Use Depth Map Shadows)和“使用光线跟踪阴影”(Use Ray Trace Shadows)。 |
| Maya® Fur™ |  |
| 多个 UV |  |
| Maya® Paint Effects™ | 使用“修改 > 转化 > Paint Effects 到多边形”(Modify > Convert > Paint Effects to Polygons)可以将 Paint Effects 转化为多边形进行渲染。 某些“Paint Effects”可能不会按照预期进行渲染。许多“Paint Effects”笔刷在单个多边形上使用透明纹理来实现某种效果（例如，叶的轮廓）。但是，Maya 矢量渲染器仅支持每对象透明度。 |
| 粒子 |  |
| 后期渲染效果 | 后期渲染效果包括运动模糊、雾和辉光等。 |
| 着色器 | 各向异性、Lambert、Blinn、Phong 和 Phong E 着色器应该会生成预期结果。其他 Maya 着色器可能会生成意外结果。不会渲染指定给单个 NURBS 或细分曲面的多个着色器。 |
| 纹理 | 纹理渲染受填充样式和多边形数量的限制。填充单个多边形的填充样式（“全色”和“网格渐变”）渲染纹理的精确度要高于其他填充样式，且包含多个多边形的模型渲染纹理的精确度要高于包含较少多边形的模型。 |
| 帧数 | “帧数”(By Frame)在向量渲染的文件名 |
