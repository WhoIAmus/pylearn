
#ціна: 89 - 39 - 19 - 9 - 4 - 2 - 1
cost = int(input()) 
going = True

money = [500, 200, 100, 50, 20, 10, 5, 2, 1]
papers_needed = 0
money_needed = cost

for i in money:
  a = money_needed//i
  papers_needed += a
  money_needed -= i * a

print(papers_needed)