import pandas as pd
import matplotlib.pyplot as plt

def gen_figure(language):
    df = pd.read_csv(f'./csv/{language}classes.csv', sep=';')
    plt.figure(figsize=(25, 10))  # Adjust the width and height as needed

    # Create a subplot without frame and axes
    ax = plt.subplot(111, frame_on=False)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

    # Plot the table with a specified font size
    table = pd.plotting.table(ax, df, loc='center', fontsize=12)

    # Auto-adjust column widths
    def auto_adjust_column_widths(table, df):
        cell_texts = df.astype(str).values
        cell_lengths = [[len(text) for text in row] for row in cell_texts]
        col_widths = [max(lengths) for lengths in zip(*cell_lengths)]

        for i, col_width in enumerate(col_widths):
            table.auto_set_column_width(i)
            for j in range(len(df)):
                cell = table[(j + 1, i)]
                cell.set_width(col_width * 0.1)  # Adjust the factor as needed

    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(2.5, 1.5)
    for (i, j), cell in table.get_celld().items():
        if i == 0:  # Header row
            cell.set_text_props(fontsize=12)  # Set header text size
            cell.set_height(0.05)  # Adjust header height as needed
    auto_adjust_column_widths(table, df)

    plt.show()


langs = ['java', 'python']
for lang in langs:
    gen_figure(lang)
