import streamlit as st
import pandas as pd
import plotly.graph_objects as go


def Title():
    # Tieu de
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.markdown("<h1 style='text-align: center; color: #B799FF;'>TRUNG TRUNG BO</h1>", unsafe_allow_html=True)
        st.markdown("---", unsafe_allow_html=True)
    with col3:
        st.write("")
def docFile(path,sheet_name):
    df = pd.read_excel(path,sheet_name=sheet_name)
    return df

def tongDoanhThu(df_bac_mien_trung):
    st.info(f'Mức doanh thu dự kiến đạt được Mục tiêu / Mức: :red[{df_bac_mien_trung["Mục tiêu / Mức"][1]}] VNĐ')
    doanh_thu_du_kien = []
    thang = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6', 'Tháng 7', 'Tháng 8', 'Tháng 9', 'Tháng 10', 'Tháng 11', 'Tháng 12']
    for i in range(1, 13):
        doanh_thu_du_kien.append(df_bac_mien_trung[f"Tháng {i}"][1])
    doanh_thu_thuc = {
        "Tháng 1": 3800000000,
        "Tháng 2": 4670000000,
        "Tháng 3": 5352000000,
        "Tháng 4": 7000000000,
        "Tháng 5": 5000000000,
        "Tháng 6": 6893000000,
        "Tháng 7": 3000000000,
        "Tháng 8": 7892000000,
        "Tháng 9": 8000000000,
        "Tháng 10": 0,
        "Tháng 11": 0,
        "Tháng 12": 0
    }
    in_real_revenue1, in_real_revenue2, in_real_revenue3, in_real_revenue4, in_real_revenue5, in_real_revenue6 = st.columns(6)
    with in_real_revenue1:
        real_revenue_thang1 = st.number_input('Nhập doanh thu thực tháng 1:', key = "real_revenue_thang1")
    with in_real_revenue2:
        real_revenue_thang2 = st.number_input('Nhập doanh thu thực tháng 2:', key = "real_revenue_thang2")
    with in_real_revenue3:
        real_revenue_thang3 = st.number_input('Nhập doanh thu thực tháng 3:', key = "real_revenue_thang3")
    with in_real_revenue4:
        real_revenue_thang4 = st.number_input('Nhập doanh thu thực tháng 4:', key = "real_revenue_thang4")
    with in_real_revenue5:
        real_revenue_thang5 = st.number_input('Nhập doanh thu thực tháng 5:', key = "real_revenue_thang5")
    with in_real_revenue6:
        real_revenue_thang6 = st.number_input('Nhập doanh thu thực tháng 6:', key = "real_revenue_thang6")
    in_real_revenue7, in_real_revenue8, in_real_revenue9, in_real_revenue10, in_real_revenue11, in_real_revenue12 = st.columns(6)
    with in_real_revenue7:
        real_revenue_thang7 = st.number_input('Nhập doanh thu thực tháng 7:', key = "real_revenue_thang7")
    with in_real_revenue8:
        real_revenue_thang8 = st.number_input('Nhập doanh thu thực tháng 8:', key = "real_revenue_thang8")
    with in_real_revenue9:
        real_revenue_thang9 = st.number_input('Nhập doanh thu thực tháng 9:', key = "real_revenue_thang9")
    with in_real_revenue10:
        real_revenue_thang10 = st.number_input('Nhập doanh thu thực tháng 10:', key = "real_revenue_thang10")
    with in_real_revenue11:
        real_revenue_thang11 = st.number_input('Nhập doanh thu thực tháng 11:', key = "real_revenue_thang11")
    with in_real_revenue12:
        real_revenue_thang12 = st.number_input('Nhập doanh thu thực tháng 12:', key = "real_revenue_thang12")
    # for i in range(1, 13):
    #     doanh_thu_thuc[f'Tháng {i}'] = f'real_revenue_thang{i}'
    doanh_thu_thuc['Tháng 1'] = real_revenue_thang1
    doanh_thu_thuc['Tháng 2'] = real_revenue_thang2
    doanh_thu_thuc['Tháng 3'] = real_revenue_thang3
    doanh_thu_thuc['Tháng 4'] = real_revenue_thang4
    doanh_thu_thuc['Tháng 5'] = real_revenue_thang5
    doanh_thu_thuc['Tháng 6'] = real_revenue_thang6
    doanh_thu_thuc['Tháng 7'] = real_revenue_thang7
    doanh_thu_thuc['Tháng 8'] = real_revenue_thang8
    doanh_thu_thuc['Tháng 9'] = real_revenue_thang9
    doanh_thu_thuc['Tháng 10'] = real_revenue_thang10
    doanh_thu_thuc['Tháng 11'] = real_revenue_thang11
    doanh_thu_thuc['Tháng 12'] = real_revenue_thang12

    doanh_thu_thuc_values = [doanh_thu_thuc[thang[i]] for i in range(len(thang))]
    thang_hien_co_doanh_thu = [t for t, dt in zip(thang, doanh_thu_thuc_values) if dt != 0]
    doanh_thu_hien_co = [dt for dt in doanh_thu_thuc_values if dt != 0]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=thang,
        y=doanh_thu_du_kien,
        name='Doanh thu dự kiến',
        marker_color='rgb(55, 83, 109)',
    ))
    fig.add_trace(go.Bar(
        x=thang,
        y=doanh_thu_thuc_values,  
        name='Doanh thu thực',
        marker_color='rgb(26, 118, 255)',
        opacity=0.7,  
    ))
    for th, dt_du_kien, dt_thuc in zip(thang, doanh_thu_du_kien, doanh_thu_thuc_values):
        y_pos = max(dt_du_kien, dt_thuc)
        percentage = dt_thuc / dt_du_kien * 100
        fig.add_trace(go.Scatter(
            x=[th],
            y=[y_pos],
            text=f"{percentage:.2f}%",
            mode='text',
            textposition='top center',  
            textfont=dict(size=12),
            showlegend=False,
        ))
    fig.add_trace(go.Scatter(
        x=thang_hien_co_doanh_thu,
        y=doanh_thu_hien_co,
        mode='markers+lines',
        name='Doanh thu thực',
        line=dict(color='red', width=2),
    ))
    fig.update_layout(
        title='Biểu đồ doanh thu thực và dự kiến theo tháng',
        xaxis_title='Tháng',
        yaxis_title='Doanh thu',
        barmode='overlay',  
    )
    st.plotly_chart(fig,use_container_width=True,height=800)
    sum_real_revenue = real_revenue_thang1+real_revenue_thang2+real_revenue_thang3+real_revenue_thang4+real_revenue_thang5+real_revenue_thang6+real_revenue_thang7+real_revenue_thang8+real_revenue_thang9+real_revenue_thang10+real_revenue_thang11+real_revenue_thang12
    sum_revenue = 0
    for id in doanh_thu_du_kien:
        sum_revenue+=id
    revenue_ratio = (sum_real_revenue/sum_revenue)*100
    formatted_result = "{:.2f}".format(revenue_ratio)
    st.info(f'Hiện tại đã đạt được doanh thu: :red[{sum_real_revenue}] VNĐ chiếm :red[{formatted_result}] % so với dự kiến')

def doanhThuSanPhamSB(df_bac_mien_trung):
    st.info(f'Mức doanh thu sản phẩm SB dự kiến đạt được Mục tiêu / Mức: :red[{df_bac_mien_trung["Mục tiêu / Mức"][1]*df_bac_mien_trung["Mục tiêu / Mức"][2]}] VNĐ')
    doanh_thu_du_kien = []
    thang = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6', 'Tháng 7', 'Tháng 8', 'Tháng 9', 'Tháng 10', 'Tháng 11', 'Tháng 12']
    for i in range(1, 13):
        doanh_thu_du_kien.append(df_bac_mien_trung[f"Tháng {i}"][2])
    doanh_thu_thuc = {
        "Tháng 1": 3800000000,
        "Tháng 2": 4670000000,
        "Tháng 3": 5352000000,
        "Tháng 4": 7000000000,
        "Tháng 5": 5000000000,
        "Tháng 6": 6893000000,
        "Tháng 7": 3000000000,
        "Tháng 8": 7892000000,
        "Tháng 9": 8000000000,
        "Tháng 10": 0,
        "Tháng 11": 0,
        "Tháng 12": 0
    }
    in_real_revenue1, in_real_revenue2, in_real_revenue3, in_real_revenue4, in_real_revenue5, in_real_revenue6 = st.columns(6)
    with in_real_revenue1:
        real_sb_revenue_thang1 = st.number_input('Nhập doanh thu thực tháng 1:', key = "real_sb_revenue_thang1")
    with in_real_revenue2:
        real_sb_revenue_thang2 = st.number_input('Nhập doanh thu thực tháng 2:', key = "real_sb_revenue_thang2")
    with in_real_revenue3:
        real_sb_revenue_thang3 = st.number_input('Nhập doanh thu thực tháng 3:', key = "real_sb_revenue_thang3")
    with in_real_revenue4:
        real_sb_revenue_thang4 = st.number_input('Nhập doanh thu thực tháng 4:', key = "real_sb_revenue_thang4")
    with in_real_revenue5:
        real_sb_revenue_thang5 = st.number_input('Nhập doanh thu thực tháng 5:', key = "real_sb_revenue_thang5")
    with in_real_revenue6:
        real_sb_revenue_thang6 = st.number_input('Nhập doanh thu thực tháng 6:', key = "real_sb_revenue_thang6")
    in_real_revenue7, in_real_revenue8, in_real_revenue9, in_real_revenue10, in_real_revenue11, in_real_revenue12 = st.columns(6)
    with in_real_revenue7:
        real_sb_revenue_thang7 = st.number_input('Nhập doanh thu thực tháng 7:', key = "real_sb_revenue_thang7")
    with in_real_revenue8:
        real_sb_revenue_thang8 = st.number_input('Nhập doanh thu thực tháng 8:', key = "real_sb_revenue_thang8")
    with in_real_revenue9:
        real_sb_revenue_thang9 = st.number_input('Nhập doanh thu thực tháng 9:', key = "real_sb_revenue_thang9")
    with in_real_revenue10:
        real_sb_revenue_thang10 = st.number_input('Nhập doanh thu thực tháng 10:', key = "real_sb_revenue_thang10")
    with in_real_revenue11:
        real_sb_revenue_thang11 = st.number_input('Nhập doanh thu thực tháng 11:', key = "real_sb_revenue_thang11")
    with in_real_revenue12:
        real_sb_revenue_thang12 = st.number_input('Nhập doanh thu thực tháng 12:', key = "real_sb_revenue_thang12")
    # for i in range(1, 13):
    #     doanh_thu_thuc[f'Tháng {i}'] = f'real_revenue_thang{i}'
    doanh_thu_thuc['Tháng 1'] = real_sb_revenue_thang1
    doanh_thu_thuc['Tháng 2'] = real_sb_revenue_thang2
    doanh_thu_thuc['Tháng 3'] = real_sb_revenue_thang3
    doanh_thu_thuc['Tháng 4'] = real_sb_revenue_thang4
    doanh_thu_thuc['Tháng 5'] = real_sb_revenue_thang5
    doanh_thu_thuc['Tháng 6'] = real_sb_revenue_thang6
    doanh_thu_thuc['Tháng 7'] = real_sb_revenue_thang7
    doanh_thu_thuc['Tháng 8'] = real_sb_revenue_thang8
    doanh_thu_thuc['Tháng 9'] = real_sb_revenue_thang9
    doanh_thu_thuc['Tháng 10'] = real_sb_revenue_thang10
    doanh_thu_thuc['Tháng 11'] = real_sb_revenue_thang11
    doanh_thu_thuc['Tháng 12'] = real_sb_revenue_thang12

    doanh_thu_thuc_values = [doanh_thu_thuc[thang[i]] for i in range(len(thang))]
    thang_hien_co_doanh_thu = [t for t, dt in zip(thang, doanh_thu_thuc_values) if dt != 0]
    doanh_thu_hien_co = [dt for dt in doanh_thu_thuc_values if dt != 0]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=thang,
        y=doanh_thu_du_kien,
        name='Doanh thu dự kiến',
        marker_color='rgb(55, 83, 109)',
    ))
    fig.add_trace(go.Bar(
        x=thang,
        y=doanh_thu_thuc_values,  
        name='Doanh thu thực',
        marker_color='rgb(26, 118, 255)',
        opacity=0.7,  
    ))
    for th, dt_du_kien, dt_thuc in zip(thang, doanh_thu_du_kien, doanh_thu_thuc_values):
        y_pos = max(dt_du_kien, dt_thuc)
        percentage = dt_thuc / dt_du_kien * 100
        fig.add_trace(go.Scatter(
            x=[th],
            y=[y_pos],
            text=f"{percentage:.2f}%",
            mode='text',
            textposition='top center',  
            textfont=dict(size=12),
            showlegend=False,
        ))
    fig.add_trace(go.Scatter(
        x=thang_hien_co_doanh_thu,
        y=doanh_thu_hien_co,
        mode='markers+lines',
        name='Doanh thu thực',
        line=dict(color='red', width=2),
    ))
    fig.update_layout(
        title='Biểu đồ doanh thu thực và dự kiến của sản phẩm SB theo tháng',
        xaxis_title='Tháng',
        yaxis_title='Doanh thu',
        barmode='overlay',  
    )
    st.plotly_chart(fig,use_container_width=True,height=800)
    sum_real_revenue = real_sb_revenue_thang1+real_sb_revenue_thang2+real_sb_revenue_thang3+real_sb_revenue_thang4+real_sb_revenue_thang5+real_sb_revenue_thang6+real_sb_revenue_thang7+real_sb_revenue_thang8+real_sb_revenue_thang9+real_sb_revenue_thang10+real_sb_revenue_thang11+real_sb_revenue_thang12
    sum_revenue = 0 
    for id in doanh_thu_du_kien:
        sum_revenue+=id
    revenue_ratio = (sum_real_revenue/sum_revenue)*100
    formatted_result = "{:.2f}".format(revenue_ratio)
    st.info(f'Hiện tại đã đạt được doanh thu sản phẩm SB: :red[{sum_real_revenue}] VNĐ chiếm :red[{formatted_result}] % so với dự kiến')

def doanhThuSanPhamTT(df_bac_mien_trung):
    st.info(f'Mức doanh thu sản phẩm TT dự kiến đạt được Mục tiêu / Mức: :red[{df_bac_mien_trung["Mục tiêu / Mức"][1]*df_bac_mien_trung["Mục tiêu / Mức"][3]}] VNĐ')
    doanh_thu_du_kien = []
    thang = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6', 'Tháng 7', 'Tháng 8', 'Tháng 9', 'Tháng 10', 'Tháng 11', 'Tháng 12']
    for i in range(1, 13):
        doanh_thu_du_kien.append(df_bac_mien_trung[f"Tháng {i}"][3])
    doanh_thu_thuc = {
        "Tháng 1": 3800000000,
        "Tháng 2": 4670000000,
        "Tháng 3": 5352000000,
        "Tháng 4": 7000000000,
        "Tháng 5": 5000000000,
        "Tháng 6": 6893000000,
        "Tháng 7": 3000000000,
        "Tháng 8": 7892000000,
        "Tháng 9": 8000000000,
        "Tháng 10": 0,
        "Tháng 11": 0,
        "Tháng 12": 0
    }
    in_real_revenue1, in_real_revenue2, in_real_revenue3, in_real_revenue4, in_real_revenue5, in_real_revenue6 = st.columns(6)
    with in_real_revenue1:
        real_tt_revenue_thang1 = st.number_input('Nhập doanh thu thực tháng 1:', key = "real_tt_revenue_thang1")
    with in_real_revenue2:
        real_tt_revenue_thang2 = st.number_input('Nhập doanh thu thực tháng 2:', key = "real_tt_revenue_thang2")
    with in_real_revenue3:
        real_tt_revenue_thang3 = st.number_input('Nhập doanh thu thực tháng 3:', key = "real_tt_revenue_thang3")
    with in_real_revenue4:
        real_tt_revenue_thang4 = st.number_input('Nhập doanh thu thực tháng 4:', key = "real_tt_revenue_thang4")
    with in_real_revenue5:
        real_tt_revenue_thang5 = st.number_input('Nhập doanh thu thực tháng 5:', key = "real_tt_revenue_thang5")
    with in_real_revenue6:
        real_tt_revenue_thang6 = st.number_input('Nhập doanh thu thực tháng 6:', key = "real_tt_revenue_thang6")
    in_real_revenue7, in_real_revenue8, in_real_revenue9, in_real_revenue10, in_real_revenue11, in_real_revenue12 = st.columns(6)
    with in_real_revenue7:
        real_tt_revenue_thang7 = st.number_input('Nhập doanh thu thực tháng 7:', key = "real_tt_revenue_thang7")
    with in_real_revenue8:
        real_tt_revenue_thang8 = st.number_input('Nhập doanh thu thực tháng 8:', key = "real_tt_revenue_thang8")
    with in_real_revenue9:
        real_tt_revenue_thang9 = st.number_input('Nhập doanh thu thực tháng 9:', key = "real_tt_revenue_thang9")
    with in_real_revenue10:
        real_tt_revenue_thang10 = st.number_input('Nhập doanh thu thực tháng 10:', key = "real_tt_revenue_thang10")
    with in_real_revenue11:
        real_tt_revenue_thang11 = st.number_input('Nhập doanh thu thực tháng 11:', key = "real_tt_revenue_thang11")
    with in_real_revenue12:
        real_tt_revenue_thang12 = st.number_input('Nhập doanh thu thực tháng 12:', key = "real_tt_revenue_thang12")
    # for i in range(1, 13):
    #     doanh_thu_thuc[f'Tháng {i}'] = f'real_revenue_thang{i}'
    doanh_thu_thuc['Tháng 1'] = real_tt_revenue_thang1
    doanh_thu_thuc['Tháng 2'] = real_tt_revenue_thang2
    doanh_thu_thuc['Tháng 3'] = real_tt_revenue_thang3
    doanh_thu_thuc['Tháng 4'] = real_tt_revenue_thang4
    doanh_thu_thuc['Tháng 5'] = real_tt_revenue_thang5
    doanh_thu_thuc['Tháng 6'] = real_tt_revenue_thang6
    doanh_thu_thuc['Tháng 7'] = real_tt_revenue_thang7
    doanh_thu_thuc['Tháng 8'] = real_tt_revenue_thang8
    doanh_thu_thuc['Tháng 9'] = real_tt_revenue_thang9
    doanh_thu_thuc['Tháng 10'] = real_tt_revenue_thang10
    doanh_thu_thuc['Tháng 11'] = real_tt_revenue_thang11
    doanh_thu_thuc['Tháng 12'] = real_tt_revenue_thang12

    doanh_thu_thuc_values = [doanh_thu_thuc[thang[i]] for i in range(len(thang))]
    thang_hien_co_doanh_thu = [t for t, dt in zip(thang, doanh_thu_thuc_values) if dt != 0]
    doanh_thu_hien_co = [dt for dt in doanh_thu_thuc_values if dt != 0]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=thang,
        y=doanh_thu_du_kien,
        name='Doanh thu dự kiến',
        marker_color='rgb(55, 83, 109)',
    ))
    fig.add_trace(go.Bar(
        x=thang,
        y=doanh_thu_thuc_values,  
        name='Doanh thu thực',
        marker_color='rgb(26, 118, 255)',
        opacity=0.7,  
    ))
    for th, dt_du_kien, dt_thuc in zip(thang, doanh_thu_du_kien, doanh_thu_thuc_values):
        y_pos = max(dt_du_kien, dt_thuc)
        percentage = dt_thuc / dt_du_kien * 100
        fig.add_trace(go.Scatter(
            x=[th],
            y=[y_pos],
            text=f"{percentage:.2f}%",
            mode='text',
            textposition='top center',  
            textfont=dict(size=12),
            showlegend=False,
        ))
    fig.add_trace(go.Scatter(
        x=thang_hien_co_doanh_thu,
        y=doanh_thu_hien_co,
        mode='markers+lines',
        name='Doanh thu thực',
        line=dict(color='red', width=2),
    ))
    fig.update_layout(
        title='Biểu đồ doanh thu thực và dự kiến của sản phẩm TT theo tháng',
        xaxis_title='Tháng',
        yaxis_title='Doanh thu',
        barmode='overlay',  
    )
    st.plotly_chart(fig,use_container_width=True,height=800)
    sum_real_revenue = real_tt_revenue_thang1+real_tt_revenue_thang2+real_tt_revenue_thang3+real_tt_revenue_thang4+real_tt_revenue_thang5+real_tt_revenue_thang6+real_tt_revenue_thang7+real_tt_revenue_thang8+real_tt_revenue_thang9+real_tt_revenue_thang10+real_tt_revenue_thang11+real_tt_revenue_thang12
    sum_revenue = 0 
    for id in doanh_thu_du_kien:
        sum_revenue+=id
    revenue_ratio = (sum_real_revenue/sum_revenue)*100
    formatted_result = "{:.2f}".format(revenue_ratio)
    st.info(f'Hiện tại đã đạt được doanh thu sản phẩm TT: :red[{sum_real_revenue}] VNĐ chiếm :red[{formatted_result}] % so với dự kiến')

def doanhThuSanPhamCL(df_bac_mien_trung):
    st.info(f'Mức doanh thu sản phẩm CL dự kiến đạt được Mục tiêu / Mức: :red[{df_bac_mien_trung["Mục tiêu / Mức"][1]*df_bac_mien_trung["Mục tiêu / Mức"][4]}] VNĐ')
    doanh_thu_du_kien = []
    thang = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6', 'Tháng 7', 'Tháng 8', 'Tháng 9', 'Tháng 10', 'Tháng 11', 'Tháng 12']
    for i in range(1, 13):
        doanh_thu_du_kien.append(df_bac_mien_trung[f"Tháng {i}"][4])
    doanh_thu_thuc = {
        "Tháng 1": 3800000000,
        "Tháng 2": 4670000000,
        "Tháng 3": 5352000000,
        "Tháng 4": 7000000000,
        "Tháng 5": 5000000000,
        "Tháng 6": 6893000000,
        "Tháng 7": 3000000000,
        "Tháng 8": 7892000000,
        "Tháng 9": 8000000000,
        "Tháng 10": 0,
        "Tháng 11": 0,
        "Tháng 12": 0
    }
    in_real_revenue1, in_real_revenue2, in_real_revenue3, in_real_revenue4, in_real_revenue5, in_real_revenue6 = st.columns(6)
    with in_real_revenue1:
        real_cl_revenue_thang1 = st.number_input('Nhập doanh thu thực tháng 1:', key = "real_cl_revenue_thang1")
    with in_real_revenue2:
        real_cl_revenue_thang2 = st.number_input('Nhập doanh thu thực tháng 2:', key = "real_cl_revenue_thang2")
    with in_real_revenue3:
        real_cl_revenue_thang3 = st.number_input('Nhập doanh thu thực tháng 3:', key = "real_cl_revenue_thang3")
    with in_real_revenue4:
        real_cl_revenue_thang4 = st.number_input('Nhập doanh thu thực tháng 4:', key = "real_cl_revenue_thang4")
    with in_real_revenue5:
        real_cl_revenue_thang5 = st.number_input('Nhập doanh thu thực tháng 5:', key = "real_cl_revenue_thang5")
    with in_real_revenue6:
        real_cl_revenue_thang6 = st.number_input('Nhập doanh thu thực tháng 6:', key = "real_cl_revenue_thang6")
    in_real_revenue7, in_real_revenue8, in_real_revenue9, in_real_revenue10, in_real_revenue11, in_real_revenue12 = st.columns(6)
    with in_real_revenue7:
        real_cl_revenue_thang7 = st.number_input('Nhập doanh thu thực tháng 7:', key = "real_cl_revenue_thang7")
    with in_real_revenue8:
        real_cl_revenue_thang8 = st.number_input('Nhập doanh thu thực tháng 8:', key = "real_cl_revenue_thang8")
    with in_real_revenue9:
        real_cl_revenue_thang9 = st.number_input('Nhập doanh thu thực tháng 9:', key = "real_cl_revenue_thang9")
    with in_real_revenue10:
        real_cl_revenue_thang10 = st.number_input('Nhập doanh thu thực tháng 10:', key = "real_cl_revenue_thang10")
    with in_real_revenue11:
        real_cl_revenue_thang11 = st.number_input('Nhập doanh thu thực tháng 11:', key = "real_cl_revenue_thang11")
    with in_real_revenue12:
        real_cl_revenue_thang12 = st.number_input('Nhập doanh thu thực tháng 12:', key = "real_cl_revenue_thang12")
    # for i in range(1, 13):
    #     doanh_thu_thuc[f'Tháng {i}'] = f'real_revenue_thang{i}'
    doanh_thu_thuc['Tháng 1'] = real_cl_revenue_thang1
    doanh_thu_thuc['Tháng 2'] = real_cl_revenue_thang2
    doanh_thu_thuc['Tháng 3'] = real_cl_revenue_thang3
    doanh_thu_thuc['Tháng 4'] = real_cl_revenue_thang4
    doanh_thu_thuc['Tháng 5'] = real_cl_revenue_thang5
    doanh_thu_thuc['Tháng 6'] = real_cl_revenue_thang6
    doanh_thu_thuc['Tháng 7'] = real_cl_revenue_thang7
    doanh_thu_thuc['Tháng 8'] = real_cl_revenue_thang8
    doanh_thu_thuc['Tháng 9'] = real_cl_revenue_thang9
    doanh_thu_thuc['Tháng 10'] = real_cl_revenue_thang10
    doanh_thu_thuc['Tháng 11'] = real_cl_revenue_thang11
    doanh_thu_thuc['Tháng 12'] = real_cl_revenue_thang12

    doanh_thu_thuc_values = [doanh_thu_thuc[thang[i]] for i in range(len(thang))]
    thang_hien_co_doanh_thu = [t for t, dt in zip(thang, doanh_thu_thuc_values) if dt != 0]
    doanh_thu_hien_co = [dt for dt in doanh_thu_thuc_values if dt != 0]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=thang,
        y=doanh_thu_du_kien,
        name='Doanh thu dự kiến',
        marker_color='rgb(55, 83, 109)',
    ))
    fig.add_trace(go.Bar(
        x=thang,
        y=doanh_thu_thuc_values,  
        name='Doanh thu thực',
        marker_color='rgb(26, 118, 255)',
        opacity=0.7,  
    ))
    for th, dt_du_kien, dt_thuc in zip(thang, doanh_thu_du_kien, doanh_thu_thuc_values):
        y_pos = max(dt_du_kien, dt_thuc)
        percentage = dt_thuc / dt_du_kien * 100
        fig.add_trace(go.Scatter(
            x=[th],
            y=[y_pos],
            text=f"{percentage:.2f}%",
            mode='text',
            textposition='top center',  
            textfont=dict(size=12),
            showlegend=False,
        ))
    fig.add_trace(go.Scatter(
        x=thang_hien_co_doanh_thu,
        y=doanh_thu_hien_co,
        mode='markers+lines',
        name='Doanh thu thực',
        line=dict(color='red', width=2),
    ))
    fig.update_layout(
        title='Biểu đồ doanh thu thực và dự kiến của sản phẩm CL theo tháng',
        xaxis_title='Tháng',
        yaxis_title='Doanh thu',
        barmode='overlay',  
    )
    st.plotly_chart(fig,use_container_width=True,height=800)
    sum_real_revenue = real_cl_revenue_thang1+real_cl_revenue_thang2+real_cl_revenue_thang3+real_cl_revenue_thang4+real_cl_revenue_thang5+real_cl_revenue_thang6+real_cl_revenue_thang7+real_cl_revenue_thang8+real_cl_revenue_thang9+real_cl_revenue_thang10+real_cl_revenue_thang11+real_cl_revenue_thang12
    sum_revenue = 0 
    for id in doanh_thu_du_kien:
        sum_revenue+=id
    revenue_ratio = (sum_real_revenue/sum_revenue)*100
    formatted_result = "{:.2f}".format(revenue_ratio)
    st.info(f'Hiện tại đã đạt được doanh thu sản phẩm CL: :red[{sum_real_revenue}] VNĐ chiếm :red[{formatted_result}] % so với dự kiến')
def loiNhuanGop(df_bac_mien_trung):
    st.info(f'Mức lợi nhuận gộp dự kiến đạt được Mục tiêu / Mức: :red[{df_bac_mien_trung["Mục tiêu / Mức"][6]}] VNĐ')
    doanh_thu_du_kien = []
    thang = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6', 'Tháng 7', 'Tháng 8', 'Tháng 9', 'Tháng 10', 'Tháng 11', 'Tháng 12']
    for i in range(1, 13):
        doanh_thu_du_kien.append(df_bac_mien_trung[f"Tháng {i}"][6])
    doanh_thu_thuc = {
        "Tháng 1": 3800000000,
        "Tháng 2": 4670000000,
        "Tháng 3": 5352000000,
        "Tháng 4": 7000000000,
        "Tháng 5": 5000000000,
        "Tháng 6": 6893000000,
        "Tháng 7": 3000000000,
        "Tháng 8": 7892000000,
        "Tháng 9": 8000000000,
        "Tháng 10": 0,
        "Tháng 11": 0,
        "Tháng 12": 0
    }
    in_real_revenue1, in_real_revenue2, in_real_revenue3, in_real_revenue4, in_real_revenue5, in_real_revenue6 = st.columns(6)
    with in_real_revenue1:
        real_profit_thang1 = st.number_input('Nhập lợi nhuận gộp thực tháng 1:', key = "real_profit_thang1")
    with in_real_revenue2:
        real_profit_thang2 = st.number_input('Nhập lợi nhuận gộp thực tháng 2:', key = "real_profit_thang2")
    with in_real_revenue3:
        real_profit_thang3 = st.number_input('Nhập lợi nhuận gộp thực tháng 3:', key = "real_profit_thang3")
    with in_real_revenue4:
        real_profit_thang4 = st.number_input('Nhập lợi nhuận gộp thực tháng 4:', key = "real_profit_thang4")
    with in_real_revenue5:
        real_profit_thang5 = st.number_input('Nhập lợi nhuận gộp thực tháng 5:', key = "real_profit_thang5")
    with in_real_revenue6:
        real_profit_thang6 = st.number_input('Nhập lợi nhuận gộp thực tháng 6:', key = "real_profit_thang6")
    in_real_revenue7, in_real_revenue8, in_real_revenue9, in_real_revenue10, in_real_revenue11, in_real_revenue12 = st.columns(6)
    with in_real_revenue7:
        real_profit_thang7 = st.number_input('Nhập lợi nhuận gộp thực tháng 7:', key = "real_profit_thang7")
    with in_real_revenue8:
        real_profit_thang8 = st.number_input('Nhập lợi nhuận gộp thực tháng 8:', key = "real_profit_thang8")
    with in_real_revenue9:
        real_profit_thang9 = st.number_input('Nhập lợi nhuận gộp thực tháng 9:', key = "real_profit_thang9")
    with in_real_revenue10:
        real_profit_thang10 = st.number_input('Nhập lợi nhuận gộp thực tháng 10:', key = "real_profit_thang10")
    with in_real_revenue11:
        real_profit_thang11 = st.number_input('Nhập lợi nhuận gộp thực tháng 11:', key = "real_profit_thang11")
    with in_real_revenue12:
        real_profit_thang12 = st.number_input('Nhập lợi nhuận gộp thực tháng 12:', key = "real_profit_thang12")
    # for i in range(1, 13):
    #     doanh_thu_thuc[f'Tháng {i}'] = f'real_revenue_thang{i}'
    doanh_thu_thuc['Tháng 1'] = real_profit_thang1
    doanh_thu_thuc['Tháng 2'] = real_profit_thang2
    doanh_thu_thuc['Tháng 3'] = real_profit_thang3
    doanh_thu_thuc['Tháng 4'] = real_profit_thang4
    doanh_thu_thuc['Tháng 5'] = real_profit_thang5
    doanh_thu_thuc['Tháng 6'] = real_profit_thang6
    doanh_thu_thuc['Tháng 7'] = real_profit_thang7
    doanh_thu_thuc['Tháng 8'] = real_profit_thang8
    doanh_thu_thuc['Tháng 9'] = real_profit_thang9
    doanh_thu_thuc['Tháng 10'] = real_profit_thang10
    doanh_thu_thuc['Tháng 11'] = real_profit_thang11
    doanh_thu_thuc['Tháng 12'] = real_profit_thang12

    doanh_thu_thuc_values = [doanh_thu_thuc[thang[i]] for i in range(len(thang))]
    thang_hien_co_doanh_thu = [t for t, dt in zip(thang, doanh_thu_thuc_values) if dt != 0]
    doanh_thu_hien_co = [dt for dt in doanh_thu_thuc_values if dt != 0]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=thang,
        y=doanh_thu_du_kien,
        name='Lợi nhuận gộp dự kiến',
        marker_color='rgb(55, 83, 109)',
    ))
    fig.add_trace(go.Bar(
        x=thang,
        y=doanh_thu_thuc_values,  
        name='Lợi nhuận gộp thực',
        marker_color='rgb(26, 118, 255)',
        opacity=0.7,  
    ))
    for th, dt_du_kien, dt_thuc in zip(thang, doanh_thu_du_kien, doanh_thu_thuc_values):
        y_pos = max(dt_du_kien, dt_thuc)
        percentage = dt_thuc / dt_du_kien * 100
        fig.add_trace(go.Scatter(
            x=[th],
            y=[y_pos],
            text=f"{percentage:.2f}%",
            mode='text',
            textposition='top center',  
            textfont=dict(size=12),
            showlegend=False,
        ))
    fig.add_trace(go.Scatter(
        x=thang_hien_co_doanh_thu,
        y=doanh_thu_hien_co,
        mode='markers+lines',
        name='Lợi nhuận gộp thực',
        line=dict(color='red', width=2),
    ))
    fig.update_layout(
        title='Biểu đồ lợi nhuận gộp thực và dự kiến theo tháng',
        xaxis_title='Tháng',
        yaxis_title='Lợi nhuận gộp',
        barmode='overlay',  
    )
    st.plotly_chart(fig,use_container_width=True,height=800)
    sum_real_revenue = real_profit_thang1+real_profit_thang2+real_profit_thang3+real_profit_thang4+real_profit_thang5+real_profit_thang6+real_profit_thang7+real_profit_thang8+real_profit_thang9+real_profit_thang10+real_profit_thang11+real_profit_thang12
    sum_revenue = 0 
    for id in doanh_thu_du_kien:
        sum_revenue+=id
    revenue_ratio = (sum_real_revenue/sum_revenue)*100
    formatted_result = "{:.2f}".format(revenue_ratio)
    st.info(f'Hiện tại đã đạt được lợi nhuận gộp: :red[{sum_real_revenue}] VNĐ chiếm :red[{formatted_result}] % so với dự kiến')
def loiNhuanRong(df_bac_mien_trung):
    st.info(f'Mức lợi nhuận ròng dự kiến đạt được Mục tiêu / Mức: :red[{df_bac_mien_trung["Mục tiêu / Mức"][7]}] VNĐ')
    doanh_thu_du_kien = []
    thang = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6', 'Tháng 7', 'Tháng 8', 'Tháng 9', 'Tháng 10', 'Tháng 11', 'Tháng 12']
    for i in range(1, 13):
        doanh_thu_du_kien.append(df_bac_mien_trung[f"Tháng {i}"][7])
    doanh_thu_thuc = {
        "Tháng 1": 3800000000,
        "Tháng 2": 4670000000,
        "Tháng 3": 5352000000,
        "Tháng 4": 7000000000,
        "Tháng 5": 5000000000,
        "Tháng 6": 6893000000,
        "Tháng 7": 3000000000,
        "Tháng 8": 7892000000,
        "Tháng 9": 8000000000,
        "Tháng 10": 0,
        "Tháng 11": 0,
        "Tháng 12": 0
    }
    in_real_revenue1, in_real_revenue2, in_real_revenue3, in_real_revenue4, in_real_revenue5, in_real_revenue6 = st.columns(6)
    with in_real_revenue1:
        real_pprofit_thang1 = st.number_input('Nhập lợi nhuận ròng thực tháng 1:', key = "real_pprofit_thang1")
    with in_real_revenue2:
        real_pprofit_thang2 = st.number_input('Nhập lợi nhuận ròng thực tháng 2:', key = "real_pprofit_thang2")
    with in_real_revenue3:
        real_pprofit_thang3 = st.number_input('Nhập lợi nhuận ròng thực tháng 3:', key = "real_pprofit_thang3")
    with in_real_revenue4:
        real_pprofit_thang4 = st.number_input('Nhập lợi nhuận ròng thực tháng 4:', key = "real_pprofit_thang4")
    with in_real_revenue5:
        real_pprofit_thang5 = st.number_input('Nhập lợi nhuận ròng thực tháng 5:', key = "real_pprofit_thang5")
    with in_real_revenue6:
        real_pprofit_thang6 = st.number_input('Nhập lợi nhuận ròng thực tháng 6:', key = "real_pprofit_thang6")
    in_real_revenue7, in_real_revenue8, in_real_revenue9, in_real_revenue10, in_real_revenue11, in_real_revenue12 = st.columns(6)
    with in_real_revenue7:
        real_pprofit_thang7 = st.number_input('Nhập lợi nhuận ròng thực tháng 7:', key = "real_pprofit_thang7")
    with in_real_revenue8:
        real_pprofit_thang8 = st.number_input('Nhập lợi nhuận ròng thực tháng 8:', key = "real_pprofit_thang8")
    with in_real_revenue9:
        real_pprofit_thang9 = st.number_input('Nhập lợi nhuận ròng thực tháng 9:', key = "real_pprofit_thang9")
    with in_real_revenue10:
        real_pprofit_thang10 = st.number_input('Nhập lợi nhuận ròng thực tháng 10:', key = "real_pprofit_thang10")
    with in_real_revenue11:
        real_pprofit_thang11 = st.number_input('Nhập lợi nhuận ròng thực tháng 11:', key = "real_pprofit_thang11")
    with in_real_revenue12:
        real_pprofit_thang12 = st.number_input('Nhập lợi nhuận ròng thực tháng 12:', key = "real_pprofit_thang12")
    # for i in range(1, 13):
    #     doanh_thu_thuc[f'Tháng {i}'] = f'real_revenue_thang{i}'
    doanh_thu_thuc['Tháng 1'] = real_pprofit_thang1
    doanh_thu_thuc['Tháng 2'] = real_pprofit_thang2
    doanh_thu_thuc['Tháng 3'] = real_pprofit_thang3
    doanh_thu_thuc['Tháng 4'] = real_pprofit_thang4
    doanh_thu_thuc['Tháng 5'] = real_pprofit_thang5
    doanh_thu_thuc['Tháng 6'] = real_pprofit_thang6
    doanh_thu_thuc['Tháng 7'] = real_pprofit_thang7
    doanh_thu_thuc['Tháng 8'] = real_pprofit_thang8
    doanh_thu_thuc['Tháng 9'] = real_pprofit_thang9
    doanh_thu_thuc['Tháng 10'] = real_pprofit_thang10
    doanh_thu_thuc['Tháng 11'] = real_pprofit_thang11
    doanh_thu_thuc['Tháng 12'] = real_pprofit_thang12

    doanh_thu_thuc_values = [doanh_thu_thuc[thang[i]] for i in range(len(thang))]
    thang_hien_co_doanh_thu = [t for t, dt in zip(thang, doanh_thu_thuc_values) if dt != 0]
    doanh_thu_hien_co = [dt for dt in doanh_thu_thuc_values if dt != 0]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=thang,
        y=doanh_thu_du_kien,
        name='Lợi nhuận ròng dự kiến',
        marker_color='rgb(55, 83, 109)',
    ))
    fig.add_trace(go.Bar(
        x=thang,
        y=doanh_thu_thuc_values,  
        name='Lợi nhuận ròng thực',
        marker_color='rgb(26, 118, 255)',
        opacity=0.7,  
    ))
    for th, dt_du_kien, dt_thuc in zip(thang, doanh_thu_du_kien, doanh_thu_thuc_values):
        y_pos = max(dt_du_kien, dt_thuc)
        percentage = dt_thuc / dt_du_kien * 100
        fig.add_trace(go.Scatter(
            x=[th],
            y=[y_pos],
            text=f"{percentage:.2f}%",
            mode='text',
            textposition='top center',  
            textfont=dict(size=12),
            showlegend=False,
        ))
    fig.add_trace(go.Scatter(
        x=thang_hien_co_doanh_thu,
        y=doanh_thu_hien_co,
        mode='markers+lines',
        name='Lợi nhuận ròng thực',
        line=dict(color='red', width=2),
    ))
    fig.update_layout(
        title='Biểu đồ lợi nhuận ròng thực và dự kiến theo tháng',
        xaxis_title='Tháng',
        yaxis_title='Lợi nhuận ròng',
        barmode='overlay',  
    )
    st.plotly_chart(fig,use_container_width=True,height=800)
    sum_real_revenue = real_pprofit_thang1+real_pprofit_thang2+real_pprofit_thang3+real_pprofit_thang4+real_pprofit_thang5+real_pprofit_thang6+real_pprofit_thang7+real_pprofit_thang8+real_pprofit_thang9+real_pprofit_thang10+real_pprofit_thang11+real_pprofit_thang12
    sum_revenue = 0 
    for id in doanh_thu_du_kien:
        sum_revenue+=id
    revenue_ratio = (sum_real_revenue/sum_revenue)*100
    formatted_result = "{:.2f}".format(revenue_ratio)
    st.info(f'Hiện tại đã đạt được lợi nhuận ròng: :red[{sum_real_revenue}] VNĐ chiếm :red[{formatted_result}] % so với dự kiến')
def tongKhachHang(df_bac_mien_trung):
    st.info(f'Tổng khách hàng dự kiến đạt được Mục tiêu / Mức: :red[{df_bac_mien_trung["Mục tiêu / Mức"][8]}]')
    doanh_thu_du_kien = []
    thang = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6', 'Tháng 7', 'Tháng 8', 'Tháng 9', 'Tháng 10', 'Tháng 11', 'Tháng 12']
    for i in range(1, 13):
        doanh_thu_du_kien.append(df_bac_mien_trung[f"Tháng {i}"][8])
    doanh_thu_thuc = {
        "Tháng 1": 3800000000,
        "Tháng 2": 4670000000,
        "Tháng 3": 5352000000,
        "Tháng 4": 7000000000,
        "Tháng 5": 5000000000,
        "Tháng 6": 6893000000,
        "Tháng 7": 3000000000,
        "Tháng 8": 7892000000,
        "Tháng 9": 8000000000,
        "Tháng 10": 0,
        "Tháng 11": 0,
        "Tháng 12": 0
    }
    in_real_revenue1, in_real_revenue2, in_real_revenue3, in_real_revenue4, in_real_revenue5, in_real_revenue6 = st.columns(6)
    with in_real_revenue1:
        consumers_sum_thang1 = st.number_input('Nhập tổng số khách hàng thực tháng 1:', key = "consumers_sum_thang1")
    with in_real_revenue2:
        consumers_sum_thang2 = st.number_input('Nhập tổng số khách hàng thực tháng 2:', key = "consumers_sum_thang2")
    with in_real_revenue3:
        consumers_sum_thang3 = st.number_input('Nhập tổng số khách hàng thực tháng 3:', key = "consumers_sum_thang3")
    with in_real_revenue4:
        consumers_sum_thang4 = st.number_input('Nhập tổng số khách hàng thực tháng 4:', key = "consumers_sum_thang4")
    with in_real_revenue5:
        consumers_sum_thang5 = st.number_input('Nhập tổng số khách hàng thực tháng 5:', key = "consumers_sum_thang5")
    with in_real_revenue6:
        consumers_sum_thang6 = st.number_input('Nhập tổng số khách hàng thực tháng 6:', key = "consumers_sum_thang6")
    in_real_revenue7, in_real_revenue8, in_real_revenue9, in_real_revenue10, in_real_revenue11, in_real_revenue12 = st.columns(6)
    with in_real_revenue7:
        consumers_sum_thang7 = st.number_input('Nhập tổng số khách hàng thực tháng 7:', key = "consumers_sum_thang7")
    with in_real_revenue8:
        consumers_sum_thang8 = st.number_input('Nhập tổng số khách hàng thực tháng 8:', key = "consumers_sum_thang8")
    with in_real_revenue9:
        consumers_sum_thang9 = st.number_input('Nhập tổng số khách hàng thực tháng 9:', key = "consumers_sum_thang9")
    with in_real_revenue10:
        consumers_sum_thang10 = st.number_input('Nhập tổng số khách hàng thực tháng 10:', key = "consumers_sum_thang10")
    with in_real_revenue11:
        consumers_sum_thang11 = st.number_input('Nhập tổng số khách hàng thực tháng 11:', key = "consumers_sum_thang11")
    with in_real_revenue12:
        consumers_sum_thang12 = st.number_input('Nhập tổng số khách hàng thực tháng 12:', key = "consumers_sum_thang12")
    # for i in range(1, 13):
    #     doanh_thu_thuc[f'Tháng {i}'] = f'real_revenue_thang{i}'
    doanh_thu_thuc['Tháng 1'] = consumers_sum_thang1
    doanh_thu_thuc['Tháng 2'] = consumers_sum_thang2
    doanh_thu_thuc['Tháng 3'] = consumers_sum_thang3
    doanh_thu_thuc['Tháng 4'] = consumers_sum_thang4
    doanh_thu_thuc['Tháng 5'] = consumers_sum_thang5
    doanh_thu_thuc['Tháng 6'] = consumers_sum_thang6
    doanh_thu_thuc['Tháng 7'] = consumers_sum_thang7
    doanh_thu_thuc['Tháng 8'] = consumers_sum_thang8
    doanh_thu_thuc['Tháng 9'] = consumers_sum_thang9
    doanh_thu_thuc['Tháng 10'] = consumers_sum_thang10
    doanh_thu_thuc['Tháng 11'] = consumers_sum_thang11
    doanh_thu_thuc['Tháng 12'] = consumers_sum_thang12

    doanh_thu_thuc_values = [doanh_thu_thuc[thang[i]] for i in range(len(thang))]
    thang_hien_co_doanh_thu = [t for t, dt in zip(thang, doanh_thu_thuc_values) if dt != 0]
    doanh_thu_hien_co = [dt for dt in doanh_thu_thuc_values if dt != 0]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=thang,
        y=doanh_thu_du_kien,
        name='Tổng khách hàng dự kiến',
        marker_color='rgb(55, 83, 109)',
    ))
    fig.add_trace(go.Bar(
        x=thang,
        y=doanh_thu_thuc_values,  
        name='Tổng khách hàng thực',
        marker_color='rgb(26, 118, 255)',
        opacity=0.7,  
    ))
    for th, dt_du_kien, dt_thuc in zip(thang, doanh_thu_du_kien, doanh_thu_thuc_values):
        y_pos = max(dt_du_kien, dt_thuc)
        percentage = dt_thuc / dt_du_kien * 100
        fig.add_trace(go.Scatter(
            x=[th],
            y=[y_pos],
            text=f"{percentage:.2f}%",
            mode='text',
            textposition='top center',  
            textfont=dict(size=12),
            showlegend=False,
        ))
    fig.add_trace(go.Scatter(
        x=thang_hien_co_doanh_thu,
        y=doanh_thu_hien_co,
        mode='markers+lines',
        name='Tổng khách hàng thực',
        line=dict(color='red', width=2),
    ))
    fig.update_layout(
        title='Biểu đồ tổng khách hàng thực và dự kiến theo tháng',
        xaxis_title='Tháng',
        yaxis_title='Tổng khách hàng',
        barmode='overlay',  
    )
    st.plotly_chart(fig,use_container_width=True,height=800)
def doanhthu_tb_khachhang(df_bac_mien_trung):
    st.info(f'Doanh thu TB/ Khách hàng dự kiến đạt được Mục tiêu / Mức: :red[{df_bac_mien_trung["Mục tiêu / Mức"][9]}]')
    doanh_thu_du_kien = []
    thang = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6', 'Tháng 7', 'Tháng 8', 'Tháng 9', 'Tháng 10', 'Tháng 11', 'Tháng 12']
    for i in range(1, 13):
        doanh_thu_du_kien.append(df_bac_mien_trung[f"Tháng {i}"][9])
    doanh_thu_thuc = {
        "Tháng 1": 3800000000,
        "Tháng 2": 4670000000,
        "Tháng 3": 5352000000,
        "Tháng 4": 7000000000,
        "Tháng 5": 5000000000,
        "Tháng 6": 6893000000,
        "Tháng 7": 3000000000,
        "Tháng 8": 7892000000,
        "Tháng 9": 8000000000,
        "Tháng 10": 0,
        "Tháng 11": 0,
        "Tháng 12": 0
    }
    in_real_revenue1, in_real_revenue2, in_real_revenue3, in_real_revenue4, in_real_revenue5, in_real_revenue6 = st.columns(6)
    with in_real_revenue1:
        revenue_consumers_thang1 = st.number_input('Nhập Doanh thu TB/ Khách hàng thực tháng 1:', key = "revenue_consumers_thang1")
    with in_real_revenue2:
        revenue_consumers_thang2 = st.number_input('Nhập Doanh thu TB/ Khách hàng thực tháng 2:', key = "revenue_consumers_thang2")
    with in_real_revenue3:
        revenue_consumers_thang3 = st.number_input('Nhập Doanh thu TB/ Khách hàng thực tháng 3:', key = "revenue_consumers_thang3")
    with in_real_revenue4:
        revenue_consumers_thang4 = st.number_input('Nhập Doanh thu TB/ Khách hàng thực tháng 4:', key = "revenue_consumers_thang4")
    with in_real_revenue5:
        revenue_consumers_thang5 = st.number_input('Nhập Doanh thu TB/ Khách hàng thực tháng 5:', key = "revenue_consumers_thang5")
    with in_real_revenue6:
        revenue_consumers_thang6 = st.number_input('Nhập Doanh thu TB/ Khách hàng thực tháng 6:', key = "revenue_consumers_thang6")
    in_real_revenue7, in_real_revenue8, in_real_revenue9, in_real_revenue10, in_real_revenue11, in_real_revenue12 = st.columns(6)
    with in_real_revenue7:
        revenue_consumers_thang7 = st.number_input('Nhập Doanh thu TB/ Khách hàng thực tháng 7:', key = "revenue_consumers_thang7")
    with in_real_revenue8:
        revenue_consumers_thang8 = st.number_input('Nhập Doanh thu TB/ Khách hàng thực tháng 8:', key = "revenue_consumers_thang8")
    with in_real_revenue9:
        revenue_consumers_thang9 = st.number_input('Nhập Doanh thu TB/ Khách hàng thực tháng 9:', key = "revenue_consumers_thang9")
    with in_real_revenue10:
        revenue_consumers_thang10 = st.number_input('Nhập Doanh thu TB/ Khách hàng thực tháng 10:', key = "revenue_consumers_thang10")
    with in_real_revenue11:
        revenue_consumers_thang11 = st.number_input('Nhập Doanh thu TB/ Khách hàng thực tháng 11:', key = "revenue_consumers_thang11")
    with in_real_revenue12:
        revenue_consumers_thang12 = st.number_input('Nhập Doanh thu TB/ Khách hàng thực tháng 12:', key = "revenue_consumers_thang12")
    # for i in range(1, 13):
    #     doanh_thu_thuc[f'Tháng {i}'] = f'real_revenue_thang{i}'
    doanh_thu_thuc['Tháng 1'] = revenue_consumers_thang1
    doanh_thu_thuc['Tháng 2'] = revenue_consumers_thang2
    doanh_thu_thuc['Tháng 3'] = revenue_consumers_thang3
    doanh_thu_thuc['Tháng 4'] = revenue_consumers_thang4
    doanh_thu_thuc['Tháng 5'] = revenue_consumers_thang5
    doanh_thu_thuc['Tháng 6'] = revenue_consumers_thang6
    doanh_thu_thuc['Tháng 7'] = revenue_consumers_thang7
    doanh_thu_thuc['Tháng 8'] = revenue_consumers_thang8
    doanh_thu_thuc['Tháng 9'] = revenue_consumers_thang9
    doanh_thu_thuc['Tháng 10'] = revenue_consumers_thang10
    doanh_thu_thuc['Tháng 11'] = revenue_consumers_thang11
    doanh_thu_thuc['Tháng 12'] = revenue_consumers_thang12

    doanh_thu_thuc_values = [doanh_thu_thuc[thang[i]] for i in range(len(thang))]
    thang_hien_co_doanh_thu = [t for t, dt in zip(thang, doanh_thu_thuc_values) if dt != 0]
    doanh_thu_hien_co = [dt for dt in doanh_thu_thuc_values if dt != 0]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=thang,
        y=doanh_thu_du_kien,
        name='Doanh thu TB/ Khách hàng dự kiến',
        marker_color='rgb(55, 83, 109)',
    ))
    fig.add_trace(go.Bar(
        x=thang,
        y=doanh_thu_thuc_values,  
        name='Doanh thu TB/ Khách hàng thực',
        marker_color='rgb(26, 118, 255)',
        opacity=0.7,  
    ))
    for th, dt_du_kien, dt_thuc in zip(thang, doanh_thu_du_kien, doanh_thu_thuc_values):
        y_pos = max(dt_du_kien, dt_thuc)
        percentage = dt_thuc / dt_du_kien * 100
        fig.add_trace(go.Scatter(
            x=[th],
            y=[y_pos],
            text=f"{percentage:.2f}%",
            mode='text',
            textposition='top center',  
            textfont=dict(size=12),
            showlegend=False,
        ))
    fig.add_trace(go.Scatter(
        x=thang_hien_co_doanh_thu,
        y=doanh_thu_hien_co,
        mode='markers+lines',
        name='Doanh thu TB/ Khách hàng thực',
        line=dict(color='red', width=2),
    ))
    fig.update_layout(
        title='Biểu đồ Doanh thu TB/ Khách hàng thực và dự kiến theo tháng',
        xaxis_title='Tháng',
        yaxis_title='Doanh thu TB/ Khách hàng',
        barmode='overlay',  
    )
    st.plotly_chart(fig,use_container_width=True,height=800)
def khachHangQuayLai(df_bac_mien_trung):
    st.info(f'Khách hàng quay lại dự kiến đạt được Mục tiêu / Mức: :red[{df_bac_mien_trung["Mục tiêu / Mức"][8]*df_bac_mien_trung["Mục tiêu / Mức"][10]}]')
    doanh_thu_du_kien = []
    thang = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6', 'Tháng 7', 'Tháng 8', 'Tháng 9', 'Tháng 10', 'Tháng 11', 'Tháng 12']
    for i in range(1, 13):
        doanh_thu_du_kien.append(df_bac_mien_trung[f"Tháng {i}"][10])
    doanh_thu_thuc = {
        "Tháng 1": 3800000000,
        "Tháng 2": 4670000000,
        "Tháng 3": 5352000000,
        "Tháng 4": 7000000000,
        "Tháng 5": 5000000000,
        "Tháng 6": 6893000000,
        "Tháng 7": 3000000000,
        "Tháng 8": 7892000000,
        "Tháng 9": 8000000000,
        "Tháng 10": 0,
        "Tháng 11": 0,
        "Tháng 12": 0
    }
    in_real_revenue1, in_real_revenue2, in_real_revenue3, in_real_revenue4, in_real_revenue5, in_real_revenue6 = st.columns(6)
    with in_real_revenue1:
        consumers_comeback_thang1 = st.number_input('Nhập khách hàng quay lại thực tháng 1:', key = "consumers_comeback_thang1")
    with in_real_revenue2:
        consumers_comeback_thang2 = st.number_input('Nhập khách hàng quay lại thực tháng 2:', key = "consumers_comeback_thang2")
    with in_real_revenue3:
        consumers_comeback_thang3 = st.number_input('Nhập khách hàng quay lại thực tháng 3:', key = "consumers_comeback_thang3")
    with in_real_revenue4:
        consumers_comeback_thang4 = st.number_input('Nhập khách hàng quay lại thực tháng 4:', key = "consumers_comeback_thang4")
    with in_real_revenue5:
        consumers_comeback_thang5 = st.number_input('Nhập khách hàng quay lại thực tháng 5:', key = "consumers_comeback_thang5")
    with in_real_revenue6:
        consumers_comeback_thang6 = st.number_input('Nhập khách hàng quay lại thực tháng 6:', key = "consumers_comeback_thang6")
    in_real_revenue7, in_real_revenue8, in_real_revenue9, in_real_revenue10, in_real_revenue11, in_real_revenue12 = st.columns(6)
    with in_real_revenue7:
        consumers_comeback_thang7 = st.number_input('Nhập khách hàng quay lại thực tháng 7:', key = "consumers_comeback_thang7")
    with in_real_revenue8:
        consumers_comeback_thang8 = st.number_input('Nhập khách hàng quay lại thực tháng 8:', key = "consumers_comeback_thang8")
    with in_real_revenue9:
        consumers_comeback_thang9 = st.number_input('Nhập khách hàng quay lại thực tháng 9:', key = "consumers_comeback_thang9")
    with in_real_revenue10:
        consumers_comeback_thang10 = st.number_input('Nhập khách hàng quay lại thực tháng 10:', key = "consumers_comeback_thang10")
    with in_real_revenue11:
        consumers_comeback_thang11 = st.number_input('Nhập khách hàng quay lại thực tháng 11:', key = "consumers_comeback_thang11")
    with in_real_revenue12:
        consumers_comeback_thang12 = st.number_input('Nhập khách hàng quay lại thực tháng 12:', key = "consumers_comeback_thang12")
    # for i in range(1, 13):
    #     doanh_thu_thuc[f'Tháng {i}'] = f'real_revenue_thang{i}'
    doanh_thu_thuc['Tháng 1'] = consumers_comeback_thang1
    doanh_thu_thuc['Tháng 2'] = consumers_comeback_thang2
    doanh_thu_thuc['Tháng 3'] = consumers_comeback_thang3
    doanh_thu_thuc['Tháng 4'] = consumers_comeback_thang4
    doanh_thu_thuc['Tháng 5'] = consumers_comeback_thang5
    doanh_thu_thuc['Tháng 6'] = consumers_comeback_thang6
    doanh_thu_thuc['Tháng 7'] = consumers_comeback_thang7
    doanh_thu_thuc['Tháng 8'] = consumers_comeback_thang8
    doanh_thu_thuc['Tháng 9'] = consumers_comeback_thang9
    doanh_thu_thuc['Tháng 10'] = consumers_comeback_thang10
    doanh_thu_thuc['Tháng 11'] = consumers_comeback_thang11
    doanh_thu_thuc['Tháng 12'] = consumers_comeback_thang12

    doanh_thu_thuc_values = [doanh_thu_thuc[thang[i]] for i in range(len(thang))]
    thang_hien_co_doanh_thu = [t for t, dt in zip(thang, doanh_thu_thuc_values) if dt != 0]
    doanh_thu_hien_co = [dt for dt in doanh_thu_thuc_values if dt != 0]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=thang,
        y=doanh_thu_du_kien,
        name='Khách hàng quay lại dự kiến',
        marker_color='rgb(55, 83, 109)',
    ))
    fig.add_trace(go.Bar(
        x=thang,
        y=doanh_thu_thuc_values,  
        name='Khách hàng quay lại thực',
        marker_color='rgb(26, 118, 255)',
        opacity=0.7,  
    ))
    for th, dt_du_kien, dt_thuc in zip(thang, doanh_thu_du_kien, doanh_thu_thuc_values):
        y_pos = max(dt_du_kien, dt_thuc)
        percentage = dt_thuc / dt_du_kien * 100
        fig.add_trace(go.Scatter(
            x=[th],
            y=[y_pos],
            text=f"{percentage:.2f}%",
            mode='text',
            textposition='top center',  
            textfont=dict(size=12),
            showlegend=False,
        ))
    fig.add_trace(go.Scatter(
        x=thang_hien_co_doanh_thu,
        y=doanh_thu_hien_co,
        mode='markers+lines',
        name='Khách hàng quay lại thực',
        line=dict(color='red', width=2),
    ))
    fig.update_layout(
        title='Biểu đồ khách hàng quay lại thực và dự kiến theo tháng',
        xaxis_title='Tháng',
        yaxis_title='Khách hàng quay lại',
        barmode='overlay',  
    )
    st.plotly_chart(fig,use_container_width=True,height=800)
def khachHangQuayLaiDT(df_bac_mien_trung):
    st.info(f'Khách hàng quay lại DT dự kiến đạt được Mục tiêu / Mức: :red[{df_bac_mien_trung["Mục tiêu / Mức"][8]*df_bac_mien_trung["Mục tiêu / Mức"][11]}]')
    doanh_thu_du_kien = []
    thang = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6', 'Tháng 7', 'Tháng 8', 'Tháng 9', 'Tháng 10', 'Tháng 11', 'Tháng 12']
    for i in range(1, 13):
        doanh_thu_du_kien.append(df_bac_mien_trung[f"Tháng {i}"][11])
    doanh_thu_thuc = {
        "Tháng 1": 3800000000,
        "Tháng 2": 4670000000,
        "Tháng 3": 5352000000,
        "Tháng 4": 7000000000,
        "Tháng 5": 5000000000,
        "Tháng 6": 6893000000,
        "Tháng 7": 3000000000,
        "Tháng 8": 7892000000,
        "Tháng 9": 8000000000,
        "Tháng 10": 0,
        "Tháng 11": 0,
        "Tháng 12": 0
    }
    in_real_revenue1, in_real_revenue2, in_real_revenue3, in_real_revenue4, in_real_revenue5, in_real_revenue6 = st.columns(6)
    with in_real_revenue1:
        consumers_comeback_DT_thang1 = st.number_input('Nhập khách hàng quay lại DT thực tháng 1:', key = "consumers_comeback_DT_thang1")
    with in_real_revenue2:
        consumers_comeback_DT_thang2 = st.number_input('Nhập khách hàng quay lại DT thực tháng 2:', key = "consumers_comeback_DT_thang2")
    with in_real_revenue3:
        consumers_comeback_DT_thang3 = st.number_input('Nhập khách hàng quay lại DT thực tháng 3:', key = "consumers_comeback_DT_thang3")
    with in_real_revenue4:
        consumers_comeback_DT_thang4 = st.number_input('Nhập khách hàng quay lại DT thực tháng 4:', key = "consumers_comeback_DT_thang4")
    with in_real_revenue5:
        consumers_comeback_DT_thang5 = st.number_input('Nhập khách hàng quay lại DT thực tháng 5:', key = "consumers_comeback_DT_thang5")
    with in_real_revenue6:
        consumers_comeback_DT_thang6 = st.number_input('Nhập khách hàng quay lại DT thực tháng 6:', key = "consumers_comeback_DT_thang6")
    in_real_revenue7, in_real_revenue8, in_real_revenue9, in_real_revenue10, in_real_revenue11, in_real_revenue12 = st.columns(6)
    with in_real_revenue7:
        consumers_comeback_DT_thang7 = st.number_input('Nhập khách hàng quay lại DT thực tháng 7:', key = "consumers_comeback_DT_thang7")
    with in_real_revenue8:
        consumers_comeback_DT_thang8 = st.number_input('Nhập khách hàng quay lại DT thực tháng 8:', key = "consumers_comeback_DT_thang8")
    with in_real_revenue9:
        consumers_comeback_DT_thang9 = st.number_input('Nhập khách hàng quay lại DT thực tháng 9:', key = "consumers_comeback_DT_thang9")
    with in_real_revenue10:
        consumers_comeback_DT_thang10 = st.number_input('Nhập khách hàng quay lại DT thực tháng 10:', key = "consumers_comeback_DT_thang10")
    with in_real_revenue11:
        consumers_comeback_DT_thang11 = st.number_input('Nhập khách hàng quay lại DT thực tháng 11:', key = "consumers_comeback_DT_thang11")
    with in_real_revenue12:
        consumers_comeback_DT_thang12 = st.number_input('Nhập khách hàng quay lại DT thực tháng 12:', key = "consumers_comeback_DT_thang12")
    # for i in range(1, 13):
    #     doanh_thu_thuc[f'Tháng {i}'] = f'real_revenue_thang{i}'
    doanh_thu_thuc['Tháng 1'] = consumers_comeback_DT_thang1
    doanh_thu_thuc['Tháng 2'] = consumers_comeback_DT_thang2
    doanh_thu_thuc['Tháng 3'] = consumers_comeback_DT_thang3
    doanh_thu_thuc['Tháng 4'] = consumers_comeback_DT_thang4
    doanh_thu_thuc['Tháng 5'] = consumers_comeback_DT_thang5
    doanh_thu_thuc['Tháng 6'] = consumers_comeback_DT_thang6
    doanh_thu_thuc['Tháng 7'] = consumers_comeback_DT_thang7
    doanh_thu_thuc['Tháng 8'] = consumers_comeback_DT_thang8
    doanh_thu_thuc['Tháng 9'] = consumers_comeback_DT_thang9
    doanh_thu_thuc['Tháng 10'] = consumers_comeback_DT_thang10
    doanh_thu_thuc['Tháng 11'] = consumers_comeback_DT_thang11
    doanh_thu_thuc['Tháng 12'] = consumers_comeback_DT_thang12

    doanh_thu_thuc_values = [doanh_thu_thuc[thang[i]] for i in range(len(thang))]
    thang_hien_co_doanh_thu = [t for t, dt in zip(thang, doanh_thu_thuc_values) if dt != 0]
    doanh_thu_hien_co = [dt for dt in doanh_thu_thuc_values if dt != 0]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=thang,
        y=doanh_thu_du_kien,
        name='Khách hàng quay lại DT dự kiến',
        marker_color='rgb(55, 83, 109)',
    ))
    fig.add_trace(go.Bar(
        x=thang,
        y=doanh_thu_thuc_values,  
        name='Khách hàng quay lại DT thực',
        marker_color='rgb(26, 118, 255)',
        opacity=0.7,  
    ))
    for th, dt_du_kien, dt_thuc in zip(thang, doanh_thu_du_kien, doanh_thu_thuc_values):
        y_pos = max(dt_du_kien, dt_thuc)
        percentage = dt_thuc / dt_du_kien * 100
        fig.add_trace(go.Scatter(
            x=[th],
            y=[y_pos],
            text=f"{percentage:.2f}%",
            mode='text',
            textposition='top center',  
            textfont=dict(size=12),
            showlegend=False,
        ))
    fig.add_trace(go.Scatter(
        x=thang_hien_co_doanh_thu,
        y=doanh_thu_hien_co,
        mode='markers+lines',
        name='Khách hàng quay lại DT thực',
        line=dict(color='red', width=2),
    ))
    fig.update_layout(
        title='Biểu đồ khách hàng quay lại thực và dự kiến theo tháng',
        xaxis_title='Tháng',
        yaxis_title='Khách hàng quay lại DT',
        barmode='overlay',  
    )
    st.plotly_chart(fig,use_container_width=True,height=800)
def main():
    # Config trang -----------------------------------------
    st.set_page_config(
        page_title="Trung Trung Bo",
        page_icon="📊",
        layout="wide"
    )
    Title()
    st.markdown("## Tài chính")
    df_bac_mien_trung = pd.read_excel("data/config/Config.xlsx",sheet_name="Trung Trung Bộ",usecols="C:P", skiprows=11, nrows=12)
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Tổng doanh thu","Doanh thu sản phẩm SB","Doanh thu sản phẩm TT","Doanh thu sản phẩm CL","Lợi nhuận gộp","Lợi nhuận ròng"])
    with tab1:
        st.markdown("### Tổng doanh thu")
        tongDoanhThu(df_bac_mien_trung)
    with tab2:
        st.markdown("### Doanh thu sản phẩm SB")
        doanhThuSanPhamSB(df_bac_mien_trung)
    with tab3:
        st.markdown("### Doanh thu sản phẩm TT")
        doanhThuSanPhamTT(df_bac_mien_trung)
    with tab4:
        st.markdown("### Doanh thu sản phẩm CL")
        doanhThuSanPhamCL(df_bac_mien_trung)
    with tab5:
        st.markdown("### Lợi nhuận gộp")
        loiNhuanGop(df_bac_mien_trung)
    with tab6:
        st.markdown("### Lợi nhuận ròng")
        loiNhuanRong(df_bac_mien_trung)
    st.markdown("# Khách hàng")
    kh_tab1, kh_tab2, kh_tab3, kh_tab4 = st.tabs(["Tổng khách hàng","Doanh thu TB/Khách","Khách hàng quay lại","Khách hàng quay lại DT > 10 triệu"])
    with kh_tab1:
        st.markdown("### Tổng khách hàng")
        tongKhachHang(df_bac_mien_trung)
    with kh_tab2:
        st.markdown("### Doanh thu TB/Khách")
        doanhthu_tb_khachhang(df_bac_mien_trung)
    with kh_tab3:
        st.markdown("### Khách hàng quay lại")
        khachHangQuayLai(df_bac_mien_trung)
    with kh_tab4:
        st.markdown("### Khách hàng quay lại DT > 10 triệu")
        khachHangQuayLaiDT(df_bac_mien_trung)

if __name__ == "__main__":
    main()