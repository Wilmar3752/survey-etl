from src.etl import extract, transform, load
from src.db_conn import engine
def main():
    list_df = extract()
    list_df_transformed = transform(list_df)
    load(engine,list_df_transformed)

if __name__ == '__main__':
    main()



