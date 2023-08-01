import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Config trang -----------------------------------------
st.set_page_config(
    page_title="Dashboard Data Analysis",
    page_icon="📊",
    layout="wide"
)

# Tieu de
col1, col2, col3 = st.columns([1,6,1])
with col1:
    st.write("")
with col2:
    st.markdown("<h1 style='text-align: center; color: #B799FF;'>DASHBOARD</h1>", unsafe_allow_html=True)
    st.markdown("---", unsafe_allow_html=True)
with col3:
    st.write("")

# Load data
df = pd.read_excel("data/du_lieu.xlsx")
ton_df = pd.read_excel("data/ton_kho/vinh/ton_kho_vinh.xlsx")
ton_dn_df = pd.read_excel("data/ton_kho/da_nang/ton_kho_da_nang.xlsx")
ton_hcm_df = pd.read_excel("data/ton_kho/ho_chi_minh/ton_kho_ho_chi_minh.xlsx")

# 1. Tong quan nganh hang
st.markdown("## 1. Tổng quan ngành hàng")

st.markdown("##### Tổng quan tăng trưởng của doanh thu và lợi nhuận qua từng tháng:", unsafe_allow_html=True)
profit_by_month = df.groupby('Tháng')['Lợi nhuận'].sum()
revenue_by_month = df.groupby('Tháng')['Doanh thu thuần'].sum()
ov_col1, ov_col2 = st.columns([5,5])
with ov_col1:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=profit_by_month.index, y=profit_by_month.values, mode='lines+markers', name='Tăng trưởng lợi nhuận'))
    fig.update_layout(title='Biểu đồ tăng trưởng lợi nhuận qua từng tháng',
                    xaxis_title='Tháng',
                    yaxis_title='Lợi nhuận',
                    )
    st.plotly_chart(fig,use_container_width=True,height=800)
with ov_col2:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=revenue_by_month.index, y=revenue_by_month.values, mode='lines+markers', name='Tăng trưởng doanh thu thuần'))
    fig.update_layout(title='Biểu đồ tăng trưởng doanh thu thuần qua từng tháng',
                    xaxis_title='Tháng',
                    yaxis_title='Doanh thu',
                    )
    st.plotly_chart(fig,use_container_width=True,height=800)
st.markdown("##### Tổng quan tăng trưởng của doanh thu và lợi nhuận qua từng tháng của các ngành hàng:", unsafe_allow_html=True)
profit_by_category_month = df.groupby(['category', 'Tháng'])['Lợi nhuận'].sum().reset_index()
revenue_by_category_month = df.groupby(['category', 'Tháng'])['Doanh thu thuần'].sum().reset_index()

tab1, tab2 = st.tabs(["Lợi nhuận", "Doanh thu"])
with tab1:
    fig = go.Figure()
    for category in df['category'].unique():
        data = profit_by_category_month[profit_by_category_month['category'] == category]
        fig.add_trace(go.Scatter(x=data['Tháng'], y=data['Lợi nhuận'], mode='lines+markers', name=category))
    fig.update_layout(title='Biểu đồ tăng trưởng lợi nhuận qua từng tháng theo từng ngành hàng',
                    xaxis_title='Tháng',
                    yaxis_title='Lợi nhuận',
                    )
    st.plotly_chart(fig,use_container_width=True,height=800)
with tab2:
    fig = go.Figure()
    for category in df['category'].unique():
        data = revenue_by_category_month[revenue_by_category_month['category'] == category]
        fig.add_trace(go.Scatter(x=data['Tháng'], y=data['Doanh thu thuần'], mode='lines+markers', name=category))
    fig.update_layout(title='Biểu đồ tăng trưởng doanh thu qua từng tháng theo từng ngành hàng',
                    xaxis_title='Tháng',
                    yaxis_title='Doanh thu thuần',
                    )
    st.plotly_chart(fig,use_container_width=True,height=800)
# 2. Bo loc tung thang
st.markdown("## 2. Bộ lọc từng tháng")
month_filter = st.selectbox("Lọc theo tháng:", df['Tháng'].unique())
df_month = df[df["Tháng"] == month_filter]
# Tính tháng trước với năm đã được chọn:
if month_filter == 1:
    pre_month = 1
else:
    pre_month = month_filter - 1

df_pre_month = df[df["Tháng"]== pre_month]

# Lấy các độ đo thống kê:
df_describe = df_month.describe().round(2).T
df_describe_pre = df_pre_month.describe().round(2).T

st.markdown("##### Tổng quan chỉ số của các tháng:", unsafe_allow_html=True)
tab1, tab2= st.tabs(["Lợi nhuận", "Doanh thu"])
with tab1:
    stats_age_col1, stats_age_col2, stats_age_col3, stats_age_col4 = st.columns(4)
    stats_age_col1.metric(
        label="Sum",
        value=round(df_month["Lợi nhuận"].sum(), 2),
        delta=round(float(df_month["Lợi nhuận"].sum() - df_pre_month["Lợi nhuận"].sum()), 2),
    )
    stats_age_col2.metric(
        label="Mean",
        value=df_describe.loc["Lợi nhuận"].loc["mean"],
        delta=round(df_describe.loc["Lợi nhuận"].loc["mean"] - df_describe_pre.loc["Lợi nhuận"].loc["mean"], 2),
    )
    stats_age_col3.metric(
        label="Median",
        value=df_describe.loc["Lợi nhuận"].loc["50%"],
        delta=round(df_describe.loc["Lợi nhuận"].loc["50%"] - df_describe_pre.loc["Lợi nhuận"].loc["50%"], 2),
    )
    stats_age_col4.metric(
        label="25%",
        value=df_describe.loc["Lợi nhuận"].loc["25%"],
        delta=round(df_describe.loc["Lợi nhuận"].loc["25%"] - df_describe_pre.loc["Lợi nhuận"].loc["25%"], 2),
    )

    stats_age_col5, stats_age_col6, stats_age_col7 = st.columns(3)
    stats_age_col5.metric(
        label="75%",
        value=df_describe.loc["Lợi nhuận"].loc["max"],
        delta=round(df_describe.loc["Lợi nhuận"].loc["max"] - df_describe_pre.loc["Lợi nhuận"].loc["max"], 2),
    )
    stats_age_col6.metric(
        label="Min",
        value=df_describe.loc["Lợi nhuận"].loc["min"],
        delta=round(df_describe.loc["Lợi nhuận"].loc["min"] - df_describe_pre.loc["Lợi nhuận"].loc["min"], 2),
    )
    stats_age_col7.metric(
        label="Max",
        value=df_describe.loc["Lợi nhuận"].loc["max"],
        delta=round(df_describe.loc["Lợi nhuận"].loc["max"] - df_describe_pre.loc["Lợi nhuận"].loc["max"], 2),
    )
with tab2:
    stats_age_col1, stats_age_col2, stats_age_col3, stats_age_col4 = st.columns(4)
    stats_age_col1.metric(
        label="Sum",
        value=round(df_month["Doanh thu thuần"].sum(), 2),
        delta=round(float(df_month["Doanh thu thuần"].sum() - df_pre_month["Doanh thu thuần"].sum()), 2),
    )
    stats_age_col2.metric(
        label="Mean",
        value=df_describe.loc["Doanh thu thuần"].loc["mean"],
        delta=round(df_describe.loc["Doanh thu thuần"].loc["mean"] - df_describe_pre.loc["Doanh thu thuần"].loc["mean"], 2),
    )
    stats_age_col3.metric(
        label="Median",
        value=df_describe.loc["Doanh thu thuần"].loc["50%"],
        delta=round(df_describe.loc["Doanh thu thuần"].loc["50%"] - df_describe_pre.loc["Doanh thu thuần"].loc["50%"], 2),
    )
    stats_age_col4.metric(
        label="25%",
        value=df_describe.loc["Doanh thu thuần"].loc["25%"],
        delta=round(df_describe.loc["Doanh thu thuần"].loc["25%"] - df_describe_pre.loc["Doanh thu thuần"].loc["25%"], 2),
    )

    stats_age_col5, stats_age_col6, stats_age_col7 = st.columns(3)
    stats_age_col5.metric(
        label="75%",
        value=df_describe.loc["Doanh thu thuần"].loc["max"],
        delta=round(df_describe.loc["Doanh thu thuần"].loc["max"] - df_describe_pre.loc["Doanh thu thuần"].loc["max"], 2),
    )
    stats_age_col6.metric(
        label="Min",
        value=df_describe.loc["Doanh thu thuần"].loc["min"],
        delta=round(df_describe.loc["Doanh thu thuần"].loc["min"] - df_describe_pre.loc["Doanh thu thuần"].loc["min"], 2),
    )
    stats_age_col7.metric(
        label="Max",
        value=df_describe.loc["Doanh thu thuần"].loc["max"],
        delta=round(df_describe.loc["Doanh thu thuần"].loc["max"] - df_describe_pre.loc["Doanh thu thuần"].loc["max"], 2),
    )

# 3. Hang ton kho
st.markdown("## 3. Hàng tồn kho")
di_tab1, di_tab2, di_tab3 = st.tabs(["KHO TỔNG VINH", "KHO TỔNG ĐÀ NẴNG", "KHO TỔNG HỒ CHÍ MINH"])
with di_tab1:
    ton_tab1, ton_tab2 = st.tabs(["Chỉ số hàng tồn đầu kì", "Chỉ số hàng tồn cuối kì"])
    ton_dau_ki_by_category_month = ton_df.groupby(['category', 'Tháng'])['Tồn đầu kì'].sum().reset_index()
    ton_cuoi_ki_by_category_month = ton_df.groupby(['category', 'Tháng'])['Tồn cuối kì'].sum().reset_index()
    with ton_tab1:
        fig = go.Figure()
        for category in df['category'].unique():
            data = ton_dau_ki_by_category_month[ton_dau_ki_by_category_month['category'] == category]
            fig.add_trace(go.Scatter(x=data['Tháng'], y=data['Tồn đầu kì'], mode='lines+markers', name=category))
        fig.update_layout(title='Biểu đồ số lượng hàng tồn đầu kì qua từng tháng theo category',
                        xaxis_title='Tháng',
                        yaxis_title='Tồn đầu kì',
                        )
        st.plotly_chart(fig,use_container_width=True,height=800)
    with ton_tab2:
        fig = go.Figure()
        for category in df['category'].unique():
            data = ton_cuoi_ki_by_category_month[ton_cuoi_ki_by_category_month['category'] == category]
            fig.add_trace(go.Scatter(x=data['Tháng'], y=data['Tồn cuối kì'], mode='lines+markers', name=category))
        fig.update_layout(title='Biểu đồ số lượng hàng tồn cuối kì qua từng tháng theo category',
                        xaxis_title='Tháng',
                        yaxis_title='Tồn cuối kì',
                        )
        st.plotly_chart(fig,use_container_width=True,height=800)
with di_tab2:
    ton_tab1, ton_tab2 = st.tabs(["Chỉ số hàng tồn đầu kì", "Chỉ số hàng tồn cuối kì"])
    ton_dau_ki_by_category_month = ton_dn_df.groupby(['category', 'Tháng'])['Tồn đầu kì'].sum().reset_index()
    ton_cuoi_ki_by_category_month = ton_dn_df.groupby(['category', 'Tháng'])['Tồn cuối kì'].sum().reset_index()
    with ton_tab1:
        fig = go.Figure()
        for category in df['category'].unique():
            data = ton_dau_ki_by_category_month[ton_dau_ki_by_category_month['category'] == category]
            fig.add_trace(go.Scatter(x=data['Tháng'], y=data['Tồn đầu kì'], mode='lines+markers', name=category))
        fig.update_layout(title='Biểu đồ số lượng hàng tồn đầu kì qua từng tháng theo category',
                        xaxis_title='Tháng',
                        yaxis_title='Tồn đầu kì',
                        )
        st.plotly_chart(fig,use_container_width=True,height=800)
    with ton_tab2:
        fig = go.Figure()
        for category in df['category'].unique():
            data = ton_cuoi_ki_by_category_month[ton_cuoi_ki_by_category_month['category'] == category]
            fig.add_trace(go.Scatter(x=data['Tháng'], y=data['Tồn cuối kì'], mode='lines+markers', name=category))
        fig.update_layout(title='Biểu đồ số lượng hàng tồn cuối kì qua từng tháng theo category',
                        xaxis_title='Tháng',
                        yaxis_title='Tồn cuối kì',
                        )
        st.plotly_chart(fig,use_container_width=True,height=800)
with di_tab3:
    ton_tab1, ton_tab2 = st.tabs(["Chỉ số hàng tồn đầu kì", "Chỉ số hàng tồn cuối kì"])
    ton_dau_ki_by_category_month = ton_hcm_df.groupby(['category', 'Tháng'])['Tồn đầu kì'].sum().reset_index()
    ton_cuoi_ki_by_category_month = ton_hcm_df.groupby(['category', 'Tháng'])['Tồn cuối kì'].sum().reset_index()
    with ton_tab1:
        fig = go.Figure()
        for category in df['category'].unique():
            data = ton_dau_ki_by_category_month[ton_dau_ki_by_category_month['category'] == category]
            fig.add_trace(go.Scatter(x=data['Tháng'], y=data['Tồn đầu kì'], mode='lines+markers', name=category))
        fig.update_layout(title='Biểu đồ số lượng hàng tồn đầu kì qua từng tháng theo category',
                        xaxis_title='Tháng',
                        yaxis_title='Tồn đầu kì',
                        )
        st.plotly_chart(fig,use_container_width=True,height=800)
    with ton_tab2:
        fig = go.Figure()
        for category in df['category'].unique():
            data = ton_cuoi_ki_by_category_month[ton_cuoi_ki_by_category_month['category'] == category]
            fig.add_trace(go.Scatter(x=data['Tháng'], y=data['Tồn cuối kì'], mode='lines+markers', name=category))
        fig.update_layout(title='Biểu đồ số lượng hàng tồn cuối kì qua từng tháng theo category',
                        xaxis_title='Tháng',
                        yaxis_title='Tồn cuối kì',
                        )
        st.plotly_chart(fig,use_container_width=True,height=800)