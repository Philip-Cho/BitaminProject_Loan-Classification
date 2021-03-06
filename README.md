# BITAmin๐ Review Project (Team No.2)
## Topic๐ต : `Loan Approval Prediction(๋์ถ ์น์ธ ์ฌ๋ถ ์์ธก)`

## Coworkers ๐
- โ ๊น๋คํฌ @DieKim
- โ ์ด์ค์ @timointhebush
- โ ์กฐ์ฑํ @Philip-Cho

## Data โ
- `Loan Application Data`
- https://www.kaggle.com/vipin20/loan-application-data
- Predict whether loan will be approved by using the informations from loan application form
- ๋์ถ ์ ์ฒญ์์ ๋ด์ฉ์ ๋ฐํ์ผ๋ก ๋์ถ ์ ๊ฒฉ ์ฌ์ฌ ์์ธก

## Project Period ๐
- 2021/07/12 ~ 2021/07/30

## What we can Think of ๐ค
As a result of our Analysis, Credit_History, LoanAmount and Income related variables were most important features for Loan Approval<br/>
์ฐ๋ฆฌ๊ฐ ์ฃผ์ ๋ชจ๋ธ๋ก ์ฌ์ฉํ ๋๋คํฌ๋ ์คํธ ๋ชจ๋ธ์ ๋ฐ๋ฅด๋ฉด, ์ ์ฉ๊ธฐ๋ก๊ณผ ๋์ถ๊ท๋ชจ ๋ฐ ์๋ ๊ด๋ จ ๋ณ์๋ค์ด ๋์ถ์น์ธ์ ์ค์ํ ์์๋ค์ด ๋์๋ค. 
<br/>
<br/>
1. **Credit_History (์ ์ฉ ๊ธฐ๋ก)**<br/>
People with Credit History were more likely to get a loan approved. **The financial industry (except BigTech/FinTech)** evaluates an individual's credit ratings based on their credit history, such as whether they have used a credit card or not, and past loan experience. However, this method has a disadvantage in that it cannot accurately evaluate **thin-filers(people who don't have credit history but ability to repay the debt - ex. student, housewife etc).** We can see these characteristics from the data we used. In this situation, **we need to think about a more reasonable way to rate individual's credit.** Many of Fintech companies are making these effort.


- ์ ์ฉ ๊ธฐ๋ก์ด ์๋ ์ฌ๋์ด ๋์ถ์ ์น์ธ ๋ฐ์ ํ๋ฅ ์ด ๋ ๋๊ฒ ๋ํ๋ฌ๋ค. **๊ธฐ์กด์ ๊ธ์ต์๊ณ๋** ์ ์ฉ์นด๋ ์ฌ์ฉ ์ฌ๋ถ, ๊ณผ๊ฑฐ ๋์ถ ๊ฒฝํ ๋ฑ์ ์ ์ฉ ๊ธฐ๋ก๋ค์ ํ ๋๋ก ๊ฐ์ธ์ ์ ์ฉ๋ฑ๊ธ์ ํ๊ฐํ๋ค. ํํธ, ์ด๋ฌํ ๋ฐฉ์์ ์ค์ง์ ์ธ ์ฑ๋ฌด์ํ ๋ฅ๋ ฅ์ ์์ผ๋ ์ ์ฉ ๊ธฐ๋ก(๊ธ์ต๊ฑฐ๋ ๊ธฐ๋ก)์ด ์๋ **์ -ํ์ผ๋ฌ(Thin Filer)๋ค์** ๋ํ ์ ํํ ํ๊ฐ๋ฅผ ํ  ์ ์๋ค๋ ๋จ์ ์ด ์๋ค. ๋ถ์ ๊ฒฐ๊ณผ์ ๋ฐ๋ฅด๋ฉด, ํด๋น ๋ฐ์ดํฐ์๋ ์ด๋ฌํ ํน์ฑ๋ค์ด ๋ํ๋๊ณ  ์๋ค. ๋ฐ๋ผ์, ์ฐ๋ฆฌ๋ ์ด๋ฌํ **์ -ํ์ผ๋ฌ๋ค์ ์ํ ๋ฐ๋์งํ ์ ์ฉํ๊ฐ ๋ฐฉ์**์ ๊ณ ๋ฏผํด๋ด์ผ ํ๋ค. ๊ทธ๋ฆฌ๊ณ  ํ์ฌ ํํํฌ ์์ฅ์์์ ์์ฐ๊ด๋ฆฌ ๊ธฐ์๋ค์ ์ด๋ฌํ ๋ธ๋ ฅ์ ํ๊ณ  ์๋ค.  


2. **LoanAmount and Income (๋์ถ๊ธ์ก๊ณผ ์๋๊ณผ์ ๊ด๊ณ)**<br/>
Data such as occupation and income level are important data that can be used to evaluate whether a loan applicant has a ability to repay the loan. According to analysis of the project, low-income group can only get small loans, and the higher their income level, the more likely they are to be approved for a large loan. **Here we need to think about how to efficiently provide loans to low-income earners who need high-value loans for the purpose of mortgages, etc.** However, we also have to consider what happened at 2008, **'Subprime Mortgage Loan Crisis'**.


- ์ง์, ์๋์์ค ๋ฑ์ ์๋ฃ๋ค์ ๋์ถ ์ ์ฒญ์๊ฐ ๋์ถ๊ธ์ ์ํํ  ๋ฅ๋ ฅ์ด ์๋์ง ํ๊ฐํ  ์ ์๋ ์ค์ํ ๋ฐ์ดํฐ์ด๋ค. ์ด ํ๋ก์ ํธ์ ๋ถ์์ ๋ฐ๋ฅด๋ฉด, ์ ์๋์๋ ์์ก ๋์ถ๋ง ๋ฐ์ ์ ์์ผ๋ฉฐ ์๋์์ค์ด ๋์์ง์๋ก ๊ณ ์ก ๋์ถ์ ์น์ธ๋ฐ์ ํ๋ฅ ์ด ๋์์ง๋ค. ์ฌ๊ธฐ์ ์ฐ๋ฆฌ๋ **์ ์๋์ ์ค์์ ์ฃผํ๋ด๋ณด๋์ถ ๋ฑ์ ๋ชฉ์ ์ผ๋ก ๊ณ ์ก๋์ถ์ด ํ์ํ ์ฌ๋๋ค์๊ฒ ์ด๋ป๊ฒ ํ๋ฉด ํจ์จ์ ์ผ๋ก ๋์ถ์ด ๊ฐ๋ฅํ ์ง**์ ๋ํด ๊ณ ๋ฏผ์ด ํ์ํ๋ค. ํํธ, ๊ณผ๊ฑฐ 2008๋ ๋ฐ์ํ๋ **'์๋ธํ๋ผ์ ๋ชจ๊ธฐ์ง๋ก  ์ฌํ'** ๋ฑ์ ์ฌ๋ก์ ๋ํด์๋ ๊ณ ๋ คํด์ผ ํ๋ค.
