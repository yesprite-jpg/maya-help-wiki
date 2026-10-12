# Maya 材质

虽然 Maya 的 3D 曲面响应灯光的方式类似于现实世界中的灯光，但是在计算机图形软件中曲面和灯光交互的方式有重大的不同。通过材质节点（应用于对象时）可以定义对象曲面在渲染时的显示方式。

请参见[曲面着色](../../../着色.md)。

在 Maya 中，材质节点定义曲面如何对灯光作出反应。Maya 中包含多种类型的材质节点，可帮助您模拟光照曲面的真实质量或行为：[曲面材质节点](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-634CAFBE-AC48-4B73-89CA-82D64FA1BC70.htm)、[体积材质节点](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-6FF09EBA-CD7C-45B7-8B49-305D748EE7B4.htm)和[置换材质节点](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-204712F3-344B-4A41-9399-51B2BD19A3F7.htm)。

您可以设定材质的属性，如场景元素的颜色、镜面反射度、反射率、透明度和曲面细节，从而创建各种各样的真实图像。

**注**

当第一次创建对象时，默认情况下 Maya 将指定“Lambert”材质（一种表面材质）的特殊版本。

## 表面材质

表面材质表示您可以在其上进行纹理贴图的曲面类型。在 Maya 中，属性（如反光度、蒙版、反射率、光泽度等）根据材质类型的不同而不同。例如，如果纹理需要有反光曲面（如铬合金），请使用 [Phong](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-3EDEB1B3-4E48-485A-9714-9998F6E4944D.htm) 材质。

对于表面材质属性的详细描述，请参见[表面材质节点](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-634CAFBE-AC48-4B73-89CA-82D64FA1BC70.htm)。

## 置换材质

置换材质允许您使用图像来指定场景中对象上的曲面释压。若要查找有关曲面释压的详细信息，请参见[关于表面起伏](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-F403A3FF-55BE-43A0-B6E1-49BA7C6BF5EE.htm)。

## 体积材质（大气）

在现实世界中，当您拍摄某个对象的照片时，该对象通常位于大气（空气）中，并由其他对象（背景）包围。

体积材质描述占用空间体积（如雾、烟、灰尘或其他精细粒子）的现象的物理外观。可以光线跟踪体积材质，并生成效果，如透过镜面反射和折射显示灯光雾。

有关体积材质的描述，请参见[关于体积材质](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-6FF09EBA-CD7C-45B7-8B49-305D748EE7B4.htm)。

若要使用体积材质，请参见[模拟雾、烟或灰尘](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-176C4583-9104-4DD3-AE91-76799AE14D23.htm)。
