import pandas as pd
import matplotlib.pyplot as plt
import os
import shutil


def clear_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')


def descriptive_statistics(num_df):
    # Calculate and print descriptive statistics for each numeric column
    print("Descriptive Statistics:\n")
    num = num_df.select_dtypes(include='number')
    for column in num.columns:
        print(f"Statistics for {column}:\n")
        print(f"Mean: {num[column].mean()}\n")
        print(f"  Median: {num[column].median()}\n")
        print(f"  Mode: {num[column].mode().iloc[0]}")
        print(f"  Standard Deviation: {num[column].std()}\n")
        print(f"  Variance: {num[column].var()}\n")
        print(f"  Minimum: {num[column].min()}\n")
        print(f"  Maximum: {num[column].max()}\n")
        print(f"  Count: {num[column].count()}\n")


def histogram_plot_for_the_each_column(num_df):
    # Plot Histogram for each pair of numeric columns
    for column in num_df.columns:
        plt.figure(figsize=(8, 6))
        plt.hist(num_df[column].dropna(), bins=30, edgecolor='k', alpha=0.7)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        # pig = os.path.join(output_file_name, f'{column}_Histogram.png')
        plt.savefig(os.path.join(output_dir, f'{column}_Histogram.png'))
        plt.close()


def box_plot_for_the_each_column(num_df):
    # Plot Histogram for each pair of numeric columns
    for column in num_df.columns:
        plt.figure(figsize=(8, 6))
        numeric_data = pd.to_numeric(num_df[column], errors='coerce').dropna()
        plt.boxplot(numeric_data)
        plt.title(f'Box_plot of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.savefig(os.path.join(output_dir, f'{column}_Box.png'))
        plt.close()


def scatter_plot_for_each_column(num_df):
    # Plot scatter plots for each pair of numeric columns
    for column1 in num_df.columns:
        for column2 in num_df.columns:
            if column1 != column2:
                plt.figure(figsize=(8, 6))
                plt.scatter(num_df[column1], num_df[column2], alpha=0.7)
                plt.title(f'Scatter Plot of {column1} vs {column2}')
                plt.xlabel(column1)
                plt.ylabel(column2)
                plt.savefig(os.path.join(output_dir, f'{column1}_{column2}_Scatter.png'))
                plt.close()


def line_plot_for_each_column(num_df):
    # Plot the data for each column of data
    plt.figure(figsize=(10, 6))

    for column in num_df.columns:
        if pd.api.types.is_numeric_dtype(num_df[column]):
            plt.plot(num_df.index, num_df[column], marker='o', label=column)

    plt.title('Line Plot of Numeric Columns')
    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.legend()
    plt.savefig(os.path.join(output_dir, f'Line_Scatter.png'))
    plt.close()


def main():
    global output_dir

    file_path = input("enter the .data file").strip()
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        print(df)
        print("File loaded successfully.")
    else:
        print("File not found. Please check the file path.")
    # Read the .dat file
    data = pd.read_csv(file_path, delimiter=',')
    file_name = os.path.basename(file_path)
    data.to_excel(f'{file_name}.xlsx', index=False)
    print(data)
    # creating output file
    base_path = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_path, 'output')
    os.makedirs(output_dir, exist_ok=True)

    # Clear the output file
    clear_directory(output_dir)
    # descriptive_statistics
    descriptive_statistics(data)
    # Histogram Plot
    histogram_plot_for_the_each_column(data)
    # Box Plot
    box_plot_for_the_each_column(data)
    # Scatter Plot
    scatter_plot_for_each_column(data)
    # Line_plot
    line_plot_for_each_column(data)


if __name__ == '__main__':
    main()
