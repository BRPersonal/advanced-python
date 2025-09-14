from leader_board import LeaderBoard

def group_by_example() -> None:
    from itertools import groupby

    # Analyze user activity patterns from server logs
    user_actions = ['login', 'login', 'browse', 'browse', 'browse',
                    'purchase', 'logout', 'logout']

    #find counts of each unique activity
    activity_patterns = [(activity,len(list(grouper))) for activity,grouper in groupby(user_actions)]
    print(f"activity_patterns={activity_patterns}")

    #Find total activities
    total_activities = sum(count for _,count in activity_patterns)
    print(f"total_activities={total_activities}")

def zip_with_star_example() -> None:
    #matrix transposition - flipping rows into columns becomes
    #easy with zip() and pythons list unpacking operator *
    quarterly_sales = [
        [120, 135, 148, 162],  # Product A by quarter
        [95, 102, 118, 125],  # Product B by quarter
        [87, 94, 101, 115]  # Product C by quarter
    ]

    # Transform to quarterly view across all products
    by_quarter = list(zip(*quarterly_sales))
    print(f"Sales by quarter:{by_quarter}")

    #find total sales for each quarter
    quarterly_totals = [sum(quarter) for quarter in by_quarter]
    print(f"totals for each quarter:{quarterly_totals}")

    #calculate growth percentage for quarters 2,3 and 4
    growth_percentages = [(quarterly_totals[i+1] - quarterly_totals[i]) / quarterly_totals[i] * 100 for i in range(len(quarterly_totals)-1)]

    #round off to 1 decimal place and suffix "%"
    formatted_percentages = [f"{rate:.1f}%" for rate in growth_percentages]
    print(f"formatted_percentages={formatted_percentages}")

def bisect_example():
    board = LeaderBoard()
    scores = [("Alice", 2850), ("Bob", 3100), ("Carol", 2650),
              ("David", 3350), ("Eva", 2900)]

    for player,score in scores:
        board.add_score(player,score)

    top_3 = board.top_players(3)
    print(f"top3={top_3}")

if __name__ == "__main__":
    # group_by_example()
    # zip_with_star_example()
    bisect_example()