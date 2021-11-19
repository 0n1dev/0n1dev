import feedparser, datetime

tistory_blog_uri="https://0n1dev.tistory.com" #Your blog address here
feed = feedparser.parse(tistory_blog_uri+"/rss")

markdown_text = """
## 소개
- 이름 : 신재원

## Favorite Skills
- Java
- Spring
- NodeJS
- Docker

## Study
- Kafka
- K8S
- RXJava

## Career
- Nexon Korea(2021.10.25 ~ )
  - 인텔리전스랩스 2021.10 ~ (Spring Boot, JPA, QueryDSL, AWS ...)
- AfreecaTV(2020.01.13 ~ 2021.10.22)
  - 광고 파트 2021.02 ~ (Spring Boot, Kafka Streams, K8S ...)
  - 전사 파트 2020.01 ~ 2021.01
  
## Activity
- F-LAB

![깃허브](https://github-readme-stats.vercel.app/api?username=0n1dev&show_icons=true)<br /> 
## Tistory Blog Posts
""" # list of blog posts will be appended here

lst = []


for i in feed['entries']:
    dt = datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%b %d, %Y")
    markdown_text += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
    print(i['link'], i['title'])

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
