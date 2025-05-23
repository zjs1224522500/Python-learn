import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.lines import Line2D


# 固定参数设定
k_s = (
    1.3  # EC小查询延迟系数（L_e^s = 1.5 * L_r^s）
)
k_l = (
    1.5  # EC大查询延迟系数（L_e^l = 10 * L_r^s）
)


# 定义公式
def calculate_R(alpha, p, k_s, k_l):
    delay_term = 1 + (k_s - 1) / (
        1 + (1 - p) * k_l
    )
    storage_term = (1 + alpha) / (1 + 2 * alpha)
    return delay_term * storage_term


# 生成网格数据
alpha = np.linspace(
    0, 1, 100
)  # Key SST 占比 α ∈ [0,1]
p = np.linspace(0, 1, 100)  # 小查询比例 p ∈ [0,1]
Alpha, P = np.meshgrid(alpha, p)
R = calculate_R(Alpha, P, k_s, k_l)

# 创建三维坐标系
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

# 绘制曲面
surface = ax.plot_surface(
    Alpha,
    P,
    R,
    cmap="viridis",
    edgecolor="none",
    alpha=0.8,
)

# 标注临界面 R=1
contour_ = ax.contour(
    Alpha,
    P,
    R,
    levels=[1],
    colors="red",
    linewidths=3,
    alpha=1,
)

# 为等高线添加标签
ax.clabel(
    contour_,
    inline=False,  # 标签不放在等高线上，避免重叠
    fontsize=10,  # 标签字体大小
    fmt="R=1",  # 标签格式
    colors="red",  # 标签颜色
)


# 添加辅助线：p=0.5 和 alpha=0.1
# 绘制 p=0.5 的辅助线
alpha_line_p = np.linspace(0, 1, 100)
p_line_p = 0.5 * np.ones_like(alpha_line_p)
R_line_p = calculate_R(
    alpha_line_p, p_line_p, k_s, k_l
)
ax.plot(
    alpha_line_p,
    p_line_p,
    R_line_p,
    color="blue",
    linestyle="--",
    linewidth=2,
    label="p=0.5",
)

# alpha_line_p2 = np.linspace(0, 1, 100)
# p_line_p2 = 0.999 * np.ones_like(alpha_line_p)
# R_line_p2 = calculate_R(
#     alpha_line_p, p_line_p, k_s, k_l
# )
# ax.plot(
#     alpha_line_p2,
#     p_line_p2,
#     R_line_p2,
#     color="orange",
#     linestyle="-",
#     linewidth=2,
#     label="p=0.999",
# )

# 绘制 alpha=0.05 的辅助线
p_line_alpha = np.linspace(0, 1, 100)
alpha_line_alpha = 0.05 * np.ones_like(
    p_line_alpha
)
R_line_alpha = calculate_R(
    alpha_line_alpha, p_line_alpha, k_s, k_l
)
ax.plot(
    alpha_line_alpha,
    p_line_alpha,
    R_line_alpha,
    color="green",
    linestyle="--",
    linewidth=2,
    label="α=0.05",
)

# 绘制 alpha=0.1 的辅助线
p_line_alpha = np.linspace(0, 1, 100)
alpha_line_alpha = 0.1 * np.ones_like(
    p_line_alpha
)
R_line_alpha = calculate_R(
    alpha_line_alpha, p_line_alpha, k_s, k_l
)
ax.plot(
    alpha_line_alpha,
    p_line_alpha,
    R_line_alpha,
    color="black",
    linestyle="-.",
    linewidth=2,
    label="α=0.1",
)


def plot_dot(
    ax,
    x,
    y,
    color_,
    label_,
    marker_,
    db_name_,
    y_diff=-0.05,
):
    R_point = calculate_R(x, y, k_s, k_l)
    # print(R_point)
    ax.scatter(
        x,
        y,
        R_point,
        color=color_,
        marker=marker_,
        s=100,
        label=label_,
    )
    # 添加R值文本标注（带背景框）
    ax.text(
        x + 0.03,  # X方向偏移（避免文字重叠）
        y + y_diff,  # Y方向偏移
        R_point + 0.05,  # Z方向偏移（抬高文字）
        f"R = {R_point:.2f}, {db_name_}",  # 格式化保留两位小数
        color="white",  # 文字颜色
        fontsize=10,
        bbox=dict(  # 背景框参数
            facecolor="black",
            alpha=0.7,
            edgecolor="none",
            boxstyle="round",
        ),
        zorder=10,  # 确保文字在顶层
    )


plot_dot(
    ax,
    0.05,
    0.5,
    "black",
    "(α=0.05, p=0.5)",
    "o",
    "TerarkDB",
    0.1,
)


plot_dot(
    ax,
    0.001,
    0,
    "blue",
    "(α=0.100, p=0)",
    "^",
    "WiscKey",
    0.1,
)

# plot_dot(
#     ax, 1, 1, "red", "(α=1, p=1)", "d", "RocksDB"
# )

# plot_dot(
#     ax,
#     1,
#     1,
#     "red",
#     "(α=inf, p=1)",
#     "d",
#     "RocksDB-Small",
# )

plot_dot(
    ax,
    1,
    1,
    "red",
    "(α=inf, p=1)",
    "d",
    "RocksDB",
)

# plot_dot(
#     ax,
#     1,
#     0,
#     "red",
#     "(α=inf, p=0)",
#     "d",
#     "RocksDB-Large",
# )


# 颜色条
cbar = fig.colorbar(
    surface,
    ax=ax,
    shrink=0.5,
    aspect=20,
    pad=0.001,
)
cbar.set_label("R Value", fontsize=12)

# 坐标轴标签
ax.set_xlabel(
    "Size Ratio (KeySST/ValueSST) - α",
    fontsize=12,
)
ax.set_ylabel(
    "Small KV request ratio - p",
    fontsize=12,
)
ax.set_zlabel(
    "Cost-effectiveness Ratio - R",
    fontsize=12,
)

# 视角调整和图例
ax.view_init(elev=30, azim=45)

# 自定义图例项（按需添加）
legend_elements = [
    # R=1 等高线（如果存在）
    Line2D(
        [0],
        [0],
        color="black",
        linestyle="-",
        linewidth=3,
        label="R=1",
    ),
    # 辅助线 p=0.5
    Line2D(
        [0],
        [0],
        color="blue",
        linestyle="--",
        linewidth=2,
        label="p=0.5",
    ),
    # 辅助线 α=0.05
    Line2D(
        [0],
        [0],
        color="green",
        linestyle="--",
        linewidth=2,
        label="α=0.05",
    ),
    # 辅助线 α=0.1
    Line2D(
        [0],
        [0],
        color="black",
        linestyle="-.",
        linewidth=2,
        label="α=0.1",
    ),
    # 交点标记
    Line2D(
        [0],
        [0],
        marker="o",
        color="black",
        linestyle="None",
        markersize=10,
        markerfacecolor="black",
        markeredgecolor="white",
        label="(α=0.05, p=0.5)",
    ),
    # 交点标记
    Line2D(
        [0],
        [0],
        marker="^",
        color="blue",
        linestyle="None",
        markersize=10,
        markerfacecolor="blue",
        markeredgecolor="white",
        label="(α=0.001, p=0)",
    ),
    # 交点标记
    Line2D(
        [0],
        [0],
        marker="d",
        color="red",
        linestyle="None",
        markersize=10,
        markerfacecolor="red",
        markeredgecolor="white",
        label="(α=1, p=1)",
    ),
]

# 手动添加图例（精确定位）
ax.legend(
    handles=legend_elements,
    loc="upper right",  # 基准定位点
    bbox_to_anchor=(1, 0.95),
    fontsize=10,
    framealpha=0.7,
    edgecolor="black",
    facecolor="white",
    ncol=2,  # 单列显示
)

# plt.show()

left_margin = 0.05
right_margin = 0.02
top_margin = 0.02
bottom_margin = 0.05

plt.subplots_adjust(
    left=left_margin / fig.get_size_inches()[0],
    right=1
    - right_margin / fig.get_size_inches()[0],
    top=1 - top_margin / fig.get_size_inches()[1],
    bottom=bottom_margin
    / fig.get_size_inches()[1],
)

plt.savefig(
    "3d_plot_rap_thin.pdf",
    format="pdf",
    dpi=300,
)

# plt.savefig(
#     "3d_plot_rap.pdf",
#     format="pdf",
#     bbox_inches="tight",
#     pad_inches=0.3,
#     dpi=300,
# )
# plt.savefig(
#     "3d_plot_rap.svg",
#     format="svg",
#     bbox_inches="tight",
#     pad_inches=0.3,
#     dpi=300,
# )
# plt.savefig(
#     "3d_plot_rap.png",
#     format="png",
#     bbox_inches="tight",
#     pad_inches=0.3,
#     dpi=300,
# )


# plt.show()
