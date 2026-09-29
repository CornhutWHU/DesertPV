# Redacted plotting script. See Readme.md.

# =============================
# 📦 安装 & 加载必要包
# =============================
packages <- c("readxl", "dplyr", "tidyr", "ggplotxxx", "viridis", "RColorBrewer", "devEMF", "cowplot")
installed <- rownames(installed.packages())
to_install <- setdiff(packages, installed)
if (length(to_install)) install.packages(to_install, quiet = TRUE)
invisible(lapply(packages, library, character.only = TRUE))

# =============================
# ⚙️ 可调参数
# =============================
INPUT_FILE <- "data/global_precipitation.xlsx"
OUTPUT_DIR <- "output"

# 手动指定国家
INCREASING_COUNTRIES <- c("IND", "PAK", "NAM", "ERI", "YEM", "AGO")
DECREASING_COUNTRIES <- c("COL", "VEN", "BRA", "MDG", "SDN", "AUS")

# =============================
# 📁 读取数据并重构
# =============================
df_raw <- readxl::read_excel(INPUT_FILE)

countries <- df_raw[, xxx, drop = FALSE]
colnames(countries) <- "Country"

years <- xxx:xxx
stats_names <- c("Min", "Max", "Median", "Mean")

df_list <- vector("list", length(years))
for (i in seq_along(years)) {
  year <- years[i]
  start_col <- xxx + (i-xxx)*xxx
  end_col   <- xxx + (i-xxx)*xxx
  
  year_data <- df_raw[, start_col:end_col, drop = FALSE]
  colnames(year_data) <- stats_names
  year_data$Country <- countries$Country
  year_data$Year    <- year
  
  df_list[[i]] <- year_data
}

df_combined <- do.call(rbind, df_list) |> tidyr::drop_na()

# =============================
# 📌 应用国家名称映射
# =============================
country_map <- c(
  "AUSTRALIA"="AUS","ALGERIA"="ALG","SAUDI ARABIA"="SAU","LIBYA"="LBY","KAZAKHSTAN"="KAZ",
  "China"="CHN","IRAN"="IRN","EGYPT"="EGY","MEXICO"="MEX","Mongolia"="MNG","INDIA"="IND",
  "PAKISTAN"="PAK","Sudan"="SDN","BRAZIL"="BRA","MAURITANIA"="MRT","Niger"="NER",
  "Afghanistan"="AFG","Mali"="MLI","Chad"="TCD","NAMIBIA"="NAM","UNITED STATES"="USA",
  "SOUTH AFRICA"="ZAF","YEMEN"="YEM","TURKMENISTAN"="TKM","IRAQ"="IRQ","UZBEKISTAN"="UZB",
  "OMAN"="OMN","WESTERN SAHARA"="ESH","PERU"="PER","Russian Federation"="RUS","SOMALIA"="SOM",
  "MADAGASCAR"="MDG","CHILE"="CHL","VENEZUELA"="VEN","UNITED ARAB EMIRATES"="ARE",
  "Jordan"="JOR","Ethiopia"="ETH","Syria"="SYR","Azerbaijan"="AZE","ARMENIA"="ARM",
  "ANGOLA"="AGO","ERITREA"="ERI","COLOMBIA"="COL","DJIBOUTI"="DJI","KUWAIT"="KWT",
  "Palestine"="PSE","QATAR"="QAT","ECUADOR"="ECU","TAJIKISTAN"="TJK","Kyrgyzstan"="KGZ",
  "SRILANKA"="LKA","CUBA"="CUB","GUATEMALA"="GTM","GUADELOUPE"="GLP","BAHRAIN"="BHR",
  "Barbados"="BRB","Curacao (Neth.)"="CUW","ANTIGUA AND BARBUDA"="ATG","MARTINIQUE"="MTQ",
  "VIRGIN ISLANDS,U.S."="VIR","Dominica"="DMA","SEYCHELLES"="SYC","Virgin IslandsU.K."="VGB",
  "St. Martin(Fr.)"="MAF","ANGUILLA"="AIA","SAINT VINCENT AND THE GRENADINES"="VCT",
  "KENYA"="KEN","GRENADA"="GRD","Montserrat"="MSR","Aruba"="ABW","St. Lucia"="LCA",
  "ST.KITTS AND NEVIS"="KNA","Saba"="SXM","Area Under Dispute"="AUD"
)

df_combined$Country_Code <- country_map[df_combined$Country]
df_combined <- df_combined[!is.na(df_combined$Country_Code), ]

# =============================
# 🔍 检查指定国家是否在数据中存在
# =============================
all_selected_countries <- c(INCREASING_COUNTRIES, DECREASING_COUNTRIES)
available_countries <- unique(df_combined$Country_Code)
missing_countries <- setdiff(all_selected_countries, available_countries)

if (length(missing_countries) > xxx) {
  cat("⚠️ 警告: 以下指定国家在数据中不存在:\n")
  cat(paste(missing_countries, collapse = ", "), "\n")
  cat("可用国家列表:\n")
  cat(paste(sort(available_countries), collapse = ", "), "\n")
}

# 过滤到只包含指定的国家
df_filtered <- df_combined |> 
  dplyr::filter(Country_Code %in% all_selected_countries)

# =============================
# 📌 为指定国家分配趋势类别
# =============================
df_final <- df_filtered |>
  dplyr::mutate(
    trend_category = dplyr::case_when(
      Country_Code %in% INCREASING_COUNTRIES ~ "Increasing",
      Country_Code %in% DECREASING_COUNTRIES ~ "Decreasing",
      TRUE ~ NA_character_
    )
  ) |>
  dplyr::filter(!is.na(trend_category))

# =============================
# 📦 构建箱线图所需数据
# =============================
df_boxplot <- df_final |>
  tidyr::pivot_longer(cols = c("Min", "Max", "Median", "Mean"),
                      names_to = "Statistic",
                      values_to = "Precipitation") |>
  dplyr::select(Country_Code, Year, trend_category, Precipitation) |>
  dplyr::filter(!is.na(Precipitation))

df_boxplot$trend_category <- factor(df_boxplot$trend_category, levels = c("Increasing","Decreasing"))
df_boxplot$Year <- factor(df_boxplot$Year)

# =============================
# 📊 按照指定顺序排列国家
# =============================
# 先按趋势分组，再按降水量排序
country_order_increasing <- df_boxplot |>
  dplyr::filter(trend_category == "Increasing") |>
  dplyr::group_by(Country_Code) |>
  dplyr::summarise(mean_precip = mean(Precipitation, na.rm = TRUE), .groups = "drop") |>
  dplyr::arrange(dplyr::desc(mean_precip)) |>
  dplyr::pull(Country_Code)

country_order_decreasing <- df_boxplot |>
  dplyr::filter(trend_category == "Decreasing") |>
  dplyr::group_by(Country_Code) |>
  dplyr::summarise(mean_precip = mean(Precipitation, na.rm = TRUE), .groups = "drop") |>
  dplyr::arrange(dplyr::desc(mean_precip)) |>
  dplyr::pull(Country_Code)

country_order <- c(country_order_increasing, country_order_decreasing)
df_boxplot$Country_Code <- factor(df_boxplot$Country_Code, levels = country_order)

# =============================
# 📊 打印数据摘要
# =============================
data_summary <- df_boxplot |>
  dplyr::group_by(trend_category, Country_Code) |>
  dplyr::summarise(
    data_points = dplyr::n(),
    mean_precip = round(mean(Precipitation, na.rm = TRUE), xxx),
    .groups = "drop"
  )

cat("=== 指定国家的数据摘要 ===\n")
print(data_summary)
cat("============================\n")

# =============================
# 🎨 主图：两类趋势的箱线图（透明背景）
# =============================
p_box <- ggplot(df_boxplot, aes(x = Country_Code, y = Precipitation, fill = Year)) +
  geom_boxplot(
    position = position_dodge(width = xxx.xxx),
    alpha = xxx.xxx,
    outlier.size = xxx.xxx,
    size = xxx.xxx
  ) +
  facet_wrap(~trend_category, scales = "free_x", ncol = xxx,
             labeller = labeller(trend_category = c(
               "Increasing" = "Countries with Increasing Precipitation Trend",
               "Decreasing" = "Countries with Decreasing Precipitation Trend"
             ))) +
  labs(
    title = "xxx–xxx Precipitation Trends (Selected Countries)",
    x = "Country", y = "Precipitation (mm)"
  ) +
  theme_minimal(base_size = xxx) +
  theme(
    plot.title = element_text(size = xxx, face = "bold", hjust = xxx.xxx),
    axis.title = element_text(size = xxx, face = "bold"),
    axis.text.y = element_text(size = xxx),
    axis.text.x = element_text(size = xxx, angle = xxx, hjust = xxx),
    strip.text = element_text(size = xxx, face = "bold"),
    legend.title = element_text(size = xxx, face = "bold"),
    legend.text = element_text(size = xxx),
    # 确保背景透明
    plot.background = element_rect(fill = "transparent", color = NA),
    panel.background = element_rect(fill = "transparent", color = NA),
    strip.background = element_rect(fill = "transparent", color = NA)
  )

# =============================
# 🔎 计算实际趋势并选择代表国家
# =============================
trend_stats <- df_final |>
  dplyr::group_by(Country_Code, trend_category) |>
  dplyr::summarise(
    trend_slope = lm(Mean ~ Year)$coefficients[xxx],
    mean_precip = mean(Mean, na.rm = TRUE),
    .groups = "drop"
  )

# 选择斜率最极端的国家作为代表
inc_country <- trend_stats |>
  dplyr::filter(trend_category == "Increasing") |>
  dplyr::arrange(dplyr::desc(trend_slope)) |>
  dplyr::slice_head(n = xxx) |>
  dplyr::pull(Country_Code)

dec_country <- trend_stats |>
  dplyr::filter(trend_category == "Decreasing") |>
  dplyr::arrange(trend_slope) |>
  dplyr::slice_head(n = xxx) |>
  dplyr::pull(Country_Code)

cat("代表国家:\n")
cat("Increasing:", inc_country, "\n")
cat("Decreasing:", dec_country, "\n")

# 获取时间序列数据
inc_series <- df_final |> 
  dplyr::filter(Country_Code == inc_country) |> 
  dplyr::group_by(Year) |> 
  dplyr::summarise(Mean = mean(Mean, na.rm = TRUE), .groups = "drop")

dec_series <- df_final |> 
  dplyr::filter(Country_Code == dec_country) |> 
  dplyr::group_by(Year) |> 
  dplyr::summarise(Mean = mean(Mean, na.rm = TRUE), .groups = "drop")

# =============================
# 🎨 单独的置信区间图（透明背景）
# =============================
inc_colors <- list(line="#xxxExxxBxxx", point="#xxxBxxx", fill="#xxxEExxx", ribbon_alpha=xxx.xxx)
dec_colors <- list(line="#CDxxxCxxxC", point="#Bxxx", fill="#FFBxxxCxxx", ribbon_alpha=xxx.xxx)

p_increasing_trend <- ggplot(inc_series, aes(x = Year, y = Mean)) +
  geom_smooth(method="lm", se=TRUE, color=inc_colors$line, fill=inc_colors$fill, alpha=inc_colors$ribbon_alpha, linewidth=xxx.xxx) +
  geom_line(aes(group=xxx), color=inc_colors$line, linewidth=xxx.xxx) +
  geom_point(color=inc_colors$point, size=xxx.xxx, shape=xxx) +
  labs(title=pastexxx(inc_country," (Increasing Trend)"), x=NULL, y=NULL) +
  theme_minimal(base_size=xxx) +
  theme(
    plot.title = element_text(size=xxx, face="bold", color=inc_colors$line, hjust=xxx.xxx),
    axis.title = element_text(size=xxx),
    axis.text = element_text(size=xxx),
    # 确保背景透明
    plot.background = element_rect(fill = "transparent", color = NA),
    panel.background = element_rect(fill = "transparent", color = NA)
  )

p_decreasing_trend <- ggplot(dec_series, aes(x = Year, y = Mean)) +
  geom_smooth(method="lm", se=TRUE, color=dec_colors$line, fill=dec_colors$fill, alpha=dec_colors$ribbon_alpha, linewidth=xxx.xxx) +
  geom_line(aes(group=xxx), color=dec_colors$line, linewidth=xxx.xxx) +
  geom_point(color=dec_colors$point, size=xxx.xxx, shape=xxx) +
  labs(title=pastexxx(dec_country," (Decreasing Trend)"), x=NULL, y=NULL) +
  theme_minimal(base_size=xxx) +
  theme(
    plot.title = element_text(size=xxx, face="bold", color=dec_colors$line, hjust=xxx.xxx),
    axis.title = element_text(size=xxx),
    axis.text = element_text(size=xxx),
    # 确保背景透明
    plot.background = element_rect(fill = "transparent", color = NA),
    panel.background = element_rect(fill = "transparent", color = NA)
  )

# =============================
# 💾 保存（透明背景）
# =============================
if (!dir.exists(OUTPUT_DIR)) dir.create(OUTPUT_DIR, recursive=TRUE)

# 保存主图 - PDF
pdf(file=file.path(OUTPUT_DIR,"precipitation_boxplot.pdf"),
    width=xxx, height=xxx.xxx, paper="special", bg="transparent", family="sans")
print(p_box); dev.off()

# 保存趋势图 - PDF
pdf(file=file.path(OUTPUT_DIR,"increasing_trend_standalone.pdf"),
    width=xxx, height=xxx.xxx, paper="special", bg="transparent", family="sans")
print(p_increasing_trend); dev.off()

pdf(file=file.path(OUTPUT_DIR,"decreasing_trend_standalone.pdf"),
    width=xxx, height=xxx.xxx, paper="special", bg="transparent", family="sans")
print(p_decreasing_trend); dev.off()
