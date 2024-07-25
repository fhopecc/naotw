
def 設定環境():
    import sys 
    cmd = f'"{sys.executable}" "{__file__}" --file2newsquery "%1"'
    增加所有檔案右鍵選單之功能('建置資訊發布提問', cmd)

def 增加所有檔案右鍵選單之功能(功能名稱:str, 指令:str):
    import winreg as reg
    import os
    import sys

    # 功能名稱
    context_menu_name = 功能名稱
    
    key_path = fr'*\shell\{context_menu_name}'
    command_key_path = fr'*\shell\{context_menu_name}\command'

    # 創建註冊表項目
    try:
        reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
        reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key_path)
        
        # 設置右鍵選單項目名稱
        with reg.OpenKey(reg.HKEY_CLASSES_ROOT, key_path, 0, reg.KEY_WRITE) as key:
            reg.SetValue(key, '', reg.REG_SZ, context_menu_name)

        # 設置指令
        with reg.OpenKey(reg.HKEY_CLASSES_ROOT, command_key_path, 0, reg.KEY_WRITE) as key:
            reg.SetValue(key, '', reg.REG_SZ, 指令)
        print(f"所有檔案右鍵選單增加【{功能名稱}】項目。")
    except Exception as e:
        print(f"添加右鍵選單項目時出錯: {e}")

def 建置資訊發布提問至剪貼簿(內容):
    '資訊發布'
    from clipboard import copy
    提問 = f'''"
        在台灣，請用繁體中文回答。以下我將提供審計部臺灣省宜蘭縣審計室對於追蹤查核意見後續改善情形後，所辦理的3則資訊發布標題與架構內容給您參考。

        第1則 
        標題：宜蘭縣部分建築物公共安全及消防安全檢查作業未臻周妥，審計機關促請改善
        內容：
        宜蘭縣政府(下稱縣政府)及所屬消防局(下稱消防局)執行建築物公共安全及消防安全檢查作業，經審計部臺灣省宜蘭縣審計室查核發現，部分供公眾使用之建築物有逾期或漏未申報公共安全或消防安全設備檢查，及停歇業場所未予列管等情事，經函請檢討改善，已完成建築物(場所)申報及加強停歇業場所之列管與追蹤，並訂定統一裁罰基準，保障民眾生命財產及維護公共安全。
        審計室指出，依建築法第77條第3項規定，供公眾使用之建築物，應由建築物所有權人、使用人定期委託中央主管建築機關認可之專業機構或人員檢查簽證，其檢查簽證結果應向當地主管建築機關申報；消防法第9條第1項規定，各類場所之管理權人，應定期檢修消防安全設備；其檢修結果，應依規定期限報請場所所在地主管機關審核，場所有歇業或停業之情形者，亦同。截至111年底止，縣政府及消防局列管應申報建築物公共安全及消防安全檢查之建築物或場所，計有6,547處及11,084處。
        然而，審計室於112年2月查核發現，列管項目中逾期未完成建築物公共安全申報者16處、漏未申報建築物公共安全者有10處、漏未申報消防安全設備檢查者有4處，又對於違反上述有關建築法之規定者，尚未訂定統一裁罰基準，另消防局對於停歇業場所及其使用現況尚無列管資料，管理作業有欠周妥，審計室遂於112年3月函請縣政府及消防局檢討改善。
        審計室表示，經追蹤改善情形，縣政府及消防局已督促所有權人或管理權人等依規定辦理申報，截至112年底止，上述30處逾期或漏未申報者均已完成申報審查作業；又停歇業場所經清查後，計有253處均已列管追蹤使用情形，保障民眾生命財產及維護公共安全。另縣政府已於112年7月17日訂定發布「宜蘭縣政府處理違反建築法使用管理規定事件統一裁罰基準」，完備制度規章。

        第2則 
        標題：宜蘭縣部分土地未依實際使用情形核課地價稅，審計機關促請改善
        內容： 
        宜蘭縣政府財政稅務局(下稱財稅局)辦理地價稅稅籍清查作業，經審計部臺灣省宜蘭縣審計室查核發現，部分課徵田賦或減免地價稅土地未依實際使用情形改課或恢復課徵地價稅，或非都市計畫公共設施保留地未按一般用地稅率核課地價稅等情事，經函請檢討改善，已釐正稅籍並依法改課或補徵地價稅1,216萬餘元，以維護租稅公平。
        審計室指出，財稅局為健全稅籍、確保稅源及遏止逃漏，以達到公平課稅、增裕庫收目標，每年度訂定地價稅稅籍及使用情形清查作業實施計畫，定期於1月1日起至9月30日止辦理課徵田賦土地、特別稅率用地及減免稅地之清查作業。
        然而，審計室於109年10月運用地理資訊系統(QGIS)與內政部國土測繪中心國土利用調查成果圖進行空間套疊分析查核發現，部分課徵田賦或減免地價稅土地，作為商業、混合使用住宅、製造業、倉儲、停車場等非供農業用途使用，或都市計畫公共設施保留地未按6‰核課地價稅，非屬公共設施保留地未按一般用地稅率核課，或已取得收益之國有土地，未依規定改課或恢復課徵地價稅等，核有短(溢)徵情事，審計室遂於109年12月函請財稅局積極檢討辦理。
        審計室表示，經追蹤改善情形，截至110年1月底止，財稅局已釐正稅籍並依法改課或補徵地價稅共計747筆、金額1,216萬餘元，退還稅款28筆、金額25萬餘元，財稅局將運用QGIS等資訊技術勾稽產出異常資料，列入爾後年度地價稅稅籍清查計畫辦理，以提升清查成效，維護租稅公平。
        
        第3則 
        標題：宜蘭縣五結防潮閘門改善工程一再流標，審計機關促請改善
        內容：
        宜蘭縣政府(下稱縣政府)辦理五結防潮閘門改善工程(下稱閘門改善工程)，經審計部臺灣省宜蘭縣審計室查核發現，縣政府未確認領標廠商未參與投標之原因，致工程發包作業遲未完成，經函請檢討改善，已洽詢原因並經調整招標文件內容後順利完成發包作業，有助閘門改善工程之進行。
        審計室指出，縣政府因冬山河排水系統之五結防潮閘門使用近50年，結構老舊水密性不佳，影響防洪禦潮功能須進行改建，於107年8月委託工程顧問公司辦理規劃設計工作，嗣於110年8月11日完成細部設計審查後，同年12月7日辦理閘門改善工程發包作業，預算金額10億1,283萬餘元，工期1,050日曆天，預定113年11月底完工。
        然而，審計室於111年3月查核發現，閘門改善工程因預算單價偏低，經檢討調整後仍因無廠商參與而流標3次，審計室遂於111年6月函請縣政府檢討妥處，經追蹤結果，縣政府雖已檢討招標文件內容，並調增工程預算為12億6,209萬元，惟因未確認領標廠商未投標之原因，截至112年3月底止，閘門改善工程已連續6次流標，工程發包作業遲未完成，乃於112年5月再函請縣政府積極研謀改善。
        審計室表示，經追蹤改善情形，縣政府已責請工程顧問公司洽詢領標廠商瞭解未參與投標之原因，並據以調整招標文件內容及工程預算單價，公開招標後則積極邀請潛在廠商參與，閘門改善工程已於112年9月13日決標，決標金額12億7,752萬餘元，預計116年6月完工，以確保防洪禦潮功能。

        請將下列的資料內容，仿照上面3則資訊發布的標題與架構內容規則，寫成1則資訊發布：
        
        資料內容如下：
[
{內容}
]
提醒，請注意：
1.簡化標題，標題文字僅簡要敘述查核發現缺失，審計機關促請改善
2.內容共分為4段論述，第1段精簡敘述全貌，要有行政機關作為，「審計部臺灣省宜蘭縣審計室查核發現」及「經函請檢討改善」，機關的改善成果。第2段要有「審計室指出」，說明行政機關相關作為。第3段要有「然而，審計室查核發現」，說明行政機關缺失，審計室函請改善。第4段要有「審計室表示，經追蹤改善情形」，行政機關改善成果。
3.盡量維持審計機關習慣的用語，不要改成白話文。
"'''
    copy(提問)

def 自檔案建置資訊發布提問(檔案路徑):
    from pathlib import Path
    建置資訊發布提問至剪貼簿(Path(檔案路徑).read_text(encoding='utf8'))

if __name__ == '__main__':
    import argparse
    import time
    import sys
    parser = argparse.ArgumentParser()
    parser.add_argument("--file2newsquery", help="自檔案建置資訊發布提問")
    args = parser.parse_args()
    if args.file2newsquery:
        自檔案建置資訊發布提問(args.file2newsquery)
        sys.exit()
    設定環境()
