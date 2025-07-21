import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df = load_and_clean_data('data/vgsales.csv')

    top_5_games_df = get_top_n_games(df, 5)

    top_5_series = top_5_games_df.set_index('Name')['Global_Sales']
    plot_bar_chart(top_5_series, 'Top 5 Games by Global Sales', 'Game')

    publishers_and_sales = get_publishers_and_sales(df, 10)
    plot_bar_chart(publishers_and_sales, 'Top 10 Publishers by Sales', 'Publisher')

    genre_and_sales = get_sales_by_genre(df)
    plot_bar_chart(genre_and_sales, 'Total Sales by Genre', 'Genre')

    sales_cor(df, 'EU_Sales', 'NA_Sales')


def load_and_clean_data(filepath : str):
    try:
        df = pd.read_csv(filepath)
        df=df.dropna()
        return df
    except FileNotFoundError:
        print(f"Plik {filepath} nie został znaleziony.")
        exit(1)
    except pd.errors.EmptyDataError:
        print(f"Plik {filepath} jest pusty.")
        exit(1)
    except Exception as e:
        print(f"Wystąpił błąd przy ładowaniu danych: {e}")
        exit(1)

def get_top_n_games(df,n : int):
    top_games=df.sort_values(by=['Global_Sales'], ascending=False).head(n)
    return top_games

def get_publishers_and_sales(df,n : int):
    sales_by_publisher=df.groupby('Publisher')['Global_Sales'].sum()
    sales_by_publisher=sales_by_publisher.sort_values(ascending=False).head(n)
    return sales_by_publisher

def sales_cor(df,continent1 : str,continent2 : str):
    continentA=df[continent1]
    continentB=df[continent2]
    cor=continentA.corr(continentB, method='spearman')
    print(f'Correlation between {continent1} and {continent2} is {cor}')
    sns.regplot(
        x=continent1,
        y=continent2,
        data=df,
        scatter_kws={'alpha': 0.3, 's': 15},
        line_kws={'color': 'red'}
    )

    plt.title(f'Korelacja i linia regresji: {continent1} vs {continent2}')
    plt.xlabel(f'{continent1} (mln)')
    plt.ylabel(f'{continent2} (mln)')
    plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.tight_layout()

    plt.show()

def get_sales_by_genre(df):
    sales_by_genre = df.groupby(df['Genre'])['Global_Sales'].sum()
    sales_by_genre=sales_by_genre.sort_values(ascending=False)
    return sales_by_genre

def plot_bar_chart(data_series, title, xlabel):

    labels = data_series.index
    values = data_series.values

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Sales (mln)")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()