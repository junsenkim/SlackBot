import os, json, datetime as dt
import requests

WEBHOOK = os.environ["SLACK_WEBHOOK_URL"]

def build_blocks():
    # TODO: 여기에 기업마당/SBA/K-Startup/캠퍼스타운/창업진흥원 크롤/수집 결과를 넣어 표 형태로 만들면 됨
    # Slack 표는 mrkdwn으로 구현(고정폭 폰트) 또는 Block Kit section 필드로 구성
    today = dt.datetime.now(dt.timezone(dt.timedelta(hours=9))).strftime("%Y-%m-%d")
    text = (
        f"*예비창업자 공고 브리핑* ({today} 09:00 KST)\n"
        "```"
        "상태 | 기관 | 공고명 | 마감\n"
        "-----|------|--------|-----\n"
        "**마감임박** | 예시 | 예시 공고 | 02-08 23:59\n"
        "```"
        "\n(지원 링크는 각 행에 함께 표기)"
    )
    return [
        {"type": "section", "text": {"type": "mrkdwn", "text": text}}
    ]

payload = {"blocks": build_blocks()}
r = requests.post(WEBHOOK, data=json.dumps(payload), headers={"Content-Type":"application/json"})
r.raise_for_status()
