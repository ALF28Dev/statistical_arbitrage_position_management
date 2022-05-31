# Statistical Arbitrage Position Management

To trade the statistical arbitrage trading strategy [found here](https://github.com/ALF28Dev/statistical_arbitrage) I have developed a platform which willorganise the position in a manner which makes them easy to track and understand.

Whenever my software detects a pair which meets my  criteria it will be placed within the pending orders database table. I can then open this position within my brokerage manually. After i have filled the order i can select open and the position will then move to the open positions database table. The position will remain here until my software detects that the position needs to be closed.

When my software detects that the position needs to be closed a new record will be placed within the pending close database table. This record will contain the new current prices of the two stocks. After i have closed the position within my brokerage i can then select the close button. The trade PL will be placed within the trade log database table and the positions will be removed from the pending close and current positions database.


<img width="796"  alt="Screenshot 2022-05-31 at 11 07 49" src="https://user-images.githubusercontent.com/87500491/171149607-2fb90180-ec8f-485a-8638-9a73ca943a0a.png">


