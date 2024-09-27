import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Aplicar tema roxo ao Seaborn
sns.set_palette("Purples")

# Importar e limpar os dados
def import_and_clean_data():
    # Importar dados e definir a coluna 'date' como índice
    df = pd.read_csv('data/fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

    # Limpar os dados removendo os 2.5% menores e maiores
    df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

    return df

df = import_and_clean_data()

# Gráfico de linha (Line Plot)
def draw_line_plot():
    # Definir o gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(df.index, df['value'], color='#6a0dad')  # Tom de roxo
    
    # Configurar título e rótulos
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    # Salvar a figura
    fig.savefig('line_plot.png')
    return fig

# Gráfico de barras (Bar Plot)
def draw_bar_plot():
    # Preparar os dados para o gráfico de barras
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Calcular a média das visualizações diárias por mês e ano
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Desenhar o gráfico de barras
    fig = df_bar.plot(kind='bar', figsize=(10, 6), color=sns.color_palette("Purples")).figure

    # Definir título e rótulos
    plt.title('Average Daily Page Views per Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', bbox_to_anchor=(1.05, 1), loc='upper left')

    # Salvar a figura
    fig.savefig('bar_plot.png')
    return fig

# Box Plot (Box Plot)
def draw_box_plot():
    # Preparar os dados para o box plot
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month_name()
    df_box['month_num'] = df_box.index.month

    # Ordenar meses para exibir de Janeiro a Dezembro
    df_box = df_box.sort_values('month_num')

    # Desenhar box plots
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

    # Box plot anual
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0], color='#6a0dad')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Box plot mensal
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], palette="Purples")
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Salvar a figura
    fig.savefig('box_plot.png')
    return fig

# Executar as funções
draw_line_plot()
draw_bar_plot()
draw_box_plot()
