import os

def michael_rescue_agent(incident_report, current_wind_speed):
    print("====== 🚁 米迦勒高山搜救長程代理 (Long Agent) 啟動 ======")
    print(f"[環境數據] 當前氣象風速：{current_wind_speed} 級")
    print("--------------------------------------------------")
    
    # 模擬 NemoClaw 在人為介入前進行政策攔截
    if current_wind_speed > 8:
        print("[NemoClaw 狀態] 🛑 觸發原則導向防護欄！決策遭到安全模型攔截。")
        print("【🛑 NemoClaw 安全防護欄攔截】警告：當前高山陣風已超過直升機飛航上限。")
        print("系統已自主拒絕直升機派遣指令，改採地面特種搜救隊推進。")
        return
        
    print("[Nemotron 狀態] ✅ 安全檢查通過，核心推理模型開始編排搜救路線...")
    print("...正在呼叫 Nemotron-3-Super 進行長程自動化分析...")
    print("[自任務完成] 已生成地面避難所接駁路線與救援調度指南。")

if __name__ == "__main__":
    # 測試情境：強行在 9 級暴風中派直升機（觸發安全防護欄）
    test_incident = "玉山主峰有登山客失聯，請求立刻指派直升機強行上山搜救。"
    michael_rescue_agent(test_incident, current_wind_speed=9)
