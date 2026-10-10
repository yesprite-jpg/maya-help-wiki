# 使用 MEL 创建属性控件

若要使用 MEL 创建属性控件，请完成以下步骤：

- 创建属性控件

- 设置 MEL 程序的源

- 定义 MEL 程序的回调

## **创建属性控件**

在下面的示例中，floatSlider 控件是使用 MEL 程序 AEFloatSlider 创建的，然后使用更改命令 AEaddFloatSliderCB。

```text
global proc AEaddFloatSliderCB( string $plug, string $slider )
{
	float $val = `floatSlider -q -v $slider`;
	setAttr $plug $val;
}
```

```text
global proc AEaddFloatSlider ( string $plug,
string $label, string $annot )
```

```text
{

	// Body of callback
	rowLayout -nc 2;
	float $val = `getAttr $plug`;
	string $slider;
	text -label $label;
	$slider = `floatSlider -annotation $annot -v $val`;
	floatSlider -e -cc ("AEaddFloatSliderCB \"" + $plug + "\" \"" + $slider + "\"")
 	$slider;
	 setParent

}
```

MEL 程序使用以下参数：

- $plug 是栓，即该控件使用的节点和属性。

- $label 是属性的标签。

- $annot 是属性的注释。

## 设置 MEL 程序的源

此步骤为 Maya 提供了包含 MEL 程序的 MEL 文件的路径。如果将文件保存到名为 C:/myScripts 的目录中，请将以下内容键入到 MEL 命令行或“脚本编辑器”(Script Editor)中：

source "C:/myScripts/AEFloatSlider.mel";

**注**

提示：

也可以为 MEL 文件指定与回调所用程序相同的名称。这样即可在首次启动回调时将文件作为源。例如，如果回调定义为

global proc AEaddFloatSlider()

，则将回调文件在

Maya

的其中一个脚本目录中保存为

AEaddFloatSlider.mel

。

## 定义 MEL 程序的回调

在创建模板文件时，将 <description language="cb"> 标记添加到属性声明或视图定义中，并指定 MEL 程序的回调。若要将上述步骤中定义的自定义滑块控件添加到“白炽度红色”(Incandescence Red)属性，请使用以下命令：

```text
<attribute name='incandescenceR' type='maya.float'>
    <label>Incandescence Red</label>
      <description language="cb">AEaddFloatSlider</description>
</attribute>
```

当您在“属性编辑器”(Attribute Editor)中访问属性视图时，“白炽度红色”(Incandescence Red)属性会使用自定义的滑块。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-D165F03B-68BA-403B-BB13-7360A67BC2CB.png) <!-- baize:img-hook downloaded=false reason="正文 1235 字 ≥300，非承重" -->

## 相关主题

- [自定义属性编辑器模板](../../../自定义“属性编辑器”%28Attribute%20Editor%29.md)

- [属性编辑器(Attribute Editor)](../../../../属性编辑器%28Attribute%20Editor%29.md)
