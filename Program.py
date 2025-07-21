import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = load_and_clean_data()
    #top_5_games = get_top_n_games(df,5)
    #plot_top_n_games(top_5_games)
    publishers_and_sales = get_publishers_and_sales(df,10)
    plot_publishers_and_sales(publishers_and_sales)


def load_and_clean_data():
    df = pd.read_csv("data/vgsales.csv")
    df=df.dropna()
    return df
def get_top_n_games(df,n):
    top_games=df.sort_values(by=['Global_Sales'], ascending=False).head(n)
    return top_games
def plot_top_n_games(top_games):
    games=top_games['Name']
    sale=top_games['Global_Sales']

    plt.bar(games,sale)
    plt.title(f'Top {len(top_games)} by global sales')
    plt.xlabel("Games")
    plt.ylabel("Sales (mln)")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.show()
def get_publishers_and_sales(df,n):
    sales_by_publisher=df.groupby('Publisher')['Global_Sales'].sum()
    sales_by_publisher=sales_by_publisher.sort_values(ascending=False).head(n)
    return sales_by_publisher
def plot_publishers_and_sales(sales_by_publisher):
    publishers = sales_by_publisher.index
    sales = sales_by_publisher.values
    plt.bar(publishers,sales)
    plt.title(f'Top {len(sales_by_publisher)} by publishers')
    plt.xlabel("Publishers")
    plt.ylabel("Sales (mln)")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()