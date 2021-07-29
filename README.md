# BITAmin💊 7기 복습프로젝트 2조 
## Topic💵 : `Loan Approval Prediction(대출 승인 여부 예측)`

## Coworkers 🎈
- ✔ 김다희 @DieKim
- ✔ 이준석 @timointhebush
- ✔ 조성택 @Philip-Cho

## Data ⚒
- `Loan Application Data`
- https://www.kaggle.com/vipin20/loan-application-data
- Predict whether loan will be approved by using the informations from loan application form
- 대출 신청서의 내용을 바탕으로 대출 적격 심사 예측

## Project Period 📄
- 2021/07/12 ~ 2021/07/30

## What we can Think
As a result of our Analysis, Credit_History, LoanAmount and Income related variables were most important features for Loan Approval. 
우리가 주요 모델로 사용한 랜덤포레스트 모델에 따르면, 신용기록과 대출규모 및 소득 관련 변수들이 대출승인에 중요한 요소들이 되었다. 
 
1. Credit_History(신용 기록) <br/>
 People with Credit History were more likely to get a loan approved. The financial industry (except BigTech/FinTech) evaluates an individual's credit ratings based on their credit history, such as whether they have used a credit card or not, and past loan experience. However, this method has a disadvantage in that it cannot accurately evaluate thin-filers(people who don't have credit history but ability to repay the debt - ex. student, housewife etc). We can see these characteristics from the data we used. In this situation, we need to think about a more reasonable way to rate individual's credit. Many of Fintech companies are making these effort


- 신용 기록이 있는 사람이 대출을 승인 받을 확률이 더 높게 나타났다. 기존의 금융업계는 신용카드 사용 여부, 과거 대출 경험 등의 신용 기록들을 토대로 개인의 신용등급을 평가한다. 한편, 이러한 방식은 실질적인 채무상환 능력은 있으나 신용 기록(금융거래 기록)이 없는 신-파일러(Thin Filer)들에 대한 정확한 평가를 할 수 없다는 단점이 있다. 분석 결과에 따르면, 해당 데이터에는 이러한 특성들이 나타나고 있다. 따라서, 우리는 이러한 신-파일러들을 위한 바람직한 신용평가 방식을 고민해봐야 한다. 그리고 현재 핀테크 시장에서의 자산관리 기업들은 이러한 노력을 하고 있다.  


2. LoanAmount and Income(대출금액과 소득과의 관계)
- 직업, 소득수준 등의 자료들은 대출 신청자가 대출금을 상환할 능력이 있는지 평가할 수 있는 중요한 데이터이다. 이 프로젝트의 분석에 따르면, 저소득자는 소액 대출만 받을 수 있으며 소득수준이 높아질수록 고액 대출을 승인받을 확률이 높아진다. 여기서 우리는 저소득자 중에서 주택담보대출 등의 목적으로 고액대출이 필요한 사람들에게 어떻게 하면 효율적으로 대출이 가능할지에 대해 고민이 필요하다
