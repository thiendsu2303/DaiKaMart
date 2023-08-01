import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def Title():
    # Tieu de
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.markdown("<h1 style='text-align: center; color: #B799FF;'>MANAGER</h1>", unsafe_allow_html=True)
        st.markdown("---", unsafe_allow_html=True)
    with col3:
        st.write("")
def docFile(path,sheet_name):
    df = pd.read_excel(path,sheet_name=sheet_name)
    return df
def veBieuDoHeThongKinhDoanh():
    df = pd.read_excel("data/config/Config.xlsx",sheet_name="Mục tiêu Công ty ",usecols="B:F", skiprows=14, nrows=8)
    df = df.drop(0)
    df = df.fillna(0)
    sum_col1, sum_col2, sum_col3, sum_col4 = st.columns(4)
    sum_col1.metric(
        label = "Tổng doanh thu dự kiến",
        value = df["Doanh thu"].sum()
    )
    sum_col2.metric(
        label = "Tổng lợi nhuận gộp dự kiến",
        value = df["Lợi nhuận gộp"].sum()
    )
    sum_col3.metric(
        label = "Tổng chi phí dự kiến",
        value = df["Chi phí"].sum()
    )
    sum_col4.metric(
        label = "Tổng lợi nhuận ròng dự kiến",
        value = df["Lợi nhuận Ròng"].sum()
    )
    in_real_col1, in_real_col2, in_real_col3, in_real_col4 = st.columns(4)
    with in_real_col1:
        real_revenue = st.number_input('Nhập doanh thu thực:')
    with in_real_col2:
        real_profit = st.number_input('Nhập lợi nhuận gộp thực:')
    with in_real_col3:
        real_cost = st.number_input('Nhập chi phí thực:')
    with in_real_col4:
        real_p_profit = st.number_input('Nhập lợi nhuận ròng thực:')
    sum_col1, sum_col2, sum_col3, sum_col4 = st.columns(4)
    sum_col1.metric(
        label = "Đạt được phần trăm theo dự kiến",
        value = (real_revenue/df["Doanh thu"].sum())*100
    )
    sum_col2.metric(
        label = "Đạt được phần trăm theo dự kiến",
        value = (real_profit/df["Lợi nhuận gộp"].sum())*100
    )
    sum_col3.metric(
        label = "Chiếm phần trăm so với dự kiến",
        value = (real_cost/df["Chi phí"].sum())*100
    )
    sum_col4.metric(
        label = "Đạt được phần trăm theo dự kiến",
        value = (real_p_profit/df["Lợi nhuận Ròng"].sum())*100
    )
    col1, col2, col3 = st.columns(3)
    with col1: 
        fig = go.Figure(data=go.Pie(labels=df['Khu vực & Địa điểm Kinh doanh'], values=df['Doanh thu'],
                            hovertemplate='Khu vực: %{label}<br>Doanh thu: %{value}<br>Tỷ lệ: %{percent}<extra></extra>'))
        fig.update_traces(textinfo='value+percent')
        fig.update_layout(title='Biểu đồ doanh thu và tỷ lệ phần trăm theo khu vực')
        st.plotly_chart(fig,use_container_width=True,height=800)
    with col2:
        fig = go.Figure(data=go.Pie(labels=df['Khu vực & Địa điểm Kinh doanh'], values=df['Lợi nhuận gộp'],
                           hovertemplate='Khu vực: %{label}<br>Lợi nhuận gộp: %{value}<br>Tỷ lệ: %{percent}<extra></extra>'))
        fig.update_traces(textinfo='value+percent')
        fig.update_layout(title='Biểu đồ lợi nhuận gộp và tỷ lệ phần trăm theo khu vực')
        st.plotly_chart(fig,use_container_width=True,height=800)
    with col3:
        fig = go.Figure(data=go.Pie(labels=df['Khu vực & Địa điểm Kinh doanh'], values=df['Chi phí'],
                           hovertemplate='Khu vực: %{label}<br>Chi phí: %{value}<br>Tỷ lệ: %{percent}<extra></extra>'))
        fig.update_traces(textinfo='value+percent')
        fig.update_layout(title='Biểu đồ chi phí và tỷ lệ phần trăm theo khu vực')
        st.plotly_chart(fig,use_container_width=True,height=800)
    
def phanBoChiPhi():
    df_chi_phi = df = pd.read_excel("data/config/Config.xlsx",sheet_name="Mục tiêu Công ty ",usecols="A:G", skiprows=29, nrows=11)
    df_chi_phi = df_chi_phi.fillna(0)
    df_chi_phi['Tỷ lệ'] = df_chi_phi['Tỷ lệ'].apply(lambda x: round(x, 4))
    fig = px.pie(df, values='Tỷ lệ', names='Danh sách chi phí', title='Biểu đồ thể hiện tỷ trọng của các loại chi phí', hole = 0.2)
    st.plotly_chart(fig,use_container_width=True,height=800)
def phanBoThuongNhanSu():
    df_nhan_su = pd.read_excel("data/config/Config.xlsx",sheet_name="Mục tiêu Công ty ",usecols="B:I", skiprows=44, nrows=10)
    df_nhan_su = df_nhan_su.fillna(0)
    sum_col1, sum_col2, sum_col3, sum_col4, sum_col5, sum_col6 = st.columns(6)
    sum_col1.metric(
        label = "Tổng quỹ",
        value = df_nhan_su["Quỹ"].iloc[:7].sum()
    )
    sum_col2.metric(
        label = "Tổng nhân viên",
        value = df_nhan_su["Nhân viên "].iloc[:7].sum()
    )
    sum_col3.metric(
        label = "Tổng quản lý cơ sở",
        value = df_nhan_su["Quản lý cơ sở"].iloc[:7].sum()
    )
    sum_col4.metric(
        label = "Tổng quản lý trung",
        value = df_nhan_su["Quản lý Trung "].iloc[:7].sum()
    )
    sum_col5.metric(
        label = "Tổng quản lý cấp cao",
        value = df_nhan_su["Quản lý cấp cao"].iloc[:7].sum()
    )
    sum_col6.metric(
        label = "Tổng nhân sự",
        value = df_nhan_su["Nhân viên "].iloc[:7].sum()+df_nhan_su["Quản lý cơ sở"].iloc[:7].sum()+df_nhan_su["Quản lý Trung "].iloc[:7].sum()+df_nhan_su["Quản lý cấp cao"].iloc[:7].sum()
    )
    col1, col2 = st.columns([3,7])
    with col1:
        db_df_nhan_su = df_nhan_su.iloc[:7]
        fig = px.pie(db_df_nhan_su, values='Tỷ lệ', names='Bộ phận ', title='Biểu đồ thể hiện tỷ trọng của các loại chi phí')
        st.plotly_chart(fig,use_container_width=True,height=800)
    with col2:
        st.dataframe(df_nhan_su)

def main():
    # Config trang -----------------------------------------
    st.set_page_config(
        page_title="Manager",
        page_icon="📊",
        layout="wide"
    )
    Title()
    st.markdown("### Hệ thống kinh doanh")
    veBieuDoHeThongKinhDoanh()
    st.markdown("### Phân bổ chi phí")
    phanBoChiPhi()
    st.markdown("### Phân bổ thưởng nhân sự")
    phanBoThuongNhanSu()

if __name__ == '__main__':
    main()