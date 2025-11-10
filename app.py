import os
import streamlit as st
from transformer_hardcoded import transform_file

st.title("PO Automation – Hardcoded")

uploaded = st.file_uploader("Upload PO Excel file", type=["xlsx", "xls"])

if uploaded is not None:
    # Run your transformer (this still just returns bytes)
    out_bytes = transform_file(uploaded)

    # Build output file name: original name + "_output"
    original_name = uploaded.name           # e.g. "106-PO-000045403-MGD ORDER PO CLIENT.xlsx"
    base, ext = os.path.splitext(original_name)
    if not ext:
        ext = ".xlsx"                       # safe default
    output_name = f"{base}_output{ext}"     # -> "106-PO-000045403-MGD ORDER PO CLIENT_output.xlsx"

    st.success("File converted successfully!")

    st.download_button(
        label="Download output file",
        data=out_bytes,
        file_name=output_name,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
