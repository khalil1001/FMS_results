import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

st.title("Results beza l bnin")
st.markdown("##### (Proud of you beza ❤️)")

df = pd.read_csv("Results.csv")
df["Moy Generale"] = (3 * (df["Moy"] + df["Moy.1"] + df["Moy.2"] + df["Moy.3"]) + df["Moy.4"]) / 13


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
