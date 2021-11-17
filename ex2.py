import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")


page_bg_img = '''
<style>
.stApp {
  background-image: url("https://marketplace.canva.com/EAD2962NKnQ/2/0/1600w/canva-rainbow-gradient-pink-and-purple-zoom-virtual-background-_Tcjok-d9b4.jpg");
  background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

#타이틀/ 서브타이틀 
st.markdown('<p align="right" style="font-family:나눔고딕OTF; color:black; font-size: 30px;">국민권익위원회 제 1회 민원 빅데이터 경진대회 출품작</p>', unsafe_allow_html=True)
st.markdown('<p align="right" style="font-family:나눔고딕OTF; color:black; font-size: 30px;"></p>', unsafe_allow_html=True)
st.markdown('<p align="right" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">제출일 : 2021. 11. 19.</p>', unsafe_allow_html=True)
st.markdown('<p align="right" style="font-family:나눔고딕OTF ExtraBold; color:black; font-size: 30px;">팀 💪굳건히</p>', unsafe_allow_html=True)
st.markdown('---------------------------------------------------- ')

#사이드바
select_event = st.sidebar.selectbox("목차", ("0️⃣ 팀 소개", "1️⃣ 추진배경", "2️⃣ 분석방법","3️⃣ 분석결과", "4️⃣ 현황 파악", "5️⃣ 정책 제언"))

# 팀 소개

if select_event == '0️⃣ 팀 소개':
 
    st.markdown('<p align="left" style="font-family:나눔고딕OTF ExtraBold; color:black; font-size: 30px;">0️⃣ 팀 💪굳건히❓</p>', unsafe_allow_html=True)
    st.markdown('<p align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">장애인이 <b>굳건히</b> 자립적인 생활을 도모할 수 있도록 <b>국</b>민 <b>권</b>익 <b>위</b>원회에 지원한 팀 💪굳건히입니다.</p>', unsafe_allow_html=True)
    st.markdown(' ')
    st.markdown('---------------------------------------------------- ')
    st.markdown('<p align="left" style="font-family:나눔고딕OTF ExtraBold; color:black; font-size: 30px;">팀원 소개</p>', unsafe_allow_html=True)
    st.markdown(' ')
    
    # 페이지 레이아웃 3갈래
    #팀원 소개
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://cdn.pixabay.com/photo/2020/06/02/06/52/cat-5249722__480.jpg", width=100)
        st.markdown('<p align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">대표자 : 박지영</p>', unsafe_allow_html=True)
        st.markdown('<p align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">국립재활원 재활연구소 연구원</p>', unsafe_allow_html=True)

    with col2:
        st.image("증명사진_이정민.jpg", width=100)
        st.markdown('<p align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">팀원 : 이정민</p>', unsafe_allow_html=True)
        st.markdown('<p align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">국립재활원 재활연구소 인턴연구원</p>', unsafe_allow_html=True)

    with col3:
        st.image("https://github.com/LAB-703/LAB-703/blob/main/%EB%B0%95%EC%98%81%EB%B9%88.jpg?raw=true", width=100)
        st.markdown('<p align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">팀원 : 박영빈</p>', unsafe_allow_html=True)
        st.markdown('<p align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">국립재활원 재활연구소 인턴연구원</p>', unsafe_allow_html=True)
    st.markdown('---------------------------------------------------- ')   
    st.markdown(' ')
    st.markdown('<p align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">※ 팀원 2명은 행정안전부와 한국지능정보사회진흥원에서 실시 중인 ‘공공빅테이터 분석 청년인재 양성사업’을 통해 국립재활원에 파견된 인턴연구원임</p>', unsafe_allow_html=True)
    
## 국립재활원, 행정안전부, 한국지능정보사회진흥원 마크 달까말까 ??????💛💛💛💛💛
    
# 서론    
elif select_event == '1️⃣ 추진배경':
    st.markdown('<pre align="left" style="font-family:나눔고딕OTF ExtraBold; color:black; font-size: 20px;">1️⃣ 추진배경</pre>', unsafe_allow_html=True)
    st.markdown('''<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">
<b>○ 국민권익위원회 장애인 관련 민원의 분포를 살펴보면 점차 증가하는 추세로 나타남</b> <br>
<b>○ 장애는 내가 원해서, 나의 부모가 원해서 생기는 것이 아닌 불가항력으로 누구에게나 발생할 수 있는 것</b> <br>
  - 장애인은 선천적 혹은 불의의 사고, 질병 등으로 일상생활, 사회생활에 상당한 제한을 가지게 됨 <br>
<b>○ 장애인의 처우와 인식이 많이 개선되었음에도 실제 장애인들이 체감하는 불편사항은 여전히 존재</b> <br>
  - 일상생활, 사회생활 중 신체활동의 제약, 시설·환경적 제약, 사회적 인식에 따른 제약 등으로 다른 사람의 도움이 필요한 경우가 많은 취약계층임 <br>
<b>○ 소수 취약계층인 장애인의 사회적·정책적 인권 보장이 필요</b> <br>
  - 장애인에 관한 문제는 개인이나 일부 소수 그룹에서 해결하기 어려우므로 정부에서 정책적으로 해결하기 위한 노력이 필요할 것으로 사료됨 <br>
</pre>''', unsafe_allow_html=True)

    
    
    
elif select_event == '2️⃣ 분석방법':
    st.markdown('<pre align="left" style="font-family:나눔고딕OTF ExtraBold; color:black; font-size: 20px;">2️⃣ 국민권익위원회 민원데이터 분석 추진방법</pre>', unsafe_allow_html=True)
    st.markdown('<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;"><b>□ 분석 과정</b></pre>', unsafe_allow_html=True)
    st.image("분석과정.png")
    st.markdown('''<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">
<b>□ 분석 방법 및 내용 </b> <br>
  ○(활용 소프트웨어) Excel, R의 ggplot, dplyr, KoNLP 등, Python의 pandas, numpy, NLTK, KONLPY 등을 이용하여 데이터를 정제하고 분석 실시 <br>
  ○(분석 방법) <br>
    가) ‘장애인’ 키워드에 대한 민원 빅데이터 API 추출 및 워드 클라우드 시각화 분석(in R)<br>
    나) 워드 클라우드 결과 관련 자료 조사, 뉴스 크롤링 및 워드 클라우드 시각화 분석(in R)<br>
    다) 국민권익위원회에서 제공받은 데이터 중 “장애인” 키워드 추출 → 총 2,622건 추출(in Excel)<br>
    라) 추출한 데이터 중 건별로 “제목”과 “질문내용”을 한 문장(제목 + 질문내용)으로 결합(in Excel)<br>
    마) 민원 글 내의 특수문자 제거 및 한국어 맞춤법 검사 수행(in Python)<br>
    바) 5가지 형태소 분석기를 비교하여 분석 목적에 적합한 성능을 보인 “kkma” 분석기 사용(in Python)<br>
    사) 총 21,043개 형태소 분석 결과 오류 검토 후 수정(in Excel)<br>
    아) 다양한 품사 중 의미 있는 명사, 동사, 형용사만 사용 및 데이터 형태 변환(in R)<br>
    자) 텍스트 군집분석을 통해 최적의 k값 후보군(k = 3, 4, 5) 도출(in Python)<br>
    차) 텍스트 마이닝 기법 중 하나인 토픽 모델링1 기법을 활용하여 시각화(in Python) <br>
</pre>''', unsafe_allow_html=True)    
    
###################################가가가가가가가가가가가가가가가가가가가가가가 ###############################   
    
elif select_event == '3️⃣ 분석결과':
    st.markdown('<pre align="left" style="font-family:나눔고딕OTF ExtraBold; color:black; font-size: 20px;">3️⃣ 국민권익위원회 민원데이터 분석 결과</pre>', unsafe_allow_html=True)
    st.markdown('<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 17px;"><b>가. 민원 빅데이터 API 추출 및 키워드 “장애인” 워드 클라우드 시각화 분석 결과</b></pre>', unsafe_allow_html=True)
    st.markdown('''<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">
  ○ 점자블록 등의 이동경로 문제(ex/공중화장실, 구청 등) <br>
  ○ 지역상품권, 수여상장 등의 종이문서에 점자 표기(ex/상품권, 임명장, 표창증서, 위촉장 등)<br>
  ○ 생활용품(ex/음료나 의약품 등) 점자 표기 <br>
</pre>''', unsafe_allow_html=True)  
    ###########################################################################################################################
    st.markdown('---------------------------------------------------- ')
    st.markdown('<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;"><b>[그림 1] 장애인-민원 연관어 분석 정보 워드클라우드(상위 50건) </b></pre>', unsafe_allow_html=True)
    HtmlFile = open("장애인-민원 연관어 분석 정보 워드클라우드(상위 50건).html", 'r',encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code, height=400,  scrolling=False)
    st.markdown('<p align="right" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">* 마우스를 올리면 value를 확인할 수 있습니다.<br> ** value의 의미는 키워드인 "장애인"과의 단어 간 연관도를 뜻합니다.<br>담당자 문의 결과, 분석 솔루션 프로그램에서 자체적으로 도출된 값이므로 정확한 공식을 파악할 수 없었습니다.</p>', unsafe_allow_html=True)
    st.markdown('<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;"><b>[그림 2] 점자표기-민원 연관어 분석 정보 워드클라우드(상위 3건 제외)</b><br>(※ 상위 3건 시각장애인, 장애인복지카드, 장애인등록증의 value가 너무 높게 나와 다른 키워드들이 보이지 않았음)</pre>', unsafe_allow_html=True)
    HtmlFile = open("점자표기-민원 연관어 분석 정보 워드클라우드(상위 3건 제외).html", 'r',encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code, height=750, scrolling=False)
    st.markdown('<p align="right" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">* 마우스를 올리면 value를 확인할 수 있습니다.<br>** value의 의미는 키워드인 "장애인"과의 단어 간 연관도를 뜻합니다. <br>담당자 문의 결과, 분석 솔루션 프로그램에서 자체적으로 도출된 값이므로 정확한 공식을 파악할 수 없었습니다.</p>', unsafe_allow_html=True)
#######################나나나나나나나나나나나나나나나나나나###############################################    
    st.markdown('---------------------------------------------------- ')
    st.markdown('<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 17px;"><b>나. 워드 클라우드 결과 관련 자료 조사, 뉴스 크롤링 및 워드 클라우드 시각화 분석</b></pre>', unsafe_allow_html=True)
    st.markdown('''<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">
<b>□ 점자 관련 자료 조사 </b>  <br>
  ❍ 점자 표기 관련 실태조사 보고서, 점자 제공에 관한 기타 법률조항 확인 <br>
</pre>''', unsafe_allow_html=True) 
#####################################################################################################################    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;"><b>[그림 3] 2020 점자 표기 실태조사(문화체육관광부 국립국어원)</b></pre>', unsafe_allow_html=True)
        st.image("점자표기 실태조사(문화체육관광부 국립국어원).png")
               
    with col2:
        st.markdown('<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;"><b>[그림 4] 제1차 점자발전기본계획(2019-2023)(문화체육관광부)</b></pre>', unsafe_allow_html=True)
        st.image("제 1차 점자발전기본계획(2019-2023) 문화체육관광부.png")
############################################################################################        
    st.markdown('''<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">
<b>□ 점자 관련 뉴스 조사</b>  <br>
  ❍ 점자 관련 신문기사(2021.01.01.-2021.11.01.의 1360건 본문) 크롤링하여 점자표기에 대한 니즈 분석  <br>
</pre>''', unsafe_allow_html=True) 
    
    st.markdown('<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;"><b>[그림 5] 점자관련 뉴스 기사에 대한 워드 클라우드 분석</b></pre>', unsafe_allow_html=True)
    HtmlFile = open("점자뉴스(워드클라우드).html", 'r',encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code, height=600, scrolling=False)
    st.markdown('<p align="right" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">* 마우스를 올리면 빈도를 확인할 수 있습니다.</p>', unsafe_allow_html=True)
        
     
    st.markdown('<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;"><b>[그림 6] 점자뉴스-상위 50개 가중치 키워드 워드클라우드</b></pre>', unsafe_allow_html=True)
    HtmlFile = open("점자뉴스-상위 50개 가중치 키워드(워드클라우드).html", 'r',encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code, height=550, scrolling=False)
    st.markdown('<p align="right" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">* 마우스를 올리면 빈도를 확인할 수 있습니다.</p>', unsafe_allow_html=True)
    st.markdown('''<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">
- 워드클라우드 전반적인 흐름으로 보아 사회 다방면에서의 점자 표기 법제화에 대한 니즈 확인 <br>
- 빠르게 피부로 와 닿을 수 있도록 배리어프리존 확장을 위한 다양한 시도가 필요한 것으로 판단됨<br>
- 최근 10월 공유 전동킥보드 이용 활성화로 인해 거리에 무분별하게 주차된 킥보드로 인해 시각장애인들이 통행에 방해를 받고 있으며, 점자블록이 파손되는 등의 불편 야기<br>
- 최근 기업(LG)에서 가전제품, 생활화학제품, 공공시설 엘리베이터 등에 부착가능한 점자스티커를 제작하여 배부.😡😡😡😡😡😡😡😡😡😡😡😡<br>
  이와 같은 사회환원활동과 함께 임직원, 관계자, ESG경영 등이 워드 클라우드에 나타남 <br>
</pre>''', unsafe_allow_html=True)
    ####################################다다다다다다다다다다다다다다다다다다다다다다##########################    
    st.markdown('---------------------------------------------------- ')
    st.markdown('<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 17px;"><b>다. 국민권익위원회 유사사례 정보(키워드 “장애인”)의 n그램  시각화 분석 결과 </b></pre>', unsafe_allow_html=True)
    st.markdown('''<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">
<b>□ 텍스트마이닝을 위한 형태소 분석 및 전처리 </b><br>
  ❍ ‘빅카인즈’ 플랫폼에서 형태소 분석 시행<br>
  ❍ (제목&” “&내용)으로 제목과 내용을 한 문장으로 결합(in Excel) <br>
  ❍ “부정어 + 동사”를 결합하여 부정의미 동사 생성 <br>
   - 기존의 “못”, “않”, “안되” 등의 부정어는 띄어쓰기, 혹은 보조동사(VXV)로 형태소 분리되어 부정의 의미를 반영하지 못함. 이 과정을 통해서 부정의 의미를 반영 <br>
  ❍ 의미가 없는 “~ 있다”, “~ 하다”, “~ 되다“, “~ 같다” 등 검토 후 삭제 <br>
  ❍ 수식의 의미를 갖는 “~ 위해”, “~ 관해”, “~ 대해” 등 삭제 <br>
</pre>''', unsafe_allow_html=True)                                                                   #  그림 순서
    st.markdown('<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;"><b>[그림 7😡😡😡😡] 국민권익위원회 민원 데이터 n그램 (n>=4)</b></pre>', unsafe_allow_html=True)
    st.image("장애인 유사사례정보 n그램 분석 시각화.png",width=900)   #😡😡😡😡 그림 사이즈
    
################################라라라라라라라라라라라라라라라라라라라########################################### 
    st.markdown('---------------------------------------------------- ')
    st.markdown('<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 17px;"><b>라. 국민권익위원회 빅데이터 분석 경진대회 데이터 중 “장애인”키워드 분석</b></pre>', unsafe_allow_html=True)
    st.markdown('''<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;"><b> □ EDA 차원에서 장애인 관련 민원 연도별 월별 분포 분석 </b>
</pre>''', unsafe_allow_html=True)                                                                          # 그림 순서
    st.markdown('<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;"><b>[그림 8😡😡😡😡] 국민권익위원회 장애인 관련 민원 연도별 월별 분포 (날짜 미기재건 : 42건) </b></pre>', unsafe_allow_html=True)
    HtmlFile = open("장애인 관련 민원 연도별 월별 분포.html", 'r',encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    st.markdown('*마우스를 올리면 연도별 월별 빈도를 확인할 수 있습니다.')
    components.html(source_code, width=900, height=550, scrolling=False)      #😡😡😡😡 그림 사이즈
    st.markdown('''<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;"><b> □ 텍스트마이닝을 위한 형태소 분석 및 전처리</pre>''', unsafe_allow_html=True)
    st.markdown('<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;"><b>[그림 8😡😡😡😡] 형태소 분석 결과(일부) </b></pre>', unsafe_allow_html=True)
    st.image("형태소분석일부.PNG")
    st.markdown('<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;"><b>[그림 8😡😡😡😡] 명/동/형용사를 건별로 한 줄에 결합(일부) </b></pre>', unsafe_allow_html=True)
    st.image("명,동,형용사를 건별로 한 줄에 결합(일부).PNG")
    st.markdown('''<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">
  ❍ hanspell 이용, 특수문자 제거 및 맞춤법 검사 시행(in Python)<br>
  ❍ 5가지 형태소 분석기 중 kkma로 형태소 분석 시행 (in Python)<br>
  ❍ 명사/동사/형용사 추출 및 민원 건별 단어 결합 (in R)<br>
  ❍ 의미가 없는 “~ 있다”, “~ 하다”, “~ 되다“, “~ 같다” 등 검토 후 삭제<br>
  ❍ 수식의 의미를 갖는 “~ 위해”, “~ 관해”, “~ 대해” 등 삭제
</pre>''', unsafe_allow_html=True)  
    st.markdown('''<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;"><b> □ 텍스트마이닝 파이계수 시각화 분석 결과 </pre>''', unsafe_allow_html=True)
    st.markdown('<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;"><b>[그림 8😡😡😡😡] 국민권익위원회 장애인 민원 데이터 파이계수(그 당시 그래프가 잘 안나왔고 제공데이터가 아님)😡😡😡 </b></pre>',unsafe_allow_html=True)
    st.image("국권위민원데이터_파이계수.png")           
    st.markdown('''<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;"><b> □ 텍스트 군집분석</b>
 ❍ 주어진 문서에 대하여 각 문서에 어떤 주제들이 존재하는지를 확인하기 위한 확률적 토픽 모델 기법 중 하나인 LDA(Latent Dirichlet Allocation, 잠재 디리클레 할당) 활용<br>
     ※ 다차원 척도를 통해 유사한 토픽을 근처에 배치하기 위한 확률 분포의 유사성을 젠슨-섀넌 발산(Jensen-Shannon Divergence) 지수를 계산한 것. <br>         해당 지표는 기본적으로 각 토픽에 있는 단어 들의 확률 분포에 따른 위치를 보여줌.<br>
 ❍ 불용어 추가 처리 후 재시각화를 반복하여 군집을 보다 효과적으로 분류<br>
 ❍ 텍스트 군집분석을 통해 최적의 k값 후보군(k = 3, 4, 5) 도출(in Python)</pre>''', unsafe_allow_html=True)
    st.image("군집비교표.png")     
    st.markdown('''<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">  ❍ 텍스트 마이닝 기법인 토픽 모델링 기법 중 LDA를 활용하여 시각화(in Python)
</pre>''', unsafe_allow_html=True)
    st.markdown('<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;"><b>[그림 8😡😡😡😡] LDA를 활용한 토픽 모델링 시각화 </b></pre>', unsafe_allow_html=True)
    HtmlFile = open("국민권익위원회 장애인 관련 민원 LDA 토픽 모델링 (k=4).html", 'r',encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code,width=1300, height=800, scrolling=False)
    st.markdown('''<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">
  ❍ GitHub 대시보드 관련 -> 이게 대시보드라 안넣어도 될듯 한데 😡😡
</pre>''', unsafe_allow_html=True) 
    

    #############미완  😡😡 😡😡 😡😡 😡😡 😡😡 😡😡 😡😡 😡😡 😡😡 😡😡 😡😡 😡😡#############
elif select_event == '4️⃣ 현황 파악':
    st.markdown('<pre align="left" style="font-family:나눔고딕OTF ExtraBold; color:black; font-size: 20px;">4️⃣ 도출된 이슈에 대한 현황 파악</pre>', unsafe_allow_html=True)
    st.markdown('''<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;"><b> □ 장애인전용주차구역 관련 현황</b>
  ❍ 대부분의 비장애인들은 주차 위반에 대해 과태료 10만원이 부과된다는 것을 알고 있지만 대수롭지 않게 생각하고 있음 </pre>''', unsafe_allow_html=True)
    st.image("캡쳐본1.png")
    st.markdown('<p align="right" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">* 출처: "최대 과태료 2백만 원" 장애인 전용 주차구역 집중 단속 현장(KBS 교양, ‘21.04.08. 방영)</p>', unsafe_allow_html=True)
    
    
    
    
    
    
    
    
    
elif select_event == '5️⃣ 정책 제언':
    st.markdown('<pre align="left" style="font-family:나눔고딕OTF ExtraBold; color:black; font-size: 20px;">5️⃣ 도출된 이슈에 대한 정책 제언</pre>', unsafe_allow_html=True)
    st.markdown('''<pre align="left" style="font-family:나눔고딕OTF; color:black; font-size: 15px;">
<b>□ 장애인전용주차구역에 대한 정책 제언</b><br>
  ❍ 주차 가능한 상황에 대한 정확한 정보 홍보 필요<br>
    - 장애인전용주차구역에 주차가 가능한 상황에 대한 현행 정보에 대한 전국민 대상 홍보<br>
    - 공익광고를 통해 준법 정신을 기르고, 장애인과 비장애인의 입장 차의 간극을 줄여 공감과 이해를 통한 사회적 통합 지향<br>
    - 장애인 주차 가능 표지에 대한 비장애인의 이해도를 높여 표지를 보고 의심하거나, 신고제도를 오·남용하지 않도록 함 <br>
  ❍ 장애인 주차표지에 대한 오∙남용 인식 개선 필요 <br>
   - 장애인과 장애인의 보호자 등에게 복지제도를 오·남용하지 않도록 인식 개선 <br>
  ❍ 비장애인의 장애인전용주차구역 주·정차 금지에 대한 인식 개선 필요 <br>
   - 장애인전용주차구역에 비장애인이 1분 1초라도 주·정차를 하면 안되는 이유에 대한 대대적인 홍보를 통하여 전국민 인식 개선<br>
  ❍ 공적 문서로 ‘장애인 주차 가능 표지’로 활용할 수 있도록 하여 표지에 대한 신뢰성 확보
</pre>''', unsafe_allow_html=True)   
    
    
    
    
    st.image("https://mediahub.seoul.go.kr/wp-content/uploads/2020/09/b246829e13c13baea2fb04c1a3ad02ff.jpg",width=900,channels="RGB",caption="출처 : 서울시")



        
        

# st.header("Button")
# if st.button("Button!!"):
#     st.write("Yes")
#     
#     
# st.header("Chart Data")
# chart_data = pd.DataFrame(np.random.randn(50, 3), columns=["a", "b", "c"])
# st.bar_chart(chart_data)


