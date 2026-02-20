from src.data_loader import load_data

from src.analysis import total_sales ,monthly_sales,region_sales,top_product,total_profit

from src.visualization import create_output_folder,plot_monthly_sales,plot_region_sales


def main():
    file_path=r"D:\PROJECT\sales_analysis\data\sales_data.csv"
    df=load_data(file_path)

    create_output_folder()

    total=total_sales(df)
    monthly=monthly_sales(df)
    region=region_sales(df)
    top=top_product(df)
    profit=total_profit(df)

    plot_monthly_sales(monthly)
    plot_region_sales(region)


    with open("outputs/summary_report.txt","w") as f:
        f.write(f"total sales:{total}\n")
        f.write(f"total profit: {profit}\n")
        f.write(f"total product: {top}\n")
    print("Analysis completed! check output folder")

if __name__=="__main__":
    main()