# Statistical Arbitrage Position Management

To trade the statistical arbitrage trading strategy [found here](https://github.com/ALF28Dev/statistical_arbitrage) I have developed a platform which willorganise the position in a manner which makes them easy to track and understand.

Whenever my software detects a pair which meets my  criteria it will be placed within the pending orders database table. I can then open this position within my brokerage manually. After i have filled the order i can select open and the position will then move to the open positions database table. The position will remain here until my software detects that the position needs to be closed.

When my software detects that the position needs to be closed a new record will be placed within the pending close database table. This record will contain the new current prices of the two stocks. After i have closed the position within my brokerage i can then select the close button. The trade PL will be placed within the trade log database table and the positions will be removed from the pending close and current positions database.


<img width="781" alt="Screenshot 2022-05-30 at 23 42 58" src="https://user-images.githubusercontent.com/87500491/171065439-5207fd80-3d0d-4027-9c71-5b5256ba6723.png">


