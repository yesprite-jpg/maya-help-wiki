# HumanIK“拉动”(Pull)和“阻力”(Resist)属性

打开“拉动”(Pull)和“阻力”(Resist)属性

- 选择角色骨架后，从“属性编辑器”(Attribute Editor)中，选择“HIKproperties”选项卡

“拉动”(Pull)属性用于确定在移动身体的其他部位时某些身体部位受影响的程度。

#### 髋部强制重力(Hips Enforce Gravity)

用于设置髋部的阻力百分比。强制角色髋部在其脚之间。默认情况下，“髋部强制重力”(Hips Enforce Gravity)设置为 60%。

**注**

必须将“髋部刚度”(Hips Stiffness)设置为非零值，才能利用“强制重力”(Enforce Gravity)设置。请参见

HIK 刚度属性

。

#### 左/右膝最大伸展(Left/Right Knee Max Extension)

可使用这些设置在腿完全伸展时限制腿，以防止出现膝部和肢体折断。值越大，肢体伸展得越平缓。默认情况下，值为 50 时会更正大多数肢体折断。

#### 左/右肘最大伸展(Left/Right Elbow Max Extension)

使用此设置可在左臂或右臂完全伸展时对其进行阻尼，以防止肘部和肢体折断。值越大，肢体伸展得越平缓。默认情况下，值为 50 时会更正大多数肢体折断。

#### 左/右膝压缩(Left/Right Knee Compression)

在伸展的腿弯曲时更改其刚度。为 100%（完整效果）时，伸展的腿不弯曲，而是推动角色的髋部，从而移动角色。

#### 左/右肘压缩(Left/Right Elbow Compression)

在伸展的手臂弯曲时更改其刚度。为 100%（完整效果）时，伸展的手臂不弯曲，而是推动角色的胸部，从而移动角色。
