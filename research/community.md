# 中英文 Home Assistant 社群現況：新手卡在哪、問什麼、後悔什麼

> 調查日 2026-10-14。只讀公開網頁（WebSearch／WebFetch／公開 JSON），沒有登入、沒有發文。
> 「（搜尋摘要）」＝原文被 403／反爬擋下，只讀到搜尋引擎摘要，可信度較低。發文者 ID 一律省略。
> 中國大陸社群的內容在 §5 另列，**台灣使用者不一定適用**。

## 0. 結論先講

1. **兩邊新手的第一題都是「用什麼硬體跑」**，答案在 2025–26 年收斂成兩條：官方成品盒 HA Green（官方「最簡單的開始方式」），或 N100 等級 x86 小主機（社群在要跑 Frigate、本地語音／LLM、會長大時的主流建議）。自己燒 SD 卡的 Raspberry Pi 兩邊都在勸退。
2. **英文圈最常後悔的是「家人受不了」和「沒保留實體開關」**；中文圈最常卡的是**米家／陸版設備的雲端與區域**，以及單火線開關。
3. **台灣特有的坑**：小米官方 HA 整合的雲端區域清單**沒有台灣**，穩定的本地控制要靠只在中國大陸販售的中樞網關（Wi-Fi 設備另有官方自己都不建議開的「局域網控制」）；陸版 220V 設備；台灣 Panasonic、日立等家電只有社群 HACS 整合。
4. **繁中語音是兩層不同的故事**：HA Assist 的 zh-TW 句庫覆蓋 95%（第 10 名，高於簡中與港中），但官方語言表的中文語音轉文字**只有 Home Assistant Cloud 一條官方支援**，本地 Whisper／Speech-to-Phrase 都標不支援；Voice PE 發表時不支援中文、官方喚醒詞只有英文。
5. **近一年 HA 官方明顯在降低新手門檻**：add-ons 改名 apps（2026.2，因為新手分不清 add-on 和 integration）、Core／Supervised 安裝方式移除（2025.12）、「進階模式」拿掉（2026.6）、開發者工具改名「工具」（2026.8）。==舊中文教學的介面用語已經對不上==。
6. **社群看不到的地方**：Reddit 整個擋自動讀取（403／400），本調查**沒有任何 Reddit 內容**；Mobile01、Dcard、知乎、瀚思彼岸只有搜尋摘要；PTT 沒有 HA 專門看板。

---

## 1. 新手最常問的 Top 10（中英合併）

排序是綜合判斷，**不是量測出來的頻率**；有數字的附取得方式。

| # | 問題 | 中文圈證據 | 英文圈證據 |
|---|---|---|---|
| 1 | **用什麼硬體跑 HA**（Pi、Green、NAS、舊電腦、N100、舊手機） | B 站搜「home assistant 新手」第一頁 42 支影片，至少 9 支標題是舊手機／玩客雲／機頂盒裝 HA（[搜尋頁](https://search.bilibili.com/all?keyword=home%20assistant%20%E6%96%B0%E6%89%8B)，2026-10-14 擷取）；[spacen 2025 入坑完全指南](https://spacen.io/ultimate-home-assistant-beginners-guide/)（2024-11-30）專節排序硬體 | [Which device should I choose…](https://community.home-assistant.io/t/which-device-should-i-choose-to-run-my-home-assistant-on/874317)（2025-04-06，4,543 次瀏覽）；[From Pi to Powerhouse: 2026 Mini PC Build](https://community.home-assistant.io/t/948147)（2025-11-06，21,298 次，安裝分類年度第 3）；[Beelink N100…](https://community.home-assistant.io/t/beelink-n100-mini-pc-and-home-assistant/826561)（11,023 次） |
| 2 | **安裝方式選哪個**（HA OS／Container），「為什麼我沒有 add-on」 | [Automata 安裝教學 RPi 篇](https://forum.automata.id/t/topic/145) 14,258 次瀏覽（[latest.json](https://forum.automata.id/latest.json)）；知乎「3 個原因放棄 Docker 版」（[連結](https://zhuanlan.zhihu.com/p/1908984989401485473)，搜尋摘要） | 官方[安裝頁](https://www.home-assistant.io/installation/)：「HA OS is the recommended installation type」，Container 沒有 apps；Core／Supervised 2025.12 [正式移除](https://www.home-assistant.io/blog/2025/12/03/release-202512/) |
| 3 | **米家／涂鴉等既有設備怎麼接** | B 站第一頁 4 支標題含「米家」；瀚思彼岸官方集成相關帖至少 9 個（[例](https://bbs.hassbian.com/thread-27895-1-1.html)，搜尋摘要） | analytics：tuya 整合 29.5%、localtuya 6.0%、xiaomi_miot 3.9%、xiaomi_home 3.5%（§6） |
| 4 | **Zigbee 怎麼開始**（ZHA 還是 Z2M、選哪支協調器、配不進去） | [FB 社團](https://www.facebook.com/groups/151166072456061/)首頁唯一可見貼文就是「Tuya 燈在 Zigbee2MQTT 找不到」；[Automata Z2M 教學](https://forum.automata.id/t/topic/216) | [ZHA vs Zigbee2Mqtt – which is the most stable?](https://community.home-assistant.io/t/zha-vs-zigbee2mqtt-which-is-the-most-stable/517106)（2023，126,949 次，至今仍是常青帖） |
| 5 | **第一批該買什麼、選哪個協定** | spacen 指南把採購管道列為 HA 官網、蝦皮、淘寶 | [Best devices for HA to start with](https://community.home-assistant.io/t/best-devices-for-ha-to-start-with/822051)（2025-01-04，24,810 次）：最高回覆是「先選一個主要協定再圍繞它買」 |
| 6 | **遠端連線**（DDNS、HTTPS、Cloudflare Tunnel、Tailscale、Nabu Casa） | [spacen Cloudflare Tunnel](https://spacen.io/home-assistant-cloudflare-tunnel-remote-control/)（2026-05-02）；Dcard 教學（[連結](https://www.dcard.tw/f/smart_home/p/231974287)，403） | [Tailscale Funnel 教學帖](https://community.home-assistant.io/t/950072)（2025-11-11，20,338 次）；[Managing HA from outside the house](https://community.home-assistant.io/t/964508)（2025-12-20） |
| 7 | **接回 Apple HomeKit／Siri、Google Home** | [PTT iOS 版搜「homeassistant」](https://www.ptt.cc/bbs/iOS/search?q=homeassistant) 3 篇中 1 篇是 HomeKit 疑問；B 站「HA 把米家接入 HomeKit」7.7 萬播放；[spacen 接 Google Home 不用 Nabu Casa](https://spacen.io/home-assistant-connect-google-home-without-nabu-casa/)（2026-05-05） | Smart Home Junkie 近期影片「Control Home Assistant with Google Home, Alexa, or Apple Home via Matter」（YouTube 標題） |
| 8 | **Matter／Thread 配對失敗、邊界路由器** | 台灣沒找到長期實測文；pj-worklife 用 Matter 把 Aqara 網關橋接進 HA（[文](https://www.pj-worklife.com.tw/aqara-zigbee-smart-home-experience/)，2025-12-20） | [Thread Border Router recommendations](https://community.home-assistant.io/t/976756)（2026-01-19，13,458 次）；[Unable to pair IKEA Matter devices](https://community.home-assistant.io/t/976399)（9,158 次，第一個建議是打開 IPv6）；IKEA 21 款 Matter-over-Thread [公告帖](https://community.home-assistant.io/t/948187) 49,546 次、硬體分類年度第 1 |
| 9 | **在家判斷、人體感測誤判；自動化怎麼寫** | B 站第一頁 3 支講「在家判斷」；[PTT 問卦](https://www.pttweb.cc/bbs/Gossiping/M.1750909062.A.911)（2025-06-26）留言提到 presence 常誤判 | Month of WTH 2024：[WTH is it this complicated to send a notification?](https://community.home-assistant.io/t/802547)（533 票，第 2 高）；[WTH Do I still need to be a rocket scientist…](https://community.home-assistant.io/t/809898)（756 讚） |
| 10 | **語音：能不能取代 Google／Alexa、中文 TTS** | [Automata](https://forum.automata.id/latest.json) 最新 30 篇裡 3 篇談 TTS；Edge TTS 在 HA 2026.10 後失效（[#933](https://forum.automata.id/t/topic/933)，2026-10-13）；spacen 作者說內建助理語音控制成功率「不到 1%」，改接 ChatGPT／Gemini（[文](https://spacen.io/empower-home-assistant-with-chatgpt-and-gemini/)，2024-08-10） | [My Journey to a reliable… locally hosted voice assistant](https://community.home-assistant.io/t/944860)（2025-10-27，89,467 次，語音分類年度第 1） |

次要但常見：「HA 值不值得、門檻多高」（[PTT 2025-02-15](https://www.pttweb.cc/bbs/Gossiping/M.1739606366.A.8B4)、[2025-06-26](https://www.pttweb.cc/bbs/Gossiping/M.1750909062.A.911) 兩篇問卦，留言都在吵門檻；[Why is HA so difficult to set-up?](https://community.home-assistant.io/t/953326) 2025-11-20，144 則回覆，前幾則都懷疑是 DHCP IP 變動）、「更新後壞了怎麼回滾」（[2025.12.0 rollback](https://community.home-assistant.io/t/958651)，8,835 次）、「add-on 和 integration 差在哪」（見 §4）。

英文論壇反覆出現的一句建議：「**先把 HA 架起來，再只買確定能用的設備**」（[What do you wish you knew…](https://community.home-assistant.io/t/starting-out-what-do-you-wish-you-knew-when-you-began-your-smart-home-journey/1012810)，2026-06-15，#9 回覆）。

---

## 2. 常見後悔與踩坑

英文主要來源是論壇 wiki 帖 [20 things I wished I knew when I started with Home Assistant](https://community.home-assistant.io/t/20-things-i-wished-i-knew-when-i-started-with-home-assistant/576359)（2023-05-29 建，作者 2025-04-15 最後更新；2026-10-14 為 135,949 次瀏覽、331 讚），下稱 **[20T]**。

| 坑 | 中文圈 | 英文圈 |
|---|---|---|
| **SD 卡壞、Pi 效能不夠** | Automata 安裝教學警告低效能記憶卡會「寫入錯誤、系統當機」，建議 A2 以上、最好 SSD（[#145](https://forum.automata.id/t/topic/145)） | [20T]：「don't rely on an SDCard which WILL corrupt over time」；裝多個 add-on「started to cripple my raspberry pi4」。官方 2025.11 不再把 HA OS log 寫進設定資料夾，理由之一是減少 SD 卡磨耗（[2025.11](https://www.home-assistant.io/blog/2025/11/05/release-202511/)） |
| **安裝方式選錯，沒有 add-on** | spacen：「Container 與 Core 不支援附加元件，也沒有一鍵更新」 | [20T] 建議 HA OS；Container 使用者回報更新失敗（[2026.3 Container Update Fails](https://community.home-assistant.io/t/993151)） |
| **雲端依賴** | 小米官方整合：本地控制要「中樞網關」，中樞網關「僅在中國大陸可用」，其他地區指令都經小米雲；token 明文存在 HA 設定檔（[ha_xiaomi_home README_zh](https://github.com/XiaoMi/ha_xiaomi_home/blob/main/doc/README_zh.md)）。涂鴉本地整合仍要先從雲端拿 local key，韌體更新後可能失效（[tuya-local](https://github.com/make-all/tuya-local)，搜尋摘要） | [20T]：只買有 API 或 HA 支援的產品；[Tado 限制 API 呼叫次數](https://community.home-assistant.io/t/928751)（2025-09-08）；[Done with Ring…](https://community.home-assistant.io/t/942271)；Matter 也有爭議：[Do Matter "owners" mind the integrated "kill switch"?](https://community.home-assistant.io/t/942167)（憑證撤銷） |
| **陸版／國際版鎖區** | PTT 留言：Aqara 分中國版與國際版，「未來可能會禁止國際版用戶新增中國版的配件」——這是留言者的預測，未證實（[PTT E-appliance](https://www.ptt.cc/bbs/E-appliance/M.1724310414.A.510.html)，2024-08-22）；配對陸版 Aqara 要把 App 地區設成中國大陸，但可能搜不到部分國際版產品（[pj-worklife](https://www.pj-worklife.com.tw/aqara-zigbee-smart-home-experience/)） | — |
| **Zigbee 設備只能加入一個網路** | 已配對 Aqara 網關的子設備不能直接加入 HA 協調器；Zigbee 與 Thread 的 mesh 不能互相中繼（[pj-worklife](https://www.pj-worklife.com.tw/aqara-zigbee-smart-home-experience/)） | — |
| **Zigbee 訊號干擾** | 中文圈沒找到量化抱怨文 | 官方 [ZHA 文件](https://www.home-assistant.io/integrations/zha)：用長 USB 延長線、遠離 USB 3.0、頻道用 15／20／25；ZBT-2 因此附 1.5 m 線；社群 [Zigbee network optimization](https://community.home-assistant.io/t/515752) 199,689 次 |
| **Wi-Fi 設備太多、路由器太爛** | PTT：多數 HomeKit「無回應」是升級路由器後解決，ISP 附的路由器常卡（[PTT E-appliance](https://www.ptt.cc/bbs/E-appliance/M.1724310414.A.510.html)） | [20T]：優先 Zigbee／Z-Wave，別讓 Wi-Fi 設備塞爆網路；IoT 放獨立網段；別用 ISP 路由器當主 AP |
| **單火線、沒有零線** | spacen：單火開關可能讓燈具「鬼火閃爍」；PTT：單火讓 LED 微亮；少數派作者先買開關才發現開關盒沒有零線（[sspai 95234](https://sspai.com/post/95234)，2025-01-02） | — |
| **家人不買帳、自動化太多** | PTT Digitalhome 心得：「理想很豐滿，可現實很骨感」，建議保留實體開關和遙控器（[文](https://www.pttweb.cc/bbs/Digitalhome/M.1737768680.A.297)，2025-01-25）；新鮮感過後裝置離線很難排查（[PTT 問卦](https://www.pttweb.cc/bbs/Gossiping/M.1750909062.A.911)） | [20T] 有一節「Home Approval Factor」：「If your partner (or kids) just get pissed once at automation, it could become a deal breaker」；作者把自動化從 150 條砍到 88 條；ZHA vs Z2M 帖主說家人「asked for regular lights back」 |
| **沒保留實體開關** | 同上 | [20T]：「Keep a physical button… if your HA is down… they don't feel trapped」 |
| **備份** | — | [20T]：「Backup on a different location than you host machine」「Update confidently, but backup often」 |
| **HACS 裝太多** | 大陸：HACS 授權、GitHub 限流（見 §5） | [20T]：「like a toddler in a candy store… 20 javascripts… crushed my mobile APP」；analytics：71.5% 的安裝有 HACS |
| **自動化用 device_id** | — | [What do you wish you knew…](https://community.home-assistant.io/t/1012810) #4 回覆：「the most important that you'll regret when it is too late」 |
| **花費膨脹** | PTT：海外買智慧家電帶回台灣，加進口費用反而更貴（[PTT 2025-02-15](https://www.pttweb.cc/bbs/Gossiping/M.1739606366.A.8B4)） | 同帖 #8：「I wish that I knew just how much this 'hobby' was going to cost me」，但同一人說漏水自動關閥省了好幾千 |
| **不要先買硬體** | 少數派新手建議先用舊電腦或虛擬機試（[sspai 105542](https://sspai.com/post/105542)，2026-01-25） | 「Set up Home Assistant first, then buy only devices that you know will work」（1012810 #9） |
| **更新造成的破壞性變更** | 舊中文教學的「附加元件」字樣已對不上 2026.2 後的介面 | 舊版 template 語法 2025.12 棄用、2026.6 移除，[棄用說明帖](https://community.home-assistant.io/t/955562) 70,391 次、1,430 則回覆（設定分類年度第 1） |

---

## 3. 台灣在地議題

### 電壓、插頭、陸版設備
- unbox.tw 的米家可用性清單說陸版產品「大部份在台灣都可以使用(99%)」，但 220V 產品「不支援寬電壓」、還有插頭問題；留言：「高瓦數建議 220v 使用，110v 可能連開機都不行」（[unbox.tw](https://www.unbox.tw/midevicelist)，清單 2021-01-07 更新）。
- PTT 留言轉述廠商說法：Yeelight 燈具「都是 220V 規格」，要請水電改線（[PTT E-appliance](https://www.ptt.cc/bbs/E-appliance/M.1724310414.A.510.html)，2024-08-29 留言）。

### 米家與伺服器區域
- 米家 App 本身不分陸版台版，差別在連哪個伺服器區域；陸版設備要把地區設成「大陸」（[unbox.tw](https://www.unbox.tw/midevicelist)）。
- 小米官方 HA 整合的雲端只有 6 區（中國大陸、歐洲、印度、俄羅斯、新加坡、美國），**沒有台灣**（[README_zh](https://github.com/XiaoMi/ha_xiaomi_home/blob/main/doc/README_zh.md)）；該 repo issue 搜「Taiwan」0 筆（2026-10-14）。台灣帳號該選哪一區，**沒找到官方說明**。
- **補充（主 agent 抽查時讀到）**：同一份 README 另寫「小米局域網控制功能不受地區限制，在全球範圍內均可用」，但只能控制同一區網內的 IP 設備（Wi-Fi、網路線），**不能控制藍牙 Mesh、Zigbee 設備**，而且官方原文是「該功能可能會引起一些異常，我們建議不要使用該功能」。所以台灣使用者的米家 Wi-Fi 設備有一條不穩定的本地路線，藍牙／Zigbee 子設備沒有。
- 2022 年的舊 blog 說當時只能用 IP＋token 接入（[alvinchen.club](https://www.alvinchen.club/2022/01/19/%E6%99%BA%E6%85%A7%E5%AE%B6%E5%BA%AD%E7%AC%AC%E4%B8%89%E6%AD%A5-home-assistant-%E6%8E%A5%E5%85%A5%E5%B0%8F%E7%B1%B3%E7%B3%BB%E7%B5%B1-xiaomi-miot/)，搜尋摘要）。

### NCC、取得管道
- 台灣正式販售的米家智慧插座有 NCC 字號；陸版設備在台灣使用是否合規，**沒找到明確答案**。
- HA Green 在台灣電商約 NT$4,500–5,600（[飛比比價](https://feebee.com.tw/all/home%20assistant/)，2025-09 頁，搜尋摘要）；spacen 2024-11 寫約 NT$3,000。==價格會變，skill 不收錄==。
- 蝦皮／淘寶集運買 Zigbee 協調器的經驗文：**沒找到**。

### 租屋
- 只找到導購型文章與 Dcard 一篇（[連結](https://www.dcard.tw/f/smart_home/p/239715049)，403）。**沒找到**租屋族用 HA 的實質討論——這是 skill 要自己補的空白。

### 台灣品牌與在地整合（只列查到的）
- Panasonic 台灣家電：社群 HACS 整合 [osk2/panasonic_smart_app](https://github.com/osk2/panasonic_smart_app)、[tsunglung/panasonic_ems2](https://github.com/tsunglung/panasonic_ems2)、[Austinsuyoyo/panasonic_iot_tw](https://github.com/Austinsuyoyo/panasonic_iot_tw)。
- 日立冷氣：依控制 App 而定，「日立雲端智慧控」要用 Hitachi_smart_app（[davidou blog](https://blog.davidou.org/archives/1883)，搜尋摘要）。
- 中央氣象署：[tsunglung/OpenCWB](https://github.com/tsunglung/OpenCWB/blob/master/README_zh-tw.md)。
- Gorgeous、歐瑞博、Sunplus 與 HA 的關係：**沒查到**。綠銀、VIZO 只出現在導購文，HA 相容性**未驗證**。

### 台電智慧電表（AMI）
- 非官方 `taipower-ha`，底層 [libtaipower](https://pypi.org/project/libtaipower)，文件說支援 AMI 15 分／時／日／月資料；GitHub README **沒讀到**、安裝狀態未確認。另有 [Taipower 雙月電費計算](https://github.com/cnstudio/Taipower-Bimonthly-Energy-Cost-homeassistant)。
- Mobile01 討論：裝了 AMI 不代表馬上能查 15 分鐘資料（[t=6289402](https://www.mobile01.com/topicdetail.php?f=168&t=6289402&p=2)，搜尋摘要）。
- DIY 派用 PZEM-004T 或 ESPHome 自己量（[Automata #255](https://forum.automata.id/t/topic/255)，10,803 次瀏覽）。

### 繁中語音
- **意圖句庫**：zh-TW 必要組合 100%（6/6）、全部組合 95%（211/222），第 10 名，高於 zh-CN（85%）、zh-HK（57%）（[OHF intents 進度](https://ohf-voice.github.io/intents/)，2026-10-14）。sentences 檔案數 zh-TW 42、en 43，zh-TW 最後更新 2026-09-17。
- **語音轉文字／合成**：官方 [`languages.yaml`](https://github.com/home-assistant/intents/blob/main/languages.yaml)（2026-10-14）對 zh-TW：speech-to-phrase false、whisper false、cloud STT **true**、piper false、cloud TTS true。也就是官方認可的繁中語音轉文字只有 Home Assistant Cloud；本地 Whisper 標不支援（這是專案的品質評等，不代表 Whisper 模型完全不能轉中文——此為推論）。Piper 只有 zh-CN 有本地聲音。
- [Speech-to-Phrase](https://github.com/OHF-Voice/speech-to-phrase) v1.4.3 支援 21 種語言，沒有中文。
- **Voice PE**：CNX Software 報導發表時「Chinese (Mandarin) are not supported at all on the device」（[2024-12-20](https://www.cnx-software.com/2024/12/20/59-voice-preview-edition-adds-an-offline-smart-speaker-to-your-home-assistant-server/)）；官方喚醒詞只有英文。台灣經銷與中文開箱：**沒找到**。
- [Voice Chapter 11](https://www.home-assistant.io/blog/2025/10/22/voice-chapter-11/)（2025-10-22）：每個衛星最多兩個喚醒詞、各接一條 pipeline，可做雙語家庭；沒提中文。
- 台灣玩家常用 Edge TTS（自訂元件），HA 2026.10 後因 Edge 改驗證而失效（[Automata #933](https://forum.automata.id/t/topic/933)）。
- Google Gemini for Home 到 2026-07-27 台灣不在開放國家內（[adersaytech](https://adersaytech.com/ai-tutorial/gemini-for-home-15min-memory.html)，搜尋摘要）。HomePod 台灣中文現況：**沒查**。

---

## 4. 近一年趨勢（2025-10 ～ 2026-10）

### HA 官方在降門檻（官方 release notes）
- [2025.12](https://www.home-assistant.io/blog/2025/12/03/release-202512/)：Core／Supervised 與 32-bit 完全移除；用途導向的觸發（「當燈打開」）。
- [2026.2](https://www.home-assistant.io/blog/2026/02/04/release-20262/)：**add-ons 改名 apps**（提案帖說新手「attempt to install add-ons when they need integrations」，[945712](https://community.home-assistant.io/t/945712)，470 讚）；新的 Home 儀表板成為新安裝預設。
- [2026.6](https://www.home-assistant.io/blog/2026/06/03/release-20266/)：拿掉「進階模式」開關；OTBR（Thread 1.4）預設開啟。
- [2026.7](https://www.home-assistant.io/blog/2026/07/01/release-20267/)：用途導向觸發成為預設；「Update all」。
- [2026.8](https://www.home-assistant.io/blog/2026/08/05/release-20268/)：新安裝網址不用再加 port；「開發者工具」改名「工具」；內建 LiteLLM、llama.cpp 對話代理。
- [2026.10](https://www.home-assistant.io/blog/2026/10/07/release-202610/)：AI 設定頁一鍵開 MCP server；Home Assistant Cloud 將於 2026.12 改名 **Home Assistant Link**（[2026-10-02](https://www.home-assistant.io/blog/2026/10/02/big-tech-ruined-the-cloud-so-were-renaming-ours/)）。
- OHF 在 [State of the Open Home 2026](https://www.home-assistant.io/blog/2026/01/20/state-of-the-open-home-2026/)（2026-04-08）的說法是「lowering the floor without lowering the ceiling」（[OHF newsletter](https://newsletter.openhomefoundation.org/building-an-open-future-for-everyone/)）。

### 硬體
- HA Yellow 2025-10 停產，官方推薦的簡單起點是 Green（[Yellow EOL](https://www.home-assistant.io/blog/2025/10/15/yellow-end-of-life/)）。
- [Connect ZBT-2](https://www.home-assistant.io/blog/2025/11/19/home-assistant-connect-zbt-2)（2025-11-19）：Zigbee **或** Thread 一次只能跑一種；ZBT-1 停產。
- N100 小主機是英文社群在要跑 Frigate／本地語音／會長大時的常見建議；中國大陸主流是舊手機、玩客雲、N100＋PVE。

### Matter／Thread
- HA 官方：「Matter now runs in 38% of Home Assistant instances」，Matter Server 9.0 支援 Matter 1.5.1、Thread 1.4，預設不再允許未認證／測試憑證的設備（[2026-06-23](https://www.home-assistant.io/blog/2026/06/23/the-matter-upgrade-youve-been-waiting-for/)）。
- IKEA 大量推出 Matter-over-Thread 產品，帶動論壇的配對問題（見 §1 #8）。
- 中國：少數派說在國內做全屋 Matter 是「苦修」——國標開關沒有 Matter 款、單火沒方案（[sspai 108005](https://sspai.com/post/108005)）。

### LLM 整合
- HA 官方路線：AI 可選、本地或雲端；「Assist will handle commands first」，只有內建句型解不了的才交給 LLM；HA 可當 MCP server（[2025-09-11](https://www.home-assistant.io/blog/2025/09/11/ai-in-home-assistant/)）。
- 用 coding agent 管 HA：少數派作者用 Claude Code 透過 HA API 寫腳本、設計自動化（[sspai 106992](https://sspai.com/post/106992)，2026-03-18）；B 站「AI 救活了我吃灰兩年的 Home Assistant」7.3 萬播放。英文論壇老手則對「靠 ChatGPT／Copilot 架設」持保留（[964508](https://community.home-assistant.io/t/964508)、[979608](https://community.home-assistant.io/t/979608)）。
- 台灣 2025-10 之後的 LLM＋HA 實作文：**沒找到**。

### YouTube（只看標題）
- 五個主要英文頻道（Everything Smart Home、Smart Home Junkie、Paul Hibbert、Home Automation Guy、BeardedTinker）最近約 30 支影片裡都**沒有新的新手教學**；最新的新手向內容是 Paul Hibbert 約一年前的「Home Assistant Setup Guide – No Raspberry Pi」「Starting A Smart Home In 2025 Is HELL」。新手教學的空窗也是這個 skill 的機會。

---

## 5. 中國大陸社群（地區差異，台灣不一定適用）

- **網路環境**：HACS 的 GitHub 授權、raw.githubusercontent 存取、加載項商店載入失敗是瀚思彼岸長年熱門題；解法有 hosts、HACS 極速版、Gitee 上的 [hacs-china](https://gitee.com/hacs-china)（[瀚思彼岸 22072](https://bbs.hassbian.com/thread-22072-1-1.html)，搜尋摘要）。台灣直連 GitHub，**不需要**。
- **小米官方整合**：中樞網關只在大陸賣，「斷網本地控制」只有大陸區帳號做得到；HA 所在區網有中樞網關時區網控制不生效（[瀚思彼岸 27895](https://bbs.hassbian.com/thread-27895-1-1.html)，搜尋摘要）。
- **在地分支**：OHF 創辦人受訪說國內用戶要「借助特殊方式或者魔改過的本土分支」才能安裝和更新（[sspai 110086](https://sspai.com/post/110086)，2026-05-26）；瀚思彼岸有「冬瓜 HA」專區。
- **國產 LLM**：DeepSeek、通義接 HA（Extended OpenAI Conversation、[deepseek_conversation](https://github.com/leofleischmann/Homeassistant-Deepseek-Integration)）。
- 國家電網／南方電網用電整合（[例](https://github.com/CubicPill/china_southern_power_grid_stat)）。
- 量級：瀚思彼岸「求助」分類至少 277 頁；B 站搜「home assistant 新手」第一頁 42 支影片——中文 HA 內容以大陸為大宗，台灣新手搜到的教學很可能是大陸環境，要注意 §5 的差異。

---

## 6. HA 官方 analytics（opt-in，僅參考）

來源：[analytics.home-assistant.io](https://analytics.home-assistant.io/) 的 `data.json`／`addons.json`／`custom_integrations.json`，2026-10-14 下載，`last_updated` 2026-10-13 12:55 UTC。網站自己說 opt-in 的「less than a fourth of all Home Assistant users」。

- 總數 700,537 個安裝；平均 14 條自動化、29 個整合、401 個實體。
- 安裝方式：HA OS 79.7%、Container 17.5%、Supervised 1.1%、Core 1.0%。
- HA OS 的主機板（分母 466,039）：虛擬機 31.3%、x86-64 19.2%、Pi 4 16.6%、**Green 16.5%**、Pi 5 10.0%、Yellow 2.0%。
- 整合（分母 555,312）：matter 41.0%、tuya 29.5%、cloud（Nabu Casa）29.0%、zha 25.6%、mcp_server 5.5%、connect_zbt2 5.1%、ollama 2.3%。
- HACS 71.5%；apps：Zigbee2MQTT 25.7%、Whisper 7.9%、Piper 9.2%、Speech-to-Phrase 3.0%。
- ZHA（142,346）與 Z2M app（約 110.7k）分母不同，**不能直接比**。
- 國家：DE 135,009、US 119,073、CN 25,321、**TW 3,699**、HK 2,182。

---

## 看不到／沒找到

| 來源 | 狀況 |
|---|---|
| Reddit（r/homeassistant、r/smarthome） | **完全看不到**：WebFetch 拒絕、WebSearch 限定 reddit.com 回 400、curl `search.json` 回 403。本文沒有任何 Reddit 內容；要的話得用登入的瀏覽器人工看 |
| FB「Taiwan Home Assistant 同好交流」 | 部分可見：about 頁讀得到（公開社團、約 34,176 人、2019-02-17 建立），首頁只看到 1 篇貼文，無法做主題統計 |
| PTT | `Smart_Home`、`DIY` 版搜尋網址回 404；iOS 版 HA 相關 3–5 篇，全是 2017–2021；近一年討論散在 Gossiping、E-appliance、Digitalhome |
| Mobile01、Dcard、知乎 | 403，只有搜尋摘要 |
| 瀚思彼岸 | HTTP 567（反爬），只有搜尋摘要 |
| 巴哈姆特 | 搜不到 HA 心得文 |
| iThome | 2025–2026 沒有 HA 報導 |
| B 站 | 搜尋頁可讀，影片內容沒看 |
| Month of WTH | 最後一屆是 2024 年 11–12 月，調查期間沒有新一屆 |
| State of the Open Home 2026 | 只讀到活動公告與 OHF 電子報摘要，沒有演講內容與數字 |
| 沒找到的內容 | 陸版設備的 NCC 合規說法；蝦皮／淘寶買協調器經驗文；租屋族用 HA 的實質討論；台灣 Voice PE 經銷；台灣近一年 LLM＋HA 實作；HomePod 台灣中文現況；`taipower-ha` README；HACS 大規模故障事件 |

## 抽查

調查 agent 在各自報告裡回原始連結重讀（共 7 處，全部一致）：OHF intents 進度頁（zh-TW 95%、第 10）、PTT E-appliance 回文（Yeelight 220V、Aqara 版本那句是預測）、HA 2026.2（add-ons 改名 apps）、FB 社團 about 頁、論壇 945712（frenck 提案）、HA 2026.8（網址不加 port、工具改名、LiteLLM／llama.cpp）、HA 2025.12（Core／Supervised 移除）。

彙整時主 agent 另外抽 3 項回原始來源重查（2026-10-14）：

1. **zh-TW 語音支援旗標**：重抓 `OHF-Voice/intents` 的 `languages.yaml`，zh-TW 為 speech-to-phrase false、whisper false、cloud true；piper false、cloud TTS true。**一致**。
2. **小米官方整合區域與中樞網關**：重抓 `ha_xiaomi_home/doc/README_zh.md`，「小米中枢网关仅在中国大陆可用」、雲端六區（中國大陸、歐洲、印度、俄羅斯、新加坡、美國），**一致**；但同段另有「局域網控制不受地區限制」的但書，調查 agent 漏寫，已補進 §3。
3. **analytics**：重抓 `data.json`，總數 700,542（調查時 700,537，資料日更）、TW 3,698（調查時 3,699）、Green 76,827／16.5%。**一致**（差異是每日更新）。
