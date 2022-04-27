import pandas as pd


class Clean_Tweets:
    """
    The PEP8 Standard AMAZING!!!
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df
        print('Automation in Action...!!!')

    def drop_unwanted_column(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.  
        """
<<<<<<< HEAD
        unwanted_rows = df[df['retweet_count'] == 'retweet_count'].index
        df.drop(unwanted_rows, inplace=True)
        df = df[df['polarity'] != 'polarity']

        return df
=======
        unwanted_rows = self.df[self.df['retweet_count']
                                == 'retweet_count'].index
        self.df.drop(unwanted_rows, inplace=True)
        self.df = self.df[self.df['polarity'] != 'polarity']

        return self.df
>>>>>>> 5ae807e99b0be5f648298425db9d9723501cba23

    def drop_duplicate(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        drop duplicate rows
        """
<<<<<<< HEAD
        df.drop_duplicates(keep=False)
=======
        self.df = self.df.drop_duplicates().drop_duplicates(subset='original_text')
>>>>>>> 5ae807e99b0be5f648298425db9d9723501cba23

        return df

    def convert_to_datetime(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        convert column to datetime
        """
<<<<<<< HEAD

        df['created_at'] = pd.to_datetime(
            df['created_at']).dt.strftime('%Y-%m-%d')

        df = df[df['created_at'] >= '2020-12-31']

        return df
=======
        self.df['created_at'] = pd.to_datetime(
            self.df['created_at'], errors='coerce')

        self.df = self.df[self.df['created_at'] >= '2020-12-31']

        return self.df
>>>>>>> 5ae807e99b0be5f648298425db9d9723501cba23

    def convert_to_numbers(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc to numbers
        """
<<<<<<< HEAD

        columns = ['polarity', 'subjectivity', 'favorite_count',
                   'retweet_count', 'followers_count', 'friends_count']
        for column in columns:
            df[column] = pd.to_numeric(df[column])

        return df
=======
        self.df['polarity'] = pd.to_numeric(
            self.df['polarity'], errors='coerce')
        self.df['retweet_count'] = pd.to_numeric(
            self.df['retweet_count'], errors='coerce')
        self.df['favorite_count'] = pd.to_numeric(
            self.df['favorite_count'], errors='coerce')

        return self.df

    def remove_non_english_tweets(self) -> pd.DataFrame:
        """
        remove non english tweets from lang
        """

        self.df = self.df.query("lang == 'en' ")

        return self.df


if __name__ == "__main__":
    tweet_df = pd.read_json("./data/covid19.json")
    cleaner = Clean_Tweets(tweet_df)
>>>>>>> 5ae807e99b0be5f648298425db9d9723501cba23
