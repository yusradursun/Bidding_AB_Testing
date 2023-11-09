# Bidding_AB_Testing
 Comparison of AB Test and Conversion of Bidding Methods

#####################################################
# Business Problem
#####################################################

Facebook recently introduced a new bidding type called "average bidding" as an alternative to the existing "maximum bidding." One of our clients, bombabomba.com, decided to test this new feature and wants to conduct an A/B test to understand whether average bidding brings more conversions than maximum bidding. The A/B test has been ongoing for 1 month, and bombabomba.com now expects you to analyze the results of this A/B test. The ultimate success metric for bombabomba.com is Purchase. Therefore, the focus should be on the Purchase metric for statistical tests.

#####################################################
# Dataset Story
#####################################################

This dataset contains information about a company's website, including details such as the number of ads seen and clicked, along with revenue information. There are two separate datasets for the Control and Test groups, which are available on different sheets of the ab_testing.xlsx Excel file. Maximum Bidding is applied to the Control group, while Average Bidding is applied to the Test group.
Columns:
- impression: Number of ad views
- Click: Number of clicks on the displayed ads
- Purchase: Number of products purchased after clicking on the ads
- Earning: Revenue generated after purchasing products
