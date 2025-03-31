import pandas as pd
import plotly.express as px


df = pd.read_csv(r"entropy\hello_world_entropy.csv")


def calculate_distinct_assemblies(df):
    distinct_counts = (
        df.groupby(["Block_ID", "Type"])["Assembly"].nunique().reset_index()
    )
    return distinct_counts


def visualize_distinct_assemblies_bar_chart(df):
    distinct_counts = calculate_distinct_assemblies(df)
    fig = px.bar(
        distinct_counts,
        x="Block_ID",
        y="Assembly",
        color="Type",
        title="Number of Distinct Assembly Types per Block and Type (Print 'Hello World')",
        labels={"Assembly": "Number of Distinct Assembly", "Block_ID": "Block #"},
        barmode="group",
    )

    fig.update_layout(
        xaxis_tickangle=-45,
        xaxis={"type": "category"},
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        font=dict(
            family="SF Pro Display, sans-serif",
            size=12,
            color="black",
        ),
    )

    fig.show()


visualize_distinct_assemblies_bar_chart(df)
