# Hypershade 浏览器

Hypershade 浏览器中的选项卡包含构成当前场景的渲染组件；例如材质、纹理、灯光和摄影机。

在每个 Hypershade 选项卡中，将每个渲染节点显示为节点图标（样例），可以视觉化表示节点的特征。编辑节点的属性或者指定纹理或特殊效果时，Hypershade 中的样例将更新。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-770E0860-3F7E-4B77-8A8E-183B06D2933D.png) <!-- baize:img-hook downloaded=false reason="正文 946 字 ≥300，非承重" -->

## 暂停材质和纹理的样例生成

如果在场景中具有许多材质和纹理，则可以启用 (![图：如果在场景中具有许多材质和纹理，则可以启用 () 和禁用 () 以下区域中的样例生成，以提高工作流的效率：这有助于避免等…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-E877B724-DC07-4153-8B4B-E4B3661E9311.png) <!-- baize:img-hook downloaded=false reason="正文 946 字 ≥300，非承重" -->) 和禁用 (![图：如果在场景中具有许多材质和纹理，则可以启用 () 和禁用 () 以下区域中的样例生成，以提高工作流的效率：这有助于避免等…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-A194F9D7-F3E4-4E37-8FA8-21F1DA8E0329.png) <!-- baize:img-hook downloaded=false reason="正文 946 字 ≥300，非承重" -->) 以下区域中的样例生成，以提高工作流的效率：这有助于避免等待样例进行渲染：

- Hypershade 浏览器中的“材质”(Materials)和“纹理”(Textures)选项卡

- 属性编辑器(Attribute Editor)

- Hypershade 工作区的着色器图表中的节点

材质查看器不受此设置的影响。

样例生成处于禁用状态时，通过单击鼠标右键并从标记菜单中选择“刷新样例”(Refresh Swatch)，可以对着色器图表中的特定节点启用样例渲染。

请参见[暂停材质和纹理的样例生成](../../../关于着色和纹理曲面/使用%20Hypershade%20的外观开发/暂停材质和纹理的样例生成以提高%20Hypershade%20性能.md)。

## 在 Hypershade 浏览器中自定义样例

可以自定义在浏览器中显示样例的方式，例如，样例的大小或顺序。请参见[自定义 Hypershade 浏览器](../../../关于着色和纹理曲面/使用%20Hypershade%20的外观开发/使用%20Hypershade%20构建和创建材质/自定义%20Hypershade%20浏览器.md)。

## 创建其他“Hypershade”选项卡

可以将其他选项卡添加到 Hypershade 浏览器以对场景中的渲染节点排序。详细信息请参见[自定义 Hypershade 浏览器](../../../关于着色和纹理曲面/使用%20Hypershade%20的外观开发/使用%20Hypershade%20构建和创建材质/自定义%20Hypershade%20浏览器.md)。

## 在浏览器中过滤节点

若要按类型过滤节点，请单击浏览器工具栏中的“显示 > 对象”(Show > Objects)，然后从可用过滤器中进行选择。

若要按名称过滤节点，请在文本框中输入过滤文本。使用 * 作为通配符。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-9A051413-006F-4B43-BB07-824CAD7FE61D.png) <!-- baize:img-hook downloaded=false reason="正文 946 字 ≥300，非承重" -->

若要清除过滤器，请单击 ![图：若要清除过滤器，请单击 。如果未应用过滤器，则图标显示为灰色的 。请参见 Hypershade 浏览器工具栏。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-ED225F9E-1068-4129-99CC-752101D51424.png) <!-- baize:img-hook downloaded=false reason="正文 946 字 ≥300，非承重" -->。如果未应用过滤器，则图标显示为灰色的 ![图：若要清除过滤器，请单击 。如果未应用过滤器，则图标显示为灰色的 。请参见 Hypershade 浏览器工具栏。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-2A5F9D3C-55F9-4E71-AE99-038E39C54688.png) <!-- baize:img-hook downloaded=false reason="正文 946 字 ≥300，非承重" -->。请参见 [Hypershade 浏览器工具栏](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-5B48E281-2DCB-4C65-9DCA-52CBA26A7BBA.htm)。

## 项目(Projects)选项卡

“项目”(Projects)选项卡显示默认项目目录的内容。

如果将项目保存在他处，请创建新的磁盘选项卡，指向保存项目的目录。请参见[自定义 Hypershade 浏览器](../../../关于着色和纹理曲面/使用%20Hypershade%20的外观开发/使用%20Hypershade%20构建和创建材质/自定义%20Hypershade%20浏览器.md)。

例如：

- Windows

  drive:\Documents and Settings\username\My Documents\maya\projects

- Mac OS X

  /Users/username/Documents/maya/projects

- Linux

  ~username/maya/projects
