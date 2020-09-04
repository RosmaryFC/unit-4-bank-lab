# W10-D05-LAB

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Banking With Python

![gif](https://media2.giphy.com/media/y3B74VeWI2QQE/giphy.gif)

| Language | Type          | Date  | Due | Author               |
| -------- | ------------- | ----- | ---- | -------------------- |
| Python   | Project 2 | 9/04/2020 | 9/04/2020 | Suresh Melvin Sigera |

## Prompt

ACME is a bank which utilizes the following file structure `bank.csv`.

```text
10001,suresh,sigera,juagw362,1000,10000
10002,james,taylor,idh36%@#FGd,10000,10000
10003,melvin,gordon,uYWE732g4ga1,2000,20000
10004,stacey,abrams,DEU8_qw3y72$,2000,20000
10005,jake,paul,d^dg23g)@,100000,100000
```

| account_id | frst_name | last_name | password | balance_checking | balance_savings|
| -------- | ------------- | ----- | ---- | ---------- |---------- |
| 10001 | suresh | sigera | juagw362 | 1000 | 10000 | 
| 10002 | james | taylor | idh36%@#FGd | 10000 | 10000 |
| ... | ... | ... | ... | ... | ... |

Given the above file structure for the ACME Bank, write the entire Python program using classes, methods, file handling, and exception handling to meet the functional requirements below:

## Requirements

You should have **a minimum of**:

* 2 classes;
* 1 file (`bank.csv` given to you);

### Your app should have the following functionality:
1. Add New Customer
     * customer can have a checking account
     * customer can have a savings account
     * customer can have both a checking and a savings account
2. Withdraw Money from Account (required login)
    * withdraw from savings
    * withdraw from checking
3. Deposit Money into Account (required login)
     * can deposit into savings
     * can deposit into checking
### (Bonus)
4. Transfer Money Between Accounts (required login)
     * can transfer from savings to checking
     * can transfer from checking to savings
     * can transfer from checking or savings to another customer's account
5. Build Overdraft Protection (required login)
     * charge customer ACME overdraft protection fee of $35 when overdrafting
     * prevent customer from withdrawing more than $100 USD if account is currently negative
        * _the account cannot have a resulting balance of less than -$100_
      OR
       * _the customer cannot make a withdrawal of greater than $100_
     * deactivate the account after 2 overdrafts
       * reactivate the account if the customer brings the account current, paying both the overdraft amount and the resulting overdraft fees
6. Display Transaction Data (You need to create another file to store the transaction history, required login)
     * index all transactions for a customer account
     * show one transaction details
     * show historical data of transactions (date and time of transaction, type of transaction, resulting balance, etc.)
## Get Started!

![gif](https://media1.tenor.com/images/757db74e0691919301cb3414f642beef/tenor.gif?itemid=3561747)
