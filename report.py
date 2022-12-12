import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import altair as alt
import plotly.graph_objects as go

st.title("제21대 국회의원 발의 법률안 키워드 분석")
st.write("최종 편집일: 2022.12.15.")
st.write("데이터저널리즘 7조: 김정우, 신유진, 안범영, 유창민")

# 국회 이미지
url = 'https://www.assembly.go.kr/cmmn/file/imageSrc.do?fileStreCours=829f7616fd59d611d6ee0bd750a47a6a&streFileNm=c4898d8acfe52e943d8691202e8e2fd5db110d2cdf90c86ad45263107332adc5'
st.image(url)

st.info(
"""
21대 국회에서 의원들은 어떤 발의안을 내놓았을까요? 

정당, 연령, 트렌드를 중심으로 법률안 키워드를 분석해보았습니다.
""")
st.markdown(
"""
* 목차
	* Ⅰ. (서론 제목)
	* Ⅱ. 국회와 사회의 트랜드 비교
	* Ⅲ. 국회의원 소속 정당 및 연령별 분석
	* Ⅳ. 결론
""")

st.header("Ⅰ. (서론 제목)")
st.markdown(
"""
**(이러쿵 저러쿵)**
"""
)


st.header("Ⅱ. 국회와 사회의 트랜드 비교")
st.subheader("1) (가제)국회 트랜드")
st.markdown(
"""
**(이러쿵 저러쿵)**
"""
)

st.subheader("2) 보수·진보 언론사별 사회 트랜드")

st.markdown(
"""
**(배경 + 분석 과정에 대한 간단한 설명)**
"""
)

option2 = st.selectbox('언론별 결과를 확인할 위원회를 선택하세요.', ('국회운영위원회', '법제사법위원회', '정무위원회', '기획재정위원회' , '교육위원회' , '과학기술정보방송통신위원회', '외교통일위원회' , '국방위원회' , '행정안전위원회' , '문화체육관광위원회', '농림축산식품해양수산위원회' , '산업통상자원중소벤처기업위원회' , '보건복지위원회' ,'환경노동위원회' , '국토교통위원회' , '정보위원회' , '여성가족위원회'))

press = {
    '국회운영위원회' : '분석 내용 : 보수 매체에서 윤석열 대통령을 국회 운영과 관련 짓는 경우가 유의미하게 높게 나타났다. 보수 매체에서는 most_common 2위(4876)인 반면, 진보 매체에서는 most_common 30위(142)에 그쳤다.', 
    '법제사법위원회' : '분석 내용 : ‘서울’ 키워드의 언급 빈도가 양 매체 모두 가장 많이 나타난 키워드이다. 21대 전반기 동안 핵심적인 키워드가 ‘수사’, 법무부‘, ’지검‘, ’경찰청‘ 등 양 매체가 모두 유사한 주제에 대해 보도했다.', 
    '정무위원회' : '분석 내용 : ‘코로나’ 키워드의 언급 빈도가 양 매체에서 모두 많이 나타났다. 보수 매체는 투자(3위-139)/미국(4위-129)에 대한 언급 빈도가 더 높았던 반면, 진보 매체는 두 키워드가 각각 10위, 9위로 상대적으로 적었다. 반면, 진보 매체가 **(내용 잘림)**', 
    '기획재정위원회' : '분석 내용 : 진보 매체에서 보수 매체에 비해 기본소득 주목 정도가 훨씬 높았다.', 
    '교육위원회' : '분석 내용 : 교육위원회에 관해서도 타 위원회에 비해 양 매체 모두 코로나 언급 수준이 유의미하게 높았다.(모두 1위) 양 매체 모두 ‘온라인’ 키워드도 두드러졌다.(온라인 수업과 관련된 것으로 사료됨.) 진보 매체에서 훨씬 높은 빈도로 ‘교육청(1위-740)’을 언급했다.(보수 매체는 6위-439).', 
    '과학기술정보방송통신위원회' : '분석 내용 : 두 매체 간의 차이가 적게 나타났다.', 
    '외교통일위원회' : '분석 내용 : ‘한국’, ‘중국’, ‘미국’ 세 키워드가 두드러지게 많이 나왔다.', 
    '국방위원회' : '분석 내용 : 진보 매체에서 ‘피해자’에 대한 언급 빈도가 더 높게 나타났다.(진보 매체는 6위, 보수 매체는 26위에 그침.)', 
    '행정안전위원회' : '분석 내용 : 두 매체 간의 차이가 적게 나타났다.', 
    '문화체육관광위원회' : '분석 내용 : 두 매체 간의 차이가 적게 나타났다.', 
    '농림축산식품해양수산위원회' : '분석 내용 : 두 매체 모두 ‘반려동물’로서 동물을 인식하는 사회의 모습을 보여주었다. 이외에도 ‘동물학대’, ‘동물권’ 등을 단어를 확인할 수 있다.', 
    '산업통상자원중소벤처기업위원회' : '분석 내용 : 보수 매체는 상위 30위 키워드 안에 ‘중소기업’ 이 없는데 반해, 진보 매체는 16위로 175번 언급되었다.', 
    '보건복지위원회' : '분석 내용 : 두 매체 간의 차이가 적게 나타났다. 두 매체 모두 ‘코로나’에 대한 언급 빈도(두 매체 모두 1위)가 매우 높았다.',
    '환경노동위원회' : '분석 내용 : 두 매체 모두 ‘노동자’에 주목하고 있다. 그러나 진보 매체는 ‘노동부’(5위-421)를 훨씬 많이 언급하고 있는 반면, 보수 매체는 10위(125)에 그쳤다. 보수 매체는 대신 일자리(4위-221) 언급 빈도가 더 높다(진보 매체 12위).', 
    '국토교통위원회' : '분석 내용 : 핵심 키워드로 ‘서울’과 ‘부동산’, ‘임대’, ‘공공’ 등 문재인 정부의 부동산 정책과 관련된 키워드가 많이 나타났다.', 
    '정보위원회' : '분석 내용 : 두 매체 간의 차이가 적게 나타났다. 핵심 키워드는 ‘서울, 코로나, 미국’ 등이다. 보수 매체에서는 부동산이 상위 언급 11위 키워드였음에도 불구하고, 진보 매체에서는 상위 30위 내에 나타나지 않았다. 보수 매체의 부동산 언급 빈도가 전반적으로 높았다.', 
    '여성가족위원회' : '분석 내용 : 보수 매체에서 ‘경찰’ 키워드의 언급 빈도가 유의미하게 높게 나타났다. 피해자, 코로나, 서울이 양 매체의 핵심 키워드이다.'}

st.write('여기에 각 위원회에 관련된 자료(ex. table, 워드클라우드, 도표)')
st.info(press[option2])

st.markdown(
"""
전반적으로 어느 분야건 코로나와의 관련성이 두드러지게 나타났다. 지역적으로는 대부분 서울 지역에 논의가 집중되고 있다.

**(결과 분석 내용)**
"""
)


st.header("Ⅲ. 국회의원 소속 정당 및 연령별 분석")
st.subheader("1) 제21대 국회의원 인적 구성")

# '이름','나이','성별','소속 정당','소속 위원회'
df = pd.read_csv('members.csv')
members = df.values.tolist()

democrtic = []
peoplepower = []
justice = []

for i in members:
	if (i[3] == "더불어민주당"):
		democrtic.append(i[1])
	elif (i[3] == "국민의힘"):
		peoplepower.append(i[1])
	elif (i[3] == "정의당"):
		justice.append(i[1])

fig = go.Figure()
fig.add_trace(go.Histogram(x=democrtic, name='더불어민주당', marker_color='#004EA1', xbins=dict(size=1)))
fig.add_trace(go.Histogram(x=peoplepower, name='국민의힘', marker_color='#E61E2B', xbins=dict(size=1)))
fig.add_trace(go.Histogram(x=justice, name='정의당', marker_color='#ffed00', xbins=dict(size=1)))

fig.update_layout(barmode='overlay', title_text='정당별 연령 분포', xaxis_title_text='나이',  yaxis_title_text='인원수')
fig.update_traces(opacity=0.75)

st.plotly_chart(fig, use_container_width=True)

demo_mean = round(np.mean(democrtic),1)
peo_mean = round(np.mean(peoplepower),1)
justice_mean = round(np.mean(justice),1)

st.markdown(
"""
그 다음으로 국회의 입법활동을 면밀히 살펴보기 위해 국회의원 소속 정당과 연령별로 비교분석을 진행할 것이다. 그에 앞서, 현재 국회의원의 인적 구성을 간단하게 살펴보자.

작성일 기준(2022.12.15.) 국회의원은 총 299명이며, 그중 더불어민주당이 169석, 국민의힘이 115석, 정의당이 6석, 기본소득당과 시대전환이 각각 1석, 무소속이 7석을 차지하고 있다. 남성은 242명(80.9%), 여성은 57명(19.1%)로 남성의 비율이 압도적으로 높게 나타났다. 연령별로는 30대 9명(3.0%), 40대 25명(8.7%), 50대 139명(46.5%), 60대 118명(39.5%), 70대 이상 8명(2.7%)으로 현재 국회가 50, 60대를 중심으로 구성되어 있음을 보여준다.

위의 히스토그램은 정당별 연령 분포를 보여준다. 거대 양당인 더불어민주당이 국민의힘은 종형 분포를 보여주며, 더불어민주당의 최빈값, 평균값이 국민의힘보다 낮게 형성되어 있다. 더불어민주당 국회의원의 평균 연령은 {}세이고, 국민의힘은 {}세, 정의당은 {}세이다.
""".format(demo_mean, peo_mean, justice_mean)
)

st.subheader("2) 정당별 법률안 발의 키워드")
st.markdown(
"""
국회의 작동에 핵심적인 역할을 하는 더불어민주당, 국민의힘, 정의당을 중심으로 국회의원들의 발의 키워드를 살펴보자. 법안 심의를 위해 국회의 17개 상임위원회에 올라온 안건에서 명사 키워드를 추출해 정당별 워드클라우드로 만들었다. **(stopwords는 무엇이었나요?)**

그 결과 더불어민주당에서는 ‘사회’, ‘국민’, 국민의힘에서는 ‘자치’, ‘시설’, 정의당에서는 ‘장애인’, ‘사회’와 같은 키워드가 주로 등장하였다. 이를 통해, 더불어민주당과 국민의힘이 거대 양당으로서 국가 전체의 제도나 국민 전반에 영향을 끼치는 기반 시설과 관련한 법안을 많이 발의하였다면, 정의당은 사회 내부의 소수자를 조망하고 이들의 인권이나 안전 등을 보장하고자 하는 법안을 많이 발의하였다고 볼 수 있다.
"""
)
img = Image.open('committee_wordcloud/democratic.png')
st.image(img, caption='더불어민주당의 국회 전체 키워드', width=350)
img = Image.open('committee_wordcloud/peoplepower.png')
st.image(img, caption='국민의힘의 국회 전체 키워드', width=350)
img = Image.open('committee_wordcloud/justice.png')
st.image(img, caption='정의당의 국회 전체 키워드', width=350)

st.markdown(
"""
자카드 유사도 분석을 통해 정당 워드클라우드 간의 유사성을 분석해보자. **(자카드 유사도 분석에 대한 간단한 설명 + 분석 과정에 대한 간단한 설명)** 분석결과는 다음과 같이 나타났다.

* 더불어민주당-국민의힘 유사도: 0.754
* 더불어민주당-정의당 유사도: 0.709
* 국민의힘-정의당 유사도: 0.653

**(분석 결과 내용)**

"""
)


st.subheader("3) 위원회별 정당, 연령 기준 워드클라우드")
option2 = st.selectbox('워드클라우드를 확인할 위원회를 선택하세요.', ('국회운영위원회', '법제사법위원회', '정무위원회', '기획재정위원회' , '교육위원회' , '과학기술정보방송통신위원회', '외교통일위원회' , '국방위원회' , '행정안전위원회' , '문화체육관광위원회', '농림축산식품해양수산위원회' , '산업통상자원중소벤처기업위원회' , '보건복지위원회' ,'환경노동위원회' , '국토교통위원회' , '정보위원회' , '여성가족위원회'))

committee = {
    '국회운영위원회' : '분석 내용 : ', 
    '법제사법위원회' : '분석 내용 : ', 
    '정무위원회' : '분석 내용 : ', 
    '기획재정위원회' : '분석 내용 : 중앙값 아래는 경제에, 중앙값 위는 과세 문제에, 다만 정의당의 경우 중앙값 위에서 가사 및 서비스에 대해 관심', 
    '교육위원회' : '분석 내용 : ', 
    '과학기술정보방송통신위원회' : '분석 내용 : ', 
    '외교통일위원회' : '분석 내용 : ', 
    '국방위원회' : '분석 내용 : ', 
    '행정안전위원회' : '분석 내용 : ', 
    '문화체육관광위원회' : '분석 내용 : ', 
    '농림축산식품해양수산위원회' : '분석 내용 : ', 
    '산업통상자원중소벤처기업위원회' : '분석 내용 : 산업통상자원중소벤처기업위원회: 중앙값 아래는 에너지와 발전에, 중앙값 위는 중소기업에 대한 발의안 많음(다만 국민의힘의 경우 기술에 대한 발의안이 많음)', 
    '보건복지위원회' : '분석 내용 : ',
    '환경노동위원회' : '분석 내용 : ', 
    '국토교통위원회' : '분석 내용 : ', 
    '정보위원회' : '분석 내용 : 중앙값 아래는 직원에, 중앙값 위는 기관에 대한 발의안(다만 정보위원회의 경우 발의안 수가 20개로 다른 위원회에 비해 매우 적음. 정의당의 경우 아예 발의안이 없음)', 
    '여성가족위원회' : '분석 내용 : '}

img = Image.open('committee_wordcloud/{}.png'.format(option2))
st.image(img)
st.info(committee[option2])
st.markdown(
"""
**(전체적인 분석 내용 종합 + 위원회별 분석내용도 간단히 있으면 좋을 거 같긴해요... 선택하면 나올 수 있게)**
"""
)

st.header("Ⅳ. 결론")
st.markdown(
"""
**(이러쿵 저러쿵)**
"""
)


st.markdown("***")
if st.button("OPEN API 및 외부자료 출처"):
	st.markdown(
	"""
    ##### OPEN API 자료
    * 열린국회정보, <국회의원 인적사항>
    * 열린국회정보, <국회의원 발의법률안>
    
    ##### 이미지
    * 국회 이미지자료실 : https://www.assembly.go.kr/cmmn/file/imageSrc.do?fileStreCours=829f7616fd59d611d6ee0bd750a47a6a&streFileNm=c4898d8acfe52e943d8691202e8e2fd5db110d2cdf90c86ad45263107332adc5
	""")
