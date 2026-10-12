# 各向异性(Anisotropic)

是表示具有凹槽的曲面的材质（着色器），例如 CD、羽毛或者天鹅绒或缎子之类的织物。“各向异性”(Anisotropic)材质上的镜面反射高光的外观取决于这些凹槽的特性及其方向。“镜面反射”(Specular)着色特性（有光泽的高光）确定凹槽的方向及其特性。

“各向同性”(isotropic)材质（如“Phong”或“Blinn”）在所有方向上反射相同的镜面反射光。如果各向同性球体自旋，其镜面反射高光保持不变。

“各向异性”(anisotropic)材质在不同方向上反射的镜面反射光有所不同。如果各向异性球体自旋，其镜面反射高光会改变，具体取决于凹槽方向。

可以设定“各向异性”(Anisotropic)材质的属性来控制高光的外观，确定凹槽的方向和扩散，设定粗糙度和反射率，并减少球形变形（Fresnel 系数）。

可以在[“创建”(Create)选项卡](../../../着色窗口和编辑器/Hypershade%20窗口/“创建”%28Create%29选项卡.md)中找到此材质。

## “镜面反射着色”(Specular Shading)属性（“各向异性”(Anisotropic)）

控制曲面上的镜面反射高光的外观。

#### 角度(Angle)

确定凹槽的方向。范围为 0.0（默认值）至 360.0。用于确定非均匀镜面反射高光的 X 和 Y 方向。

![图：确定凹槽的方向。范围为 0.0（默认值）至 360.0。用于确定非均匀镜面反射高光的 X 和 Y 方向。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-34F1EB5A-8DD0-46C1-AC4D-C2F4B76D5BA1.png) <!-- baize:img-hook downloaded=false reason="正文 1592 字 ≥300，非承重" -->

#### 扩散 X/扩散 Y (Spread X/Spread Y)

确定凹槽在 X 和 Y 方向上的扩散程度。X 方向是 U 方向逆时针旋转指定角度。Y 方向与 UV 空间中的 X 方向垂直。

对于“扩散 X”(Spread X)，范围从 0.1 到 100.0，默认值为 13。对于“扩散 Y”(Spread Y)，范围从 0.1 到 100.0，默认值为 3.0

大值对应于在 X 或 Y 方向上平滑变化的曲面。小值对应于具有精细结构的曲面。增加时，X 或 Y 方向上的镜面反射高光的大小会收缩；减小时，镜面反射高光会扩散。

当“扩散 X”(Spread X)值等于“扩散 Y”(Spread Y)值时，表面将变为各向同性 — 所有方向上的平滑度相同。当“扩散 X”(Spread X)值大于“扩散 Y”(Spread Y)值时，曲面在 X 方向上平滑，在 Y 方向上粗糙。

例如，当渲染表面（例如纤维走向为 X 方向的一块布料）时，高光非均匀地扩散，并且 Y 方向上的高光较多。

#### 粗糙度(Roughness)

确定曲面的总体粗糙度。范围为 0.01 至 1.0。默认值为 0.7。较小的值对应于较平滑的曲面，并且镜面反射高光较集中。较大的值对应于较粗糙的曲面，并且镜面反射高光较分散 — 类似于漫反射。

#### Fresnel 系数(Fresnel Index)

*Fresnel* 是由许多同心圆构成的平透镜，可减少球形变形。“Fresnel 系数”(Fresnel Index)值计算将反射光波连接到传入光波的 fresnel 因子。例如，水的“Fresnel 系数”(Fresnel Index)为 1.33。值的范围从 1.0 到 20.0。

#### 镜面反射颜色(Specular Color)

请参见[常见表面材质镜面反射着色属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-D9193CD6-EF2C-4EA3-A31E-C3BDB3E17F87.htm)。

#### 反射率(Reflectivity)

请参见[常见表面材质镜面反射着色属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-D9193CD6-EF2C-4EA3-A31E-C3BDB3E17F87.htm)。

#### 反射的颜色(Reflected Color)

请参见[常见表面材质镜面反射着色属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-D9193CD6-EF2C-4EA3-A31E-C3BDB3E17F87.htm)。

#### 各向异性反射率(Anisotropic Reflectivity)

如果启用，Maya 将自动计算“反射率”(Reflectivity)作为“粗糙度”(Roughness)的一部分。“反射率”(Reflectivity)在默认情况下处于启用状态。

如果禁用该选项，Maya 将使用环境贴图的指定“反射率”(Reflectivity)值（映射在“反射的颜色”(Reflected Color)属性上），类似于“Phong”和“Blinn”材质的工作方式。

在以下示例中，启用了“各向异性反射率”(Anisotropic Reflectivity)，环境映射在“反射的颜色”(Reflected Color)上，并且“粗糙度”(Roughness)设定为 0.01、0.05、0.1 和 1.0（从非常光滑到非常粗糙）。

![图：如果启用，Maya 将自动计算“反射率”(Reflectivity)作为“粗糙度”(Roughness)的一部分。“反射…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-58FA499B-EEDE-4778-9652-A042B62A0FB4.png) <!-- baize:img-hook downloaded=false reason="正文 1592 字 ≥300，非承重" -->
