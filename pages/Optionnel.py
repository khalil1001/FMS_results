import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

st.title("Results beza l bnin")
st.markdown("##### (Proud of you beza ❤️)")

df = pd.read_csv("Results_optionnel.csv")
df.replace(" ", pd.NA, inplace=True)
for col in df.columns[1:]:  # Starting from the second column
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["Moy"] = df.iloc[:, 1:].sum(axis=1) / 2

df.sort_values(by=["Moy"])


def highlight_specific_rows(indexes, color):
    def style_row(row):
        return ["background-color: {}".format(color) if row.name in indexes else "" for _ in row]

    return style_row


def format_if_numeric(value):
    try:
        # Attempt to convert the value to a float and format
        return "{:.2f}".format(float(value))
    except (ValueError, TypeError):
        # Return the value unchanged if it's not a number
        return value


# Applying style to the DataFrame
styled_df = df.style.apply(highlight_specific_rows([179], "lightgreen"), axis=1).format(format_if_numeric)
st.dataframe(styled_df)
