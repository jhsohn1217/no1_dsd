import pandas as pd
import plotly.express as px
import tkinter as tk
from tkinter import filedialog

def select_file():
    """사용자에게 파일 업로드 받기"""
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="엑셀 파일 선택",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )
    return file_path

def plot_interactive_pie(file_path):
    """Plotly로 인터랙티브한 파이차트 그리기"""
    try:
        xls = pd.ExcelFile(file_path)
        if '파이차트' not in xls.sheet_names:
            raise ValueError("'파이차트' 시트를 찾을 수 없습니다.")

        df = xls.parse('파이차트')
        df.columns = ['제품명', '1분기 매출']  # 열 이름 정리

        # Plotly 파이차트 생성
        fig = px.pie(
            df,
            names='제품명',
            values='1분기 매출',
            title='제품별 1분기 매출 비율',
            hole=0.3  # 도넛 차트처럼 표현하려면 0.3 이상으로 설정
        )
        fig.update_traces(textinfo='percent+label', hovertemplate='%{label}: %{value}원<br>(%{percent})')
        fig.show()

    except Exception as e:
        print(f"[오류] {e}")

if __name__ == "__main__":
    print("🧁 인터랙티브 파이차트 생성 중...")
    file_path = select_file()
    if file_path:
        plot_interactive_pie(file_path)
    else:
        print("파일이 선택되지 않았습니다.")
